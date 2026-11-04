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

- **Nome do Projeto:** TEST-005_microsoft__InnerEye-DeepLearning
- **Commit SHA Analisado:** `69a64d1df50ba0523be453c2fad4ff54cf31367f`
- **Data e Horário da Execução (UTC):** `2026-11-04T22:15:06.566196+00:00`
- **Versão do TraceAST-62304:** `1.0.0`
- **Hash do Catálogo de Regras:** `35cab4357bb9a065b099324cbaf932c804bbfe9119eabd990ae48127794741e1`
- **Versão do Python:** `3.13.14`

### Perfil do Produto Informado pelo Usuário
- **Nome declarado:** Unknown Medical Software Project
- **Finalidade médica pretendida (`intended_purpose`):** unknown
- **Usuários pretendidos (`intended_users`):** unknown
- **Mercado-alvo (`target_market`):** Brazil
- **Tipo de software (`software_type`):** unknown
- **Componentes de IA declarados (`ai_components`):** `None`
- **Contexto de decisão clínica (`clinical_decision_context`):** unknown
- **Limitações decorrentes do perfil:**
  - Nenhum arquivo de perfil do produto (product_profile.yaml) foi fornecido na execução.
  - Finalidade médica pretendida (intended_purpose) não informada ou desconhecida. O sistema não infere finalidade clínica pelos nomes de classes ou funções; a contextualização regulatória requer revisão humana.
  - Contexto de decisão clínica (clinical_decision_context) desconhecido. Impossível contextualizar o impacto operacional sem definição formal pelo fabricante.
  - Presença de componentes de IA (ai_components) não declarada no perfil; regras de ML serão avaliadas apenas por sinais estruturais no código.

## B. Integridade da Análise

- **Quantidade total de arquivos encontrados:** 611
- **Quantidade de arquivos Python (`.py`):** 265
- **Arquivos Python analisados com sucesso:** 265
- **Arquivos Python que falharam na análise:** 0
- **Percentual de cobertura da inspeção sintática:** 100.0%

*Nenhum arquivo Python falhou durante o parsing sintático AST.*

## C. Visão Geral dos Indicadores Técnicos

| Estado do Indicador | Expressão Padronizada | Quantidade |
|---|---|---|
| `observed` | Evidência identificada | 3 |
| `partial` | Evidência parcial — indicador técnico que merece investigação | 4 |
| `not_observed` | Evidência não identificada no repositório analisado | 1 |
| `unable_to_assess` | Impossível avaliar com os dados disponíveis | 0 |
| `not_applicable` | Não aplicável ao escopo declarado | 0 |
| **Revisão Humana** | **Itens que exigem revisão humana (`human_review_required`)** | **8** |

## D. Achados Detalhados

### TA-001 (R01) — Cobertura e integridade da inspeção estática
- **Categoria:** Integridade da Inspeção
- **Status:** `observed` (Evidência identificada)
- **Prioridade de Revisão Técnica:** `informational` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência identificada: todos os 265 arquivos Python encontrados foram analisados com sucesso via AST (cobertura de inspeção: 100.0%).
- **Justificativa de Rastreabilidade:** Inspeção concluída sem falhas de parsing em 265/265 arquivos Python.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `conftest.py` | `<module>` | 1–43 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: db690de1cccf...) |
| `mypy_runner.py` | `<module>` | 1–97 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 33407bad98f1...) |
| `score.py` | `<module>` | 1–317 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: b7ceb54158a5...) |
| `setup.py` | `<module>` | 1–143 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: fb63178cae36...) |
| `InnerEye/Azure/azure_config.py` | `<module>` | 1–266 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: c7c86bff64b6...) |
| `InnerEye/Azure/azure_runner.py` | `<module>` | 1–338 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: d2b2e625537d...) |
| `InnerEye/Azure/azure_util.py` | `<module>` | 1–386 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 735e6878a1ad...) |
| `InnerEye/Azure/parser_util.py` | `<module>` | 1–49 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: b8b855305eeb...) |
| `InnerEye/Azure/run_pytest.py` | `<module>` | 1–59 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 9f3411e868e1...) |
| `InnerEye/Azure/secrets_handling.py` | `<module>` | 1–162 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: a801d9c4af38...) |
| `InnerEye/Azure/tensorboard_monitor.py` | `<module>` | 1–109 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 20e26f4d3b65...) |
| `InnerEye/Common/common_util.py` | `<module>` | 1–508 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 64db58f9bc38...) |
| `InnerEye/Common/fixed_paths.py` | `<module>` | 1–130 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e5fc0b9885fa...) |
| `InnerEye/Common/fixed_paths_for_tests.py` | `<module>` | 1–40 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: f8655d7c6033...) |
| `InnerEye/Common/generic_parsing.py` | `<module>` | 1–369 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: dd6e7f86c4f4...) |

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
Manter a verificação sintática íntegra no fluxo de desenvolvimento.

