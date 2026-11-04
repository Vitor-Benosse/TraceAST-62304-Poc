# Catálogo de Regras Determinísticas — TraceAST-62304 v1.0 (Português)

[![en](https://img.shields.io/badge/lang-English%20(Main)-blue.svg)](./RULE_CATALOG.md)
[![pt-br](https://img.shields.io/badge/lang-Portugu%C3%AAs%20(pt--BR)-green.svg)](./RULE_CATALOG.pt-br.md)

> 🌐 **Language / Idioma:** **[Read in English (Primary) — `RULE_CATALOG.md`](./RULE_CATALOG.md)** | **Português (`RULE_CATALOG.pt-br.md`)**
> 📖 **Portal Interativo:** [Documentação Completa (PT-BR)](./docs/index.pt-br.html) | [Full Documentation Portal (EN)](./docs/index.html)

Este documento apresenta o catálogo inicial de **8 regras determinísticas (`R01`–`R08`)** do TraceAST-62304 para revisão, validação e aprovação por especialistas em Engenharia de Software Médico (IEC 62304) e Assuntos Regulatórios (ANVISA RDC 657/2022).

> **Nota Normativa Importante:**
> As regras abaixo representam **indicadores técnicos estruturais** extraídos estaticamente do código-fonte e de arquivos de configuração. Nenhuma heurística de código equivale isoladamente ao cumprimento ou descumprimento de uma obrigação normativa. Todas as correspondências encontram-se inicialmente com status `pending_expert_review`.

---

## Quadro de Revisão por Especialista

| Rule ID | Título da Regra | Categoria | Referências Preliminares | Status da Validação Regulatória | Aprovação do Especialista (Assinatura/Data) |
|---|---|---|---|---|---|
| `R01` | Cobertura e integridade da inspeção estática | Integridade da Inspeção | IEC 62304 Sec. 5.5.5; RDC 657/2022 Art. 14 | `pending_expert_review` | [ ] Pendente / [ ] Revisada / [ ] Aprovada |
| `R02` | Gerenciamento de dependências e componentes externos (SOUP) | Gerenciamento de Configuração e SOUP | IEC 62304 Sec. 5.3.3, 5.3.4, 7.1.2, 7.1.3, 8.1.2; RDC 657/2022 Art. 14 | `pending_expert_review` | [ ] Pendente / [ ] Revisada / [ ] Aprovada |
| `R03` | Evidências de testes automatizados no repositório | Verificação e Testes de Software | IEC 62304 Sec. 5.5.5, 5.6.3, 5.7; RDC 657/2022 Art. 14 | `pending_expert_review` | [ ] Pendente / [ ] Revisada / [ ] Aprovada |
| `R04` | Integração contínua (CI/CD) e automação de verificação | Verificação e Integração Contínua | IEC 62304 Sec. 5.5.5, 5.6.4, 5.6.6 | `pending_expert_review` | [ ] Pendente / [ ] Revisada / [ ] Aprovada |
| `R05` | Tratamento de erros e exceções em operações de I/O | Confiabilidade e Tratamento de Falhas | IEC 62304 Sec. 5.1.12, 5.5.3, 7.1.2 | `pending_expert_review` | [ ] Pendente / [ ] Revisada / [ ] Aprovada |
| `R06` | Sinais estruturais de validação de entradas | Verificação de Interfaces e Entradas | IEC 62304 Sec. 5.2.2, 5.3.2, 5.4.3 | `pending_expert_review` | [ ] Pendente / [ ] Revisada / [ ] Aprovada |
| `R07` | Proveniência, carregamento e versionamento de artefatos de modelos | Rastreabilidade de Modelos de IA/ML | IEC 62304 Sec. 8.1.1, 8.3; OpenRegulatory ML SOP Sec. 1.2, 2.5 | `pending_expert_review` | [ ] Pendente / [ ] Revisada / [ ] Aprovada |
| `R08` | Sinais estruturais de separação entre treinamento e inferência | Arquitetura e Isolamento de Ambientes (IA/ML) | IEC 62304 Sec. 5.3.1, 5.3.5; OpenRegulatory ML SOP Sec. 2.1, 2.6 | `pending_expert_review` | [ ] Pendente / [ ] Revisada / [ ] Aprovada |

---

## Especificação Detalhada das Regras

### R01 — Cobertura e integridade da inspeção estática
- **Objetivo:** Garantir transparência sobre o universo de arquivos inspecionados e impedir que arquivos com erro de sintaxe ou leitura sejam omitidos silenciosamente.
- **Evidência Procurada:** Contagem de arquivos `.py`, hashes SHA-256 e registro detalhado de falhas (`SyntaxError`, `UnicodeDecodeError`, `OSError`).
- **Método de Detecção:** Varredura recursiva e parsing via `ast.parse`.
- **Critérios de Identificação:**
  - `observed`: 100% dos arquivos `.py` analisados com sucesso.
  - `partial`: ao menos 1 arquivo `.py` analisado com sucesso e ao menos 1 falha registrada.
  - `unable_to_assess`: nenhum arquivo `.py` encontrado ou 100% de falha no parsing.
- **Limitações:** Sucesso sintático no `ast.parse` não comprova ausência de erros semânticos ou adequação funcional.

### R02 — Gerenciamento de dependências e componentes externos (SOUP)
- **Objetivo:** Apoiar o levantamento preliminar de *Software of Unknown Provenance* (SOUP) e o controle de versões de bibliotecas externas.
- **Evidência Procurada:** Arquivos `requirements*.txt`, `pyproject.toml`, `poetry.lock`, especificadores de versão (`==` vs abertos) e cruzamento com módulos importados na AST.
- **Critérios de Identificação:**
  - `observed`: manifesto presente com todas as dependências declaradas fixadas (`==`) e sem imports de terceiros omitidos.
  - `partial`: manifesto presente, porém com versões abertas/não fixadas ou imports externos não declarados no manifesto.
  - `not_observed`: ausência de arquivo de gerenciamento de dependências no repositório.
- **Limitações:** Dependências sem versão fixada no repositório não constituem automaticamente não conformidade; a lista formal de SOUP pode residir em documentação externa do Sistema de Gestão da Qualidade (SGQ).

### R03 — Evidências de testes automatizados no repositório
- **Objetivo:** Identificar artefatos observáveis de verificação de unidades e testes no repositório.
- **Evidência Procurada:** Diretórios `tests/` ou `test/`, arquivos `test_*.py` / `*_test.py`, funções `test_*` e uso de `pytest`/`unittest`.
- **Critérios de Identificação:**
  - `observed`: arquivos de teste com funções/métodos de teste verificáveis.
  - `partial`: diretório ou arquivo de configuração de testes presente sem funções de teste identificáveis.
  - `not_observed`: ausência de diretórios e arquivos de teste no repositório inspecionado.
- **Limitações:** A ausência de testes no repositório indica apenas ausência de evidência observável neste repositório, e não prova que a empresa não executa testes.

### R04 — Integração contínua (CI/CD) e automação de verificação
- **Objetivo:** Identificar configurações versionadas de execução automatizada de testes.
- **Evidência Procurada:** Workflows `.github/workflows/*.yml` e `.gitlab-ci.yml` contendo chamadas a `pytest`, `unittest`, `tox` ou `coverage`.
- **Critérios de Identificação:**
  - `observed`: workflow CI/CD com comando explícito de execução de testes.
  - `partial`: workflow CI/CD sem comando explícito de teste Python.
  - `not_observed`: ausência de arquivos de CI/CD no repositório.
- **Limitações:** O pipeline de integração contínua pode ser executado em infraestrutura externa não refletida em `.github/workflows`.

### R05 — Tratamento de erros e exceções em operações de I/O
- **Objetivo:** Localizar operações candidatas de entrada/saída de dados sem tratamento local de exceções ou com blocos `except` vazios/`pass`.
- **Evidência Procurada:** Chamadas AST de I/O (`open`, `read_csv`, `dcmread`, `load`, etc.), escopos `ast.Try` e handlers `ast.ExceptHandler`.
- **Critérios de Identificação:**
  - `observed`: todas as operações candidatas de I/O estão protegidas por blocos `try-except` não vazios e não há `except: pass`.
  - `partial`: coexistência de operações de I/O protegidas e desprotegidas, ou presença de blocos `except` vazios/`pass`.
  - `not_observed`: operações de I/O sem nenhum bloco `try-except` não vazio, ou ausência total de operações de I/O.
- **Limitações:** A presença de `try-except` não comprova tratamento seguro para o paciente; o tratamento também pode ocorrer em funções chamadoras de nível superior.

### R06 — Sinais estruturais de validação de entradas
- **Objetivo:** Mapear funções e guardas condicionais dedicadas à validação de dados recebidos.
- **Evidência Procurada:** Definições de funções `validate_*`/`check_*`/`verify_*`, chamadas de validação (`isinstance`, `model_validate`), condicionais `if` que levantam exceção (`raise`) e instruções `assert`.
- **Critérios de Identificação:**
  - `observed`: funções dedicadas de validação ou guardas condicionais com levantamento de exceção.
  - `partial`: apenas instruções `assert` ou guardas simples sem levantamento de erro.
  - `not_observed`: nenhum sinal estrutural de validação detectado.
- **Limitações:** Uma condição sintática não garante validação clínica ou fisiológica suficiente.

### R07 — Proveniência, carregamento e versionamento de artefatos de modelos
- **Objetivo:** Identificar operações de carregamento/salvamento de modelos de IA/ML e referências a arquivos de checkpoint (`.pt`, `.pth`, `.onnx`, `.h5`, `.safetensors`).
- **Critérios de Identificação:**
  - `not_applicable`: `ai_components=false` no perfil e ausência de bibliotecas/sinais de IA no código.
  - `partial`: artefatos ou chamadas de carga/salvamento identificados (sempre requer revisão documental externa de proveniência do modelo).
  - `not_observed`: projeto com IA sem chamadas explícitas de carregamento/salvamento ou artefatos localizados.
- **Limitações:** A presença de um arquivo `.pt` ou `.pth` não comprova proveniência completa, controle de versão de dados de treino nem validação clínica.

### R08 — Sinais estruturais de separação entre treinamento e inferência
- **Objetivo:** Sinalizar possível acoplamento no mesmo módulo entre rotinas de treinamento (`backward`, `step`, `fit`, `model.train`) e rotinas de inferência (`forward`, `predict`, `model.eval`, `no_grad`).
- **Critérios de Identificação:**
  - `not_applicable`: `ai_components=false` no perfil e ausência de sinais de IA.
  - `observed`: sinais de treinamento e de inferência presentes em arquivos distintos, sem sobreposição no mesmo módulo.
  - `partial`: sinais de treinamento e inferência coexistem no mesmo arquivo, ou apenas uma das fases foi identificada.
  - `not_observed`: nenhum sinal estrutural de treinamento ou inferência detectado.
- **Limitações:** A AST não prova isolamento efetivo de infraestrutura em produção sem análise do fluxo de execução e implantação.

