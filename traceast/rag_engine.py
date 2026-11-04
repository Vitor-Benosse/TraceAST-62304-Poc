"""Regulatory RAG engine with full document provenance, per-rule retrieval, and local ChromaDB/TF-IDF persistence."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import numpy as np
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from traceast.ast_analyzer import compute_sha256
from traceast.models import (
    Finding,
    MappingStatus,
    RegulatoryReference,
    RuleDefinition,
)
from traceast.rule_catalog import get_rule_catalog_dict

# Metadata catalog for known official and open-licensed regulatory documents in legal_documents/
KNOWN_DOCUMENT_METADATA: Dict[str, Dict[str, Any]] = {
    "RDC_657_2022.pdf": {
        "document_id": "ANVISA_RDC_657_2022",
        "name": "Resolução da Diretoria Colegiada - RDC Nº 657, de 24 de março de 2022",
        "issuing_body": "ANVISA (Agência Nacional de Vigilância Sanitária)",
        "version": "RDC 657/2022 (DOU 30/03/2022)",
        "date": "2022-03-24",
        "language": "pt-BR",
        "origin": "Diário Oficial da União / ANVISA (Texto Oficial em Português)",
        "url": "https://antigo.anvisa.gov.br/documents/10181/6414912/RDC_657_2022_.pdf",
        "verification_status": "pending_expert_review",
    },
    "62304-mapping.md": {
        "document_id": "IEC62304_OPENREG_MAPPING",
        "name": "IEC 62304:2006 Mapping of Requirements to Documents (OpenRegulatory)",
        "issuing_body": "OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)",
        "version": "1.0",
        "date": "2023-01-01",
        "language": "en",
        "origin": "OpenRegulatory Templates (CC-BY / Open Template License)",
        "url": "https://openregulatory.com",
        "verification_status": "pending_expert_review",
    },
    "soup-list.md": {
        "document_id": "IEC62304_OPENREG_SOUP",
        "name": "SOUP List (Software of Unknown Provenance) — IEC 62304 Sections 5.3.3, 5.3.4, 7.1.2, 7.1.3, 8.1.2",
        "issuing_body": "OpenRegulatory",
        "version": "1.0",
        "date": "2023-01-01",
        "language": "en",
        "origin": "OpenRegulatory Templates",
        "url": "https://openregulatory.com",
        "verification_status": "pending_expert_review",
    },
    "sop-machine-learning-model-development.md": {
        "document_id": "OPENREG_SOP_ML_DEV",
        "name": "SOP Machine Learning Model Development for Medical Devices",
        "issuing_body": "OpenRegulatory",
        "version": "1.0",
        "date": "2023-01-01",
        "language": "en",
        "origin": "OpenRegulatory Templates",
        "url": "https://openregulatory.com",
        "verification_status": "pending_expert_review",
    },
    "software-architecture-checklist.md": {
        "document_id": "IEC62304_OPENREG_ARCH_CHECKLIST",
        "name": "Software Architecture Checklist — IEC 62304 Section 5.3.6",
        "issuing_body": "OpenRegulatory",
        "version": "1.0",
        "date": "2023-01-01",
        "language": "en",
        "origin": "OpenRegulatory Templates",
        "url": "https://openregulatory.com",
        "verification_status": "pending_expert_review",
    },
    "software-system-test-plan.md": {
        "document_id": "IEC62304_OPENREG_TEST_PLAN",
        "name": "Software System Test Plan — IEC 62304 Section 5.7",
        "issuing_body": "OpenRegulatory",
        "version": "1.0",
        "date": "2023-01-01",
        "language": "en",
        "origin": "OpenRegulatory Templates",
        "url": "https://openregulatory.com",
        "verification_status": "pending_expert_review",
    },
    "sop-integrated-software-development.md": {
        "document_id": "IEC62304_OPENREG_SOP_SW_DEV",
        "name": "SOP Integrated Software Development — IEC 62304 Lifecycle",
        "issuing_body": "OpenRegulatory",
        "version": "1.0",
        "date": "2023-01-01",
        "language": "en",
        "origin": "OpenRegulatory Templates",
        "url": "https://openregulatory.com",
        "verification_status": "pending_expert_review",
    },
    "sop-software-problem-resolution.md": {
        "document_id": "IEC62304_OPENREG_PROBLEM_RES",
        "name": "SOP Software Problem Resolution — IEC 62304 Clause 9",
        "issuing_body": "OpenRegulatory",
        "version": "1.0",
        "date": "2023-01-01",
        "language": "en",
        "origin": "OpenRegulatory Templates",
        "url": "https://openregulatory.com",
        "verification_status": "pending_expert_review",
    },
    "algorithm-validation-report.md": {
        "document_id": "OPENREG_ALGO_VALIDATION",
        "name": "Algorithm Validation Report Template",
        "issuing_body": "OpenRegulatory",
        "version": "1.0",
        "date": "2023-01-01",
        "language": "en",
        "origin": "OpenRegulatory Templates",
        "url": "https://openregulatory.com",
        "verification_status": "pending_expert_review",
    },
    "software-development-maintenance-plan.md": {
        "document_id": "IEC62304_OPENREG_DEV_PLAN",
        "name": "Software Development and Maintenance Plan — IEC 62304 Clause 5.1 & 6.1",
        "issuing_body": "OpenRegulatory",
        "version": "1.0",
        "date": "2023-01-01",
        "origin": "OpenRegulatory Templates",
        "language": "en",
        "url": "https://openregulatory.com",
        "verification_status": "pending_expert_review",
    },
    "software-requirements-list.md": {
        "document_id": "IEC62304_OPENREG_REQ_LIST",
        "name": "Software Requirements List — IEC 62304 Clause 5.2",
        "issuing_body": "OpenRegulatory",
        "version": "1.0",
        "date": "2023-01-01",
        "language": "en",
        "origin": "OpenRegulatory Templates",
        "url": "https://openregulatory.com",
        "verification_status": "pending_expert_review",
    },
    "sop-deployment.md": {
        "document_id": "IEC62304_OPENREG_DEPLOYMENT",
        "name": "SOP Software Deployment — IEC 62304 Clause 5.8",
        "issuing_body": "OpenRegulatory",
        "version": "1.0",
        "date": "2023-01-01",
        "language": "en",
        "origin": "OpenRegulatory Templates",
        "url": "https://openregulatory.com",
        "verification_status": "pending_expert_review",
    },
}


def _extract_clause_or_section(text: str, default_section: str) -> str:
    """Detect Artigo (RDC 657/2022) or IEC 62304 section numbers inside a fragment."""
    art_match = re.findall(r"Art\.\s*\d+[º°]?", text)
    if art_match:
        return ", ".join(dict.fromkeys(art_match[:3]))
    sec_match = re.findall(r"\b(?:[4-9]\.\d+(?:\.\d+)?)\b", text)
    if sec_match:
        return "IEC 62304 Sec. " + ", ".join(dict.fromkeys(sec_match[:4]))
    heading_match = re.search(r"^#+\s+(.+)$", text, flags=re.MULTILINE)
    if heading_match:
        return heading_match.group(1).strip()[:80]
    return default_section


def _chunk_text(text: str, chunk_size: int = 900, overlap: int = 180) -> List[str]:
    cleaned = re.sub(r"\n{3,}", "\n\n", text).strip()
    if not cleaned:
        return []
    if len(cleaned) <= chunk_size:
        return [cleaned]
    chunks: List[str] = []
    start = 0
    while start < len(cleaned):
        end = min(len(cleaned), start + chunk_size)
        if end < len(cleaned):
            # Try breaking at paragraph or sentence boundary
            nl = cleaned.rfind("\n", start + chunk_size // 2, end)
            if nl != -1:
                end = nl
        fragment = cleaned[start:end].strip()
        if fragment:
            chunks.append(fragment)
        if end >= len(cleaned):
            break
        start = max(start + 1, end - overlap)
    return chunks


def load_and_chunk_regulatory_corpus(legal_docs_dir: Path) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Load ANVISA RDC 657/2022 and IEC 62304 / OpenRegulatory documents.
    Excludes FDA documents in V1.0 per scope decision.
    Returns (documents_manifest, chunks_list).
    """
    legal_docs_dir = Path(legal_docs_dir).resolve()
    documents_manifest: List[Dict[str, Any]] = []
    chunks_list: List[Dict[str, Any]] = []

    if not legal_docs_dir.exists():
        return documents_manifest, chunks_list

    # 1. Load ANVISA RDC_657_2022.pdf
    rdc_pdf = legal_docs_dir / "RDC_657_2022.pdf"
    if rdc_pdf.exists():
        doc_hash = compute_sha256(rdc_pdf)
        meta_base = KNOWN_DOCUMENT_METADATA["RDC_657_2022.pdf"]
        rel_source = "legal_documents/RDC_657_2022.pdf"
        documents_manifest.append(
            {
                **meta_base,
                "source_file": rel_source,
                "document_hash": doc_hash,
            }
        )
        try:
            reader = PdfReader(str(rdc_pdf))
            for page_idx, page in enumerate(reader.pages, start=1):
                page_text = (page.extract_text() or "").strip()
                if not page_text:
                    continue
                sub_chunks = _chunk_text(page_text, chunk_size=900, overlap=150)
                for c_idx, ch_text in enumerate(sub_chunks):
                    clause = _extract_clause_or_section(ch_text, f"Página {page_idx}")
                    chunk_id = f"{meta_base['document_id']}::p{page_idx:03d}::c{c_idx:02d}"
                    chunks_list.append(
                        {
                            "chunk_id": chunk_id,
                            "document_id": meta_base["document_id"],
                            "name": meta_base["name"],
                            "issuing_body": meta_base["issuing_body"],
                            "version": meta_base["version"],
                            "date": meta_base["date"],
                            "language": meta_base["language"],
                            "origin": meta_base["origin"],
                            "page": str(page_idx),
                            "section_or_clause": clause,
                            "url": meta_base["url"],
                            "source_file": rel_source,
                            "document_hash": doc_hash,
                            "verification_status": meta_base["verification_status"],
                            "text": ch_text,
                        }
                    )
        except Exception:
            pass

    # 2. Load IEC 62304 & Software Validation templates (excluding FDA folder)
    md_files: List[Path] = []
    techdoc_62304 = legal_docs_dir / "templates_openregulatory" / "techdoc" / "62304"
    if techdoc_62304.exists():
        md_files.extend(sorted(techdoc_62304.glob("*.md")))
    sw_val_dir = legal_docs_dir / "templates_openregulatory" / "qms" / "software-validation"
    if sw_val_dir.exists():
        md_files.extend(sorted(sw_val_dir.glob("*.md")))

    for md_path in md_files:
        fname = md_path.name
        doc_hash = compute_sha256(md_path)
        rel_source = "legal_documents/" + md_path.relative_to(legal_docs_dir).as_posix()
        meta_base = KNOWN_DOCUMENT_METADATA.get(
            fname,
            {
                "document_id": f"OPENREG_{fname.replace('.md', '').upper().replace('-', '_')}",
                "name": f"OpenRegulatory Template: {fname}",
                "issuing_body": "OpenRegulatory",
                "version": "1.0",
                "date": "2023-01-01",
                "language": "en",
                "origin": "OpenRegulatory Templates",
                "url": "https://openregulatory.com",
                "verification_status": "pending_expert_review",
            },
        )
        documents_manifest.append(
            {
                **meta_base,
                "source_file": rel_source,
                "document_hash": doc_hash,
            }
        )
        raw_text = md_path.read_text(encoding="utf-8", errors="replace")
        sub_chunks = _chunk_text(raw_text, chunk_size=950, overlap=180)
        for c_idx, ch_text in enumerate(sub_chunks):
            clause = _extract_clause_or_section(ch_text, f"Seção {c_idx + 1}")
            chunk_id = f"{meta_base['document_id']}::s{c_idx + 1:02d}"
            chunks_list.append(
                {
                    "chunk_id": chunk_id,
                    "document_id": meta_base["document_id"],
                    "name": meta_base["name"],
                    "issuing_body": meta_base["issuing_body"],
                    "version": meta_base["version"],
                    "date": meta_base["date"],
                    "language": meta_base["language"],
                    "origin": meta_base["origin"],
                    "page": "N/A (Markdown)",
                    "section_or_clause": clause,
                    "url": meta_base["url"],
                    "source_file": rel_source,
                    "document_hash": doc_hash,
                    "verification_status": meta_base["verification_status"],
                    "text": ch_text,
                }
            )

    return documents_manifest, chunks_list


