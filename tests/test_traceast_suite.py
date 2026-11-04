"""Comprehensive automated pytest suite for TraceAST-62304 (Unit, Integration, Negative, and Scientific Evaluation tests)."""

from __future__ import annotations

import json
from pathlib import Path
import pytest
from pydantic import ValidationError

from traceast.ast_analyzer import analyze_repository_static
from traceast.cli import main as cli_main
from traceast.config import TraceASTConfig, load_product_profile
from traceast.evaluation import (
    classify_pair_outcome,
    compute_cohens_kappa,
    evaluate_rag_recall_at_k,
    generate_and_score_synthetic_benchmark,
    generate_expert_annotation_templates,
    score_tool_against_consensus,
)
from traceast.llm_agent import build_sanitized_llm_payload, enrich_findings_with_optional_llm
from traceast.models import (
    ConfidenceLevel,
    EvidenceItem,
    Finding,
    FindingStatus,
    FindingsReport,
    ReviewPriority,
)
from traceast.pipeline import run_pre_audit_pipeline
from traceast.rag_engine import RegulatoryRAGEngine
from traceast.rules_engine import evaluate_all_rules

PROJECT_ROOT = Path(__file__).resolve().parent.parent
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
WELL_STRUCTURED_REPO = FIXTURES_DIR / "repo_well_structured"
DEFICIENT_REPO = FIXTURES_DIR / "repo_deficient_and_coupled"
FALSE_POSITIVE_REPO = FIXTURES_DIR / "repo_false_positive_traps"


# ---------------------------------------------------------------------------
# 1 & 2. File Discovery, Exclusions, SHA-256, and Parse Coverage
# ---------------------------------------------------------------------------

def test_01_file_discovery_and_100_percent_coverage() -> None:
    """Verify recursive file discovery, SHA-256 hashes, and 100% coverage on well-structured fixture."""
    analysis = analyze_repository_static(WELL_STRUCTURED_REPO)
    summary = analysis["inspection_summary"]

    assert summary["python_files_found"] == 4
    assert summary["python_files_parsed_successfully"] == 4
    assert summary["python_files_failed"] == 0
    assert summary["inspection_coverage_percent"] == 100.0
    assert len(analysis["failed_files"]) == 0

    for pf in analysis["parsed_files"]:
        assert len(pf["sha256"]) == 64
        assert pf["line_count"] >= 1


def test_02_syntax_error_recording_and_partial_coverage() -> None:
    """Verify broken Python files are never silently ignored and record exact SyntaxError line & reason."""
    analysis = analyze_repository_static(DEFICIENT_REPO)
    summary = analysis["inspection_summary"]

    assert summary["python_files_found"] == 2
    assert summary["python_files_parsed_successfully"] == 1
    assert summary["python_files_failed"] == 1
    assert summary["inspection_coverage_percent"] == 50.0

    failed = analysis["failed_files"][0]
    assert failed["file"] == "broken_syntax.py"
    assert failed["error_type"] == "SyntaxError"
    assert failed["line"] is not None
    assert len(failed["sha256"]) == 64


def test_03_secret_and_excluded_dirs_protection(tmp_path: Path) -> None:
    """Verify .env files and .venv/__pycache__ directories are excluded from inspection."""
    (tmp_path / ".env").write_text("GROQ_API_KEY=secret123", encoding="utf-8")
    venv_dir = tmp_path / ".venv"
    venv_dir.mkdir()
    (venv_dir / "ignored.py").write_text("x = 1", encoding="utf-8")
    (tmp_path / "app.py").write_text("def run():\n    return True\n", encoding="utf-8")

    analysis = analyze_repository_static(tmp_path)
    summary = analysis["inspection_summary"]
    assert summary["python_files_found"] == 1
    assert summary["excluded_sensitive_files_count"] == 1
    assert analysis["parsed_files"][0]["file"] == "app.py"


# ---------------------------------------------------------------------------
# 3. AST Extraction (Nested, Async, Try/Except, Logging, I/O, Model Signals)
# ---------------------------------------------------------------------------

