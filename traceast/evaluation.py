"""Scientific evaluation module for JMIR Medical Informatics study: expert scoring, Cohen's kappa, cluster bootstrap CIs, RAG Recall@3, and 20-repository benchmark execution."""

from __future__ import annotations

import csv
import json
import os
from pathlib import Path
import random
import shutil
import subprocess
import time
from typing import Any, Dict, List, Optional, Set, Tuple

from traceast.config import TraceASTConfig
from traceast.pipeline import _remove_read_only, run_pre_audit_pipeline
from traceast.rag_engine import RegulatoryRAGEngine
from traceast.rule_catalog import RULE_DEFINITIONS

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TEST_SET_MANIFEST_PATH = PROJECT_ROOT / "test_set_manifest.json"

ANNOTATION_CSV_COLUMNS: List[str] = [
    "repository_id",
    "repository_name",
    "repository_url",
    "commit_sha",
    "expected_class",
    "rule_id",
    "rule_title",
    "reviewer_id",
    "evidence_present",
    "evidence_absent",
    "evidence_partial",
    "unable_to_assess",
    "not_applicable",
    "status_label",
    "review_priority",
    "related_file_and_line",
    "justification",
    "warrants_human_audit_investigation",
    "reviewer_notes",
]

POSITIVE_SIGNAL_STATES: Set[str] = {"observed", "partial"}
NEGATIVE_SIGNAL_STATES: Set[str] = {"not_observed"}
EXCLUDED_OR_INAPPLICABLE_STATES: Set[str] = {"not_applicable", "unable_to_assess"}


def load_test_set_manifest(manifest_path: Optional[Path] = None) -> Dict[str, Any]:
    """Load the frozen 20-repository external test set manifest from test_set_manifest.json."""
    target = Path(manifest_path or DEFAULT_TEST_SET_MANIFEST_PATH).resolve()
    if target.exists():
        return json.loads(target.read_text(encoding="utf-8"))
    return {"generated": "2026-11-04", "excluded": ["Medical-Report-Generator-from-Chest-X-Ray-Images"], "repos": []}


def generate_expert_annotation_templates(
    output_dir: Path,
    manifest_path: Optional[Path] = None,
) -> Dict[str, str]:
    """
    Create the 160-row CSV annotation sheets (20 external test repositories x 8 rules)
    for two independent reviewers, a third adjudicator, and the consolidated consensus file.
    """
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = load_test_set_manifest(manifest_path)
    repos = manifest.get("repos", [])

    files_created: Dict[str, str] = {}
    for role in ("reviewer_1", "reviewer_2", "adjudicator_3", "consensus"):
        fname = f"expert_annotation_{role}_template.csv"
        fpath = output_dir / fname
        with open(fpath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=ANNOTATION_CSV_COLUMNS)
            writer.writeheader()
            if repos:
                for repo in repos:
                    repo_id = f"TEST-{int(repo['id']):03d}"
                    for rule in RULE_DEFINITIONS:
                        writer.writerow(
                            {
                                "repository_id": repo_id,
                                "repository_name": repo["repo"],
                                "repository_url": repo["url"],
                                "commit_sha": repo["commit_sha"],
                                "expected_class": repo.get("expected_class", ""),
                                "rule_id": rule.rule_id,
                                "rule_title": rule.title,
                                "reviewer_id": role,
                                "evidence_present": "",
                                "evidence_absent": "",
                                "evidence_partial": "",
                                "unable_to_assess": "",
                                "not_applicable": "",
                                "status_label": "",
                                "review_priority": "",
                                "related_file_and_line": "",
                                "justification": "",
                                "warrants_human_audit_investigation": "",
                                "reviewer_notes": "",
                            }
                        )
            else:
                for idx in range(1, 21):
                    repo_id = f"TEST-{idx:03d}"
                    for rule in RULE_DEFINITIONS:
                        writer.writerow(
                            {
                                "repository_id": repo_id,
                                "repository_name": "",
                                "repository_url": "",
                                "commit_sha": "",
                                "expected_class": "",
                                "rule_id": rule.rule_id,
                                "rule_title": rule.title,
                                "reviewer_id": role,
                                "evidence_present": "",
                                "evidence_absent": "",
                                "evidence_partial": "",
                                "unable_to_assess": "",
                                "not_applicable": "",
                                "status_label": "",
                                "review_priority": "",
                                "related_file_and_line": "",
                                "justification": "",
                                "warrants_human_audit_investigation": "",
                                "reviewer_notes": "",
                            }
                        )
        files_created[role] = str(fpath)
    return files_created


def compute_cohens_kappa(labels_r1: List[str], labels_r2: List[str]) -> float:
    """Calculate unweighted Cohen's kappa for inter-rater agreement between two independent reviewers."""
    if len(labels_r1) != len(labels_r2) or len(labels_r1) == 0:
        raise ValueError("Reviewer label lists must be non-empty and have the same length.")

    n = len(labels_r1)
    categories = sorted(set(labels_r1) | set(labels_r2))
    if len(categories) <= 1:
        return 1.0

    observed_agreements = sum(1 for a, b in zip(labels_r1, labels_r2) if a == b)
    p_o = observed_agreements / n

    p_e = 0.0
    for cat in categories:
        p_1 = sum(1 for a in labels_r1 if a == cat) / n
        p_2 = sum(1 for b in labels_r2 if b == cat) / n
        p_e += p_1 * p_2

    if abs(1.0 - p_e) < 1e-12:
        return 1.0
    return round((p_o - p_e) / (1.0 - p_e), 4)


def classify_pair_outcome(tool_status: str, human_status: str) -> str:
    """
    Classify a single (tool_status, human_status) comparison into TP, FP, FN, or TN.
    When the human reference standard classifies a rule as 'not_applicable' or 'unable_to_assess',
    a tool output of 'not_observed', 'not_applicable', or 'unable_to_assess' is scored as TN (never FN).
    """
    t = tool_status.strip().lower()
    h = human_status.strip().lower()

    if h in EXCLUDED_OR_INAPPLICABLE_STATES:
        if t in NEGATIVE_SIGNAL_STATES or t in EXCLUDED_OR_INAPPLICABLE_STATES:
            return "TN"
        return "FP"

    tool_positive = t in POSITIVE_SIGNAL_STATES
    human_positive = h in POSITIVE_SIGNAL_STATES

    if tool_positive and human_positive:
        return "TP"
    if tool_positive and not human_positive:
        return "FP"
    if not tool_positive and human_positive:
        return "FN"
    return "TN"


