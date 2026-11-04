# Relatório de Triagem Pré-Auditoria — TraceAST-62304 v1.0.0

> **Posicionamento:** *AI-assisted, evidence-traceable pre-audit screening for medical software development repositories.*

### Avisos Regulatórios e Limitações Obrigatórias
- O TraceAST-62304 é uma ferramenta assistiva de triagem pré-auditoria (AI-assisted, evidence-traceable pre-audit screening) e NÃO substitui auditores humanos.
- Este relatório NÃO declara conformidade regulatória nem certificação perante a IEC 62304, ANVISA RDC 657/2022 ou qualquer autoridade sanitária.
- O sistema NÃO determina automaticamente a classe regulatória do dispositivo (RDC 657/2022) nem a classe de segurança de software (IEC 62304 Classes A, B ou C).
- A ausência de determinada evidência no repositório inspecionado (not_observed) representa apenas ausência de evidência observável no escopo estático analisado, e NÃO prova de não conformidade.
- A presença de um indicador técnico (observed) indica que um elemento estrutural foi localizado no código, e NÃO que o controle ou processo atende integralmente aos requisitos normativos.
- Nenhuma afirmação é feita sobre desempenho clínico, acurácia diagnóstica, segurança clínica ou eficácia do modelo.
- Todas as correspondências entre regras técnicas e referências normativas requerem validação por especialista em assuntos regulatórios e engenharia de SaMD.

## A. Identificação

- **Nome do Projeto:** ChestXRay-AI-Diagnostic-Support
- **Commit SHA Analisado:** `8fa5e256a105fafdb824590e9f5ada3c1e062879`
- **Data e Horário da Execução (UTC):** `2026-11-04T16:18:25.985899+00:00`
- **Versão do TraceAST-62304:** `1.0.0`
- **Hash do Catálogo de Regras:** `35cab4357bb9a065b099324cbaf932c804bbfe9119eabd990ae48127794741e1`
- **Versão do Python:** `3.13.14`

### Perfil do Produto Informado pelo Usuário
- **Nome declarado:** ChestXRay-AI-Diagnostic-Support
- **Finalidade médica pretendida (`intended_purpose`):** Auxílio à triagem de radiografias torácicas em ambiente hospitalar por médicos radiologistas
- **Usuários pretendidos (`intended_users`):** Médicos radiologistas e clínicos devidamente habilitados
- **Mercado-alvo (`target_market`):** Brazil
- **Tipo de software (`software_type`):** AI-enabled SaMD
- **Componentes de IA declarados (`ai_components`):** `True`
- **Contexto de decisão clínica (`clinical_decision_context`):** Suporte informativo à elaboração de laudos radiológicos; não substitui a interpretação médica final

## B. Integridade da Análise

- **Quantidade total de arquivos encontrados:** 148
- **Quantidade de arquivos Python (`.py`):** 24
- **Arquivos Python analisados com sucesso:** 23
- **Arquivos Python que falharam na análise:** 1
- **Percentual de cobertura da inspeção sintática:** 95.83%

### Registro de Arquivos com Falha de Parsing
| Arquivo | Tipo de Erro | Linha | Motivo Registrado |
|---|---|---|---|
| `tests/fixtures/repo_deficient_and_coupled/broken_syntax.py` | `SyntaxError` | 3 | Erro de sintaxe Python na linha 3: '(' was never closed |

## C. Visão Geral dos Indicadores Técnicos

| Estado do Indicador | Expressão Padronizada | Quantidade |
|---|---|---|
| `observed` | Evidência identificada | 3 |
| `partial` | Evidência parcial — indicador técnico que merece investigação | 5 |
| `not_observed` | Evidência não identificada no repositório analisado | 0 |
| `unable_to_assess` | Impossível avaliar com os dados disponíveis | 0 |
| `not_applicable` | Não aplicável ao escopo declarado | 0 |
| **Revisão Humana** | **Itens que exigem revisão humana (`human_review_required`)** | **8** |

## D. Achados Detalhados

### TA-001 (R01) — Cobertura e integridade da inspeção estática
- **Categoria:** Integridade da Inspeção
- **Status:** `partial` (Evidência parcial — indicador técnico que merece investigação)
- **Prioridade de Revisão Técnica:** `high` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência parcial: 23 de 24 arquivos Python foram analisados com sucesso (95.83%), mas 1 arquivo(s) falharam no parsing AST (tests/fixtures/repo_deficient_and_coupled/broken_syntax.py).
- **Justificativa de Rastreabilidade:** Arquivos com falha não puderam ter sua AST extraída (tests/fixtures/repo_deficient_and_coupled/broken_syntax.py); nenhum arquivo com falha foi ignorado silenciosamente.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `analyzer.py` | `<module>` | 1–52 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 50425c0f566f...) |
| `audit_agent.py` | `<module>` | 1–34 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 8565b4290820...) |
| `regulatory_db.py` | `<module>` | 1–34 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 6a0cf62a4455...) |
| `tests/test_traceast_suite.py` | `<module>` | 1–385 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e4d79ff5d4c8...) |
| `tests/fixtures/repo_deficient_and_coupled/model_pipeline.py` | `<module>` | 1–26 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 3f82389bcd3f...) |
| `tests/fixtures/repo_false_positive_traps/scheduler.py` | `<module>` | 1–11 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 1b15cab5686f...) |
| `tests/fixtures/repo_well_structured/src/data_io.py` | `<module>` | 1–34 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: c2f9159ab2ff...) |
| `tests/fixtures/repo_well_structured/src/inference.py` | `<module>` | 1–34 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 97ba97d0a917...) |
| `tests/fixtures/repo_well_structured/src/trainer.py` | `<module>` | 1–23 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 24db7e80837b...) |
| `tests/fixtures/repo_well_structured/tests/test_inference.py` | `<module>` | 1–14 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: d5f9f3702b04...) |
| `traceast/__init__.py` | `<module>` | 1–8 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 51b060a68f75...) |
| `traceast/__main__.py` | `<module>` | 1–8 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 8bf123c504f5...) |
| `traceast/ast_analyzer.py` | `<module>` | 1–1192 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 9a7c1a6e14cc...) |
| `traceast/cli.py` | `<module>` | 1–192 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 3117d44fe9f7...) |
| `traceast/config.py` | `<module>` | 1–175 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: bce88d610768...) |
*... e mais 1 evidência(s) registrada(s) em `findings.json`.*

