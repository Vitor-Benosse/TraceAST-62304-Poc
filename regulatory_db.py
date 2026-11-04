"""Refactored Regulatory RAG database builder delegating to traceast.rag_engine."""

from __future__ import annotations

import argparse
from pathlib import Path

from traceast.rag_engine import RegulatoryRAGEngine


def build_regulatory_database(
    docs_dir: Path = Path("./legal_documents"),
    persist_dir: Path = Path("./db_regulacao_v1"),
) -> RegulatoryRAGEngine:
    """Ingest ANVISA RDC 657/2022 and IEC 62304 references (excluding FDA in V1.0) with full provenance metadata."""
    return RegulatoryRAGEngine(legal_docs_dir=docs_dir, persist_dir=persist_dir)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build and test the TraceAST-62304 Regulatory RAG Index (ANVISA RDC 657/2022 + IEC 62304)."
    )
    parser.add_argument("--docs-dir", default="./legal_documents", help="Regulatory documents folder.")
    parser.add_argument("--persist-dir", default="./db_regulacao_v1", help="Persistence directory.")
    args = parser.parse_args()

    engine = build_regulatory_database(Path(args.docs_dir), Path(args.persist_dir))
    print(
        f"Indexed {len(engine.documents_manifest)} regulatory documents into {len(engine.chunks)} traceable fragments."
    )


if __name__ == "__main__":
    main()
