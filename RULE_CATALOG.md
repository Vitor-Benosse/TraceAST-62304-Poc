# Deterministic Rule Catalog — TraceAST-62304 v1.0

[![en](https://img.shields.io/badge/lang-English%20(Main)-blue.svg)](./RULE_CATALOG.md)
[![pt-br](https://img.shields.io/badge/lang-Portugu%C3%AAs%20(pt--BR)-green.svg)](./RULE_CATALOG.pt-br.md)

> 🌐 **Language / Idioma:** **English (Primary — `RULE_CATALOG.md`)** | **[Ler em Português (`RULE_CATALOG.pt-br.md`)](./RULE_CATALOG.pt-br.md)**
> 📖 **Interactive Portal:** [Full Documentation Portal (EN)](./docs/index.html) | [Documentação Completa (PT-BR)](./docs/index.pt-br.html)

This document presents the initial catalog of **8 deterministic rules (`R01`–`R08`)** implemented in TraceAST-62304 for review, validation, and sign-off by specialists in Medical Software Engineering (IEC 62304) and Regulatory Affairs (ANVISA RDC 657/2022).

> **Important Normative Note:**
> The rules below represent **structural technical indicators** statically extracted from source code and configuration files. No code heuristic alone equates to compliance or non-compliance with a regulatory obligation. All normative mappings initially carry the status `pending_expert_review`.

---

## Specialist Review Table

| Rule ID | Rule Title | Category | Preliminary References | Regulatory Validation Status | Specialist Sign-Off (Signature/Date) |
|---|---|---|---|---|---|
| `R01` | Static inspection coverage and integrity | Inspection Integrity | IEC 62304 Sec. 5.5.5; RDC 657/2022 Art. 14 | `pending_expert_review` | [ ] Pending / [ ] Reviewed / [ ] Approved |
| `R02` | Dependency and external component management (SOUP) | Configuration & SOUP Management | IEC 62304 Sec. 5.3.3, 5.3.4, 7.1.2, 7.1.3, 8.1.2; RDC 657/2022 Art. 14 | `pending_expert_review` | [ ] Pending / [ ] Reviewed / [ ] Approved |
| `R03` | Automated testing evidence in repository | Software Verification & Testing | IEC 62304 Sec. 5.5.5, 5.6.3, 5.7; RDC 657/2022 Art. 14 | `pending_expert_review` | [ ] Pending / [ ] Reviewed / [ ] Approved |
| `R04` | Continuous integration (CI/CD) and verification automation | Verification & Continuous Integration | IEC 62304 Sec. 5.5.5, 5.6.4, 5.6.6 | `pending_expert_review` | [ ] Pending / [ ] Reviewed / [ ] Approved |
| `R05` | Error and exception handling in I/O operations | Reliability & Fault Handling | IEC 62304 Sec. 5.1.12, 5.5.3, 7.1.2 | `pending_expert_review` | [ ] Pending / [ ] Reviewed / [ ] Approved |
| `R06` | Structural signals of input validation | Interface & Input Verification | IEC 62304 Sec. 5.2.2, 5.3.2, 5.4.3 | `pending_expert_review` | [ ] Pending / [ ] Reviewed / [ ] Approved |
| `R07` | Provenance, loading, and versioning of model artifacts | AI/ML Model Traceability | IEC 62304 Sec. 8.1.1, 8.3; OpenRegulatory ML SOP Sec. 1.2, 2.5 | `pending_expert_review` | [ ] Pending / [ ] Reviewed / [ ] Approved |
| `R08` | Structural signals of separation between training and inference | Architecture & Environment Isolation (AI/ML) | IEC 62304 Sec. 5.3.1, 5.3.5; OpenRegulatory ML SOP Sec. 2.1, 2.6 | `pending_expert_review` | [ ] Pending / [ ] Reviewed / [ ] Approved |

---

## Detailed Rule Specifications

### R01 — Static inspection coverage and integrity
- **Objective:** Ensure transparency regarding the universe of inspected files and prevent files with syntax or encoding errors from being silently omitted.
- **Target Evidence:** Count of `.py` files, SHA-256 hashes, and detailed failure records (`SyntaxError`, `UnicodeDecodeError`, `OSError`).
- **Detection Method:** Recursive directory scan and parsing via `ast.parse`.
- **Identification Criteria:**
  - `observed`: 100% of `.py` files parsed successfully.
  - `partial`: At least 1 `.py` file parsed successfully and at least 1 parse failure recorded.
  - `unable_to_assess`: No `.py` files found or 100% parsing failure.
- **Limitations:** Syntactic success in `ast.parse` does not prove the absence of semantic errors or functional adequacy.

### R02 — Dependency and external component management (SOUP)
- **Objective:** Support preliminary identification of *Software of Unknown Provenance* (SOUP) and version pinning control of third-party libraries.
- **Target Evidence:** `requirements*.txt`, `pyproject.toml`, `poetry.lock`, version specifiers (`==` vs. unpinned ranges), and cross-referencing against AST imported modules.
- **Identification Criteria:**
  - `observed`: Dependency manifest present with all declared dependencies pinned (`==`) and no undeclared third-party imports.
  - `partial`: Manifest present, but with unpinned/open versions or external imports not declared in the manifest.
  - `not_observed`: No dependency management file found in the repository.
- **Limitations:** Unpinned dependencies in the repository do not automatically constitute non-compliance; the formal SOUP list may reside in external Quality Management System (QMS) documentation.

### R03 — Automated testing evidence in repository
- **Objective:** Identify observable unit verification and automated test artifacts in the repository.
- **Target Evidence:** `tests/` or `test/` directories, `test_*.py` / `*_test.py` files, `test_*` functions, and `pytest`/`unittest` imports.
- **Identification Criteria:**
  - `observed`: Test files containing verifiable `test_*` functions/methods.
  - `partial`: Test directory or configuration file present without identifiable test functions.
  - `not_observed`: No test directories or test files found in the inspected repository.
- **Limitations:** Absence of tests in the repository only indicates absence of observable evidence in this repository, not proof that the organization does not perform testing.

### R04 — Continuous integration (CI/CD) and verification automation
- **Objective:** Identify version-controlled configurations for automated test execution.
- **Target Evidence:** `.github/workflows/*.yml` and `.gitlab-ci.yml` workflows containing calls to `pytest`, `unittest`, `tox`, or `coverage`.
- **Identification Criteria:**
  - `observed`: CI/CD workflow with an explicit test execution command.
  - `partial`: CI/CD workflow present without an explicit Python test command.
  - `not_observed`: No CI/CD workflow files found in the repository.
- **Limitations:** Continuous integration pipelines may run on external infrastructure not reflected in `.github/workflows`.

### R05 — Error and exception handling in I/O operations
- **Objective:** Locate candidate data input/output operations lacking local exception handling or containing empty/`pass` `except` blocks.
- **Target Evidence:** AST I/O calls (`open`, `read_csv`, `dcmread`, `load`, etc.), `ast.Try` scopes, and `ast.ExceptHandler` nodes.
- **Identification Criteria:**
  - `observed`: All candidate I/O operations are protected by non-empty `try-except` blocks and there are no silent `except: pass` handlers.
  - `partial`: Coexistence of protected and unprotected I/O operations, or presence of empty/`pass` `except` blocks.
  - `not_observed`: Candidate I/O operations without any non-empty `try-except` block, or complete absence of I/O operations.
- **Limitations:** Syntactic `try-except` presence does not prove patient-safe error handling; exception handling may also occur in higher-level caller functions.

### R06 — Structural signals of input validation
- **Objective:** Map dedicated functions and conditional guards used to validate incoming data.
- **Target Evidence:** `validate_*`/`check_*`/`verify_*` function definitions, validation calls (`isinstance`, `model_validate`), `if` conditionals raising exceptions (`raise`), and `assert` statements.
- **Identification Criteria:**
  - `observed`: Dedicated validation functions or conditional guards raising explicit exceptions.
  - `partial`: Only `assert` statements or simple guards without raising exceptions.
  - `not_observed`: No structural input validation signals detected.
- **Limitations:** A syntactic check does not guarantee sufficient clinical or physiological validation.

### R07 — Provenance, loading, and versioning of model artifacts
- **Objective:** Identify AI/ML model loading/saving operations and references to checkpoint files (`.pt`, `.pth`, `.onnx`, `.h5`, `.safetensors`).
- **Identification Criteria:**
  - `not_applicable`: `ai_components=false` in the product profile and no AI libraries/signals in the code.
  - `partial`: Model artifacts or loading/saving calls identified (always requires external documentary review of model provenance).
  - `not_observed`: AI-enabled project lacking explicit model loading/saving calls or artifact references.
- **Limitations:** Presence of a `.pt` or `.pth` file does not prove complete provenance, training dataset version control, or clinical validation.

### R08 — Structural signals of separation between training and inference
- **Objective:** Flag potential coupling within the same module between training routines (`backward`, `step`, `fit`, `model.train`) and inference routines (`forward`, `predict`, `model.eval`, `no_grad`).
- **Identification Criteria:**
  - `not_applicable`: `ai_components=false` in the product profile and no AI signals in the code.
  - `observed`: Training and inference signals reside in separate files without overlap in the same module.
  - `partial`: Training and inference signals coexist in the same file, or only one phase was identified.
  - `not_observed`: No structural training or inference signals detected.
- **Limitations:** AST analysis does not prove effective production infrastructure isolation without execution flow and deployment review.