#### Referências Regulatórias Relacionadas
- **IEC62304** (IEC) — Cláusula/Seção: `5.5.5` | Status da Validação: `pending_expert_review`
- **ANVISA_RDC_657_2022** (ANVISA) — Cláusula/Seção: `Art. 14` | Status da Validação: `pending_expert_review`
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 5.5.2, 5.5.3, 5.5.4` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s13` (Score: `0.2247`)
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 5.1.9, 5.1.10, 5.1.11` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s06` (Score: `0.19`)
- **IEC62304_OPENREG_DEV_PLAN** (OpenRegulatory) — Cláusula/Seção: `IEC 62304 Sec. 5.1.5, 5.1.6, 5.1.7, 5.1.8` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_DEV_PLAN::s03` (Score: `0.1647`)

#### Limitações Técnicas
- Cobertura de 100% no parsing sintático significa apenas que a árvore AST pôde ser construída, não que o código está livre de defeitos lógicos ou em conformidade normativa.
- Arquivos em outras linguagens de programação (C++, JavaScript, etc.) não são analisados na V1.0.

#### Recomendação de Investigação ou Correção
Corrigir os erros de sintaxe ou codificação nos arquivos listados e reexecutar a triagem para garantir cobertura completa.

### TA-002 (R02) — Gerenciamento de dependências e componentes externos (SOUP)
- **Categoria:** Gerenciamento de Configuração e SOUP
- **Status:** `partial` (Evidência parcial — indicador técnico que merece investigação)
- **Prioridade de Revisão Técnica:** `medium` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência parcial: manifesto(s) de dependências localizado(s) (requirements.txt, tests/fixtures/repo_deficient_and_coupled/requirements.txt, tests/fixtures/repo_well_structured/requirements.txt, pyproject.toml), contendo 27 pacote(s) com versão fixada e 3 pacote(s) sem versão exata fixada. Imports externos não declarados no manifesto: src. Componentes de IA/ML: PyDICOM, PyTorch, Sentence Transformers, scikit-learn.
- **Justificativa de Rastreabilidade:** A presença de dependências sem versão fixada ou imports omitidos não representa automaticamente uma não conformidade, mas é um indicador técnico que merece investigação para controle de SOUP.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `requirements.txt` | `pydantic` | 2–2 | `dependency_declaration` | Pacote 'pydantic' declarado em 'requirements.txt' (especificador: '==2.14.1', fixado: True, importado no código: True) |
| `requirements.txt` | `PyYAML` | 3–3 | `dependency_declaration` | Pacote 'PyYAML' declarado em 'requirements.txt' (especificador: '==6.0.3', fixado: True, importado no código: True) |
| `requirements.txt` | `python-dotenv` | 4–4 | `dependency_declaration` | Pacote 'python-dotenv' declarado em 'requirements.txt' (especificador: '==1.2.4', fixado: True, importado no código: True) |
| `requirements.txt` | `pypdf` | 5–5 | `dependency_declaration` | Pacote 'pypdf' declarado em 'requirements.txt' (especificador: '==6.21.3', fixado: True, importado no código: True) |
| `requirements.txt` | `scikit-learn` | 6–6 | `dependency_declaration` | Pacote 'scikit-learn' declarado em 'requirements.txt' (especificador: '==1.9.1', fixado: True, importado no código: True) |
| `requirements.txt` | `scipy` | 7–7 | `dependency_declaration` | Pacote 'scipy' declarado em 'requirements.txt' (especificador: '==1.18.1', fixado: True, importado no código: False) |
| `requirements.txt` | `numpy` | 8–8 | `dependency_declaration` | Pacote 'numpy' declarado em 'requirements.txt' (especificador: '==2.5.4', fixado: True, importado no código: True) |
| `requirements.txt` | `chromadb` | 9–9 | `dependency_declaration` | Pacote 'chromadb' declarado em 'requirements.txt' (especificador: '==1.5.9', fixado: True, importado no código: False) |
| `requirements.txt` | `sentence-transformers` | 10–10 | `dependency_declaration` | Pacote 'sentence-transformers' declarado em 'requirements.txt' (especificador: '==6.2.0', fixado: True, importado no código: True) |
| `requirements.txt` | `groq` | 11–11 | `dependency_declaration` | Pacote 'groq' declarado em 'requirements.txt' (especificador: '==0.37.1', fixado: True, importado no código: True) |
| `requirements.txt` | `jsonschema` | 12–12 | `dependency_declaration` | Pacote 'jsonschema' declarado em 'requirements.txt' (especificador: '==4.26.0', fixado: True, importado no código: False) |
| `requirements.txt` | `pytest` | 13–13 | `dependency_declaration` | Pacote 'pytest' declarado em 'requirements.txt' (especificador: '==9.2.0', fixado: True, importado no código: True) |
| `tests/fixtures/repo_deficient_and_coupled/requirements.txt` | `torch` | 1–1 | `dependency_declaration` | Pacote 'torch' declarado em 'tests/fixtures/repo_deficient_and_coupled/requirements.txt' (especificador: '>=2.0.0', fixado: False, importado no código: True) |
| `tests/fixtures/repo_deficient_and_coupled/requirements.txt` | `numpy` | 2–2 | `dependency_declaration` | Pacote 'numpy' declarado em 'tests/fixtures/repo_deficient_and_coupled/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `tests/fixtures/repo_deficient_and_coupled/requirements.txt` | `pandas` | 3–3 | `dependency_declaration` | Pacote 'pandas' declarado em 'tests/fixtures/repo_deficient_and_coupled/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: True) |
*... e mais 12 evidência(s) registrada(s) em `findings.json`.*

#### Referências Regulatórias Relacionadas
- **IEC62304** (IEC) — Cláusula/Seção: `5.3.3; 5.3.4; 7.1.2; 7.1.3; 8.1.2` | Status da Validação: `pending_expert_review`
- **ANVISA_RDC_657_2022** (ANVISA) — Cláusula/Seção: `Art. 14` | Status da Validação: `pending_expert_review`
- **IEC62304_OPENREG_SOUP** (OpenRegulatory) — Cláusula/Seção: `IEC 62304 Sec. 5.3.3, 5.3.4, 7.1.2, 7.1.3` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_SOUP::s01` (Score: `0.5173`)
- **IEC62304_OPENREG_SOUP** (OpenRegulatory) — Cláusula/Seção: `Seção 5` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_SOUP::s05` (Score: `0.2119`)
- **IEC62304_OPENREG_SOUP** (OpenRegulatory) — Cláusula/Seção: `2 SOUP List` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_SOUP::s03` (Score: `0.2114`)

