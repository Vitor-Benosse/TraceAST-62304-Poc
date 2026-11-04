# Scientific Validation Protocol — TraceAST-62304 v1.0

[![en](https://img.shields.io/badge/lang-English%20(Main)-blue.svg)](./VALIDATION_PROTOCOL.md)
[![pt-br](https://img.shields.io/badge/lang-Portugu%C3%AAs%20(pt--BR)-green.svg)](./VALIDATION_PROTOCOL.pt-br.md)

> 🌐 **Language / Idioma:** **English (Primary — `VALIDATION_PROTOCOL.md`)** | **[Ler em Português (`VALIDATION_PROTOCOL.pt-br.md`)](./VALIDATION_PROTOCOL.pt-br.md)**
> 📖 **Interactive Portal:** [Full Documentation Portal (EN)](./docs/index.html) | [Documentação Completa (PT-BR)](./docs/index.pt-br.html)

**Target Study:** Submission to *JMIR Medical Informatics*
**Positioning:** *AI-assisted, evidence-traceable pre-audit screening for medical software development repositories.*

---

## 1. Validation Study Objective

To evaluate the capability of **TraceAST-62304** to identify traceable technical indicators (`R01`–`R08`) and retrieve relevant normative references (ANVISA RDC 657/2022 and IEC 62304) across Python medical software repositories, comparing the tool's deterministic output against a *reference standard* established by independent human specialists.

---

## 2. Strict Separation Between Development Set and External Test Set

To ensure scientific validity and prevent data leakage or rule overfitting:

1. **Development Set (`development_split`):**
   - Includes the controlled synthetic fixtures (`tests/fixtures/`) and the `Medical-Report-Generator-from-Chest-X-Ray-Images` repository used during initial Proof-of-Concept design.
   - The `Medical-Report-Generator-from-Chest-X-Ray-Images` repository remains locked in the development split inside `evaluation_artifacts/dataset_split_manifest.json` and **must never be reported as independent external validation**.
2. **External Test Set (`external_test_split`):**
   - Comprises at least $N = 20$ public Python medical software / medical AI repositories selected according to pre-specified inclusion criteria.
   - **Rule Freeze Policy:** The rule catalog (`RULE_CATALOG_VERSION = 1.0.0`, recorded via SHA-256 in `run_manifest.json`) must be frozen prior to running on the external test set. No heuristic may be tuned after observing external test set results.

---

## 3. Human Specialist Annotation Procedure (Reference Standard)

Official annotation templates are generated via:

```bash
python -m traceast evaluate --out ./evaluation_artifacts
```

This produces four structured 160-row CSV files in `evaluation_artifacts/templates/` (covering all 20 external test repositories `TEST-001`–`TEST-020` $\times$ 8 rules `R01`–`R08` defined in [`test_set_manifest.json`](./test_set_manifest.json); see full tool execution results in [`evaluation_artifacts/TEST_SET_EXECUTION_REPORT.md`](./evaluation_artifacts/TEST_SET_EXECUTION_REPORT.md)):
- `expert_annotation_reviewer_1_template.csv` (Independent Reviewer 1)
- `expert_annotation_reviewer_2_template.csv` (Independent Reviewer 2)
- `expert_annotation_adjudicator_3_template.csv` (Reviewer 3 — Tie-Breaker / Adjudicator)
- `expert_annotation_consensus_template.csv` (Consolidated Final Consensus)

### Blind Annotation Rules:
1. **Independence:** Reviewers 1 and 2 inspect each repository independently and blinded both to TraceAST-62304's output and to each other.
2. **Structured Recording:** For each `(repository_id, rule_id)` pair, the reviewer records:
   - Evidence state (`observed`, `partial`, `not_observed`, `unable_to_assess`, `not_applicable`);
   - Review priority (`high`, `medium`, `low`, `informational`);
   - Related file and line range;
   - Technical justification;
   - Whether the item would warrant investigation during a formal human audit (`warrants_human_audit_investigation`).
3. **Inter-Rater Agreement (*Cohen's Kappa*):** Prior to reconciliation, the original pre-consensus labels from Reviewers 1 and 2 are preserved and passed to `compute_cohens_kappa` to report $\kappa$ in the manuscript.
4. **Adjudication:** Disagreements between Reviewers 1 and 2 are resolved by Reviewer 3, producing `consensus_reference_standard.json`.

---

## 4. Statistical Metrics and Scoring Rules

The scoring engine (`traceast/evaluation.py`) compares tool findings against the human consensus according to these definitions:

- **Positive Indicator Signal:** `observed` or `partial`.
- **Negative Indicator Signal:** `not_observed`.
- **Non-Applicability Rule:** When human consensus classifies a rule as `not_applicable` or `unable_to_assess`, a tool output of `not_observed` or `not_applicable` is scored as a **True Negative (`TN`)**, and **never penalized as a False Negative (`FN`)**.
- **Computed Metrics (per rule and micro/macro aggregated):**
  - *True Positives* (TP), *False Positives* (FP), *False Negatives* (FN), *True Negatives* (TN)
  - $\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$
  - $\text{Recall (Sensitivity)} = \frac{\text{TP}}{\text{TP} + \text{FN}}$
  - $\text{F1-score} = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$
- **Confidence Intervals (95% CI):** Computed via **Cluster Bootstrap** ($B = 1000$ resamples with replacement), using `repository_id` as the primary resampling cluster to account for intra-repository correlation across the 8 rules.

---

## 5. Regulatory Retrieval Evaluation (RAG `Recall@3`)

1. The reference query benchmark maps each rule (`R01`–`R08`) to the expected relevant normative documents in the corpus (`ANVISA_RDC_657_2022` and `IEC62304` templates/mappings).
2. For each query, the system retrieves the top $k = 3$ chunks with highest similarity and computes:
   - **Hit Rate Recall@3:** Proportion of rules for which at least one expected relevant reference document appears in the top-3 retrieved chunks.
   - **Fractional Recall@3:** Mean proportion of expected relevant reference documents retrieved within the top-3 chunks.