def test_04_ast_extraction_nested_and_async_structures() -> None:
    """Verify AST visitor extracts classes, methods, nested functions, and async methods with line numbers."""
    analysis = analyze_repository_static(WELL_STRUCTURED_REPO)
    by_file = {pf["file"]: pf for pf in analysis["parsed_files"]}

    data_io = by_file["src/data_io.py"]
    func_symbols = {fn["symbol"]: fn for fn in data_io["functions"]}
    assert "validate_dicom_input" in func_symbols
    assert "validate_dicom_input._nested_range_validator" in func_symbols
    assert func_symbols["validate_dicom_input._nested_range_validator"]["is_nested"] is True
    assert len(data_io["logging_calls"]) >= 2

    inference = by_file["src/inference.py"]
    inf_symbols = {fn["symbol"]: fn for fn in inference["functions"]}
    assert "ChestDiagnosticModel.async_predict_study" in inf_symbols
    assert inf_symbols["ChestDiagnosticModel.async_predict_study"]["is_async"] is True
    assert inf_symbols["ChestDiagnosticModel.async_predict_study"]["kind"] == "async_method"


def test_05_ast_empty_pass_except_and_unprotected_io() -> None:
    """Verify AST visitor detects empty/pass except handlers and unprotected I/O operations."""
    analysis = analyze_repository_static(DEFICIENT_REPO)
    pf = analysis["parsed_files"][0]
    assert pf["file"] == "model_pipeline.py"

    assert len(pf["try_blocks"]) == 1
    tb = pf["try_blocks"][0]
    assert tb["has_empty_except"] is True
    assert tb["has_pass_in_except"] is True

    unprotected = [op for op in pf["io_operations"] if not op["inside_non_empty_try"]]
    assert len(unprotected) >= 2


# ---------------------------------------------------------------------------
# 4 & 5. Deterministic Rules Engine (Positive, Deficient, and Negative/Traps)
# ---------------------------------------------------------------------------

def test_06_rules_on_well_structured_repository() -> None:
    """Verify expected statuses for R01-R08 on the well-structured medical software fixture."""
    analysis = analyze_repository_static(WELL_STRUCTURED_REPO)
    profile = load_product_profile(PROJECT_ROOT / "product_profile.example.yaml")
    findings = evaluate_all_rules(analysis, profile, repo_path=WELL_STRUCTURED_REPO)
    by_rule = {f.rule_id: f for f in findings}

    assert by_rule["R01"].status == FindingStatus.OBSERVED
    assert by_rule["R02"].status == FindingStatus.OBSERVED
    assert by_rule["R03"].status == FindingStatus.OBSERVED
    assert by_rule["R04"].status == FindingStatus.OBSERVED
    assert by_rule["R05"].status == FindingStatus.OBSERVED
    assert by_rule["R06"].status == FindingStatus.OBSERVED
    # R07 is partial because checkpoint loading requires external provenance documentation
    assert by_rule["R07"].status == FindingStatus.PARTIAL
    # R08 is observed because training (src/trainer.py) and inference (src/inference.py) are in separate modules
    assert by_rule["R08"].status == FindingStatus.OBSERVED


def test_07_rules_on_deficient_and_coupled_repository() -> None:
    """Verify expected statuses for R01-R08 on the deficient/coupled fixture."""
    analysis = analyze_repository_static(DEFICIENT_REPO)
    profile = load_product_profile(None)
    findings = evaluate_all_rules(analysis, profile, repo_path=DEFICIENT_REPO)
    by_rule = {f.rule_id: f for f in findings}

    assert by_rule["R01"].status == FindingStatus.PARTIAL
    assert by_rule["R02"].status == FindingStatus.PARTIAL
    assert by_rule["R03"].status == FindingStatus.NOT_OBSERVED
    assert by_rule["R04"].status == FindingStatus.NOT_OBSERVED
    assert by_rule["R05"].status == FindingStatus.NOT_OBSERVED
    assert by_rule["R06"].status == FindingStatus.NOT_OBSERVED
    assert by_rule["R07"].status == FindingStatus.PARTIAL
    assert by_rule["R08"].status == FindingStatus.PARTIAL