#### Limitações Técnicas
- Uma dependência sem versão fixada no repositório não representa automaticamente uma não conformidade, pois o congelamento de versões pode ocorrer em artefatos de build ou containers externos.
- A listagem em requirements.txt não substitui a documentação formal de SOUP (requisitos funcionais, nível de risco e verificação de anomalias conhecidas).

#### Recomendação de Investigação ou Correção
Avaliar o congelamento de versões (pinning/lockfile), reconciliar bibliotecas importadas no código com o manifesto e manter a matriz de rastreabilidade de SOUP atualizada.

### TA-003 (R03) — Evidências de testes automatizados no repositório
- **Categoria:** Verificação e Testes de Software
- **Status:** `observed` (Evidência identificada)
- **Prioridade de Revisão Técnica:** `low` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência identificada: 7 arquivo(s) de teste localizado(s) (diretórios: tests; frameworks: pytest; 24 função(ões)/método(s) de teste).
- **Justificativa de Rastreabilidade:** Módulos e funções de teste automatizado foram observados no repositório.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `tests/test_traceast_suite.py` | `test_01_file_discovery_and_100_percent_coverage` | 45–58 | `test_module` | Módulo de teste 'tests/test_traceast_suite.py' identificado (15 funções/métodos candidatos de teste). |
| `tests/fixtures/repo_deficient_and_coupled/model_pipeline.py` | `CoupledMedicalModel.__init__` | 8–9 | `test_module` | Módulo de teste 'tests/fixtures/repo_deficient_and_coupled/model_pipeline.py' identificado (3 funções/métodos candidatos de teste). |
| `tests/fixtures/repo_false_positive_traps/scheduler.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/fixtures/repo_false_positive_traps/scheduler.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/fixtures/repo_well_structured/src/data_io.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/fixtures/repo_well_structured/src/data_io.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/fixtures/repo_well_structured/src/inference.py` | `ChestDiagnosticModel.__init__` | 13–15 | `test_module` | Módulo de teste 'tests/fixtures/repo_well_structured/src/inference.py' identificado (4 funções/métodos candidatos de teste). |
| `tests/fixtures/repo_well_structured/src/trainer.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/fixtures/repo_well_structured/src/trainer.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/fixtures/repo_well_structured/tests/test_inference.py` | `test_validate_dicom_input_valid` | 7–8 | `test_module` | Módulo de teste 'tests/fixtures/repo_well_structured/tests/test_inference.py' identificado (2 funções/métodos candidatos de teste). |

#### Referências Regulatórias Relacionadas
- **IEC62304** (IEC) — Cláusula/Seção: `5.5.5; 5.6.3; 5.7` | Status da Validação: `pending_expert_review`
- **ANVISA_RDC_657_2022** (ANVISA) — Cláusula/Seção: `Art. 14` | Status da Validação: `pending_expert_review`
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 5.7.3, 5.7.4, 5.7.5` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s17` (Score: `0.2354`)
- **IEC62304_OPENREG_SOP_SW_DEV** (OpenRegulatory) — Cláusula/Seção: `8. Software System Testing` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_SOP_SW_DEV::s23` (Score: `0.1909`)
- **IEC62304_OPENREG_SOP_SW_DEV** (OpenRegulatory) — Cláusula/Seção: `8. Software System Testing` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_SOP_SW_DEV::s22` (Score: `0.1849`)

#### Limitações Técnicas
- A ausência de um diretório de testes no repositório analisado indica apenas ausência de evidência observável neste repositório, e NÃO prova que o fabricante não realiza testes em outro ambiente.
- A presença de arquivos de teste não comprova que os testes cobrem os requisitos de segurança ou passam.

#### Recomendação de Investigação ou Correção
Revisão humana necessária para verificar a rastreabilidade entre os casos de teste automatizados, os requisitos de software e os controles de risco (IEC 62304 Seções 5.5, 5.6 e 5.7).

