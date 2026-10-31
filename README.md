# TraceAST-62304: Autonomous RegTech Architecture for Medical AI Auditing (SaMD)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/Vitor-Benosse/TraceAST-62304-Poc/blob/master/README.pt-br.md)

**Academic Proof of Concept (PoC) and Prior Art Declaration**

This repository presents the academic foundation and technological core (Proof of Concept) of the **TraceAST-62304** project. The system consists of an autonomous regulatory traceability agent designed to audit medical Artificial Intelligence repositories and generate preliminary compliance analyses and risk matrices.

The primary objective of this publication is to establish **Prior Art** for scientific validation and intellectual property protection.

---

## 1. Scientific Foundation: Exemption from Research Ethics Committee Review (CEP)

The research methodology of this project is based on the legal and scientific premise that submission to a Research Ethics Committee (CEP) is not required, for the following reasons:

1. **No Real Clinical Data:** The architecture does not consume, store, or process identifiable biomedical data or real patient medical images.
2. **Strictly Syntactic Evaluation:** The audit pipeline exclusively extracts **Abstract Syntax Trees (ASTs)** from the structural source code of open-source Artificial Intelligence repositories.
3. **Regulatory Focus:** The system assesses *software engineering* compliance with global standards by evaluating the presence of safeguards in the code (e.g., `try...except` blocks), rather than the diagnostic accuracy of the medical model itself.

This approach eliminates risks associated with privacy and GDPR/HIPAA regulations, drastically accelerating the regulatory validation cycle ("RegTech").

---

## 2. Theoretical and Technological Architecture

The core of this PoC addresses traditional limitations of Large Language Models (LLMs)—such as context-window saturation and hallucinations—by combining two advanced techniques:

### A. Intelligent Semantic Slicing (AST Module)
Sending the entire codebase of a hospital system to an LLM is inefficient and exposes intellectual property. To address this, we use Python's native `ast` module to extract only the critical semantic "skeleton":
- **Patient Data Isolation:** Actively identifies data manipulation nodes (I/O) and maps safeguards (`ast.Try`), listing error-handling logic. This helps assess the algorithm's resilience to telemetry corruption (e.g., faulty ICU sensors).
- **Environment Separation (Training vs. Production):** The extractor searches for explicit network-architecture signatures (such as PyTorch's `forward` method), enabling the agent to identify whether inappropriate training routines are coupled with the real-time inference flow.

### B. Clinical Reasoning Engine and Vector Brain (RAG)
- **Regulatory Harmonization:** Guidelines from the **FDA** (USA), **ANVISA (RDC 657/2022)**, and the international **IEC 62304** standard (via IMDRF) were converted into mathematical vectors (embeddings) using the `sentence-transformers/all-MiniLM-L6-v2` model.
- **ChromaDB:** Acts as the long-term vector database, enabling precise similarity searches (Retrieval-Augmented Generation, or RAG).
- **LLM Agent (Groq):** The `qwen/qwen3.8-27b` model (or a model from the Llama 3 family) is configured with a temperature of `0.2` to promote logical rigor. It receives the sliced AST code and retrieved regulations to produce a Technical Risk Dossier.

---

## 3. Repository Structure

- `analyzer.py`: AST-based syntactic extractor for mapping AI frameworks, classes, network-architecture methods (`forward`), I/O functions, and safeguards (`try...except`).
- `regulatory_db.py`: Document-ingestion pipeline (`.pdf` and `.md`), text slicing, and local ChromaDB vector database generation.
- `audit_agent.py`: Audit runner that integrates similarity search in ChromaDB with the cloud-based reasoning engine (Groq).
- `legal_documents/`: Directory for public regulatory documents (FDA, ANVISA RDC 657/2022, and IEC 62304 / ISO 14971 templates).
- `.env.example`: Configuration template for environment variables.

---

## 4. Step-by-Step Execution Guide

Evaluators, researchers, and reviewers who want to run the Proof of Concept locally can follow these instructions:

### Prerequisites
- Python 3.9 or later.
- Git.
- A free API key from [Groq Cloud](https://console.groq.com/).

### Step 1: Install and Configure the Environment
Clone this repository and create a virtual environment:
```bash
git clone https://github.com/YOUR_USERNAME/TraceAST-62304-PoC.git
cd TraceAST-62304-PoC
python -m venv venv
# Linux/macOS:
source venv/bin/activate
```

In Windows Git Bash, use:
```bash
source venv/Scripts/activate
```

In Windows PowerShell, use:
```powershell
.\venv\Scripts\Activate.ps1
```

In Windows Command Prompt (cmd), use:
```bat
venv\Scripts\activate.bat
```

Install the required dependencies:
```bash
pip install langchain-chroma langchain-huggingface langchain-groq python-dotenv sentence-transformers
```

### Step 2: Configure Credentials
Create a file named `.env` in the project root and add your Groq credentials:
```env
GROQ_API_KEY="your_api_key_here"
GROQ_MODEL="qwen/qwen3.8-27b"
```

### Step 3: Run the Proof of Concept
The public PoC consists of easy-to-run command-line scripts that demonstrate the end-to-end workflow:

1. **AST Extraction (Semantic Slicing):**
   Run the analyzer against a public medical AI repository (you can change the repository URL). The script will create a summary of its classes, I/O logic, and safety methods.
   ```bash
   python analyzer.py https://github.com/anandr07/Medical-Report-Generator-from-Chest-X-Ray-Images
   ```

2. **Regulatory Audit (Vector Database + LLM):**
   Build the vector database by processing the documents in `legal_documents/`, generating embeddings locally, and persisting the ChromaDB database:
   ```bash
   python regulatory_db.py
   ```

   Run the agent to simulate receiving the AST code and querying the regulatory database, returning the LLM's risk assessment:
   ```bash
   python audit_agent.py
   ```
   The model response is limited to 800 tokens to stay within the Groq free tier's output-token-per-minute limit.

---

## 5. Contact and Authorship
Developed as academic research focused on optimizing regulatory validation for *Software as a Medical Device* (SaMD). For discussions about the architecture and methodological details, see the scientific paper associated with this publication or open an *Issue* in this repository.