def test_08_negative_test_false_positive_resistance_and_not_applicable() -> None:
    """Verify docstrings/strings mentioning torch.load/open do NOT trigger false positives and R07/R08 are not_applicable."""
    analysis = analyze_repository_static(FALSE_POSITIVE_REPO)
    profile = load_product_profile(FALSE_POSITIVE_REPO / "profile_non_ai.yaml")
    findings = evaluate_all_rules(analysis, profile, repo_path=FALSE_POSITIVE_REPO)
    by_rule = {f.rule_id: f for f in findings}

    pf = analysis["parsed_files"][0]
    assert len(pf["io_operations"]) == 0
    assert len(pf["model_artifacts"]) == 0
    assert len(pf["training_signals"]) == 0
    assert len(pf["inference_signals"]) == 0

    assert by_rule["R07"].status == FindingStatus.NOT_APPLICABLE
    assert by_rule["R08"].status == FindingStatus.NOT_APPLICABLE
    assert len(by_rule["R07"].justification) > 10


# ---------------------------------------------------------------------------
# 6. JSON Schema / Pydantic Validation & Anti-Hallucination Guards
# ---------------------------------------------------------------------------

def test_09_schema_validation_rejects_invalid_findings() -> None:
    """Verify Pydantic schema rejects invalid line ranges or findings lacking both evidence and justification."""
    with pytest.raises(ValidationError):
        EvidenceItem(
            file="src/app.py",
            symbol="func",
            line_start=50,
            line_end=10,
            evidence_type="ast_call",
            description="Invalid line range",
        )

    with pytest.raises(ValidationError):
        Finding(
            finding_id="TA-001",
            rule_id="R01",
            title="Test",
            category="Cat",
            status=FindingStatus.NOT_OBSERVED,
            status_label_pt="Label",
            review_priority=ReviewPriority.LOW,
            confidence=ConfidenceLevel.HIGH,
            description="Desc",
            justification="   ",
            evidence=[],
            regulatory_references=[],
            limitations=["Limitation 1"],
            recommended_action="Action",
        )


# ---------------------------------------------------------------------------
# 7. Regulatory RAG Retrieval & Provenance Traceability
# ---------------------------------------------------------------------------

def test_10_rag_retrieval_per_rule_and_fda_exclusion() -> None:
    """Verify RAG indexes ANVISA RDC 657/2022 + IEC 62304 templates, excludes FDA in V1.0, and returns top-3 per rule."""
    rag = RegulatoryRAGEngine(legal_docs_dir=PROJECT_ROOT / "legal_documents")
    doc_ids = {d["document_id"] for d in rag.documents_manifest}

    assert "ANVISA_RDC_657_2022" in doc_ids
    assert "IEC62304_OPENREG_MAPPING" in doc_ids
    assert "IEC62304_OPENREG_SOUP" in doc_ids
    # Verify no FDA document was indexed in V1.0
    assert not any("FDA" in d_id for d_id in doc_ids)

    results_r02 = rag.retrieve_for_query(
        query_pt="SOUP bibliotecas de terceiros gerenciamento de configuração IEC 62304",
        query_en="SOUP list Software of Unknown Provenance requirements.txt IEC 62304",
        top_k=3,
    )
    assert len(results_r02) == 3
    for item in results_r02:
        assert item["chunk_id"]
        assert len(item["document_hash"]) == 64
        assert item["similarity_score"] >= 0.0
        assert item["page"]


# ---------------------------------------------------------------------------
# 8. Fault Handling & Optional LLM Guardrails
# ---------------------------------------------------------------------------