### TA-004 (R04) — Integração contínua (CI/CD) e automação de verificação
- **Categoria:** Verificação e Integração Contínua
- **Status:** `observed` (Evidência identificada)
- **Prioridade de Revisão Técnica:** `low` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência identificada: 1 configuração(ões) de CI/CD localizada(s) com comandos declarados para execução automatizada de testes (evidências de cobertura: não identificadas).
- **Justificativa de Rastreabilidade:** Arquivos de workflow CI/CD contendo etapas de execução de testes foram encontrados.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `.github/workflows/ci.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/ci.yml' (comandos de teste: - name: Run automated test suite (pytest), python -m pytest -v; cobertura: False) |

#### Referências Regulatórias Relacionadas
- **IEC62304** (IEC) — Cláusula/Seção: `5.5.5; 5.6.4; 5.6.6` | Status da Validação: `pending_expert_review`
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 5.6.6, 5.6.7, 5.6.8` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s16` (Score: `0.5773`)
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 5.6.3, 5.6.4, 5.6.5` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s15` (Score: `0.5169`)
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 5.5.5, 5.6.1, 5.6.2` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s14` (Score: `0.3814`)

#### Limitações Técnicas
- Pipelines de CI/CD podem estar hospedados em servidores externos (Jenkins, Azure DevOps, GitLab externo) sem arquivo de configuração versionado na pasta .github/workflows.
- A presença do arquivo YAML não garante que o workflow esteja ativo ou aprovado nas branches protegidas.

#### Recomendação de Investigação ou Correção
Verificar se os registros de execução do CI/CD são arquivados como evidência de verificação e regressão a cada versão liberada (IEC 62304 Seção 5.6.6 e 5.8).

### TA-005 (R05) — Tratamento de erros e exceções em operações de I/O
- **Categoria:** Confiabilidade e Tratamento de Falhas
- **Status:** `partial` (Evidência parcial — indicador técnico que merece investigação)
- **Prioridade de Revisão Técnica:** `high` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência parcial: entre 54 operação(ões) candidatas de I/O, 9 possuem bloco try-except não vazio e 45 não possuem tratamento local observável. Foram identificados 4 bloco(s) except vazios ou com 'pass'.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: coexistem operações de I/O sem captura local de exceção ou blocos except que suprimem falhas com pass.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `analyzer.py` | `main` | 42–42 | `ast_io_operation` | Operação candidata de I/O 'json.dumps' em 'main' (dentro de try-except não vazio: False) |
| `analyzer.py` | `main` | 47–47 | `ast_io_operation` | Operação candidata de I/O 'out_path.write_text' em 'main' (dentro de try-except não vazio: False) |
| `analyzer.py` | `main` | 47–47 | `ast_io_operation` | Operação candidata de I/O 'json.dumps' em 'main' (dentro de try-except não vazio: False) |
| `tests/test_traceast_suite.py` | `test_03_secret_and_excluded_dirs_protection` | 80–80 | `ast_io_operation` | Operação candidata de I/O 'write_text' em 'test_03_secret_and_excluded_dirs_protection' (dentro de try-except não vazio: False) |
| `tests/test_traceast_suite.py` | `test_03_secret_and_excluded_dirs_protection` | 83–83 | `ast_io_operation` | Operação candidata de I/O 'write_text' em 'test_03_secret_and_excluded_dirs_protection' (dentro de try-except não vazio: False) |
| `tests/test_traceast_suite.py` | `test_03_secret_and_excluded_dirs_protection` | 84–84 | `ast_io_operation` | Operação candidata de I/O 'write_text' em 'test_03_secret_and_excluded_dirs_protection' (dentro de try-except não vazio: False) |
| `tests/test_traceast_suite.py` | `test_11_llm_optional_fallback_and_immutability_of_status.mock_llm_ok` | 267–273 | `ast_io_operation` | Operação candidata de I/O 'json.dumps' em 'test_11_llm_optional_fallback_and_immutability_of_status.mock_llm_ok' (dentro de try-except não vazio: False) |
| `tests/test_traceast_suite.py` | `test_13_full_pipeline_execution_and_artifacts` | 329–329 | `ast_io_operation` | Operação candidata de I/O 'read_text' em 'test_13_full_pipeline_execution_and_artifacts' (dentro de try-except não vazio: False) |
| `tests/test_traceast_suite.py` | `test_13_full_pipeline_execution_and_artifacts` | 331–331 | `ast_io_operation` | Operação candidata de I/O 'read_text' em 'test_13_full_pipeline_execution_and_artifacts' (dentro de try-except não vazio: False) |
| `tests/fixtures/repo_deficient_and_coupled/model_pipeline.py` | `CoupledMedicalModel.__init__` | 9–9 | `ast_io_operation` | Operação candidata de I/O 'torch.load' em 'CoupledMedicalModel.__init__' (dentro de try-except não vazio: False) |
| `tests/fixtures/repo_deficient_and_coupled/model_pipeline.py` | `CoupledMedicalModel.forward` | 13–13 | `ast_io_operation` | Operação candidata de I/O 'pd.read_csv' em 'CoupledMedicalModel.forward' (dentro de try-except não vazio: False) |
| `tests/fixtures/repo_deficient_and_coupled/model_pipeline.py` | `CoupledMedicalModel.forward` | 15–15 | `ast_io_operation` | Operação candidata de I/O 'open' em 'CoupledMedicalModel.forward' (dentro de try-except não vazio: False) |
| `tests/fixtures/repo_deficient_and_coupled/model_pipeline.py` | `CoupledMedicalModel.forward` | 14–17 | `ast_empty_or_pass_except` | Bloco try-except em 'CoupledMedicalModel.forward' possui handler vazio ou com instrução 'pass' (exceções: Exception) |
| `tests/fixtures/repo_well_structured/src/data_io.py` | `safe_load_dicom` | 26–26 | `ast_io_operation` | Operação candidata de I/O 'pydicom.dcmread' em 'safe_load_dicom' (dentro de try-except não vazio: True) |
| `tests/fixtures/repo_well_structured/src/inference.py` | `ChestDiagnosticModel.load_weights` | 19–19 | `ast_io_operation` | Operação candidata de I/O 'torch.load' em 'ChestDiagnosticModel.load_weights' (dentro de try-except não vazio: True) |
*... e mais 15 evidência(s) registrada(s) em `findings.json`.*

#### Referências Regulatórias Relacionadas
- **IEC62304** (IEC) — Cláusula/Seção: `5.1.12; 5.5.3; 7.1.2` | Status da Validação: `pending_expert_review`
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 5.1.12, 5.2.1, 5.2.2` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s07` (Score: `0.4122`)
- **IEC62304_OPENREG_DEV_PLAN** (OpenRegulatory) — Cláusula/Seção: `IEC 62304 Sec. 5.1.5, 5.1.6, 5.1.7, 5.1.8` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_DEV_PLAN::s03` (Score: `0.3344`)
- **IEC62304_OPENREG_DEV_PLAN** (OpenRegulatory) — Cláusula/Seção: `IEC 62304 Sec. 5.1.12, 6.1` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_DEV_PLAN::s04` (Score: `0.2835`)

#### Limitações Técnicas
- A presença de um bloco try-except NÃO comprova que o tratamento de erro é clinicamente seguro ou adequado aos controles de risco do dispositivo.
- O tratamento de exceções pode ocorrer em níveis superiores da pilha de chamadas (caller functions) não visíveis na inspeção intrafuncional.

#### Recomendação de Investigação ou Correção
Revisar cada operação de leitura/escrita sem tratamento de erro e eliminar blocos except vazios/pass que possam mascarar corrupção de arquivos ou dados clínicos.

### TA-006 (R06) — Sinais estruturais de validação de entradas
- **Categoria:** Verificação de Interfaces e Entradas
- **Status:** `observed` (Evidência identificada)
- **Prioridade de Revisão Técnica:** `medium` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `medium`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência identificada: 168 sinal(is) estrutural(is) de validação de entrada localizado(s), incluindo 37 função(ões)/chamada(s) de validação e 9 guarda(s) condicional(is) com levantamento de exceção.
- **Justificativa de Rastreabilidade:** Foram identificados mecanismos explícitos de verificação de entrada no código. A presença estrutural não garante suficiência clínica ou completude da validação.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `analyzer.py` | `analyze_repository` | 21–22 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'analyze_repository' |
| `tests/test_traceast_suite.py` | `test_01_file_discovery_and_100_percent_coverage` | 50–50 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'test_01_file_discovery_and_100_percent_coverage' |
| `tests/test_traceast_suite.py` | `test_01_file_discovery_and_100_percent_coverage` | 51–51 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'test_01_file_discovery_and_100_percent_coverage' |
| `tests/test_traceast_suite.py` | `test_01_file_discovery_and_100_percent_coverage` | 52–52 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'test_01_file_discovery_and_100_percent_coverage' |
| `tests/test_traceast_suite.py` | `test_01_file_discovery_and_100_percent_coverage` | 53–53 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'test_01_file_discovery_and_100_percent_coverage' |
| `tests/test_traceast_suite.py` | `test_01_file_discovery_and_100_percent_coverage` | 54–54 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'test_01_file_discovery_and_100_percent_coverage' |
| `tests/test_traceast_suite.py` | `test_01_file_discovery_and_100_percent_coverage` | 57–57 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'test_01_file_discovery_and_100_percent_coverage' |
| `tests/test_traceast_suite.py` | `test_01_file_discovery_and_100_percent_coverage` | 58–58 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'test_01_file_discovery_and_100_percent_coverage' |
| `tests/test_traceast_suite.py` | `test_02_syntax_error_recording_and_partial_coverage` | 66–66 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'test_02_syntax_error_recording_and_partial_coverage' |
| `tests/test_traceast_suite.py` | `test_02_syntax_error_recording_and_partial_coverage` | 67–67 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'test_02_syntax_error_recording_and_partial_coverage' |
| `tests/test_traceast_suite.py` | `test_02_syntax_error_recording_and_partial_coverage` | 68–68 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'test_02_syntax_error_recording_and_partial_coverage' |
| `tests/test_traceast_suite.py` | `test_02_syntax_error_recording_and_partial_coverage` | 69–69 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'test_02_syntax_error_recording_and_partial_coverage' |
| `tests/test_traceast_suite.py` | `test_02_syntax_error_recording_and_partial_coverage` | 72–72 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'test_02_syntax_error_recording_and_partial_coverage' |
| `tests/test_traceast_suite.py` | `test_02_syntax_error_recording_and_partial_coverage` | 73–73 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'test_02_syntax_error_recording_and_partial_coverage' |
| `tests/test_traceast_suite.py` | `test_02_syntax_error_recording_and_partial_coverage` | 74–74 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'test_02_syntax_error_recording_and_partial_coverage' |
*... e mais 15 evidência(s) registrada(s) em `findings.json`.*

#### Referências Regulatórias Relacionadas
- **IEC62304** (IEC) — Cláusula/Seção: `5.2.2; 5.3.2; 5.4.3` | Status da Validação: `pending_expert_review`
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 5.2.6, 5.3.1, 5.3.2` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s09` (Score: `0.4719`)
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 5.4.3, 5.4.4, 5.5.1` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s12` (Score: `0.1413`)
- **IEC62304_OPENREG_SOP_SW_DEV** (OpenRegulatory) — Cláusula/Seção: `IEC 62304 Sec. 5.4.3, 5.4.4, 5.5.1, 5.5.2` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_SOP_SW_DEV::s02` (Score: `0.1133`)