### TA-002 (R02) — Gerenciamento de dependências e componentes externos (SOUP)
- **Categoria:** Gerenciamento de Configuração e SOUP
- **Status:** `not_observed` (Evidência não identificada no repositório analisado)
- **Prioridade de Revisão Técnica:** `high` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência não identificada no repositório analisado: não foram localizados arquivos de gerenciamento de dependências (requirements.txt, pyproject.toml, poetry.lock). Foram identificados 45 módulos externos importados no código (GPUtil, IPython, InnerEye_DICOM_RT, PIL, SimpleITK, attr, azure, azureml, conda_merge, dataclasses_json). Possível lacuna documental de SOUP.
- **Justificativa de Rastreabilidade:** Ausência de manifesto de dependências observável no diretório inspecionado.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `conftest.py` | `pytest` | 1–1 | `undeclared_import` | Módulo externo 'pytest' importado em 'conftest.py', mas não localizado nos manifestos de dependências inspecionados. |
| `score.py` | `InnerEye_DICOM_RT` | 1–1 | `undeclared_import` | Módulo externo 'InnerEye_DICOM_RT' importado em 'score.py', mas não localizado nos manifestos de dependências inspecionados. |
| `score.py` | `azureml` | 1–1 | `undeclared_import` | Módulo externo 'azureml' importado em 'score.py', mas não localizado nos manifestos de dependências inspecionados. |
| `score.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'score.py', mas não localizado nos manifestos de dependências inspecionados. |
| `score.py` | `param` | 1–1 | `undeclared_import` | Módulo externo 'param' importado em 'score.py', mas não localizado nos manifestos de dependências inspecionados. |
| `setup.py` | `ruamel` | 1–1 | `undeclared_import` | Módulo externo 'ruamel' importado em 'setup.py', mas não localizado nos manifestos de dependências inspecionados. |
| `setup.py` | `setuptools` | 1–1 | `undeclared_import` | Módulo externo 'setuptools' importado em 'setup.py', mas não localizado nos manifestos de dependências inspecionados. |
| `InnerEye/Azure/azure_config.py` | `azureml` | 1–1 | `undeclared_import` | Módulo externo 'azureml' importado em 'InnerEye/Azure/azure_config.py', mas não localizado nos manifestos de dependências inspecionados. |
| `InnerEye/Azure/azure_config.py` | `git` | 1–1 | `undeclared_import` | Módulo externo 'git' importado em 'InnerEye/Azure/azure_config.py', mas não localizado nos manifestos de dependências inspecionados. |
| `InnerEye/Azure/azure_config.py` | `param` | 1–1 | `undeclared_import` | Módulo externo 'param' importado em 'InnerEye/Azure/azure_config.py', mas não localizado nos manifestos de dependências inspecionados. |
| `InnerEye/Azure/azure_runner.py` | `health_azure` | 1–1 | `undeclared_import` | Módulo externo 'health_azure' importado em 'InnerEye/Azure/azure_runner.py', mas não localizado nos manifestos de dependências inspecionados. |
| `InnerEye/Azure/azure_util.py` | `azureml` | 1–1 | `undeclared_import` | Módulo externo 'azureml' importado em 'InnerEye/Azure/azure_util.py', mas não localizado nos manifestos de dependências inspecionados. |
| `InnerEye/Azure/azure_util.py` | `health_azure` | 1–1 | `undeclared_import` | Módulo externo 'health_azure' importado em 'InnerEye/Azure/azure_util.py', mas não localizado nos manifestos de dependências inspecionados. |
| `InnerEye/Azure/run_pytest.py` | `azureml` | 1–1 | `undeclared_import` | Módulo externo 'azureml' importado em 'InnerEye/Azure/run_pytest.py', mas não localizado nos manifestos de dependências inspecionados. |
| `InnerEye/Azure/run_pytest.py` | `pytest` | 1–1 | `undeclared_import` | Módulo externo 'pytest' importado em 'InnerEye/Azure/run_pytest.py', mas não localizado nos manifestos de dependências inspecionados. |
*... e mais 561 evidência(s) registrada(s) em `findings.json`.*

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
Documentar todas as bibliotecas externas (SOUP) em manifesto versionado (ex.: requirements.txt ou pyproject.toml) e elaborar a lista formal de SOUP conforme IEC 62304 (Seção 8.1.2 e 5.3.3).

### TA-003 (R03) — Evidências de testes automatizados no repositório
- **Categoria:** Verificação e Testes de Software
- **Status:** `observed` (Evidência identificada)
- **Prioridade de Revisão Técnica:** `low` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência identificada: 98 arquivo(s) de teste localizado(s) (diretórios: tests; frameworks: pytest, unittest; 701 função(ões)/método(s) de teste).
- **Justificativa de Rastreabilidade:** Módulos e funções de teste automatizado foram observados no repositório.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `InnerEye/Common/Statistics/mann_whitney_test.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'InnerEye/Common/Statistics/mann_whitney_test.py' identificado (0 funções/métodos candidatos de teste). |
| `InnerEye/Common/Statistics/wilcoxon_signed_rank_test.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'InnerEye/Common/Statistics/wilcoxon_signed_rank_test.py' identificado (0 funções/métodos candidatos de teste). |
| `TestSubmodule/test_submodule_runner.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'TestSubmodule/test_submodule_runner.py' identificado (0 funções/métodos candidatos de teste). |
| `Tests/AfterTraining/test_after_training.py` | `test_registered_model_file_structure_and_instantiate` | 151–188 | `test_module` | Módulo de teste 'Tests/AfterTraining/test_after_training.py' identificado (15 funções/métodos candidatos de teste). |
| `Tests/Azure/test_azure_config.py` | `test_validate` | 17–20 | `test_module` | Módulo de teste 'Tests/Azure/test_azure_config.py' identificado (7 funções/métodos candidatos de teste). |
| `Tests/Azure/test_azure_util.py` | `test_os_path_to_azure_friendly_container_path` | 26–33 | `test_module` | Módulo de teste 'Tests/Azure/test_azure_util.py' identificado (9 funções/métodos candidatos de teste). |
| `Tests/Azure/test_download_pytest.py` | `test_download_pytest_file` | 17–39 | `test_module` | Módulo de teste 'Tests/Azure/test_download_pytest.py' identificado (1 funções/métodos candidatos de teste). |
| `Tests/Azure/test_git.py` | `test_git_info` | 18–37 | `test_module` | Módulo de teste 'Tests/Azure/test_git.py' identificado (2 funções/métodos candidatos de teste). |
| `Tests/Azure/test_monitor.py` | `test_monitor_args_run_ids` | 22–31 | `test_module` | Módulo de teste 'Tests/Azure/test_monitor.py' identificado (4 funções/métodos candidatos de teste). |
| `Tests/Azure/test_parsing.py` | `test_is_empty_list` | 20–24 | `test_module` | Módulo de teste 'Tests/Azure/test_parsing.py' identificado (7 funções/métodos candidatos de teste). |
| `Tests/Azure/test_recovery_id.py` | `test_split_recovery_id` | 21–25 | `test_module` | Módulo de teste 'Tests/Azure/test_recovery_id.py' identificado (2 funções/métodos candidatos de teste). |
| `Tests/Azure/test_secrets_handling.py` | `test_environ_get_set` | 30–42 | `test_module` | Módulo de teste 'Tests/Azure/test_secrets_handling.py' identificado (5 funções/métodos candidatos de teste). |
| `Tests/Common/test_commandline_parsing.py` | `test_create_ml_runner_args` | 24–94 | `test_module` | Módulo de teste 'Tests/Common/test_commandline_parsing.py' identificado (5 funções/métodos candidatos de teste). |
| `Tests/Common/test_generic_parsing.py` | `test_string_or_list` | 44–55 | `test_module` | Módulo de teste 'Tests/Common/test_generic_parsing.py' identificado (7 funções/métodos candidatos de teste). |
| `Tests/Common/test_metrics_dict.py` | `test_average_metric_values` | 25–37 | `test_module` | Módulo de teste 'Tests/Common/test_metrics_dict.py' identificado (27 funções/métodos candidatos de teste). |
*... e mais 85 evidência(s) registrada(s) em `findings.json`.*

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
- **Status:** `partial` (Evidência parcial — indicador técnico que merece investigação)
- **Prioridade de Revisão Técnica:** `medium` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência parcial: arquivo(s) de workflow CI/CD encontrado(s) (.github/workflows/check-pr-title.yml, .github/workflows/codeql-analysis.yml, .github/workflows/issues_to_ado.yml, .github/workflows/linting_and_hello_world.yml, .github/workflows/main.yml), porém sem comandos explícitos de execução de testes Python (pytest/unittest) identificados.
- **Justificativa de Rastreabilidade:** Configuração de CI presente, mas sem etapa observável de teste automatizado.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `.github/workflows/check-pr-title.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/check-pr-title.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/codeql-analysis.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/codeql-analysis.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/issues_to_ado.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/issues_to_ado.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/linting_and_hello_world.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/linting_and_hello_world.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/main.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/main.yml' (comandos de teste: nenhum detectado; cobertura: False) |

#### Referências Regulatórias Relacionadas
- **IEC62304** (IEC) — Cláusula/Seção: `5.5.5; 5.6.4; 5.6.6` | Status da Validação: `pending_expert_review`
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 5.6.6, 5.6.7, 5.6.8` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s16` (Score: `0.5773`)
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 5.6.3, 5.6.4, 5.6.5` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s15` (Score: `0.5169`)
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 5.5.5, 5.6.1, 5.6.2` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s14` (Score: `0.3814`)

#### Limitações Técnicas
- Pipelines de CI/CD podem estar hospedados em servidores externos (Jenkins, Azure DevOps, GitLab externo) sem arquivo de configuração versionado na pasta .github/workflows.
- A presença do arquivo YAML não garante que o workflow esteja ativo ou aprovado nas branches protegidas.

#### Recomendação de Investigação ou Correção
Incluir etapa de execução de testes automatizados e verificação no pipeline de CI/CD.

### TA-005 (R05) — Tratamento de erros e exceções em operações de I/O
- **Categoria:** Confiabilidade e Tratamento de Falhas
- **Status:** `partial` (Evidência parcial — indicador técnico que merece investigação)
- **Prioridade de Revisão Técnica:** `high` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência parcial: entre 263 operação(ões) candidatas de I/O, 3 possuem bloco try-except não vazio e 260 não possuem tratamento local observável. Foram identificados 6 bloco(s) except vazios ou com 'pass'.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: coexistem operações de I/O sem captura local de exceção ou blocos except que suprimem falhas com pass.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `setup.py` | N/A | 24–24 | `ast_io_operation` | Operação candidata de I/O 'read_text' em '<module>' (dentro de try-except não vazio: False) |
| `setup.py` | N/A | 41–41 | `ast_io_operation` | Operação candidata de I/O 'write_text' em '<module>' (dentro de try-except não vazio: False) |
| `setup.py` | N/A | 95–95 | `ast_io_operation` | Operação candidata de I/O 'open' em '<module>' (dentro de try-except não vazio: False) |
| `InnerEye/Azure/secrets_handling.py` | `SecretsHandling.read_secrets_from_file` | 50–50 | `ast_io_operation` | Operação candidata de I/O 'secrets_file.read_text' em 'SecretsHandling.read_secrets_from_file' (dentro de try-except não vazio: False) |
| `InnerEye/Azure/secrets_handling.py` | `read_settings_yaml_file` | 154–154 | `ast_io_operation` | Operação candidata de I/O 'ruamel.yaml.load' em 'read_settings_yaml_file' (dentro de try-except não vazio: False) |
| `InnerEye/Azure/secrets_handling.py` | `read_settings_yaml_file` | 154–154 | `ast_io_operation` | Operação candidata de I/O 'yaml_file.open' em 'read_settings_yaml_file' (dentro de try-except não vazio: False) |
| `InnerEye/Common/common_util.py` | `merge_conda_files` | 460–460 | `ast_io_operation` | Operação candidata de I/O 'pip_file.read_text' em 'merge_conda_files' (dentro de try-except não vazio: False) |
| `InnerEye/Common/common_util.py` | `merge_conda_files` | 506–506 | `ast_io_operation` | Operação candidata de I/O 'result_file.open' em 'merge_conda_files' (dentro de try-except não vazio: False) |
| `InnerEye/Common/common_util.py` | `merge_conda_files` | 507–507 | `ast_io_operation` | Operação candidata de I/O 'ruamel.yaml.dump' em 'merge_conda_files' (dentro de try-except não vazio: False) |
| `InnerEye/Common/generic_parsing.py` | `GenericConfig.add_args._get_basic_type.list_or_dict` | 209–209 | `ast_io_operation` | Operação candidata de I/O 'json.loads' em 'GenericConfig.add_args._get_basic_type.list_or_dict' (dentro de try-except não vazio: False) |
| `InnerEye/Common/resource_monitor.py` | `ResourceMonitor.store_to_file` | 229–229 | `ast_io_operation` | Operação candidata de I/O 'self.aggregate_metrics_file.write_text' em 'ResourceMonitor.store_to_file' (dentro de try-except não vazio: False) |
| `InnerEye/Common/resource_monitor.py` | `ResourceMonitor.read_aggregate_metrics` | 238–238 | `ast_io_operation` | Operação candidata de I/O 'pd.read_csv' em 'ResourceMonitor.read_aggregate_metrics' (dentro de try-except não vazio: False) |
| `InnerEye/Common/Statistics/mann_whitney_test.py` | `read_csv_file` | 265–265 | `ast_io_operation` | Operação candidata de I/O 'open' em 'read_csv_file' (dentro de try-except não vazio: False) |
| `InnerEye/Common/Statistics/mann_whitney_test.py` | `compare_scores_across_institutions` | 279–279 | `ast_io_operation` | Operação candidata de I/O 'pd.read_csv' em 'compare_scores_across_institutions' (dentro de try-except não vazio: False) |
| `InnerEye/Common/Statistics/mann_whitney_test.py` | `mann_whitney_on_key` | 140–143 | `ast_empty_or_pass_except` | Bloco try-except em 'mann_whitney_on_key' possui handler vazio ou com instrução 'pass' (exceções: ValueError) |
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
- **Descrição:** Evidência identificada: 3344 sinal(is) estrutural(is) de validação de entrada localizado(s), incluindo 484 função(ões)/chamada(s) de validação e 374 guarda(s) condicional(is) com levantamento de exceção.
- **Justificativa de Rastreabilidade:** Foram identificados mecanismos explícitos de verificação de entrada no código. A presença estrutural não garante suficiência clínica ou completude da validação.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `mypy_runner.py` | `main` | 81–82 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'main' |
| `mypy_runner.py` | `main` | 90–91 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'main' |
| `score.py` | `create_inference_pipeline` | 103–104 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'create_inference_pipeline' |
| `score.py` | `run_inference` | 129–131 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'run_inference' |
| `score.py` | `extract_zipped_files_and_flatten` | 159–164 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'extract_zipped_files_and_flatten' |
| `score.py` | `convert_nifti_to_zipped_dicom_rt` | 234–236 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'convert_nifti_to_zipped_dicom_rt' |
| `score.py` | `check_input_file` | 243–259 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'check_input_file' |
| `score.py` | `check_input_file` | 255–258 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'check_input_file' |
| `score.py` | `score_image` | 282–283 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'score_image' |
| `setup.py` | N/A | 91–93 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em '<module>' |
| `setup.py` | N/A | 100–101 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em '<module>' |
| `setup.py` | N/A | 100–100 | `validation_validation_call` | Sinal de validação (validation_call) em '<module>' |
| `setup.py` | N/A | 102–103 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em '<module>' |
| `InnerEye/Azure/azure_config.py` | `AzureConfig.validate` | 120–122 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'AzureConfig.validate' |
| `InnerEye/Azure/azure_config.py` | `AzureConfig.validate` | 121–122 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'AzureConfig.validate' |
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
- **Descrição:** Evidência parcial: foram identificados 39 sinal(is) de carregamento, salvamento ou referência a checkpoints de modelos (14 arquivo(s) de modelo no repositório). A existência de chamadas de carga ou arquivos .pt/.pth/.onnx não comprova proveniência completa nem controle de versão do modelo.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: artefatos de modelo exigem rastreabilidade documental de versão, dataset de treinamento, hiperparâmetros e verificação de integridade (hash).

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `InnerEye/ML/deep_learning_config.py` | `DeepLearningConfig.load_checkpoint_and_modify` | 883–883 | `model_model_load` | Operação/referência de modelo (model_load) em 'DeepLearningConfig.load_checkpoint_and_modify' |
| `InnerEye/ML/deep_learning_config.py` | `load_checkpoint` | 893–893 | `model_model_load` | Operação/referência de modelo (model_load) em 'load_checkpoint' |
| `InnerEye/ML/run_ml.py` | `MLRunner.run_inference_for_lightning_models` | 438–438 | `model_model_load` | Operação/referência de modelo (model_load) em 'MLRunner.run_inference_for_lightning_models' |
| `InnerEye/ML/run_ml.py` | `MLRunner.run_inference_for_lightning_models` | 439–439 | `model_model_load` | Operação/referência de modelo (model_load) em 'MLRunner.run_inference_for_lightning_models' |
| `InnerEye/ML/SSL/utils.py` | `create_ssl_image_classifier` | 78–78 | `model_model_load` | Operação/referência de modelo (model_load) em 'create_ssl_image_classifier' |
| `InnerEye/ML/SSL/lightning_modules/ssl_online_evaluator.py` | `SSLOnlineEvaluatorInnerEye.on_pretrain_routine_start` | 113–113 | `model_model_load` | Operação/referência de modelo (model_load) em 'SSLOnlineEvaluatorInnerEye.on_pretrain_routine_start' |
| `InnerEye/ML/SSL/lightning_modules/ssl_online_evaluator.py` | `SSLOnlineEvaluatorInnerEye.on_pretrain_routine_start` | 115–115 | `model_model_load` | Operação/referência de modelo (model_load) em 'SSLOnlineEvaluatorInnerEye.on_pretrain_routine_start' |
| `InnerEye/ML/utils/checkpoint_handling.py` | `find_recovery_checkpoint` | 331–331 | `model_model_load` | Operação/referência de modelo (model_load) em 'find_recovery_checkpoint' |
| `InnerEye/ML/utils/lr_scheduler.py` | `SchedulerWithWarmUp.load_state_dict` | 140–140 | `model_model_load` | Operação/referência de modelo (model_load) em 'SchedulerWithWarmUp.load_state_dict' |
| `InnerEye/ML/utils/lr_scheduler.py` | `SchedulerWithWarmUp.load_state_dict` | 141–141 | `model_model_load` | Operação/referência de modelo (model_load) em 'SchedulerWithWarmUp.load_state_dict' |
| `InnerEye/ML/visualizers/activation_maps.py` | `extract_activation_maps` | 89–89 | `model_model_load` | Operação/referência de modelo (model_load) em 'extract_activation_maps' |
| `InnerEye/ML/visualizers/activation_maps.py` | `extract_activation_maps` | 90–90 | `model_model_load` | Operação/referência de modelo (model_load) em 'extract_activation_maps' |
| `Tests/ML/test_model_training.py` | `_test_model_train` | 193–193 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '_test_model_train' |
| `Tests/ML/test_model_training.py` | `test_recover_training_mean_teacher_model` | 351–351 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'test_recover_training_mean_teacher_model' |
| `Tests/ML/utils/test_checkpoint_handling.py` | `create_checkpoint_file` | 35–35 | `model_model_save` | Operação/referência de modelo (model_save) em 'create_checkpoint_file' |
*... e mais 15 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência parcial: sinais estruturais de treinamento e de inferência coexistem no(s) mesmo(s) arquivo(s) (InnerEye/ML/SSL/lightning_modules/byol/byol_module.py, InnerEye/ML/SSL/lightning_modules/simclr_module.py, InnerEye/ML/SSL/lightning_modules/ssl_classifier_module.py, InnerEye/ML/SSL/lightning_modules/ssl_online_evaluator.py, InnerEye/ML/config.py, InnerEye/ML/configs/classification/CovidModel.py, InnerEye/ML/configs/classification/GlaucomaPublic.py, InnerEye/ML/configs/other/HelloContainer.py, InnerEye/ML/configs/unit_testing/passthrough_model.py, InnerEye/ML/deep_learning_config.py, InnerEye/ML/lightning_base.py, InnerEye/ML/lightning_container.py, InnerEye/ML/lightning_models.py, InnerEye/ML/model_config_base.py, InnerEye/ML/run_ml.py, InnerEye/ML/utils/layer_util.py, InnerEye/ML/utils/temperature_scaling.py, Tests/AfterTraining/test_after_training.py, Tests/ML/configs/lightning_test_containers.py, Tests/ML/models/architectures/test_crop_size_multiple.py, Tests/ML/models/losses/test_cross_entropy_loss.py, Tests/ML/pipelines/test_inference.py, Tests/ML/runners/test_runner.py, Tests/ML/utils/test_image_util.py). Indicador técnico que merece investigação quanto à segregação arquitetural entre desenvolvimento/treino e produção/inferência.
- **Justificativa de Rastreabilidade:** Coexistência de sinais de treinamento e inferência em InnerEye/ML/SSL/lightning_modules/byol/byol_module.py, InnerEye/ML/SSL/lightning_modules/simclr_module.py, InnerEye/ML/SSL/lightning_modules/ssl_classifier_module.py, InnerEye/ML/SSL/lightning_modules/ssl_online_evaluator.py, InnerEye/ML/config.py, InnerEye/ML/configs/classification/CovidModel.py, InnerEye/ML/configs/classification/GlaucomaPublic.py, InnerEye/ML/configs/other/HelloContainer.py, InnerEye/ML/configs/unit_testing/passthrough_model.py, InnerEye/ML/deep_learning_config.py, InnerEye/ML/lightning_base.py, InnerEye/ML/lightning_container.py, InnerEye/ML/lightning_models.py, InnerEye/ML/model_config_base.py, InnerEye/ML/run_ml.py, InnerEye/ML/utils/layer_util.py, InnerEye/ML/utils/temperature_scaling.py, Tests/AfterTraining/test_after_training.py, Tests/ML/configs/lightning_test_containers.py, Tests/ML/models/architectures/test_crop_size_multiple.py, Tests/ML/models/losses/test_cross_entropy_loss.py, Tests/ML/pipelines/test_inference.py, Tests/ML/runners/test_runner.py, Tests/ML/utils/test_image_util.py. Requer inspeção humana do fluxo de controle para verificar se o modelo é congelado em produção.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `score.py` | `init_from_model_inference_json` | 62–77 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'init_from_model_inference_json' |
| `score.py` | `create_inference_pipeline` | 80–106 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'create_inference_pipeline' |
| `score.py` | `run_inference` | 114–140 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'run_inference' |
| `InnerEye/ML/config.py` | `SegmentationModelBase.get_model_train_test_dataset_splits` | 703–711 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'SegmentationModelBase.get_model_train_test_dataset_splits' |
| `InnerEye/ML/config.py` | `SegmentationModelBase.validate_inference_stride_size` | 584–599 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'SegmentationModelBase.validate_inference_stride_size' |
| `InnerEye/ML/config.py` | `SegmentationModelBase.inference_stride_size` | 626–632 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'SegmentationModelBase.inference_stride_size' |
| `InnerEye/ML/config.py` | `SegmentationModelBase.inference_stride_size` | 635–642 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'SegmentationModelBase.inference_stride_size' |
| `InnerEye/ML/deep_learning_config.py` | `DeepLearningConfig.get_train_epochs` | 818–823 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'DeepLearningConfig.get_train_epochs' |
| `InnerEye/ML/deep_learning_config.py` | `DeepLearningConfig.get_total_number_of_training_epochs` | 825–830 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'DeepLearningConfig.get_total_number_of_training_epochs' |
| `InnerEye/ML/deep_learning_config.py` | `WorkflowParams.is_inference_required` | 303–352 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'WorkflowParams.is_inference_required' |
| `InnerEye/ML/lightning_base.py` | `TrainAndValDataLightning.train_dataloader` | 74–75 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'TrainAndValDataLightning.train_dataloader' |
| `InnerEye/ML/lightning_base.py` | `InferenceDataLightning.train_dataloader` | 107–108 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'InferenceDataLightning.train_dataloader' |
| `InnerEye/ML/lightning_base.py` | `InnerEyeContainer.before_training_on_global_rank_zero` | 189–198 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'InnerEyeContainer.before_training_on_global_rank_zero' |
| `InnerEye/ML/lightning_base.py` | `InnerEyeLightning.training_epoch_end` | 256–260 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'InnerEyeLightning.training_epoch_end' |
| `InnerEye/ML/lightning_base.py` | `InnerEyeLightning.on_train_end` | 287–292 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'InnerEyeLightning.on_train_end' |
*... e mais 15 evidência(s) registrada(s) em `findings.json`.*

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
1. **TA-002 (R02 — Gerenciamento de dependências e componentes externos (SOUP))** [Evidência não identificada no repositório analisado]: Documentar todas as bibliotecas externas (SOUP) em manifesto versionado (ex.: requirements.txt ou pyproject.toml) e elaborar a lista formal de SOUP conforme IEC 62304 (Seção 8.1.2 e 5.3.3).
1. **TA-005 (R05 — Tratamento de erros e exceções em operações de I/O)** [Evidência parcial — indicador técnico que merece investigação]: Revisar cada operação de leitura/escrita sem tratamento de erro e eliminar blocos except vazios/pass que possam mascarar corrupção de arquivos ou dados clínicos.
1. **TA-007 (R07 — Proveniência, carregamento e versionamento de artefatos de modelos)** [Evidência parcial — indicador técnico que merece investigação]: Documentar formalmente a proveniência de cada modelo carregado (identificador de versão, hash SHA-256 do artefato, dataset de origem, hiperparâmetros e Relatório de Validação de Algoritmo).
1. **TA-008 (R08 — Sinais estruturais de separação entre treinamento e inferência)** [Evidência parcial — indicador técnico que merece investigação]: Revisar a arquitetura dos módulos listados para separar claramente os scripts de treinamento do pipeline de inferência clínica e documentar o controle de implantação (SOP Deployment).

### Prioridade de Revisão Média (`medium`)
1. **TA-004 (R04 — Integração contínua (CI/CD) e automação de verificação)** [Evidência parcial — indicador técnico que merece investigação]: Incluir etapa de execução de testes automatizados e verificação no pipeline de CI/CD.
1. **TA-006 (R06 — Sinais estruturais de validação de entradas)** [Evidência identificada]: Revisão humana necessária para verificar se os critérios de validação cobrem formatos inválidos, valores ausentes, limites fisiológicos/dimensionais e proteção contra entradas malformadas.

### Prioridade de Revisão Baixa (`low`)
1. **TA-003 (R03 — Evidências de testes automatizados no repositório)** [Evidência identificada]: Revisão humana necessária para verificar a rastreabilidade entre os casos de teste automatizados, os requisitos de software e os controles de risco (IEC 62304 Seções 5.5, 5.6 e 5.7).

### Informativo (`informational`)
1. **TA-001 (R01 — Cobertura e integridade da inspeção estática)** [Evidência identificada]: Manter a verificação sintática íntegra no fluxo de desenvolvimento.