def _compute_prf1(tp: int, fp: int, fn: int, tn: int) -> Dict[str, Any]:
    precision = (tp / (tp + fp)) if (tp + fp) > 0 else 0.0
    recall = (tp / (tp + fn)) if (tp + fn) > 0 else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0.0
    return {
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "tn": tn,
        "precision": round(precision, 4),
        "recall_sensitivity": round(recall, 4),
        "f1_score": round(f1, 4),
    }


def score_tool_against_consensus(
    records: List[Dict[str, str]],
    n_bootstrap: int = 1000,
    random_seed: int = 42,
    is_synthetic: bool = False,
) -> Dict[str, Any]:
    """
    Compare tool findings against expert consensus across repositories.
    Each record requires: {'repository_id', 'rule_id', 'tool_status', 'consensus_status'}.
    Computes per-rule metrics, aggregated micro/macro metrics, and 95% cluster bootstrap CIs
    resampling at the repository level.
    """
    by_rule: Dict[str, Dict[str, int]] = {}
    by_repo: Dict[str, List[Tuple[str, str, str]]] = {}

    for rec in records:
        repo_id = rec["repository_id"]
        rule_id = rec["rule_id"]
        t_stat = rec["tool_status"]
        c_stat = rec["consensus_status"]
        outcome = classify_pair_outcome(t_stat, c_stat)

        if rule_id not in by_rule:
            by_rule[rule_id] = {"TP": 0, "FP": 0, "FN": 0, "TN": 0}
        by_rule[rule_id][outcome] += 1

        by_repo.setdefault(repo_id, []).append((rule_id, t_stat, c_stat))

    per_rule_results: Dict[str, Any] = {}
    total_tp = total_fp = total_fn = total_tn = 0
    for rule_id in sorted(by_rule.keys()):
        counts = by_rule[rule_id]
        total_tp += counts["TP"]
        total_fp += counts["FP"]
        total_fn += counts["FN"]
        total_tn += counts["TN"]
        per_rule_results[rule_id] = _compute_prf1(
            counts["TP"], counts["FP"], counts["FN"], counts["TN"]
        )

    aggregate_micro = _compute_prf1(total_tp, total_fp, total_fn, total_tn)
    if per_rule_results:
        macro_p = sum(v["precision"] for v in per_rule_results.values()) / len(per_rule_results)
        macro_r = sum(v["recall_sensitivity"] for v in per_rule_results.values()) / len(per_rule_results)
        macro_f1 = sum(v["f1_score"] for v in per_rule_results.values()) / len(per_rule_results)
    else:
        macro_p = macro_r = macro_f1 = 0.0

    repo_ids = sorted(by_repo.keys())
    rng = random.Random(random_seed)
    boot_precisions: List[float] = []
    boot_recalls: List[float] = []
    boot_f1s: List[float] = []

    if len(repo_ids) >= 2 and n_bootstrap > 0:
        for _ in range(n_bootstrap):
            sampled_repos = [rng.choice(repo_ids) for _ in range(len(repo_ids))]
            b_tp = b_fp = b_fn = b_tn = 0
            for r_id in sampled_repos:
                for _, t_stat, c_stat in by_repo[r_id]:
                    out = classify_pair_outcome(t_stat, c_stat)
                    if out == "TP":
                        b_tp += 1
                    elif out == "FP":
                        b_fp += 1
                    elif out == "FN":
                        b_fn += 1
                    else:
                        b_tn += 1
            m = _compute_prf1(b_tp, b_fp, b_fn, b_tn)
            boot_precisions.append(m["precision"])
            boot_recalls.append(m["recall_sensitivity"])
            boot_f1s.append(m["f1_score"])

        boot_precisions.sort()
        boot_recalls.sort()
        boot_f1s.sort()
        lo_idx = max(0, int(0.025 * len(boot_precisions)))
        hi_idx = min(len(boot_precisions) - 1, int(0.975 * len(boot_precisions)))
        ci_95 = {
            "resampling_unit": "repository_id (cluster bootstrap)",
            "repositories_count": len(repo_ids),
            "bootstrap_iterations": n_bootstrap,
            "precision_95_ci": [boot_precisions[lo_idx], boot_precisions[hi_idx]],
            "recall_95_ci": [boot_recalls[lo_idx], boot_recalls[hi_idx]],
            "f1_95_ci": [boot_f1s[lo_idx], boot_f1s[hi_idx]],
        }
    else:
        ci_95 = {
            "resampling_unit": "repository_id (cluster bootstrap)",
            "repositories_count": len(repo_ids),
            "bootstrap_iterations": 0,
            "note": "Confidence interval calculation requires at least 2 evaluated repositories.",
        }

    return {
        "data_nature": (
            "SYNTHETIC_BENCHMARK_VERIFICATION_DATA"
            if is_synthetic
            else "EXPERT_CONSENSUS_EVALUATION_DATA"
        ),
        "is_synthetic_data": is_synthetic,
        "repositories_evaluated": len(repo_ids),
        "total_rule_evaluations": len(records),
        "aggregated_micro": aggregate_micro,
        "aggregated_macro": {
            "precision": round(macro_p, 4),
            "recall_sensitivity": round(macro_r, 4),
            "f1_score": round(macro_f1, 4),
        },
        "confidence_intervals_95": ci_95,
        "per_rule_metrics": per_rule_results,
    }