#### Limitações Técnicas
- A presença de uma condição if ou função de validação NÃO garante que os limites fisiológicos, formatos DICOM ou restrições clínicas de entrada foram devidamente validados.
- Instruções assert em Python podem ser desabilitadas em execução otimizada (python -O).

#### Recomendação de Investigação ou Correção
Revisão humana necessária para verificar se os critérios de validação cobrem formatos inválidos, valores ausentes, limites fisiológicos/dimensionais e proteção contra entradas malformadas.

### TA-007 (R07) — Proveniência, carregamento e versionamento de artefatos de modelos
- **Categoria:** Rastreabilidade de Modelos de IA/ML
- **Status:** `partial` (Evidência parcial — indicador técnico que merece investigação)
- **Prioridade de Revisão Técnica:** `high` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência parcial: foram identificados 5 sinal(is) de carregamento, salvamento ou referência a checkpoints de modelos (0 arquivo(s) de modelo no repositório). A existência de chamadas de carga ou arquivos .pt/.pth/.onnx não comprova proveniência completa nem controle de versão do modelo.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: artefatos de modelo exigem rastreabilidade documental de versão, dataset de treinamento, hiperparâmetros e verificação de integridade (hash).

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `tests/fixtures/repo_deficient_and_coupled/model_pipeline.py` | `CoupledMedicalModel.__init__` | 9–9 | `model_model_load` | Operação/referência de modelo (model_load) em 'CoupledMedicalModel.__init__' |
| `tests/fixtures/repo_deficient_and_coupled/model_pipeline.py` | `CoupledMedicalModel.__init__` | 9–9 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'CoupledMedicalModel.__init__' |
| `tests/fixtures/repo_well_structured/src/inference.py` | `ChestDiagnosticModel.load_weights` | 19–19 | `model_model_load` | Operação/referência de modelo (model_load) em 'ChestDiagnosticModel.load_weights' |
| `tests/fixtures/repo_well_structured/src/trainer.py` | `train_chest_model` | 19–19 | `model_model_save` | Operação/referência de modelo (model_save) em 'train_chest_model' |
| `tests/fixtures/repo_well_structured/src/trainer.py` | `train_chest_model` | 19–19 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'train_chest_model' |

