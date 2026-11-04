# Technical and Regulatory Limitations Declaration — TraceAST-62304 v1.0

[![en](https://img.shields.io/badge/lang-English%20(Main)-blue.svg)](./LIMITATIONS.md)
[![pt-br](https://img.shields.io/badge/lang-Portugu%C3%AAs%20(pt--BR)-green.svg)](./LIMITATIONS.pt-br.md)

> 🌐 **Language / Idioma:** **English (Primary — `LIMITATIONS.md`)** | **[Ler em Português (`LIMITATIONS.pt-br.md`)](./LIMITATIONS.pt-br.md)**
> 📖 **Interactive Portal:** [Full Documentation Portal (EN)](./docs/index.html) | [Documentação Completa (PT-BR)](./docs/index.pt-br.html)

**TraceAST-62304** is a technical *pre-audit screening* instrument and must be used with full awareness of its methodological boundaries.

---

## 1. Regulatory and Clinical Limitations

1. **No Replacement of Human Auditors:** The system does not replace quality engineers, IEC 62304 specialists, clinical evaluators, or ANVISA inspectors.
2. **No Declaration of Compliance or Certification:** No status output (`observed`, `partial`, etc.) may be interpreted as a regulatory compliance certificate.
3. **No Risk Class Determination:** The system does not automatically classify medical devices under ANVISA RDC 657/2022 (Classes I–IV) nor determine Software Safety Classification under IEC 62304 (Classes A, B, or C). The `review_priority` field refers exclusively to technical investigation priority for the engineering team.
4. **No Clinical Evaluation:** Static source code inspection cannot evaluate clinical efficacy, diagnostic sensitivity/specificity, dataset population bias, or real-world clinical safety.
5. **Meaning of `not_observed`:** When evidence is not found in the repository (`not_observed`), it means only that the structural indicator was not located in the inspected repository files. Quality Management System (QMS) documents, validation plans, risk management matrices (ISO 14971), and test reports frequently reside in external document management systems.

---

## 2. Static AST Analysis Limitations (Python V1.0)

1. **Language Scope:** Version 1.0 exclusively analyzes Python (`.py`) files. Hybrid repositories containing C/C++, CUDA, JavaScript/TypeScript, or R have only their Python layer inspected.
2. **No Dynamic Execution:** For security and reproducibility, target repository code is never executed. Consequently, the tool does not resolve dynamic runtime types, reflection (dynamic `getattr`), or configurations fetched from external servers at runtime.
3. **Heuristic Boundaries (`R01`–`R08`):**
   - **Exception Handling (`R05`):** Verifying that a read operation is enclosed in a `try-except` block does not prove that the exception is handled in a patient-safe manner, nor does it detect if error catching occurs in a higher-level caller function.
   - **Input Validation (`R06`):** Identifying a `validate_*` function or an `isinstance` check does not prove that physiological ranges, DICOM metadata, or clinical invariants are properly verified.
   - **Model Provenance (`R07`):** Detecting `torch.load` or a `.pt` file does not prove that the model has version traceability, an audited training dataset, or documented hyperparameters.
   - **Training/Inference Separation (`R08`):** Verifying that training and inference functions reside in separate files does not guarantee production environment isolation; conversely, PyTorch classes (`nn.Module`) define `forward` used in both training and inference, requiring human review of control flow.

---

## 3. RAG Module and Optional LLM Limitations

1. **Initial Normative Scope:** The V1.0 knowledge base covers **ANVISA RDC 657/2022** (official Portuguese text) and mapped **IEC 62304** references/templates. FDA guidelines are not implemented in V1.0.
2. **IEC 62304 Copyright Compliance:** The public repository does not redistribute the copyrighted full text of IEC 62304; it uses verifiable clause references and open templates (*OpenRegulatory*), whose mappings require specialist review and sign-off (`pending_expert_review`).
3. **Similarity Retrieval:** Returning top-3 chunks in RAG does not guarantee that the retrieved excerpt exhausts all regulatory requirements applicable to a specific product.
4. **Optional LLM:** When enabled by the user, the LLM acts solely as a writer of accessible explanations for findings already determined by static rules. It has no architectural permission to alter statuses, invent evidence, or issue regulatory judgments.
