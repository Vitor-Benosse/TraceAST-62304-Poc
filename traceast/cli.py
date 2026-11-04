"""Command-line interface for TraceAST-62304."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import List, Optional

from traceast import __positioning__, __tool_name__, __version__
from traceast.config import TraceASTConfig
from traceast.evaluation import (
    evaluate_rag_recall_at_k,
    generate_and_score_synthetic_benchmark,
    generate_expert_annotation_templates,
    generate_study_dataset_manifest,
)
from traceast.pipeline import run_pre_audit_pipeline
from traceast.rag_engine import RegulatoryRAGEngine
from traceast.rule_catalog import compute_rule_catalog_hash


def _cmd_scan(args: argparse.Namespace) -> int:
    repo_target = args.repo
    out_dir = Path(args.out).resolve()
    profile_path = Path(args.profile).resolve() if args.profile else None

    enable_rag = not args.no_rag
    enable_llm = bool(args.with_llm)

    if enable_llm:
        print(
            "[AVISO DE PRIVACIDADE] O modo --with-llm foi habilitado. "
            "Apenas metadados estruturados (sem código-fonte integral ou docstrings) serão enviados ao provedor externo."
        )

    config = TraceASTConfig(
        enable_rag=enable_rag,
        enable_llm=enable_llm,
        allow_code_excerpts_to_llm=bool(args.allow_code_excerpts),
    )

    print(f"[{__tool_name__} v{__version__}] Iniciando triagem pré-auditoria...")
    print(f"  Repositório-alvo : {repo_target}")
    print(f"  Perfil do produto: {profile_path or 'Não informado (usando padrão com limitações explícitas)'}")
    print(f"  RAG habilitado   : {enable_rag}")
    print(f"  LLM opcional     : {enable_llm}")
    print(f"  Diretório saída  : {out_dir}")

    try:
        result = run_pre_audit_pipeline(
            repo_target=repo_target,
            out_dir=out_dir,
            profile_path=profile_path,
            config=config,
        )
    except Exception as e:
        print(f"[ERRO] Falha durante a execução da análise: {e}", file=sys.stderr)
        return 1

    summary = result["analysis"]["inspection_summary"]
    counts = result["report"].summary_counts
    print("\n[CONCLUÍDO] Triagem finalizada com sucesso:")
    print(
        f"  Arquivos Python analisados : {summary['python_files_parsed_successfully']}/{summary['python_files_found']} "
        f"({summary['inspection_coverage_percent']}% cobertura; {summary['python_files_failed']} falhas)"
    )
    print(
        f"  Resumo dos indicadores     : observed={counts['observed']}, partial={counts['partial']}, "
        f"not_observed={counts['not_observed']}, unable_to_assess={counts['unable_to_assess']}, "
        f"not_applicable={counts['not_applicable']}"
    )
    print("  Artefatos gerados:")
    for k, v in result["written_files"].items():
        print(f"    - {k}: {v}")
    return 0


def _cmd_version(_args: argparse.Namespace) -> int:
    info = {
        "tool_name": __tool_name__,
        "version": __version__,
        "positioning": __positioning__,
        "python_version": sys.version.split()[0],
        "rule_catalog_sha256": compute_rule_catalog_hash(),
    }
    print(json.dumps(info, indent=2, ensure_ascii=False))
    return 0


def _cmd_build_rag(args: argparse.Namespace) -> int:
    docs_dir = Path(args.docs_dir).resolve()
    persist_dir = Path(args.persist_dir).resolve()
    print(f"[{__tool_name__}] Indexando base regulatória de '{docs_dir}' em '{persist_dir}'...")
    engine = RegulatoryRAGEngine(legal_docs_dir=docs_dir, persist_dir=persist_dir)
    print(
        f"[CONCLUÍDO] {len(engine.documents_manifest)} documentos e {len(engine.chunks)} fragmentos indexados "
        f"(backend: {engine.backend_used})."
    )
    return 0


def _cmd_evaluate(args: argparse.Namespace) -> int:
    out_dir = Path(args.out).resolve()
    docs_dir = Path(args.docs_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[{__tool_name__}] Gerando artefatos de avaliação científica em '{out_dir}'...")
    templates = generate_expert_annotation_templates(out_dir / "templates")
    synth_score = generate_and_score_synthetic_benchmark(out_dir)
    rag_eval = evaluate_rag_recall_at_k(legal_docs_dir=docs_dir, k=3, output_dir=out_dir)
    manifest_path = generate_study_dataset_manifest(out_dir)

    print("[CONCLUÍDO] Artefatos de avaliação científica gerados:")
    print(f"  - Templates de anotação de especialistas: {len(templates)} arquivos em {out_dir / 'templates'}")
    print(
        f"  - Validação do motor de pontuação (DADOS SINTÉTICOS): F1 micro={synth_score['aggregated_micro']['f1_score']}, "
        f"Cohen's kappa={synth_score['inter_rater_agreement_cohens_kappa']}"
    )
    print(
        f"  - Avaliação RAG Recall@3: hit_rate={rag_eval['hit_rate_recall_at_k']} "
        f"({rag_eval['queries_with_relevant_hit_at_k']}/{rag_eval['total_queries']} consultas)"
    )
    print(f"  - Manifesto de separação Dev/Test: {manifest_path}")
    return 0


def _cmd_test(args: argparse.Namespace) -> int:
    import pytest
    pytest_args = list(args.pytest_args) if args.pytest_args else ["-v"]
    return int(pytest.main(pytest_args))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="traceast",
        description=f"{__tool_name__} v{__version__} — {__positioning__}",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"{__tool_name__} {__version__}",
    )
    subparsers = parser.add_subparsers(dest="command")

    # scan subcommand
    scan_p = subparsers.add_parser("scan", help="Executar triagem pré-auditoria em um repositório Python.")
    scan_p.add_argument("--repo", required=True, help="Caminho local ou URL Git do repositório a ser analisado.")
    scan_p.add_argument("--profile", default=None, help="Caminho para o arquivo YAML de perfil do produto.")
    scan_p.add_argument("--out", default="./reports/latest", help="Diretório de saída para os relatórios e manifestos.")
    scan_p.add_argument("--no-rag", action="store_true", help="Desabilitar recuperação de referências regulatórias via RAG.")
    scan_p.add_argument("--with-llm", action="store_true", help="Habilitar explicações complementares via LLM externo.")
    scan_p.add_argument(
        "--allow-code-excerpts",
        action="store_true",
        help="Permitir envio de nomes de arquivos e símbolos internos no resumo estruturado para o LLM.",
    )
    scan_p.set_defaults(func=_cmd_scan)

    # version subcommand
    ver_p = subparsers.add_parser("version", help="Exibir versão detalhada do sistema e hash do catálogo de regras.")
    ver_p.set_defaults(func=_cmd_version)

    # build-rag subcommand
    rag_p = subparsers.add_parser("build-rag", help="Construir e persistir o índice da base documental regulatória.")
    rag_p.add_argument("--docs-dir", default="./legal_documents", help="Diretório contendo documentos regulatórios.")
    rag_p.add_argument("--persist-dir", default="./db_regulacao_v1", help="Diretório para persistir o índice RAG.")
    rag_p.set_defaults(func=_cmd_build_rag)

    # evaluate subcommand
    eval_p = subparsers.add_parser("evaluate", help="Gerar templates de avaliação científica, Recall@3 do RAG e teste sintético do motor de pontuação.")
    eval_p.add_argument("--out", default="./evaluation_artifacts", help="Diretório de saída dos dados de avaliação.")
    eval_p.add_argument("--docs-dir", default="./legal_documents", help="Diretório da base regulatória.")
    eval_p.set_defaults(func=_cmd_evaluate)

    # test subcommand
    test_p = subparsers.add_parser("test", help="Executar a suíte de testes automatizados com pytest.")
    test_p.add_argument("pytest_args", nargs="*", help="Argumentos opcionais repassados ao pytest.")
    test_p.set_defaults(func=_cmd_test)

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return 0
    return int(args.func(args))