#### Referências Regulatórias Relacionadas
- **IEC62304** (IEC) — Cláusula/Seção: `8.1.1; 8.3` | Status da Validação: `pending_expert_review`
- **OPENREGULATORY_ML_SOP** (OpenRegulatory) — Cláusula/Seção: `Section 1.2; Section 2.5` | Status da Validação: `pending_expert_review`
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 8.1.1, 8.1.2, 8.1.3` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s28` (Score: `0.1611`)
- **OPENREG_INSTRUCTIONS_ON_DATA_ACQUISITION** (OpenRegulatory) — Cláusula/Seção: `Instructions on Data Acquisition` | Status da Validação: `pending_expert_review` | Fragmento: `OPENREG_INSTRUCTIONS_ON_DATA_ACQUISITION::s01` (Score: `0.1569`)
- **OPENREG_SOP_ML_DEV** (OpenRegulatory) — Cláusula/Seção: `2.6. Production Deployment of ML Model` | Status da Validação: `pending_expert_review` | Fragmento: `OPENREG_SOP_ML_DEV::s14` (Score: `0.1532`)

#### Limitações Técnicas
- A existência de um arquivo .pt, .pth ou .onnx NÃO comprova a proveniência do modelo, a qualidade dos dados de treinamento nem a reprodutibilidade dos hiperparâmetros.
- Pesos de modelos frequentemente são armazenados fora do repositório Git (DVC, MLflow, S3, HuggingFace Hub).

#### Recomendação de Investigação ou Correção
Documentar formalmente a proveniência de cada modelo carregado (identificador de versão, hash SHA-256 do artefato, dataset de origem, hiperparâmetros e Relatório de Validação de Algoritmo).

### TA-008 (R08) — Sinais estruturais de separação entre treinamento e inferência
- **Categoria:** Arquitetura e Isolamento de Ambientes (IA/ML)
- **Status:** `partial` (Evidência parcial — indicador técnico que merece investigação)
- **Prioridade de Revisão Técnica:** `high` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `medium`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência parcial: sinais estruturais de treinamento e de inferência coexistem no(s) mesmo(s) arquivo(s) (tests/fixtures/repo_deficient_and_coupled/model_pipeline.py). Indicador técnico que merece investigação quanto à segregação arquitetural entre desenvolvimento/treino e produção/inferência.
- **Justificativa de Rastreabilidade:** Coexistência de sinais de treinamento e inferência em tests/fixtures/repo_deficient_and_coupled/model_pipeline.py. Requer inspeção humana do fluxo de controle para verificar se o modelo é congelado em produção.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `tests/fixtures/repo_deficient_and_coupled/model_pipeline.py` | `CoupledMedicalModel.train_and_predict_online` | 20–25 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'CoupledMedicalModel.train_and_predict_online' |
| `tests/fixtures/repo_deficient_and_coupled/model_pipeline.py` | `CoupledMedicalModel.train_and_predict_online` | 21–21 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'CoupledMedicalModel.train_and_predict_online' |
| `tests/fixtures/repo_deficient_and_coupled/model_pipeline.py` | `CoupledMedicalModel.train_and_predict_online` | 23–23 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'CoupledMedicalModel.train_and_predict_online' |
| `tests/fixtures/repo_deficient_and_coupled/model_pipeline.py` | `CoupledMedicalModel.train_and_predict_online` | 24–24 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'CoupledMedicalModel.train_and_predict_online' |
| `tests/fixtures/repo_deficient_and_coupled/model_pipeline.py` | `CoupledMedicalModel.forward` | 11–18 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'CoupledMedicalModel.forward' |
| `tests/fixtures/repo_deficient_and_coupled/model_pipeline.py` | `CoupledMedicalModel.train_and_predict_online` | 20–25 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'CoupledMedicalModel.train_and_predict_online' |
| `tests/fixtures/repo_well_structured/src/inference.py` | `ChestDiagnosticModel.forward` | 24–26 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'ChestDiagnosticModel.forward' |
| `tests/fixtures/repo_well_structured/src/inference.py` | `ChestDiagnosticModel.async_predict_study` | 28–33 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'ChestDiagnosticModel.async_predict_study' |
| `tests/fixtures/repo_well_structured/src/inference.py` | `ChestDiagnosticModel.async_predict_study` | 31–31 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'ChestDiagnosticModel.async_predict_study' |
| `tests/fixtures/repo_well_structured/src/trainer.py` | `train_chest_model` | 9–22 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'train_chest_model' |
| `tests/fixtures/repo_well_structured/src/trainer.py` | `train_chest_model` | 11–11 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'train_chest_model' |
| `tests/fixtures/repo_well_structured/src/trainer.py` | `train_chest_model` | 13–13 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'train_chest_model' |
| `tests/fixtures/repo_well_structured/src/trainer.py` | `train_chest_model` | 15–15 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'train_chest_model' |
| `tests/fixtures/repo_well_structured/src/trainer.py` | `train_chest_model` | 16–16 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'train_chest_model' |

