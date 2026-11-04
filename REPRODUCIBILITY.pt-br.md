# Guia de Reprodutibilidade Científica — TraceAST-62304 v1.0 (Português)

[![en](https://img.shields.io/badge/lang-English%20(Main)-blue.svg)](./REPRODUCIBILITY.md)
[![pt-br](https://img.shields.io/badge/lang-Portugu%C3%AAs%20(pt--BR)-green.svg)](./REPRODUCIBILITY.pt-br.md)

> 🌐 **Language / Idioma:** **[Read in English (Primary) — `REPRODUCIBILITY.md`](./REPRODUCIBILITY.md)** | **Português (`REPRODUCIBILITY.pt-br.md`)**
> 📖 **Portal Interativo:** [Documentação Completa (PT-BR)](./docs/index.pt-br.html) | [Full Documentation Portal (EN)](./docs/index.html)

Este documento descreve os controles implementados para assegurar que todas as análises, métricas e relatórios gerados pelo **TraceAST-62304** possam ser reproduzidos de forma exata por revisores científicos e equipes de engenharia.

---

## 1. Controles de Reprodutibilidade Implementados

Cada execução do comando `python -m traceast scan` gera automaticamente o arquivo `run_manifest.json` contendo:

1. **Versão do Sistema:** `TraceAST-62304 v1.0.0`.
2. **Versão Exata do Interpretador Python:** Registrada via `sys.version`.
3. **Commit SHA do Repositório Analisado:** Extraído de `.git/HEAD` quando disponível.
4. **Hash SHA-256 do Catálogo de Regras (`rule_catalog_sha256`):** Hash criptográfico canônico de todas as definições das regras `R01`–`R08`.
5. **Hashes SHA-256 de Todos os Arquivos Python Inspecionados:** Registrados individualmente em `repository_inventory.json`.
6. **Hashes SHA-256 dos Documentos Regulatórios Utilizados no RAG:** Registrados em `run_manifest.json` e `retrieval_trace.json`.
7. **Identificação do Modelo de Embeddings e Backend de Recuperação:** Nome do modelo, versão e modo de execução registrados.
8. **Auditoria de Uso de LLM Externo:** Registra se houve chamada externa, provedor, modelo, parâmetros (`temperature`, `max_tokens`), *tokens* consumidos e tempo gasto.
9. **Duração por Etapa:** Tempos em segundos para AST/inventário, motor de regras, RAG, LLM e pipeline total.

---

## 2. Procedimento de Execução em Ambiente Limpo

### Passo 1: Criar Ambiente Virtual Isolado

No Windows PowerShell:
```powershell
python -m venv venv_clean
.\venv_clean\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

No Linux / macOS:
```bash
python3 -m venv venv_clean
source venv_clean/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Passo 2: Verificar a Versão e o Hash do Catálogo de Regras

```bash
python -m traceast version
```

### Passo 3: Executar a Suíte Completa de Testes Automatizados

```bash
python -m pytest -v
```

### Passo 4: Construir o Índice RAG Local e Executar Análise Determinística

```bash
python -m traceast build-rag --docs-dir ./legal_documents --persist-dir ./db_regulacao_v1
python -m traceast scan --repo ./tests/fixtures/repo_well_structured --profile ./product_profile.example.yaml --out ./reports/repro_check
```

### Passo 5: Gerar os Artefatos de Avaliação Científica

```bash
python -m traceast evaluate --out ./evaluation_artifacts
```

---

## 3. Artefatos a Preservar para Submissão à JMIR Medical Informatics

Para garantir auditoria científica completa do manuscrito, preserve e arquive em repositório suplementar (ex.: Zenodo / OSF):

1. O pacote de código congelado com `requirements.txt` e `RULE_CATALOG.pt-br.md` / `RULE_CATALOG.md`.
2. O arquivo `evaluation_artifacts/dataset_split_manifest.json` com os SHAs exatos dos commits de todos os repositórios avaliados.
3. Para cada repositório avaliado, o diretório completo de saída contendo:
   - `findings.json`
   - `report.md`
   - `run_manifest.json`
   - `repository_inventory.json`
   - `retrieval_trace.json`
   - `analysis_metrics.json`
4. As planilhas originais preenchidas separadamente pelo Avaliador 1, Avaliador 2, Adjudicador 3 e a planilha de Consenso.
5. O arquivo JSON de resultado da comparação estatística (TP, FP, FN, TN, Precision, Recall, F1, IC 95% via *cluster bootstrap* e *Cohen's kappa*) e o relatório `rag_recall_at_3_evaluation.json`.