def test_11_llm_optional_fallback_and_immutability_of_status() -> None:
    """Verify LLM payload masks source code, preserves deterministic status, and falls back gracefully on API error."""
    analysis = analyze_repository_static(WELL_STRUCTURED_REPO)
    profile = load_product_profile(None)
    findings = evaluate_all_rules(analysis, profile, repo_path=WELL_STRUCTURED_REPO)

    payload = build_sanitized_llm_payload(findings[0], allow_internal_names=False)
    assert payload["evidence_summary"][0]["file_ref"] == "file_1.py"

    # Simulate valid custom LLM callable
    def mock_llm_ok(_inp: dict) -> str:
        return json.dumps(
            {
                "accessible_explanation": "Explicação acessível gerada em teste controlado.",
                "suggested_documents_to_review": ["SOUP List", "Software System Test Plan"],
                "preliminary_corrective_actions": ["Revisar evidências com engenheiro de qualidade."],
            }
        )

    cfg = TraceASTConfig(enable_llm=True)
    enriched, log_ok = enrich_findings_with_optional_llm(findings, cfg, custom_llm_callable=mock_llm_ok)
    assert log_ok["calls_succeeded"] == 8
    for orig, enr in zip(findings, enriched):
        assert orig.status == enr.status
        assert enr.llm_explanation is not None

    # Simulate failing LLM callable — pipeline must not crash and must preserve findings
    def mock_llm_fail(_inp: dict) -> str:
        raise RuntimeError("Simulated API timeout")

    fallback_findings, log_fail = enrich_findings_with_optional_llm(findings, cfg, custom_llm_callable=mock_llm_fail)
    assert log_fail["calls_failed"] == 8
    assert len(fallback_findings) == 8
    assert fallback_findings[0].llm_explanation is None


def test_12_missing_repository_and_empty_directory_handling(tmp_path: Path) -> None:
    """Verify missing path raises FileNotFoundError and empty directory produces unable_to_assess for R01."""
    with pytest.raises(FileNotFoundError):
        analyze_repository_static(tmp_path / "non_existent_repo_dir")

    empty_repo = tmp_path / "empty_repo"
    empty_repo.mkdir()
    analysis = analyze_repository_static(empty_repo)
    findings = evaluate_all_rules(analysis, load_product_profile(None), repo_path=empty_repo)
    assert findings[0].rule_id == "R01"
    assert findings[0].status == FindingStatus.UNABLE_TO_ASSESS


# ---------------------------------------------------------------------------
# 9 & 10. Full Pipeline Execution, Report Generation, and Scientific Evaluation
# ---------------------------------------------------------------------------

def test_13_full_pipeline_execution_and_artifacts(tmp_path: Path) -> None:
    """Verify end-to-end pipeline generates findings.json, report.md, run_manifest.json, repository_inventory.json, retrieval_trace.json, and analysis_metrics.json."""
    out_dir = tmp_path / "run_output"
    res = run_pre_audit_pipeline(
        repo_target=WELL_STRUCTURED_REPO,
        out_dir=out_dir,
        profile_path=PROJECT_ROOT / "product_profile.example.yaml",
    )

    for expected_file in (
        "findings.json",
        "report.md",
        "run_manifest.json",
        "repository_inventory.json",
        "retrieval_trace.json",
        "analysis_metrics.json",
    ):
        fpath = out_dir / expected_file
        assert fpath.exists(), f"Missing output artifact: {expected_file}"

    validated = FindingsReport.model_validate_json((out_dir / "findings.json").read_text(encoding="utf-8"))
    assert len(validated.findings) == 8
    md_text = (out_dir / "report.md").read_text(encoding="utf-8")
    for section_header in (
        "## A. Identificação",
        "## B. Integridade da Análise",
        "## C. Visão Geral dos Indicadores Técnicos",
        "## D. Achados Detalhados",
        "## E. Referências Regulatórias e Rastreabilidade Documental",
        "## F. Plano de Ação Preliminar Organizado por Prioridade de Revisão",
    ):
        assert section_header in md_text


def test_14_scientific_evaluation_scoring_kappa_and_rag_recall(tmp_path: Path) -> None:
    """Verify scientific scoring engine, non-penalization of not_applicable, Cohen's kappa, cluster bootstrap CIs, and RAG Recall@3."""
    # Verify Fase 12 rule: tool 'not_observed' when human says 'not_applicable' or 'unable_to_assess' is TN, not FN!
    assert classify_pair_outcome("not_observed", "not_applicable") == "TN"
    assert classify_pair_outcome("not_observed", "unable_to_assess") == "TN"
    assert classify_pair_outcome("observed", "observed") == "TP"
    assert classify_pair_outcome("observed", "not_observed") == "FP"
    assert classify_pair_outcome("not_observed", "observed") == "FN"

    kappa_perfect = compute_cohens_kappa(["observed", "not_observed"], ["observed", "not_observed"])
    assert kappa_perfect == 1.0

    templates = generate_expert_annotation_templates(tmp_path / "templates")
    assert len(templates) == 4

    synth_metrics = generate_and_score_synthetic_benchmark(tmp_path)
    assert synth_metrics["is_synthetic_data"] is True
    assert synth_metrics["repositories_evaluated"] == 10
    assert "precision_95_ci" in synth_metrics["confidence_intervals_95"]

    rag_eval = evaluate_rag_recall_at_k(PROJECT_ROOT / "legal_documents", k=3, output_dir=tmp_path)
    assert rag_eval["total_queries"] == 8
    assert rag_eval["hit_rate_recall_at_k"] >= 0.75