#### Referências Regulatórias Relacionadas
- **IEC62304** (IEC) — Cláusula/Seção: `5.3.1; 5.3.5` | Status da Validação: `pending_expert_review`
- **OPENREGULATORY_ML_SOP** (OpenRegulatory) — Cláusula/Seção: `Section 2.1; Section 2.6` | Status da Validação: `pending_expert_review`
- **OPENREG_SOP_ML_DEV** (OpenRegulatory) — Cláusula/Seção: `2.6. Production Deployment of ML Model` | Status da Validação: `pending_expert_review` | Fragmento: `OPENREG_SOP_ML_DEV::s14` (Score: `0.3274`)
- **OPENREG_SOP_ML_DEV** (OpenRegulatory) — Cláusula/Seção: `1.2. Project Management Tool` | Status da Validação: `pending_expert_review` | Fragmento: `OPENREG_SOP_ML_DEV::s03` (Score: `0.2897`)
- **OPENREG_SOP_ML_DEV** (OpenRegulatory) — Cláusula/Seção: `2.7. Handling of Updates` | Status da Validação: `pending_expert_review` | Fragmento: `OPENREG_SOP_ML_DEV::s15` (Score: `0.15`)

#### Limitações Técnicas
- A análise estática AST NÃO consegue provar separação efetiva em tempo de execução nem isolamento de infraestrutura entre servidores de desenvolvimento e produção.
- Classes de modelos (como torch.nn.Module) naturalmente definem o método forward usado tanto no treino quanto na inferência; portanto, a presença no mesmo arquivo exige análise humana do fluxo de execução.

#### Recomendação de Investigação ou Correção
Revisar a arquitetura dos módulos listados para separar claramente os scripts de treinamento do pipeline de inferência clínica e documentar o controle de implantação (SOP Deployment).

## E. Referências Regulatórias e Rastreabilidade Documental

- **Modelo de Embeddings Configurado:** `sentence-transformers/all-MiniLM-L6-v2`
- **Motor de Recuperação Executado:** `local_deterministic_tfidf (sentence-transformers/all-MiniLM-L6-v2 configured)`

| Regra | Fragmento (`chunk_id`) | Documento | Emissor | Página/Seção | Score | Hash SHA-256 (Prefixo) | Status |
|---|---|---|---|---|---|---|---|
| `R01` | `IEC62304_OPENREG_MAPPING::s13` | `IEC62304_OPENREG_MAPPING` | OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006) | Pág. N/A (Markdown) / IEC 62304 Sec. 5.5.2, 5.5.3, 5.5.4 | `0.2247` | `a34c3dc8be56...` | `pending_expert_review` |
| `R01` | `IEC62304_OPENREG_MAPPING::s06` | `IEC62304_OPENREG_MAPPING` | OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006) | Pág. N/A (Markdown) / IEC 62304 Sec. 5.1.9, 5.1.10, 5.1.11 | `0.19` | `a34c3dc8be56...` | `pending_expert_review` |
| `R01` | `IEC62304_OPENREG_DEV_PLAN::s03` | `IEC62304_OPENREG_DEV_PLAN` | OpenRegulatory | Pág. N/A (Markdown) / IEC 62304 Sec. 5.1.5, 5.1.6, 5.1.7, 5.1.8 | `0.1647` | `0eaa930e62cb...` | `pending_expert_review` |
| `R02` | `IEC62304_OPENREG_SOUP::s01` | `IEC62304_OPENREG_SOUP` | OpenRegulatory | Pág. N/A (Markdown) / IEC 62304 Sec. 5.3.3, 5.3.4, 7.1.2, 7.1.3 | `0.5173` | `800238730b35...` | `pending_expert_review` |
| `R02` | `IEC62304_OPENREG_SOUP::s05` | `IEC62304_OPENREG_SOUP` | OpenRegulatory | Pág. N/A (Markdown) / Seção 5 | `0.2119` | `800238730b35...` | `pending_expert_review` |
| `R02` | `IEC62304_OPENREG_SOUP::s03` | `IEC62304_OPENREG_SOUP` | OpenRegulatory | Pág. N/A (Markdown) / 2 SOUP List | `0.2114` | `800238730b35...` | `pending_expert_review` |
| `R03` | `IEC62304_OPENREG_MAPPING::s17` | `IEC62304_OPENREG_MAPPING` | OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006) | Pág. N/A (Markdown) / IEC 62304 Sec. 5.7.3, 5.7.4, 5.7.5 | `0.2354` | `a34c3dc8be56...` | `pending_expert_review` |
| `R03` | `IEC62304_OPENREG_SOP_SW_DEV::s23` | `IEC62304_OPENREG_SOP_SW_DEV` | OpenRegulatory | Pág. N/A (Markdown) / 8. Software System Testing | `0.1909` | `de0c62933df0...` | `pending_expert_review` |
| `R03` | `IEC62304_OPENREG_SOP_SW_DEV::s22` | `IEC62304_OPENREG_SOP_SW_DEV` | OpenRegulatory | Pág. N/A (Markdown) / 8. Software System Testing | `0.1849` | `de0c62933df0...` | `pending_expert_review` |
| `R04` | `IEC62304_OPENREG_MAPPING::s16` | `IEC62304_OPENREG_MAPPING` | OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006) | Pág. N/A (Markdown) / IEC 62304 Sec. 5.6.6, 5.6.7, 5.6.8 | `0.5773` | `a34c3dc8be56...` | `pending_expert_review` |
| `R04` | `IEC62304_OPENREG_MAPPING::s15` | `IEC62304_OPENREG_MAPPING` | OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006) | Pág. N/A (Markdown) / IEC 62304 Sec. 5.6.3, 5.6.4, 5.6.5 | `0.5169` | `a34c3dc8be56...` | `pending_expert_review` |
| `R04` | `IEC62304_OPENREG_MAPPING::s14` | `IEC62304_OPENREG_MAPPING` | OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006) | Pág. N/A (Markdown) / IEC 62304 Sec. 5.5.5, 5.6.1, 5.6.2 | `0.3814` | `a34c3dc8be56...` | `pending_expert_review` |
| `R05` | `IEC62304_OPENREG_MAPPING::s07` | `IEC62304_OPENREG_MAPPING` | OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006) | Pág. N/A (Markdown) / IEC 62304 Sec. 5.1.12, 5.2.1, 5.2.2 | `0.4122` | `a34c3dc8be56...` | `pending_expert_review` |
| `R05` | `IEC62304_OPENREG_DEV_PLAN::s03` | `IEC62304_OPENREG_DEV_PLAN` | OpenRegulatory | Pág. N/A (Markdown) / IEC 62304 Sec. 5.1.5, 5.1.6, 5.1.7, 5.1.8 | `0.3344` | `0eaa930e62cb...` | `pending_expert_review` |
| `R05` | `IEC62304_OPENREG_DEV_PLAN::s04` | `IEC62304_OPENREG_DEV_PLAN` | OpenRegulatory | Pág. N/A (Markdown) / IEC 62304 Sec. 5.1.12, 6.1 | `0.2835` | `0eaa930e62cb...` | `pending_expert_review` |
| `R06` | `IEC62304_OPENREG_MAPPING::s09` | `IEC62304_OPENREG_MAPPING` | OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006) | Pág. N/A (Markdown) / IEC 62304 Sec. 5.2.6, 5.3.1, 5.3.2 | `0.4719` | `a34c3dc8be56...` | `pending_expert_review` |
| `R06` | `IEC62304_OPENREG_MAPPING::s12` | `IEC62304_OPENREG_MAPPING` | OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006) | Pág. N/A (Markdown) / IEC 62304 Sec. 5.4.3, 5.4.4, 5.5.1 | `0.1413` | `a34c3dc8be56...` | `pending_expert_review` |
| `R06` | `IEC62304_OPENREG_SOP_SW_DEV::s02` | `IEC62304_OPENREG_SOP_SW_DEV` | OpenRegulatory | Pág. N/A (Markdown) / IEC 62304 Sec. 5.4.3, 5.4.4, 5.5.1, 5.5.2 | `0.1133` | `de0c62933df0...` | `pending_expert_review` |
| `R07` | `IEC62304_OPENREG_MAPPING::s28` | `IEC62304_OPENREG_MAPPING` | OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006) | Pág. N/A (Markdown) / IEC 62304 Sec. 8.1.1, 8.1.2, 8.1.3 | `0.1611` | `a34c3dc8be56...` | `pending_expert_review` |
| `R07` | `OPENREG_INSTRUCTIONS_ON_DATA_ACQUISITION::s01` | `OPENREG_INSTRUCTIONS_ON_DATA_ACQUISITION` | OpenRegulatory | Pág. N/A (Markdown) / Instructions on Data Acquisition | `0.1569` | `cabb255a6479...` | `pending_expert_review` |
| `R07` | `OPENREG_SOP_ML_DEV::s14` | `OPENREG_SOP_ML_DEV` | OpenRegulatory | Pág. N/A (Markdown) / 2.6. Production Deployment of ML Model | `0.1532` | `fa0b58737139...` | `pending_expert_review` |
| `R08` | `OPENREG_SOP_ML_DEV::s14` | `OPENREG_SOP_ML_DEV` | OpenRegulatory | Pág. N/A (Markdown) / 2.6. Production Deployment of ML Model | `0.3274` | `fa0b58737139...` | `pending_expert_review` |
| `R08` | `OPENREG_SOP_ML_DEV::s03` | `OPENREG_SOP_ML_DEV` | OpenRegulatory | Pág. N/A (Markdown) / 1.2. Project Management Tool | `0.2897` | `fa0b58737139...` | `pending_expert_review` |
| `R08` | `OPENREG_SOP_ML_DEV::s15` | `OPENREG_SOP_ML_DEV` | OpenRegulatory | Pág. N/A (Markdown) / 2.7. Handling of Updates | `0.15` | `fa0b58737139...` | `pending_expert_review` |

