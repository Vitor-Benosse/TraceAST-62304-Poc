"""Pre-audit screening runner entrypoint for the integrated TraceAST-62304 pipeline."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from traceast.cli import main as cli_main


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Execute the integrated TraceAST-62304 pre-audit screening pipeline."
    )
    parser.add_argument("--repo", default=".", help="Path or Git URL of the repository to screen.")
    parser.add_argument("--profile", default=None, help="Path to product_profile.yaml.")
    parser.add_argument("--out", default="./reports/latest", help="Output directory for reports.")
    parser.add_argument("--no-rag", action="store_true", help="Disable RAG regulatory retrieval.")
    parser.add_argument("--with-llm", action="store_true", help="Enable optional LLM explanations.")
    args = parser.parse_args()

    cli_argv = ["scan", "--repo", args.repo, "--out", args.out]
    if args.profile:
        cli_argv.extend(["--profile", args.profile])
    if args.no_rag:
        cli_argv.append("--no-rag")
    if args.with_llm:
        cli_argv.append("--with-llm")
    return cli_main(cli_argv)


if __name__ == "__main__":
    sys.exit(main())
