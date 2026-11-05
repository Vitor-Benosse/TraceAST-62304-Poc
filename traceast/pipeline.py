"""End-to-end integrated pre-audit screening pipeline for TraceAST-62304."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import time
from typing import Any, Callable, Dict, Optional

from traceast import __positioning__, __tool_name__, __version__
from traceast.ast_analyzer import analyze_repository_static
from traceast.config import MANDATORY_DISCLAIMERS, TraceASTConfig, load_product_profile
from traceast.llm_agent import enrich_findings_with_optional_llm
from traceast.models import FindingsReport, ProductProfile
from traceast.rag_engine import RegulatoryRAGEngine
from traceast.reporting import compute_summary_counts, write_all_outputs
from traceast.rule_catalog import RULE_CATALOG_VERSION, compute_rule_catalog_hash
from traceast.rules_engine import evaluate_all_rules


def _remove_read_only(func: Any, path: str, exc: Any) -> None:
    if isinstance(exc, PermissionError):
        Path(path).chmod(stat.S_IWRITE | stat.S_IREAD)
        func(path)
    else:
        raise exc


def resolve_repository_target(repo_arg: str | Path) -> tuple[Path, Optional[Path]]:
    """
    Resolve a local repository directory or clone a remote Git URL into a temporary directory
    without executing any code from the target repository.
    Returns (resolved_repo_path, temp_dir_to_cleanup_or_None).
    """
    repo_str = str(repo_arg).strip()
    if repo_str.startswith(("http://", "https://", "git@")):
        tmp_dir = Path(tempfile.mkdtemp(prefix="traceast_clone_"))
        proc = subprocess.run(
            ["git", "clone", "--depth", "1", repo_str, str(tmp_dir)],
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode != 0:
            shutil.rmtree(tmp_dir, onexc=_remove_read_only)
            raise RuntimeError(f"Não foi possível clonar o repositório '{repo_str}': {proc.stderr.strip()}")
        return tmp_dir, tmp_dir

    local_path = Path(repo_str).resolve()
    if not local_path.exists() or not local_path.is_dir():
        raise FileNotFoundError(f"Caminho do repositório não encontrado: {local_path}")
    return local_path, None


def run_pre_audit_pipeline(
    repo_target: str | Path,
    out_dir: Path,
    profile_path: Optional[Path] = None,
    config: Optional[TraceASTConfig] = None,
    custom_llm_callable: Optional[Callable[[Dict[str, Any]], str]] = None,
) -> Dict[str, Any]:
    """
    Execute the complete TraceAST-62304 pipeline from repository inspection to validated report generation.
    Never modifies or executes code in the target repository.
    """
    t0 = time.perf_counter()
    cfg = config or TraceASTConfig()
    profile: ProductProfile = load_product_profile(profile_path)

    repo_path, cleanup_dir = resolve_repository_target(repo_target)
    try:
        project_name = (
            profile.name
            if profile.name != "Unknown Medical Software Project"
            else repo_path.name
        )

        # Step 1-4: File inventory, AST analysis, dependencies, tests, CI/CD, evidence extraction
        t_ast_start = time.perf_counter()
        analysis = analyze_repository_static(repo_path, excluded_dirs=cfg.excluded_dirs)
        ast_duration = round(time.perf_counter() - t_ast_start, 4)

        # Step 5: Deterministic rule evaluation (R01-R08)
        t_rules_start = time.perf_counter()
        findings = evaluate_all_rules(analysis=analysis, profile=profile, repo_path=repo_path)
        rules_duration = round(time.perf_counter() - t_rules_start, 4)

        # Step 6: Per-rule Regulatory RAG retrieval
        retrieval_trace: Optional[Dict[str, Any]] = None
        rag_duration = 0.0
        documents_hashes: Dict[str, str] = {}
        if cfg.enable_rag:
            t_rag_start = time.perf_counter()
            rag_engine = RegulatoryRAGEngine(
                legal_docs_dir=cfg.legal_docs_dir,
                persist_dir=cfg.rag_persist_dir,
                embedding_model_name=cfg.embedding_model,
                embedding_model_version=cfg.embedding_model_version,
            )
            findings, retrieval_trace = rag_engine.enrich_findings_with_rag(findings, top_k=3)
            documents_hashes = {
                doc["document_id"]: doc["document_hash"]
                for doc in rag_engine.documents_manifest
            }
            rag_duration = round(time.perf_counter() - t_rag_start, 4)

        # Step 7: Optional LLM explanation (strictly read-only on deterministic status/evidence)
        findings, llm_audit_log = enrich_findings_with_optional_llm(
            findings=findings,
            config=cfg,
            custom_llm_callable=custom_llm_callable,
        )

        # Step 8: Schema validation of complete FindingsReport
        exec_timestamp = datetime.now(timezone.utc).isoformat()
        summary_counts = compute_summary_counts(findings)
        findings_report = FindingsReport(
            schema_version="1.0.0",
            tool_name=__tool_name__,
            tool_version=__version__,
            positioning=__positioning__,
            project_name=project_name,
            commit_sha=analysis["commit_sha"],
            execution_timestamp=exec_timestamp,
            product_profile=profile,
            findings=findings,
            summary_counts=summary_counts,
            mandatory_disclaimers=list(MANDATORY_DISCLAIMERS),
        )

        total_duration = round(time.perf_counter() - t0, 4)
        rule_catalog_hash = compute_rule_catalog_hash()

        run_manifest = {
            "tool_name": __tool_name__,
            "tool_version": __version__,
            "execution_timestamp": exec_timestamp,
            "python_version": sys.version,
            "repository_analyzed": str(repo_target),
            "resolved_repository_path": str(repo_path),
            "commit_sha": analysis["commit_sha"],
            "rule_catalog_version": RULE_CATALOG_VERSION,
            "rule_catalog_sha256": rule_catalog_hash,
            "regulatory_documents_sha256": documents_hashes,
            "configuration": cfg.sanitized_Metadata(),
            "llm_usage_audit": llm_audit_log,
            "durations_seconds": {
                "ast_and_inventory": ast_duration,
                "rules_engine": rules_duration,
                "rag_retrieval": rag_duration,
                "llm_explanations": llm_audit_log["duration_seconds"],
                "total_pipeline": total_duration,
            },
        }

        analysis_metrics = {
            "project_name": project_name,
            "commit_sha": analysis["commit_sha"],
            "inspection_summary": analysis["inspection_summary"],
            "structural_counts": {
                "total_classes": sum(len(pf["classes"]) for pf in analysis["parsed_files"]),
                "total_functions_and_methods": sum(len(pf["functions"]) for pf in analysis["parsed_files"]),
                "nested_functions": sum(
                    sum(1 for fn in pf["functions"] if fn["is_nested"])
                    for pf in analysis["parsed_files"]
                ),
                "async_functions_and_methods": sum(
                    sum(1 for fn in pf["functions"] if fn["is_async"])
                    for pf in analysis["parsed_files"]
                ),
                "total_try_blocks": sum(len(pf["try_blocks"]) for pf in analysis["parsed_files"]),
                "empty_or_pass_except_blocks": sum(
                    sum(1 for tb in pf["try_blocks"] if tb["has_empty_except"] or tb["has_pass_in_except"])
                    for pf in analysis["parsed_files"]
                ),
                "total_io_operations": sum(len(pf["io_operations"]) for pf in analysis["parsed_files"]),
                "total_validation_signals": sum(len(pf["validation_signals"]) for pf in analysis["parsed_files"]),
                "total_model_artifact_signals": sum(len(pf["model_artifacts"]) for pf in analysis["parsed_files"])
                + len(analysis["standalone_model_files"]),
                "total_training_signals": sum(len(pf["training_signals"]) for pf in analysis["parsed_files"]),
                "total_inference_signals": sum(len(pf["inference_signals"]) for pf in analysis["parsed_files"]),
                "declared_dependencies_count": len(analysis["dependencies"]["declared_dependencies"]),
                "pinned_dependencies_count": analysis["dependencies"]["pinned_count"],
                "unpinned_dependencies_count": analysis["dependencies"]["unpinned_count"],
                "test_files_count": len(analysis["tests_and_ci"]["test_files"]),
                "ci_workflows_count": len(analysis["tests_and_ci"]["ci_workflows"]),
            },
            "findings_summary": summary_counts,
            "durations_seconds": run_manifest["durations_seconds"],
        }

        # Step 9: Write all output artifacts
        written_files = write_all_outputs(
            out_dir=out_dir,
            report=findings_report,
            analysis=analysis,
            run_manifest=run_manifest,
            analysis_metrics=analysis_metrics,
            retrieval_trace=retrieval_trace,
        )

        return {
            "report": findings_report,
            "analysis": analysis,
            "run_manifest": run_manifest,
            "analysis_metrics": analysis_metrics,
            "retrieval_trace": retrieval_trace,
            "written_files": {k: str(v) for k, v in written_files.items()},
        }
    finally:
        if cleanup_dir is not None and cleanup_dir.exists():
            shutil.rmtree(cleanup_dir, onexc=_remove_read_only)