## F. Plano de Ação Preliminar Organizado por Prioridade de Revisão

### Prioridade de Revisão Alta (`high`)
1. **TA-001 (R01 — Cobertura e integridade da inspeção estática)** [Evidência parcial — indicador técnico que merece investigação]: Corrigir os erros de sintaxe ou codificação nos arquivos listados e reexecutar a triagem para garantir cobertura completa.
1. **TA-005 (R05 — Tratamento de erros e exceções em operações de I/O)** [Evidência parcial — indicador técnico que merece investigação]: Revisar cada operação de leitura/escrita sem tratamento de erro e eliminar blocos except vazios/pass que possam mascarar corrupção de arquivos ou dados clínicos.
1. **TA-007 (R07 — Proveniência, carregamento e versionamento de artefatos de modelos)** [Evidência parcial — indicador técnico que merece investigação]: Documentar formalmente a proveniência de cada modelo carregado (identificador de versão, hash SHA-256 do artefato, dataset de origem, hiperparâmetros e Relatório de Validação de Algoritmo).
1. **TA-008 (R08 — Sinais estruturais de separação entre treinamento e inferência)** [Evidência parcial — indicador técnico que merece investigação]: Revisar a arquitetura dos módulos listados para separar claramente os scripts de treinamento do pipeline de inferência clínica e documentar o controle de implantação (SOP Deployment).

### Prioridade de Revisão Média (`medium`)
1. **TA-002 (R02 — Gerenciamento de dependências e componentes externos (SOUP))** [Evidência parcial — indicador técnico que merece investigação]: Avaliar o congelamento de versões (pinning/lockfile), reconciliar bibliotecas importadas no código com o manifesto e manter a matriz de rastreabilidade de SOUP atualizada.
1. **TA-006 (R06 — Sinais estruturais de validação de entradas)** [Evidência identificada]: Revisão humana necessária para verificar se os critérios de validação cobrem formatos inválidos, valores ausentes, limites fisiológicos/dimensionais e proteção contra entradas malformadas.

### Prioridade de Revisão Baixa (`low`)
1. **TA-003 (R03 — Evidências de testes automatizados no repositório)** [Evidência identificada]: Revisão humana necessária para verificar a rastreabilidade entre os casos de teste automatizados, os requisitos de software e os controles de risco (IEC 62304 Seções 5.5, 5.6 e 5.7).
1. **TA-004 (R04 — Integração contínua (CI/CD) e automação de verificação)** [Evidência identificada]: Verificar se os registros de execução do CI/CD são arquivados como evidência de verificação e regressão a cada versão liberada (IEC 62304 Seção 5.6.6 e 5.8).
