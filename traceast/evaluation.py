"""Scientific evaluation module for JMIR Medical Informatics study: expert scoring, Cohen's kappa, cluster bootstrap CIs, and RAG Recall@3."""

from __future__ import annotations

import csv
import json
import random
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from traceast.rag_engine import RegulatoryRAGEngine
from traceast.rule_catalog import RULE_DEFINITIONS

ANNOTATION_CSV_COLUMNS: List[str] = [
    "repository_id",
    "rule_id",
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


def generate_expert_annotation_templates(output_dir: Path) -> Dict[str, str]:
    """
    Create blank CSV templates for two independent reviewers, a third adjudicator,
    and the consolidated consensus file. Does NOT fabricate human evaluations.
    """
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    files_created: Dict[str, str] = {}
    for role in ("reviewer_1", "reviewer_2", "adjudicator_3", "consensus"):
        fname = f"expert_annotation_{role}_template.csv"
        fpath = output_dir / fname
        with open(fpath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=ANNOTATION_CSV_COLUMNS)
            writer.writeheader()
            for rule in RULE_DEFINITIONS:
                writer.writerow(
                    {
                        "repository_id": "REPO_ID_PLACEHOLDER",
                        "rule_id": rule.rule_id,
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
                        "reviewer_notes": "TEMPLATE EM BRANCO — AGUARDANDO AVALIAÇÃO HUMANA INDEPENDENTE",
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
    Classify a single (tool_status, human_status) comparison into TP, FP, FN, TN, or EXCLUDED_INAPPLICABLE.
    Follows Fase 12 rule:
    Do NOT treat tool 'not_observed' as a false negative when the human evaluator considers
    the rule 'not_applicable' or 'unable_to_assess'.
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

    # Cluster bootstrap resampling repositories with replacement
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
            "note": "Intervalo de confiança requer pelo menos 2 repositórios avaliados.",
        }

    return {
        "data_nature": (
            "SYNTHETIC_TEST_DATA — DADOS FICTÍCIOS EXCLUSIVOS PARA TESTE DO MOTOR DE PONTUAÇÃO"
            if is_synthetic
            else "EXPERT_EVALUATION_DATA"
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


def generate_and_score_synthetic_benchmark(output_dir: Optional[Path] = None) -> Dict[str, Any]:
    """
    Generate clearly labeled synthetic test data across 10 fictional repositories (80 rule evaluations)
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
            # Simulate high but imperfect reviewer agreement and tool performance
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
    """
    Evaluate RAG retrieval using Recall@3 against a pre-annotated query reference set.
    """
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
        "annotation_status": "PRELIMINARY_INTERNAL_REFERENCE_SET (Requer revisão final por especialistas humanos)",
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


def generate_study_dataset_manifest(output_dir: Path) -> Path:
    """
    Create the dataset split manifest separating development repositories from external test repositories
    (locking Medical-Report-Generator-from-Chest-X-Ray-Images in the development split per Fase 12.4).
    """
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "study_title": "TraceAST-62304: AI-Assisted Evidence-Traceable Pre-Audit Screening for SaMD Repositories",
        "target_journal": "JMIR Medical Informatics",
        "protocol_rule": (
            "As regras determinísticas (R01–R08) foram definidas e calibradas exclusivamente no conjunto de "
            "desenvolvimento (development_split). É estritamente proibido ajustar heurísticas com base nos "
            "resultados do conjunto de teste (external_test_split)."
        ),
        "development_split": [
            {
                "repository_id": "DEV-001",
                "name": "Medical-Report-Generator-from-Chest-X-Ray-Images",
                "url": "https://github.com/anandr07/Medical-Report-Generator-from-Chest-X-Ray-Images",
                "license": "Unlicensed / Public GitHub Repository (inspected locally without redistribution)",
                "commit_sha": "pending_clone_verification",
                "split": "development",
                "role": (
                    "Repositório utilizado no manuscrito original da PoC; mantido exclusivamente no conjunto "
                    "de desenvolvimento e NÃO apresentado como validação externa independente."
                ),
            }
        ],
        "external_test_split": {
            "target_sample_size": 20,
            "current_status": "PENDING_EXTERNAL_EXPERT_ANNOTATION",
            "selection_criteria": [
                "Repositórios públicos em Python com aplicação declarada em imagem médica, suporte à decisão clínica ou SaMD.",
                "Congelamento do SHA do commit antes da execução do TraceAST-62304 e da revisão cega pelos dois especialistas.",
            ],
            "planned_slots": [
                {
                    "repository_id": f"TEST-{i:03d}",
                    "name": "PENDING_SELECTION",
                    "url": None,
                    "license": None,
                    "commit_sha": None,
                    "split": "test",
                    "expert_reviewer_1_status": "pending",
                    "expert_reviewer_2_status": "pending",
                    "adjudication_status": "pending",
                }
                for i in range(1, 21)
            ],
        },
    }
    manifest_file = output_dir / "dataset_split_manifest.json"
    manifest_file.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return manifest_file