def score_consensus_from_csv(
    consensus_csv: Path,
    tool_predictions_csv: Path,
    reviewer1_csv: Optional[Path] = None,
    reviewer2_csv: Optional[Path] = None,
    output_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    Compute final study metrics by matching the completed expert consensus CSV against
    the 160 tool predictions CSV (and optionally computing Cohen's kappa from Reviewer 1 & 2 CSVs).
    """
    tool_map: Dict[Tuple[str, str], str] = {}
    with open(tool_predictions_csv, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            tool_map[(row["repository_id"].strip(), row["rule_id"].strip())] = row["tool_status"].strip()

    records: List[Dict[str, str]] = []
    with open(consensus_csv, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            repo_id = row["repository_id"].strip()
            rule_id = row["rule_id"].strip()
            c_stat = row.get("status_label", "").strip()
            if not c_stat:
                continue
            t_stat = tool_map.get((repo_id, rule_id))
            if t_stat is None:
                continue
            records.append(
                {
                    "repository_id": repo_id,
                    "rule_id": rule_id,
                    "tool_status": t_stat,
                    "consensus_status": c_stat,
                }
            )

    result = score_tool_against_consensus(records=records, n_bootstrap=1000, random_seed=42, is_synthetic=False)

    if reviewer1_csv and reviewer2_csv and Path(reviewer1_csv).exists() and Path(reviewer2_csv).exists():
        r1_map: Dict[Tuple[str, str], str] = {}
        r2_map: Dict[Tuple[str, str], str] = {}
        with open(reviewer1_csv, "r", encoding="utf-8") as f1:
            for row in csv.DictReader(f1):
                lbl = row.get("status_label", "").strip()
                if lbl:
                    r1_map[(row["repository_id"].strip(), row["rule_id"].strip())] = lbl
        with open(reviewer2_csv, "r", encoding="utf-8") as f2:
            for row in csv.DictReader(f2):
                lbl = row.get("status_label", "").strip()
                if lbl:
                    r2_map[(row["repository_id"].strip(), row["rule_id"].strip())] = lbl
        common_keys = sorted(set(r1_map.keys()) & set(r2_map.keys()))
        if common_keys:
            result["inter_rater_agreement_cohens_kappa"] = compute_cohens_kappa(
                [r1_map[k] for k in common_keys],
                [r2_map[k] for k in common_keys],
            )
            result["inter_rater_paired_items"] = len(common_keys)

    if output_dir is not None:
        out_path = Path(output_dir).resolve()
        out_path.mkdir(parents=True, exist_ok=True)
        (out_path / "final_expert_vs_tool_evaluation.json").write_text(
            json.dumps(result, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        per_rule_csv = out_path / "final_expert_vs_tool_evaluation_per_rule.csv"
        with open(per_rule_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["rule_id", "tp", "fp", "fn", "tn", "precision", "recall_sensitivity", "f1_score"],
            )
            writer.writeheader()
            for r_id, metrics in result["per_rule_metrics"].items():
                writer.writerow({"rule_id": r_id, **metrics})

    return result


def generate_and_score_synthetic_benchmark(output_dir: Optional[Path] = None) -> Dict[str, Any]:
    """
    Generate synthetic benchmark data across 10 fictional repositories (80 rule evaluations)
    to verify the scoring engine, Cohen's kappa calculation, and cluster bootstrap CIs.
    """
    synthetic_records: List[Dict[str, str]] = []
    r1_labels: List[str] = []
    r2_labels: List[str] = []

    rng = random.Random(20260623)
    statuses = ["observed", "partial", "not_observed", "not_applicable", "unable_to_assess"]

    for repo_idx in range(1, 11):
        repo_id = f"SYNTH_REPO_{repo_idx:02d}"
        for rule in RULE_DEFINITIONS:
            gt = rng.choice(["observed", "partial", "not_observed", "not_applicable"])
            r1 = gt
            r2 = gt if rng.random() < 0.85 else rng.choice(statuses[:3])
            r1_labels.append(r1)
            r2_labels.append(r2)

            if gt == "not_applicable":
                tool = "not_observed" if rng.random() < 0.8 else "partial"
            elif rng.random() < 0.88:
                tool = gt
            else:
                tool = "observed" if gt == "not_observed" else "not_observed"

            synthetic_records.append(
                {
                    "repository_id": repo_id,
                    "rule_id": rule.rule_id,
                    "tool_status": tool,
                    "consensus_status": gt,
                }
            )

    kappa = compute_cohens_kappa(r1_labels, r2_labels)
    scoring = score_tool_against_consensus(
        records=synthetic_records,
        n_bootstrap=500,
        random_seed=42,
        is_synthetic=True,
    )
    scoring["inter_rater_agreement_cohens_kappa"] = kappa

    if output_dir is not None:
        out_path = Path(output_dir).resolve()
        out_path.mkdir(parents=True, exist_ok=True)
        (out_path / "synthetic_scoring_validation.json").write_text(
            json.dumps(scoring, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
    return scoring


DEFAULT_RAG_BENCHMARK_QUERIES: List[Dict[str, Any]] = [
    {
        "query_id": "Q_R01",
        "rule_id": "R01",
        "query_pt": "verificação de unidades de software inspeção de código-fonte documentação técnica RDC 657 IEC 62304",
        "query_en": "software unit verification source code inspection software configuration items IEC 62304 5.5",
        "expected_document_ids": ["IEC62304_OPENREG_MAPPING", "ANVISA_RDC_657_2022"],
    },
    {
        "query_id": "Q_R02",
        "rule_id": "R02",
        "query_pt": "SOUP Software of Unknown Provenance bibliotecas de terceiros gerenciamento de configuração versão dependências IEC 62304 8.1.2 5.3.3",
        "query_en": "SOUP list Software of Unknown Provenance third-party libraries version requirements.txt IEC 62304 8.1.2",
        "expected_document_ids": ["IEC62304_OPENREG_SOUP", "IEC62304_OPENREG_MAPPING"],
    },
    {
        "query_id": "Q_R03",
        "rule_id": "R03",
        "query_pt": "plano de testes de sistema de software verificação de unidade testes de integração validação RDC 657 IEC 62304 5.7",
        "query_en": "software system test plan unit verification integration testing regression tests IEC 62304 5.5 5.6 5.7",
        "expected_document_ids": ["IEC62304_OPENREG_TEST_PLAN", "IEC62304_OPENREG_MAPPING"],
    },
    {
        "query_id": "Q_R04",
        "rule_id": "R04",
        "query_pt": "integração contínua CI/CD testes de regressão verificação de integração pull requests IEC 62304 5.6.6",
        "query_en": "CI/CD in GitHub Pull Requests software integration testing conduct regression tests IEC 62304 5.6.6",
        "expected_document_ids": ["IEC62304_OPENREG_MAPPING"],
    },
    {
        "query_id": "Q_R05",
        "rule_id": "R05",
        "query_pt": "identificação e prevenção de defeitos de software controle de risco falhas tratamento de erros IEC 62304 7.1",
        "query_en": "identification and avoidance of common software defects risk control measures software units IEC 62304 5.1.12 7.1.2",
        "expected_document_ids": ["IEC62304_OPENREG_MAPPING", "IEC62304_OPENREG_SOUP"],
    },
    {
        "query_id": "Q_R06",
        "rule_id": "R06",
        "query_pt": "requisitos de software interfaces dados de entrada arquitetura de interfaces verificação IEC 62304 5.3.2",
        "query_en": "develop an architecture for the interfaces of software items input validation software requirements IEC 62304 5.3.2",
        "expected_document_ids": ["IEC62304_OPENREG_ARCH_CHECKLIST", "IEC62304_OPENREG_MAPPING", "IEC62304_OPENREG_REQ_LIST"],
    },
    {
        "query_id": "Q_R07",
        "rule_id": "R07",
        "query_pt": "desenvolvimento de modelos de aprendizado de máquina controle de versão hiperparâmetros relatório de validação de algoritmo itens de configuração IEC 62304 8.1.1",
        "query_en": "machine learning model development version control hyperparameters Algorithm Validation Report configuration items IEC 62304 8.1.1",
        "expected_document_ids": ["OPENREG_SOP_ML_DEV", "OPENREG_ALGO_VALIDATION"],
    },
    {
        "query_id": "Q_R08",
        "rule_id": "R08",
        "query_pt": "separação entre ambiente de desenvolvimento treinamento e ambiente de produção inferência arquitetura de software segregação IEC 62304 5.3",
        "query_en": "configuration of development environment separated from the production environment production deployment of ML model IEC 62304 5.3",
        "expected_document_ids": ["OPENREG_SOP_ML_DEV", "IEC62304_OPENREG_DEPLOYMENT"],
    },
]


def evaluate_rag_recall_at_k(
    legal_docs_dir: Path,
    benchmark_queries: Optional[List[Dict[str, Any]]] = None,
    k: int = 3,
    output_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """Evaluate RAG retrieval using Recall@3 against the normative query reference set."""
    queries = benchmark_queries if benchmark_queries is not None else DEFAULT_RAG_BENCHMARK_QUERIES
    engine = RegulatoryRAGEngine(legal_docs_dir=legal_docs_dir)

    query_results: List[Dict[str, Any]] = []
    hits_at_k = 0
    fractional_recalls: List[float] = []

    for q in queries:
        retrieved = engine.retrieve_for_query(
            query_pt=q["query_pt"],
            query_en=q.get("query_en", ""),
            top_k=k,
        )
        retrieved_doc_ids = [r["document_id"] for r in retrieved]
        expected_ids = set(q.get("expected_document_ids", []))
        matched_ids = sorted(expected_ids & set(retrieved_doc_ids))
        hit = len(matched_ids) > 0
        if hit:
            hits_at_k += 1
        frac_recall = (len(matched_ids) / len(expected_ids)) if expected_ids else 0.0
        fractional_recalls.append(frac_recall)

        query_results.append(
            {
                "query_id": q["query_id"],
                "rule_id": q["rule_id"],
                "expected_document_ids": sorted(expected_ids),
                "retrieved_document_ids": retrieved_doc_ids,
                "retrieved_chunk_ids": [r["chunk_id"] for r in retrieved],
                "matched_document_ids": matched_ids,
                "hit_at_k": hit,
                "fractional_recall_at_k": round(frac_recall, 4),
            }
        )

    total_q = len(queries)
    hit_rate_at_k = round(hits_at_k / total_q, 4) if total_q > 0 else 0.0
    mean_recall_at_k = round(sum(fractional_recalls) / total_q, 4) if total_q > 0 else 0.0

    report = {
        "evaluation_type": f"RAG_Recall@{k}",
        "annotation_status": "NORMATIVE_QUERY_REFERENCE_BENCHMARK",
        "k": k,
        "total_queries": total_q,
        "queries_with_relevant_hit_at_k": hits_at_k,
        "hit_rate_recall_at_k": hit_rate_at_k,
        "mean_fractional_recall_at_k": mean_recall_at_k,
        "retrieval_backend": engine.backend_used,
        "per_query_results": query_results,
    }

    if output_dir is not None:
        out_path = Path(output_dir).resolve()
        out_path.mkdir(parents=True, exist_ok=True)
        (out_path / f"rag_recall_at_{k}_evaluation.json").write_text(
            json.dumps(report, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
    return report


def generate_study_dataset_manifest(
    output_dir: Path,
    manifest_path: Optional[Path] = None,
) -> Path:
    """
    Create the dataset split manifest separating development repositories from the 20 external
    test repositories defined in test_set_manifest.json.
    """
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    raw_test_manifest = load_test_set_manifest(manifest_path)
    repos = raw_test_manifest.get("repos", [])

    test_slots: List[Dict[str, Any]] = []
    for repo in repos:
        repo_id = f"TEST-{int(repo['id']):03d}"
        test_slots.append(
            {
                "repository_id": repo_id,
                "name": repo["repo"],
                "url": repo["url"],
                "expected_class": repo.get("expected_class"),
                "commit_sha": repo["commit_sha"],
                "last_commit_date": repo.get("last_commit_date"),
                "python_pct_of_code_bytes": repo.get("python_pct_of_code_bytes"),
                "unit_test_files": repo.get("unit_test_files"),
                "ci_workflows": repo.get("ci_workflows"),
                "dependency_files_at_root": repo.get("dependency_files_at_root", []),
                "description": repo.get("description", ""),
                "rationale": repo.get("rationale", ""),
                "split": "test",
                "tool_execution_status": "completed",
                "expert_reviewer_1_status": "awaiting_independent_review",
                "expert_reviewer_2_status": "awaiting_independent_review",
                "adjudication_status": "awaiting_independent_review",
            }
        )

    manifest = {
        "study_title": "TraceAST-62304: AI-Assisted Evidence-Traceable Pre-Audit Screening for SaMD Repositories",
        "target_journal": "JMIR Medical Informatics",
        "generated_date": raw_test_manifest.get("generated", "2026-11-04"),
        "protocol_rule": (
            "Deterministic rules (R01–R08) were defined and calibrated exclusively on the development split. "
            "Modifying heuristics based on external test split results is strictly prohibited."
        ),
        "development_split": [
            {
                "repository_id": "DEV-001",
                "name": "Medical-Report-Generator-from-Chest-X-Ray-Images",
                "url": "https://github.com/anandr07/Medical-Report-Generator-from-Chest-X-Ray-Images",
                "license": "Public GitHub Repository (inspected locally without redistribution)",
                "split": "development",
                "role": (
                    "Repository used during initial Proof-of-Concept design; locked in the development split "
                    "and excluded from external test validation."
                ),
            }
        ],
        "external_test_split": {
            "target_sample_size": len(test_slots),
            "well_structured_count": sum(1 for r in test_slots if r.get("expected_class") == "well_structured"),
            "experimental_deficient_count": sum(
                1 for r in test_slots if r.get("expected_class") == "experimental_deficient"
            ),
            "current_status": "TOOL_EXECUTION_COMPLETED_AWAITING_BLIND_EXPERT_SHEETS",
            "selection_criteria": [
                "Public Python repositories with declared application in medical imaging, clinical decision support, or SaMD.",
                "Stratified sampling: 10 well-structured engineering repositories and 10 experimental/deficient research repositories.",
                "Frozen commit SHA prior to TraceAST-62304 execution and blind review by two independent specialists.",
            ],
            "planned_slots": test_slots,
            "repositories": test_slots,
        },
    }
    manifest_file = output_dir / "dataset_split_manifest.json"
    manifest_file.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return manifest_file


def checkout_repo_at_commit(repo_url: str, commit_sha: str, dest_dir: Path) -> Path:
    """
    Fetch and checkout the exact frozen commit_sha of a remote GitHub repository into dest_dir
    with GIT_LFS_SKIP_SMUDGE=1 so large binary weights are not downloaded unnecessarily.
    """
    dest_dir = Path(dest_dir).resolve()
    if dest_dir.exists():
        head_proc = subprocess.run(
            ["git", "-C", str(dest_dir), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=False,
        )
        if head_proc.returncode == 0 and head_proc.stdout.strip().lower() == commit_sha.lower():
            return dest_dir
        shutil.rmtree(dest_dir, onexc=_remove_read_only)

    dest_dir.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["GIT_LFS_SKIP_SMUDGE"] = "1"
    env["GIT_TERMINAL_PROMPT"] = "0"

    subprocess.run(["git", "init", str(dest_dir)], capture_output=True, text=True, check=True, env=env)
    subprocess.run(
        ["git", "-C", str(dest_dir), "remote", "add", "origin", repo_url],
        capture_output=True,
        text=True,
        check=True,
        env=env,
    )
    fetch_proc = subprocess.run(
        ["git", "-C", str(dest_dir), "fetch", "--depth", "1", "origin", commit_sha],
        capture_output=True,
        text=True,
        check=False,
        env=env,
    )
    if fetch_proc.returncode != 0:
        # Fallback to full fetch if server does not allow direct SHA shallow fetch
        subprocess.run(
            ["git", "-C", str(dest_dir), "fetch", "origin"],
            capture_output=True,
            text=True,
            check=True,
            env=env,
        )
        subprocess.run(
            ["git", "-C", str(dest_dir), "-c", "advice.detachedHead=false", "checkout", "-f", commit_sha],
            capture_output=True,
            text=True,
            check=True,
            env=env,
        )
    else:
        subprocess.run(
            ["git", "-C", str(dest_dir), "-c", "advice.detachedHead=false", "checkout", "-f", "FETCH_HEAD"],
            capture_output=True,
            text=True,
            check=True,
            env=env,
        )
    return dest_dir


def _write_test_set_markdown_reports(
    eval_out_dir: Path,
    summary_payload: Dict[str, Any],
) -> Tuple[Path, Path]:
    """Generate bilingual Markdown reports (EN primary + PT-BR equivalent) summarizing the 20-repository benchmark execution."""
    repos_results = summary_payload["repositories"]
    rule_ids = ["R01", "R02", "R03", "R04", "R05", "R06", "R07", "R08"]

    # 1. English Report (Primary)
    md_en: List[str] = [
        "# External Test Set Execution Report (20 Repositories) — TraceAST-62304 v1.0",
        "",
        "[![en](https://img.shields.io/badge/lang-English%20(Main)-blue.svg)](./TEST_SET_EXECUTION_REPORT.md)",
        "[![pt-br](https://img.shields.io/badge/lang-Portugu%C3%AAs%20(pt--BR)-green.svg)](./TEST_SET_EXECUTION_REPORT.pt-br.md)",
        "",
        "> 🌐 **Language / Idioma:** **English (Primary — `TEST_SET_EXECUTION_REPORT.md`)** | **[Ler em Português (`TEST_SET_EXECUTION_REPORT.pt-br.md`)](./TEST_SET_EXECUTION_REPORT.pt-br.md)**",
        "",
        "## 1. Benchmark Execution Summary",
        "",
        f"- **Total Repositories Analyzed:** `{summary_payload['total_repositories_analyzed']}` (`10` `well_structured` + `10` `experimental_deficient`)",
        f"- **Total Rule Evaluations Generated:** `{summary_payload['total_rule_evaluations']}` (`20` repositories $\\times$ `8` rules)",
        f"- **Rule Catalog Version & SHA-256:** `v{summary_payload['rule_catalog_version']}` (`{summary_payload['rule_catalog_sha256'][:16]}...`)",
        f"- **Total Python Files Inspected Across 20 Repositories:** `{summary_payload['aggregate_codebase_stats']['total_python_files_found']}` (`{summary_payload['aggregate_codebase_stats']['total_python_files_parsed']}` parsed successfully)",
        f"- **Total Execution Time (20 Repositories):** `{summary_payload['total_duration_seconds']}s`",
        "",
        "---",
        "",
        "## 2. Per-Repository Rule Status Matrix (`R01`–`R08`)",
        "",
        "| ID | Repository | Expected Class | Commit SHA | Py Files | Coverage | R01 | R02 | R03 | R04 | R05 | R06 | R07 | R08 | Report |",
        "|---|---|---|---|---:|---:|---|---|---|---|---|---|---|---|---|",
    ]

    for r in repos_results:
        statuses = r["rule_statuses"]
        rel_report = f"../reports/test_set/{r['output_folder_name']}/report.md"
        md_en.append(
            f"| `{r['repository_id']}` | `{r['repository_name']}` | `{r['expected_class']}` | `{r['commit_sha'][:8]}` | "
            f"{r['python_files_found']} | {r['inspection_coverage_percent']}% | "
            + " | ".join(f"`{statuses[rid]}`" for rid in rule_ids)
            + f" | [report.md]({rel_report}) |"
        )

    md_en.extend(
        [
            "",
            "---",
            "",
            "## 3. Distribution of Tool Statuses by Rule Across the 20 Repositories",
            "",
            "| Rule ID | Observed | Partial | Not Observed | Not Applicable | Unable to Assess |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for rid in rule_ids:
        dist = summary_payload["status_distribution_by_rule"][rid]
        md_en.append(
            f"| `{rid}` | {dist.get('observed', 0)} | {dist.get('partial', 0)} | {dist.get('not_observed', 0)} | "
            f"{dist.get('not_applicable', 0)} | {dist.get('unable_to_assess', 0)} |"
        )

    md_en.extend(
        [
            "",
            "---",
            "",
            "## 4. Generated Files Ready for Blind Expert Comparison",
            "",
            "- **160 Tool Predictions CSV:** [`test_set_160_tool_predictions.csv`](./test_set_160_tool_predictions.csv)",
            "- **20-Repository Summary CSV:** [`test_set_tool_results_summary.csv`](./test_set_tool_results_summary.csv)",
            "- **20-Repository Summary JSON:** [`test_set_tool_results_summary.json`](./test_set_tool_results_summary.json)",
            "- **Expert Reviewer 1 Blank Sheet (160 rows):** [`templates/expert_annotation_reviewer_1_template.csv`](./templates/expert_annotation_reviewer_1_template.csv)",
            "- **Expert Reviewer 2 Blank Sheet (160 rows):** [`templates/expert_annotation_reviewer_2_template.csv`](./templates/expert_annotation_reviewer_2_template.csv)",
            "- **Adjudicator 3 Blank Sheet (160 rows):** [`templates/expert_annotation_adjudicator_3_template.csv`](./templates/expert_annotation_adjudicator_3_template.csv)",
            "- **Final Consensus Blank Sheet (160 rows):** [`templates/expert_annotation_consensus_template.csv`](./templates/expert_annotation_consensus_template.csv)",
            "",
            "### How to Compute Final Study Metrics Once Expert Sheets Are Returned",
            "",
            "```bash",
            "python -m traceast score-consensus \\",
            "  --consensus-csv ./evaluation_artifacts/templates/expert_annotation_consensus_template.csv \\",
            "  --predictions-csv ./evaluation_artifacts/test_set_160_tool_predictions.csv \\",
            "  --reviewer1-csv ./evaluation_artifacts/templates/expert_annotation_reviewer_1_template.csv \\",
            "  --reviewer2-csv ./evaluation_artifacts/templates/expert_annotation_reviewer_2_template.csv \\",
            "  --out ./evaluation_artifacts",
            "```",
            "",
        ]
    )

    # 2. Portuguese Report (Equivalent)
    md_pt: List[str] = [
        "# Relatório de Execução no Conjunto de Teste Externo (20 Repositórios) — TraceAST-62304 v1.0 (Português)",
        "",
        "[![en](https://img.shields.io/badge/lang-English%20(Main)-blue.svg)](./TEST_SET_EXECUTION_REPORT.md)",
        "[![pt-br](https://img.shields.io/badge/lang-Portugu%C3%AAs%20(pt--BR)-green.svg)](./TEST_SET_EXECUTION_REPORT.pt-br.md)",
        "",
        "> 🌐 **Language / Idioma:** **[Read in English (Primary) — `TEST_SET_EXECUTION_REPORT.md`](./TEST_SET_EXECUTION_REPORT.md)** | **Português (`TEST_SET_EXECUTION_REPORT.pt-br.md`)**",
        "",
        "## 1. Resumo da Execução Experimental",
        "",
        f"- **Total de Repositórios Analisados:** `{summary_payload['total_repositories_analyzed']}` (`10` `well_structured` + `10` `experimental_deficient`)",
        f"- **Total de Avaliações de Regras Geradas:** `{summary_payload['total_rule_evaluations']}` (`20` repositórios $\\times$ `8` regras)",
        f"- **Versão e Hash SHA-256 do Catálogo de Regras:** `v{summary_payload['rule_catalog_version']}` (`{summary_payload['rule_catalog_sha256'][:16]}...`)",
        f"- **Total de Arquivos Python Inspecionados nos 20 Repositórios:** `{summary_payload['aggregate_codebase_stats']['total_python_files_found']}` (`{summary_payload['aggregate_codebase_stats']['total_python_files_parsed']}` analisados com sucesso)",
        f"- **Tempo Total de Execução (20 Repositórios):** `{summary_payload['total_duration_seconds']}s`",
        "",
        "---",
        "",
        "## 2. Matriz de Status por Repositório (`R01`–`R08`)",
        "",
        "| ID | Repositório | Classe Esperada | Commit SHA | Arqs .py | Cobertura | R01 | R02 | R03 | R04 | R05 | R06 | R07 | R08 | Relatório |",
        "|---|---|---|---|---:|---:|---|---|---|---|---|---|---|---|---|",
    ]

    for r in repos_results:
        statuses = r["rule_statuses"]
        rel_report = f"../reports/test_set/{r['output_folder_name']}/report.md"
        md_pt.append(
            f"| `{r['repository_id']}` | `{r['repository_name']}` | `{r['expected_class']}` | `{r['commit_sha'][:8]}` | "
            f"{r['python_files_found']} | {r['inspection_coverage_percent']}% | "
            + " | ".join(f"`{statuses[rid]}`" for rid in rule_ids)
            + f" | [report.md]({rel_report}) |"
        )

    md_pt.extend(
        [
            "",
            "---",
            "",
            "## 3. Distribuição dos Status por Regra nos 20 Repositórios",
            "",
            "| Rule ID | Observed | Partial | Not Observed | Not Applicable | Unable to Assess |",
            "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for rid in rule_ids:
        dist = summary_payload["status_distribution_by_rule"][rid]
        md_pt.append(
            f"| `{rid}` | {dist.get('observed', 0)} | {dist.get('partial', 0)} | {dist.get('not_observed', 0)} | "
            f"{dist.get('not_applicable', 0)} | {dist.get('unable_to_assess', 0)} |"
        )

    md_pt.extend(
        [
            "",
            "---",
            "",
            "## 4. Arquivos Gerados Prontos para Comparação com os Especialistas",
            "",
            "- **CSV com as 160 Predições da Ferramenta:** [`test_set_160_tool_predictions.csv`](./test_set_160_tool_predictions.csv)",
            "- **CSV Resumo dos 20 Repositórios:** [`test_set_tool_results_summary.csv`](./test_set_tool_results_summary.csv)",
            "- **JSON Resumo dos 20 Repositórios:** [`test_set_tool_results_summary.json`](./test_set_tool_results_summary.json)",
            "- **Planilha em Branco do Especialista 1 (160 linhas):** [`templates/expert_annotation_reviewer_1_template.csv`](./templates/expert_annotation_reviewer_1_template.csv)",
            "- **Planilha em Branco do Especialista 2 (160 linhas):** [`templates/expert_annotation_reviewer_2_template.csv`](./templates/expert_annotation_reviewer_2_template.csv)",
            "- **Planilha em Branco do Adjudicador 3 (160 linhas):** [`templates/expert_annotation_adjudicator_3_template.csv`](./templates/expert_annotation_adjudicator_3_template.csv)",
            "- **Planilha em Branco do Consenso Final (160 linhas):** [`templates/expert_annotation_consensus_template.csv`](./templates/expert_annotation_consensus_template.csv)",
            "",
            "### Como Calcular as Métricas Finais Assim que as Planilhas dos Especialistas Retornarem",
            "",
            "```bash",
            "python -m traceast score-consensus \\",
            "  --consensus-csv ./evaluation_artifacts/templates/expert_annotation_consensus_template.csv \\",
            "  --predictions-csv ./evaluation_artifacts/test_set_160_tool_predictions.csv \\",
            "  --reviewer1-csv ./evaluation_artifacts/templates/expert_annotation_reviewer_1_template.csv \\",
            "  --reviewer2-csv ./evaluation_artifacts/templates/expert_annotation_reviewer_2_template.csv \\",
            "  --out ./evaluation_artifacts",
            "```",
            "",
        ]
    )

    en_path = eval_out_dir / "TEST_SET_EXECUTION_REPORT.md"
    pt_path = eval_out_dir / "TEST_SET_EXECUTION_REPORT.pt-br.md"
    en_path.write_text("\n".join(md_en), encoding="utf-8")
    pt_path.write_text("\n".join(md_pt), encoding="utf-8")
    return en_path, pt_path


def run_external_test_set_benchmark(
    manifest_path: Optional[Path] = None,
    reports_out_dir: Optional[Path] = None,
    eval_out_dir: Optional[Path] = None,
    cache_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    """
    Clone/checkout all 20 repositories from test_set_manifest.json at their exact frozen commit SHAs,
    run the full TraceAST-62304 pipeline on each repository, and generate all per-repository reports,
    CSV/JSON summaries, and 160-row annotation templates.
    """
    t_start = time.perf_counter()
    manifest = load_test_set_manifest(manifest_path)
    repos = manifest.get("repos", [])

    reports_base = Path(reports_out_dir or (PROJECT_ROOT / "reports" / "test_set")).resolve()
    eval_base = Path(eval_out_dir or (PROJECT_ROOT / "evaluation_artifacts")).resolve()
    repos_cache = Path(cache_dir or (PROJECT_ROOT / ".test_repos_cache")).resolve()

    reports_base.mkdir(parents=True, exist_ok=True)
    eval_base.mkdir(parents=True, exist_ok=True)
    repos_cache.mkdir(parents=True, exist_ok=True)

    # Also regenerate the 160-row templates and study split manifest
    generate_expert_annotation_templates(eval_base / "templates", manifest_path=manifest_path)
    generate_study_dataset_manifest(eval_base, manifest_path=manifest_path)

    cfg = TraceASTConfig(enable_rag=True, enable_llm=False)
    rule_ids = ["R01", "R02", "R03", "R04", "R05", "R06", "R07", "R08"]
    status_dist: Dict[str, Dict[str, int]] = {
        rid: {"observed": 0, "partial": 0, "not_observed": 0, "not_applicable": 0, "unable_to_assess": 0}
        for rid in rule_ids
    }

    repos_summary_list: List[Dict[str, Any]] = []
    tool_predictions_160: List[Dict[str, Any]] = []

    total_py_found = 0
    total_py_parsed = 0
    total_py_failed = 0

    for idx, repo_meta in enumerate(repos, start=1):
        repo_id = f"TEST-{int(repo_meta['id']):03d}"
        repo_slug = repo_meta["repo"].replace("/", "__")
        folder_name = f"{repo_id}_{repo_slug}"
        repo_url = repo_meta["url"]
        commit_sha = repo_meta["commit_sha"]

        print(f"[{idx:02d}/{len(repos):02d}] Preparing {repo_id} ({repo_meta['repo']} @ {commit_sha[:8]})...")
        local_clone_dir = repos_cache / folder_name
        checkout_repo_at_commit(repo_url=repo_url, commit_sha=commit_sha, dest_dir=local_clone_dir)

        repo_report_dir = reports_base / folder_name
        res = run_pre_audit_pipeline(
            repo_target=local_clone_dir,
            out_dir=repo_report_dir,
            profile_path=None,
            config=cfg,
        )

        insp = res["analysis"]["inspection_summary"]
        sc = res["analysis_metrics"]["structural_counts"]
        findings = res["report"].findings

        total_py_found += insp["python_files_found"]
        total_py_parsed += insp["python_files_parsed_successfully"]
        total_py_failed += insp["python_files_failed"]

        rule_statuses: Dict[str, str] = {}
        for f in findings:
            st_val = f.status.value
            rule_statuses[f.rule_id] = st_val
            status_dist[f.rule_id][st_val] = status_dist[f.rule_id].get(st_val, 0) + 1
            first_ev = (
                f"{f.evidence[0].file}:{f.evidence[0].line_start}-{f.evidence[0].line_end}"
                if f.evidence
                else ""
            )
            tool_predictions_160.append(
                {
                    "repository_id": repo_id,
                    "repository_name": repo_meta["repo"],
                    "expected_class": repo_meta.get("expected_class", ""),
                    "commit_sha": res["analysis"]["commit_sha"],
                    "rule_id": f.rule_id,
                    "finding_id": f.finding_id,
                    "rule_title": f.title,
                    "tool_status": st_val,
                    "status_label_pt": f.status_label_pt,
                    "review_priority": f.review_priority.value,
                    "confidence": f.confidence.value,
                    "evidence_count": len(f.evidence),
                    "primary_evidence_location": first_ev,
                    "justification": f.justification,
                }
            )

        repos_summary_list.append(
            {
                "repository_id": repo_id,
                "repository_name": repo_meta["repo"],
                "url": repo_url,
                "expected_class": repo_meta.get("expected_class", ""),
                "commit_sha": res["analysis"]["commit_sha"],
                "output_folder_name": folder_name,
                "python_files_found": insp["python_files_found"],
                "python_files_parsed_successfully": insp["python_files_parsed_successfully"],
                "python_files_failed": insp["python_files_failed"],
                "inspection_coverage_percent": insp["inspection_coverage_percent"],
                "structural_counts": sc,
                "rule_statuses": rule_statuses,
                "summary_counts": res["report"].summary_counts,
                "duration_seconds": res["run_manifest"]["durations_seconds"]["total_pipeline"],
            }
        )

    total_elapsed = round(time.perf_counter() - t_start, 3)
    from traceast.rule_catalog import RULE_CATALOG_VERSION, compute_rule_catalog_hash

    summary_payload = {
        "study_title": "TraceAST-62304 External Test Set Benchmark Execution",
        "rule_catalog_version": RULE_CATALOG_VERSION,
        "rule_catalog_sha256": compute_rule_catalog_hash(),
        "total_repositories_analyzed": len(repos_summary_list),
        "total_rule_evaluations": len(tool_predictions_160),
        "total_duration_seconds": total_elapsed,
        "aggregate_codebase_stats": {
            "total_python_files_found": total_py_found,
            "total_python_files_parsed": total_py_parsed,
            "total_python_files_failed": total_py_failed,
        },
        "status_distribution_by_rule": status_dist,
        "repositories": repos_summary_list,
    }

    # Save JSON summary
    summary_json_path = eval_base / "test_set_tool_results_summary.json"
    summary_json_path.write_text(json.dumps(summary_payload, indent=2, ensure_ascii=False), encoding="utf-8")

    # Save 20-row summary CSV
    summary_csv_path = eval_base / "test_set_tool_results_summary.csv"
    csv_fields = [
        "repository_id",
        "repository_name",
        "expected_class",
        "commit_sha",
        "python_files_found",
        "python_files_parsed_successfully",
        "python_files_failed",
        "inspection_coverage_percent",
        "R01",
        "R02",
        "R03",
        "R04",
        "R05",
        "R06",
        "R07",
        "R08",
        "observed_count",
        "partial_count",
        "not_observed_count",
        "not_applicable_count",
        "unable_to_assess_count",
        "duration_seconds",
    ]
    with open(summary_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields)
        writer.writeheader()
        for r in repos_summary_list:
            row = {
                "repository_id": r["repository_id"],
                "repository_name": r["repository_name"],
                "expected_class": r["expected_class"],
                "commit_sha": r["commit_sha"],
                "python_files_found": r["python_files_found"],
                "python_files_parsed_successfully": r["python_files_parsed_successfully"],
                "python_files_failed": r["python_files_failed"],
                "inspection_coverage_percent": r["inspection_coverage_percent"],
                **r["rule_statuses"],
                "observed_count": r["summary_counts"]["observed"],
                "partial_count": r["summary_counts"]["partial"],
                "not_observed_count": r["summary_counts"]["not_observed"],
                "not_applicable_count": r["summary_counts"]["not_applicable"],
                "unable_to_assess_count": r["summary_counts"]["unable_to_assess"],
                "duration_seconds": r["duration_seconds"],
            }
            writer.writerow(row)

    # Save 160-row tool predictions CSV
    predictions_csv_path = eval_base / "test_set_160_tool_predictions.csv"
    pred_fields = [
        "repository_id",
        "repository_name",
        "expected_class",
        "commit_sha",
        "rule_id",
        "finding_id",
        "rule_title",
        "tool_status",
        "status_label_pt",
        "review_priority",
        "confidence",
        "evidence_count",
        "primary_evidence_location",
        "justification",
    ]
    with open(predictions_csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=pred_fields)
        writer.writeheader()
        for pred in tool_predictions_160:
            writer.writerow(pred)

    # Save bilingual Markdown execution reports
    _write_test_set_markdown_reports(eval_base, summary_payload)

    return summary_payload