def test_15_cli_commands_execution(tmp_path: Path) -> None:
    """Verify CLI version and scan subcommands return exit code 0."""
    assert cli_main(["version"]) == 0
    scan_out = tmp_path / "cli_scan"
    rc = cli_main(
        [
            "scan",
            "--repo",
            str(WELL_STRUCTURED_REPO),
            "--profile",
            str(PROJECT_ROOT / "product_profile.example.yaml"),
            "--out",
            str(scan_out),
        ]
    )
    assert rc == 0
    assert (scan_out / "findings.json").exists()


def test_16_documentation_portal_links_and_sections() -> None:
    """Verify bilingual docs (docs/index.html, docs/index.pt-br.html, and all Markdown pairs) exist, contain all 20 sections, and have valid links."""
    import re

    docs_dir = PROJECT_ROOT / "docs"
    index_en = docs_dir / "index.html"
    index_pt = docs_dir / "index.pt-br.html"
    styles_css = docs_dir / "styles.css"
    app_js = docs_dir / "app.js"

    assert index_en.exists()
    assert index_pt.exists()
    assert styles_css.exists()
    assert app_js.exists()

    css_text = styles_css.read_text(encoding="utf-8")
    js_text = app_js.read_text(encoding="utf-8")
    assert len(css_text) > 2000
    assert len(js_text) > 1000

    for html_file, expected_counterpart in ((index_en, "index.pt-br.html"), (index_pt, "index.html")):
        html_text = html_file.read_text(encoding="utf-8")
        assert len(html_text) > 25000
        assert expected_counterpart in html_text, f"{html_file.name} must link to {expected_counterpart}"

        # Verify all 20 required sections (#sec-01 .. #sec-20) exist as IDs
        all_ids = set(re.findall(r'\bid="([^"]+)"', html_text))
        for sec_num in range(1, 21):
            sec_id = f"sec-{sec_num:02d}"
            assert sec_id in all_ids, f"Missing required documentation section ID {sec_id} in {html_file.name}"

        # Verify all internal anchor links (#...) resolve to an existing ID
        anchor_hrefs = re.findall(r'\bhref="#([^"]+)"', html_text)
        assert len(anchor_hrefs) >= 20
        for target_id in anchor_hrefs:
            assert target_id in all_ids, f"Broken internal anchor link #{target_id} in {html_file.name}"

        # Verify all relative file links resolve to real files on disk
        rel_links = re.findall(r'\b(?:href|src)="(\.\.?/[^"#?]+)"', html_text)
        assert len(rel_links) >= 20
        for rel in rel_links:
            resolved = (docs_dir / rel).resolve()
            assert resolved.exists(), f"Broken relative file link '{rel}' in {html_file.name} -> {resolved} does not exist"

    # Verify all 6 bilingual Markdown pairs exist and cross-link to each other
    md_bases = [
        "README",
        "ARCHITECTURE",
        "RULE_CATALOG",
        "VALIDATION_PROTOCOL",
        "REPRODUCIBILITY",
        "LIMITATIONS",
    ]
    for base in md_bases:
        en_file = PROJECT_ROOT / f"{base}.md"
        pt_file = PROJECT_ROOT / f"{base}.pt-br.md"
        assert en_file.exists(), f"Missing English markdown file: {en_file.name}"
        assert pt_file.exists(), f"Missing Portuguese markdown file: {pt_file.name}"
        en_text = en_file.read_text(encoding="utf-8")
        pt_text = pt_file.read_text(encoding="utf-8")
        assert f"{base}.pt-br.md" in en_text, f"{en_file.name} must link to {pt_file.name}"
        assert f"{base}.md" in pt_text, f"{pt_file.name} must link to {en_file.name}"