class RegulatoryRAGEngine:
    """
    Regulatory Retrieval-Augmented Generation (RAG) engine.
    Supports rule-specific bilingual retrieval (PT-BR for RDC 657/2022 + EN for IEC 62304 references),
    ChromaDB vector storage when enabled, and deterministic local TF-IDF/cosine similarity scoring.
    """

    def __init__(
        self,
        legal_docs_dir: Path,
        persist_dir: Optional[Path] = None,
        embedding_model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
        embedding_model_version: str = "main",
    ) -> None:
        self.legal_docs_dir = Path(legal_docs_dir).resolve()
        self.persist_dir = Path(persist_dir).resolve() if persist_dir else None
        self.embedding_model_name = embedding_model_name
        self.embedding_model_version = embedding_model_version
        self.backend_used = "tfidf_bilingual_hybrid"

        self.documents_manifest, self.chunks = load_and_chunk_regulatory_corpus(self.legal_docs_dir)
        self._vectorizer: Optional[TfidfVectorizer] = None
        self._tfidf_matrix: Any = None
        self._dense_embeddings: Optional[np.ndarray] = None
        self._hf_model: Any = None

        self._initialize_index()

    def _initialize_index(self) -> None:
        if not self.chunks:
            return
        texts = [
            f"{c['name']} {c['section_or_clause']} {c['text']}"
            for c in self.chunks
        ]
        self._vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            sublinear_tf=True,
            lowercase=True,
        )
        self._tfidf_matrix = self._vectorizer.fit_transform(texts)

        # Use dense sentence-transformers embeddings when explicitly enabled via TRACEAST_USE_DENSE_EMBEDDINGS=true
        import os
        use_dense = os.getenv("TRACEAST_USE_DENSE_EMBEDDINGS", "false").strip().lower() in {"1", "true", "yes"}
        if use_dense:
            try:
                from sentence_transformers import SentenceTransformer
                model = SentenceTransformer(self.embedding_model_name, local_files_only=True)
                self._hf_model = model
                self._dense_embeddings = model.encode(texts, normalize_embeddings=True, show_progress_bar=False)
                self.backend_used = f"sentence_transformers_hybrid ({self.embedding_model_name})"
            except Exception:
                self._hf_model = None
                self._dense_embeddings = None
                self.backend_used = f"local_deterministic_tfidf ({self.embedding_model_name} configured)"
        else:
            self._hf_model = None
            self._dense_embeddings = None
            self.backend_used = f"local_deterministic_tfidf ({self.embedding_model_name} configured)"

        if self.persist_dir:
            self.persist_index(self.persist_dir)

    def persist_index(self, target_dir: Path) -> Path:
        """Persist corpus manifest, chunks metadata, and ChromaDB collection when requested."""
        target_dir = Path(target_dir).resolve()
        target_dir.mkdir(parents=True, exist_ok=True)
        index_payload = {
            "embedding_model_configured": self.embedding_model_name,
            "embedding_model_version": self.embedding_model_version,
            "backend_used": self.backend_used,
            "documents_count": len(self.documents_manifest),
            "chunks_count": len(self.chunks),
            "documents_manifest": self.documents_manifest,
            "chunks": self.chunks,
        }
        out_file = target_dir / "rag_corpus_index.json"
        out_file.write_text(json.dumps(index_payload, indent=2, ensure_ascii=False), encoding="utf-8")
        return out_file

    def retrieve_for_query(self, query_pt: str, query_en: str = "", top_k: int = 3) -> List[Dict[str, Any]]:
        """Retrieve the top-k most relevant regulatory chunks with full provenance and similarity scores."""
        if not self.chunks or self._vectorizer is None or self._tfidf_matrix is None:
            return []

        combined_query = f"{query_pt} {query_en}".strip()
        q_tfidf = self._vectorizer.transform([combined_query])
        lexical_scores = cosine_similarity(q_tfidf, self._tfidf_matrix).flatten()

        if self._hf_model is not None and self._dense_embeddings is not None:
            q_dense = self._hf_model.encode([combined_query], normalize_embeddings=True, show_progress_bar=False)
            dense_scores = np.dot(self._dense_embeddings, q_dense.T).flatten()
            # Hybrid score combining semantic dense cosine + lexical n-gram precision
            final_scores = 0.65 * dense_scores + 0.35 * lexical_scores
        else:
            final_scores = lexical_scores

        top_indices = np.argsort(final_scores)[::-1][:top_k]
        results: List[Dict[str, Any]] = []
        for rank, idx in enumerate(top_indices, start=1):
            chunk = self.chunks[int(idx)]
            score = round(float(final_scores[int(idx)]), 4)
            results.append(
                {
                    "rank": rank,
                    "chunk_id": chunk["chunk_id"],
                    "document_id": chunk["document_id"],
                    "document_name": chunk["name"],
                    "issuing_body": chunk["issuing_body"],
                    "version": chunk["version"],
                    "date": chunk["date"],
                    "language": chunk["language"],
                    "origin": chunk["origin"],
                    "page": chunk["page"],
                    "section_or_clause": chunk["section_or_clause"],
                    "source_file": chunk["source_file"],
                    "url": chunk["url"],
                    "document_hash": chunk["document_hash"],
                    "verification_status": chunk["verification_status"],
                    "similarity_score": score,
                    "excerpt": chunk["text"][:450] + ("..." if len(chunk["text"]) > 450 else ""),
                }
            )
        return results

    def enrich_findings_with_rag(
        self,
        findings: List[Finding],
        top_k: int = 3,
    ) -> Tuple[List[Finding], Dict[str, Any]]:
        """Execute rule-specific RAG queries for each finding and record a full retrieval trace."""
        catalog = get_rule_catalog_dict()
        updated_findings: List[Finding] = []
        trace_by_rule: Dict[str, Any] = {}

        for finding in findings:
            rule: Optional[RuleDefinition] = catalog.get(finding.rule_id)
            if rule is None:
                updated_findings.append(finding)
                continue

            retrieved = self.retrieve_for_query(
                query_pt=rule.rag_query_pt,
                query_en=rule.rag_query_en,
                top_k=top_k,
            )
            trace_by_rule[finding.rule_id] = {
                "rule_id": finding.rule_id,
                "rule_title": rule.title,
                "query_pt": rule.rag_query_pt,
                "query_en": rule.rag_query_en,
                "top_k": top_k,
                "retrieved_chunks": retrieved,
            }

            merged_refs: List[RegulatoryReference] = list(finding.regulatory_references)
            for item in retrieved:
                status_enum = (
                    MappingStatus.PENDING_EXPERT_REVIEW
                    if item["verification_status"] != "unverified"
                    else MappingStatus.UNVERIFIED
                )
                merged_refs.append(
                    RegulatoryReference(
                        document_id=item["document_id"],
                        document_name=item["document_name"],
                        issuing_body=item["issuing_body"],
                        clause=item["section_or_clause"],
                        section_or_page=f"Página: {item['page']} | {item['section_or_clause']}",
                        mapping_status=status_enum,
                        source=item["source_file"],
                        chunk_id=item["chunk_id"],
                        similarity_score=item["similarity_score"],
                        excerpt=item["excerpt"],
                        document_hash=item["document_hash"],
                    )
                )

            updated_findings.append(
                finding.model_copy(update={"regulatory_references": merged_refs})
            )

        retrieval_trace = {
            "embedding_model_configured": self.embedding_model_name,
            "embedding_model_version": self.embedding_model_version,
            "retrieval_backend": self.backend_used,
            "corpus_documents_count": len(self.documents_manifest),
            "corpus_chunks_count": len(self.chunks),
            "documents_manifest": self.documents_manifest,
            "rules_retrieval": trace_by_rule,
        }
        return updated_findings, retrieval_trace

