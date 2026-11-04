"""Configuration, privacy controls, and product profile loader for TraceAST-62304."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Set
import yaml
from dotenv import load_dotenv

from traceast.models import ProductProfile

DEFAULT_EXCLUDED_DIRS: Set[str] = {
    ".git",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    "node_modules",
    "site-packages",
    "dist",
    "build",
    ".pytest_cache",
    ".mypy_cache",
    ".tox",
    ".eggs",
    "db_regulacao",
    "db_regulacao_v1",
    "repo_temp",
    ".test_repos_cache",
}

SENSITIVE_FILE_PATTERNS: Set[str] = {
    ".env",
    ".env.local",
    ".env.production",
    ".env.development",
    "secrets.yaml",
    "secrets.yml",
    "secrets.json",
    "credentials.json",
    "id_rsa",
    "id_ed25519",
}

MANDATORY_DISCLAIMERS: List[str] = [
    "O TraceAST-62304 é uma ferramenta assistiva de triagem pré-auditoria (AI-assisted, evidence-traceable pre-audit screening) e NÃO substitui auditores humanos.",
    "Este relatório NÃO declara conformidade regulatória nem certificação perante a IEC 62304, ANVISA RDC 657/2022 ou qualquer autoridade sanitária.",
    "O sistema NÃO determina automaticamente a classe regulatória do dispositivo (RDC 657/2022) nem a classe de segurança de software (IEC 62304 Classes A, B ou C).",
    "A ausência de determinada evidência no repositório inspecionado (not_observed) representa apenas ausência de evidência observável no escopo estático analisado, e NÃO prova de não conformidade.",
    "A presença de um indicador técnico (observed) indica que um elemento estrutural foi localizado no código, e NÃO que o controle ou processo atende integralmente aos requisitos normativos.",
    "Nenhuma afirmação é feita sobre desempenho clínico, acurácia diagnóstica, segurança clínica ou eficácia do modelo.",
    "Todas as correspondências entre regras técnicas e referências normativas requerem validação por especialista em assuntos regulatórios e engenharia de SaMD.",
]


class TraceASTConfig:
    """Runtime configuration with privacy-first local defaults."""

    def __init__(
        self,
        project_root: Optional[Path] = None,
        enable_rag: bool = True,
        enable_llm: bool = False,
        allow_code_excerpts_to_llm: bool = False,
        excluded_dirs: Optional[Set[str]] = None,
        embedding_model: Optional[str] = None,
        rag_persist_dir: Optional[Path] = None,
        legal_docs_dir: Optional[Path] = None,
    ) -> None:
        self.project_root = (project_root or Path(__file__).resolve().parent.parent).resolve()
        env_path = self.project_root / ".env"
        if env_path.exists():
            load_dotenv(env_path)

        self.enable_rag = enable_rag
        env_enable_llm = os.getenv("TRACEAST_ENABLE_LLM", "false").strip().lower() in {"1", "true", "yes"}
        self.enable_llm = enable_llm or env_enable_llm
        self.allow_code_excerpts_to_llm = allow_code_excerpts_to_llm or (
            os.getenv("TRACEAST_ALLOW_CODE_EXCERPTS", "false").strip().lower() in {"1", "true", "yes"}
        )

        extra_excluded = os.getenv("TRACEAST_EXCLUDE_DIRS", "")
        custom_Excludes = {d.strip() for d in extra_excluded.split(",") if d.strip()}
        self.excluded_dirs: Set[str] = set(DEFAULT_EXCLUDED_DIRS) | (excluded_dirs or set()) | custom_Excludes

        self.embedding_model: str = (
            embedding_model
            or os.getenv("TRACEAST_EMBEDDING_MODEL")
            or "sentence-transformers/all-MiniLM-L6-v2"
        )
        self.embedding_model_version: str = os.getenv("TRACEAST_EMBEDDING_MODEL_VERSION", "main")

        self.rag_persist_dir: Path = (
            rag_persist_dir
            or Path(os.getenv("TRACEAST_RAG_DB_DIR", str(self.project_root / "db_regulacao_v1")))
        ).resolve()
        self.legal_docs_dir: Path = (
            legal_docs_dir
            or Path(os.getenv("TRACEAST_LEGAL_DOCS_DIR", str(self.project_root / "legal_documents")))
        ).resolve()

        self.llm_provider: str = os.getenv("TRACEAST_LLM_PROVIDER", "groq")
        self.groq_model: str = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
        self.llm_temperature: float = float(os.getenv("TRACEAST_LLM_TEMPERATURE", "0.1"))
        self.llm_max_tokens: int = int(os.getenv("TRACEAST_LLM_MAX_TOKENS", "800"))

    def has_groq_api_key(self) -> bool:
        """Check whether GROQ_API_KEY is present without ever exposing or logging its value."""
        key = os.getenv("GROQ_API_KEY", "").strip()
        return bool(key and key != "your_api_key_here" and key != "sua_chave_de_api_aqui")

    def sanitized_Metadata(self) -> Dict[str, Any]:
        """Return safe configuration metadata for manifests without any secrets or API keys."""
        return {
            "enable_rag": self.enable_rag,
            "enable_llm": self.enable_llm,
            "allow_code_excerpts_to_llm": self.allow_code_excerpts_to_llm,
            "excluded_dirs": sorted(self.excluded_dirs),
            "embedding_model": self.embedding_model,
            "embedding_model_version": self.embedding_model_version,
            "llm_provider": self.llm_provider if self.enable_llm else None,
            "llm_model": self.groq_model if self.enable_llm else None,
            "llm_parameters": (
                {
                    "temperature": self.llm_temperature,
                    "max_tokens": self.llm_max_tokens,
                }
                if self.enable_llm
                else None
            ),
            "api_key_configured": self.has_groq_api_key(),
        }


def load_product_profile(profile_path: Optional[Path] = None) -> ProductProfile:
    """Load product context YAML or return an explicit unknown-profile default."""
    if profile_path is None:
        return ProductProfile(
            profile_limitations=[
                "Nenhum arquivo de perfil do produto (product_profile.yaml) foi fornecido na execução.",
            ]
        )

    resolved = Path(profile_path).resolve()
    if not resolved.exists():
        return ProductProfile(
            profile_source_path=str(resolved),
            profile_limitations=[
                f"Arquivo de perfil informado não encontrado ({resolved.name}); assumindo campos como desconhecidos.",
            ],
        )

    raw_data = yaml.safe_load(resolved.read_text(encoding="utf-8")) or {}
    product_section = raw_data.get("product", raw_data) if isinstance(raw_data, dict) else {}
    if not isinstance(product_section, dict):
        product_section = {}

    ai_val = product_section.get("ai_components", None)
    if isinstance(ai_val, str) and ai_val.strip().lower() in {"unknown", "desconhecido", ""}:
        ai_val = None

    target_market = product_section.get("target_market", ["Brazil"])
    if isinstance(target_market, str):
        target_market = [target_market]

    return ProductProfile(
        name=str(product_section.get("name", "Unknown Medical Software Project")),
        intended_purpose=str(product_section.get("intended_purpose", "unknown")),
        intended_users=str(product_section.get("intended_users", "unknown")),
        target_market=list(target_market),
        software_type=str(product_section.get("software_type", "unknown")),
        ai_components=ai_val if isinstance(ai_val, bool) else None,
        clinical_decision_context=str(product_section.get("clinical_decision_context", "unknown")),
        profile_source_path=str(resolved),
    )

