"""Refactored AST & repository static analyzer entrypoint delegating to traceast.ast_analyzer."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict

from traceast.ast_analyzer import analyze_repository_static
from traceast.pipeline import resolve_repository_target, _remove_read_only
import shutil


def analyze_repository(repo_target: str | Path) -> Dict[str, Any]:
    """Analyze a local directory or remote Git repository URL without executing target code."""
    repo_path, cleanup_dir = resolve_repository_target(repo_target)
    try:
        return analyze_repository_static(repo_path)
    finally:
        if cleanup_dir is not None and cleanup_dir.exists():
            shutil.rmtree(cleanup_dir, onexc=_remove_read_only)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="TraceAST-62304 Static AST & Repository Inspector."
    )
    parser.add_argument(
        "repo",
        nargs="?",
        default=".",
        help="Local repository path or Git URL to analyze.",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Optional JSON file path to save the extracted inventory and evidences.",
    )
    args = parser.parse_args()
    result = analyze_repository(args.repo)
    output_json = json.dumps(result["inspection_summary"], indent=2, ensure_ascii=False)
    print(output_json)
    if args.out:
        out_path = Path(args.out).resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Full static analysis saved to: {out_path}")


if __name__ == "__main__":
    main()
