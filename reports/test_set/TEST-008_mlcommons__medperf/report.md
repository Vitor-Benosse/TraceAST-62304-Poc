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

- **Nome do Projeto:** TEST-008_mlcommons__medperf
- **Commit SHA Analisado:** `b73b1f26c841ffbd732df41c08d7be57b9ebe1de`
- **Data e Horário da Execução (UTC):** `2026-11-04T22:15:43.169897+00:00`
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

- **Quantidade total de arquivos encontrados:** 1475
- **Quantidade de arquivos Python (`.py`):** 781
- **Arquivos Python analisados com sucesso:** 781
- **Arquivos Python que falharam na análise:** 0
- **Percentual de cobertura da inspeção sintática:** 100.0%

*Nenhum arquivo Python falhou durante o parsing sintático AST.*

## C. Visão Geral dos Indicadores Técnicos

| Estado do Indicador | Expressão Padronizada | Quantidade |
|---|---|---|
| `observed` | Evidência identificada | 4 |
| `partial` | Evidência parcial — indicador técnico que merece investigação | 4 |
| `not_observed` | Evidência não identificada no repositório analisado | 0 |
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
- **Descrição:** Evidência identificada: todos os 781 arquivos Python encontrados foram analisados com sucesso via AST (cobertura de inspeção: 100.0%).
- **Justificativa de Rastreabilidade:** Inspeção concluída sem falhas de parsing em 781/781 arquivos Python.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `cli/auto_login.py` | `<module>` | 1–69 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: bd9dedd1935e...) |
| `cli/cli_tests_move_storage.py` | `<module>` | 1–26 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 90e78b31beb5...) |
| `cli/setup.py` | `<module>` | 1–34 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 1d292cf7ce90...) |
| `cli/medperf/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 02bc43d06321...) |
| `cli/medperf/__main__.py` | `<module>` | 1–4 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 1b9904548f5e...) |
| `cli/medperf/_version.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: b98ddc300329...) |
| `cli/medperf/certificates.py` | `<module>` | 1–98 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: ec88e92b9796...) |
| `cli/medperf/cli.py` | `<module>` | 1–133 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 12ea2e3a35a5...) |
| `cli/medperf/config.py` | `<module>` | 1–364 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: da141da86dfa...) |
| `cli/medperf/decorators.py` | `<module>` | 1–248 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 20ba961824e9...) |
| `cli/medperf/encryption.py` | `<module>` | 1–113 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 74cab3b2203b...) |
| `cli/medperf/enums.py` | `<module>` | 1–39 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: afb3904beb43...) |
| `cli/medperf/exceptions.py` | `<module>` | 1–66 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: c2f1aeb29953...) |
| `cli/medperf/init.py` | `<module>` | 1–60 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 241af9e43c29...) |
| `cli/medperf/utils.py` | `<module>` | 1–740 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 54bfc77c8c31...) |

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
- **Status:** `partial` (Evidência parcial — indicador técnico que merece investigação)
- **Prioridade de Revisão Técnica:** `medium` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência parcial: manifesto(s) de dependências localizado(s) (cli/requirements.txt, cli/test-requirements.txt, docs/requirements.txt, examples/BraTS/data_prep/project/requirements.txt, examples/BraTS/metrics/project/requirements.txt, examples/BraTS/model_deepmedic/project/requirements.txt, examples/BraTS/model_deepscan/project/requirements.txt, examples/BraTS/model_nnunet/project/requirements.txt, examples/BraTS2023/data_prep/project/requirements.txt, examples/BraTS2023/dummy_model/project/requirements.txt, examples/BraTS2023/synthesis_metrics/project/requirements.txt, examples/BraTS2024/data_prep/project/requirements.txt, examples/BraTS2024/dummy_model/project/requirements.txt, examples/BraTS2024/mock_metrics/requirements.txt, examples/BraTS2024/mock_prep/requirements.txt, examples/cc/base_image/requirements.txt, examples/cc/chestxray/implementation/requirements.txt, examples/cc/mock_benchmark/requirements.txt, examples/cc/rano/implementation/requirements.txt, examples/ChestXRay/chexpert_prep/project/requirements.txt, examples/ChestXRay/chexpert_prep_separate_labels/project/requirements.txt, examples/ChestXRay/metrics/project/requirements.txt, examples/ChestXRay/xrv_densenet/project/requirements.txt, examples/ChestXRay/xrv_resnet/project/requirements.txt, examples/chestxray_tutorial/data_preparator/project/requirements.txt, examples/chestxray_tutorial/metrics/project/requirements.txt, examples/chestxray_tutorial/model_custom_cnn/project/requirements.txt, examples/chestxray_tutorial/model_mobilenetv2/project/requirements.txt, examples/DataPrepManualSteps/data_prep/project/requirements.txt, examples/DFCI/metrics/project/requirements.txt, examples/DFCI/prep/project/requirements.txt, examples/fl/fl/project/requirements.txt, examples/fl/fl_admin/project/requirements.txt, examples/fl/mock_cert/project/requirements.txt, examples/fl/prep/project/requirements.txt, examples/fl_post/fl/project/requirements.txt, examples/flower/fl/project/requirements.txt, examples/flower/fl_admin/project/requirements.txt, examples/SurgMLCube/surg_metrics/project/requirements.txt, examples/SurgMLCube/surg_model_TeCNO/project/requirements.txt, examples/SurgMLCube/surg_prep/project/requirements.txt, examples/tests/metrics/project/requirements.txt, examples/tests/model-bug/project/requirements.txt, examples/tests/model-cpu/project/requirements.txt, examples/tests/prep-sep/project/requirements.txt, scripts/monitor/requirements.txt, scripts/update_container_hashes/requirements.txt, server/requirements.txt, server/test-requirements.txt), contendo 119 pacote(s) com versão fixada e 112 pacote(s) sem versão exata fixada. Imports externos não declarados no manifesto: account_management, admin, aggregator, annotations_loaded, anyio, asset, assets, auth0, auth_provider_token, base_page, batchgenerators, benchmark, benchmarkdataset, benchmarkmodel, ca, certificate, check, coarse2fine_testing, coarse_testing, collaborator, comms, compute, config_management, container_hashes_utils, crypto, cube, data, data_loader, dataset, direct, distutils, docker_runner, docker_utils, encrypted_key, environ, factory, fast_functions, filesystem, filters, flwr, formatters, gcp, gcp_utils, get_data, git, google, googleapiclient, hooks, imp, infer, init_model, interface, invalid_handler, invalid_subject_updated, jwt, keras, keyring, kms, local, medperf, metrics, metrics_GLI, migration_cube, mlcube, model, model_def, models, nnunet, nnunet_data_setup, nnunet_model_setup, nnunet_setup, nnunet_v1, normalized_surface_dice, openfl, params_cases, parser, permissions, plan, preparation_dashboard, prepare, preprocess, prompt_handler, pytest, rano_monitor, report_handler, report_updated, rest, rest_framework, rest_framework_simplejwt, result, routes, runner, runner_pt_chkpt, runner_pt_utils, sanity_check, seed_utils, serializers, setuptools, simple_container, singularity_runner, singularity_utils, skimage, source, sources, src, starlette, stats, stdin, storage, synapse, tarball_reviewed_watchdog, task, testing_utils, token_storage, tomli_w, traindataset_association, training, trainingevent, update_plan, user, utils, validate_params, web_ui, workload_identity. Componentes de IA/ML: Keras, NiBabel, ONNX, PyTorch, SimpleITK, TensorFlow, TorchVision, scikit-learn.
- **Justificativa de Rastreabilidade:** A presença de dependências sem versão fixada ou imports omitidos não representa automaticamente uma não conformidade, mas é um indicador técnico que merece investigação para controle de SOUP.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `cli/requirements.txt` | `typer` | 1–1 | `dependency_declaration` | Pacote 'typer' declarado em 'cli/requirements.txt' (especificador: '~=0.12.0', fixado: False, importado no código: True) |
| `cli/requirements.txt` | `rich` | 2–2 | `dependency_declaration` | Pacote 'rich' declarado em 'cli/requirements.txt' (especificador: '~=13.7.0', fixado: False, importado no código: False) |
| `cli/requirements.txt` | `PyYAML` | 3–3 | `dependency_declaration` | Pacote 'PyYAML' declarado em 'cli/requirements.txt' (especificador: '==6.0.1', fixado: True, importado no código: True) |
| `cli/requirements.txt` | `requests` | 4–4 | `dependency_declaration` | Pacote 'requests' declarado em 'cli/requirements.txt' (especificador: '>=2.26.0', fixado: False, importado no código: True) |
| `cli/requirements.txt` | `pydantic` | 5–5 | `dependency_declaration` | Pacote 'pydantic' declarado em 'cli/requirements.txt' (especificador: '==1.10.13', fixado: True, importado no código: True) |
| `cli/requirements.txt` | `yaspin` | 6–6 | `dependency_declaration` | Pacote 'yaspin' declarado em 'cli/requirements.txt' (especificador: '==2.1.0', fixado: True, importado no código: True) |
| `cli/requirements.txt` | `tabulate` | 7–7 | `dependency_declaration` | Pacote 'tabulate' declarado em 'cli/requirements.txt' (especificador: '==0.9.0', fixado: True, importado no código: True) |
| `cli/requirements.txt` | `pexpect` | 8–8 | `dependency_declaration` | Pacote 'pexpect' declarado em 'cli/requirements.txt' (especificador: '==4.8.0', fixado: True, importado no código: True) |
| `cli/requirements.txt` | `colorama` | 9–9 | `dependency_declaration` | Pacote 'colorama' declarado em 'cli/requirements.txt' (especificador: '==0.4.4', fixado: True, importado no código: True) |
| `cli/requirements.txt` | `time-machine` | 10–10 | `dependency_declaration` | Pacote 'time-machine' declarado em 'cli/requirements.txt' (especificador: '==2.4.0', fixado: True, importado no código: False) |
| `cli/requirements.txt` | `pytest-mock` | 11–11 | `dependency_declaration` | Pacote 'pytest-mock' declarado em 'cli/requirements.txt' (especificador: '==3.14.0', fixado: True, importado no código: False) |
| `cli/requirements.txt` | `pyfakefs` | 12–12 | `dependency_declaration` | Pacote 'pyfakefs' declarado em 'cli/requirements.txt' (especificador: '==5.8.0', fixado: True, importado no código: False) |
| `cli/requirements.txt` | `validators` | 13–13 | `dependency_declaration` | Pacote 'validators' declarado em 'cli/requirements.txt' (especificador: '==0.18.2', fixado: True, importado no código: True) |
| `cli/requirements.txt` | `merge-args` | 14–14 | `dependency_declaration` | Pacote 'merge-args' declarado em 'cli/requirements.txt' (especificador: '==0.1.5', fixado: True, importado no código: True) |
| `cli/requirements.txt` | `synapseclient` | 15–15 | `dependency_declaration` | Pacote 'synapseclient' declarado em 'cli/requirements.txt' (especificador: '==4.1.1', fixado: True, importado no código: True) |
*... e mais 821 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência identificada: 138 arquivo(s) de teste localizado(s) (diretórios: raiz/módulos; frameworks: pytest, unittest; 840 função(ões)/método(s) de teste).
- **Justificativa de Rastreabilidade:** Módulos e funções de teste automatizado foram observados no repositório.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `cli/medperf/commands/compatibility_test/compatibility_test.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'cli/medperf/commands/compatibility_test/compatibility_test.py' identificado (0 funções/métodos candidatos de teste). |
| `cli/medperf/commands/mlcube/run_test.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'cli/medperf/commands/mlcube/run_test.py' identificado (0 funções/métodos candidatos de teste). |
| `cli/medperf/tests/__init__.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'cli/medperf/tests/__init__.py' identificado (0 funções/métodos candidatos de teste). |
| `cli/medperf/tests/conftest.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'cli/medperf/tests/conftest.py' identificado (0 funções/métodos candidatos de teste). |
| `cli/medperf/tests/test_account_management.py` | `MockConfig.__init__` | 11–12 | `test_module` | Módulo de teste 'cli/medperf/tests/test_account_management.py' identificado (4 funções/métodos candidatos de teste). |
| `cli/medperf/tests/test_certificates.py` | `test_verify_certificate_authority_success` | 21–43 | `test_module` | Módulo de teste 'cli/medperf/tests/test_certificates.py' identificado (5 funções/métodos candidatos de teste). |
| `cli/medperf/tests/test_utils.py` | `test_setup_logging_filters_sensitive_data` | 57–69 | `test_module` | Módulo de teste 'cli/medperf/tests/test_utils.py' identificado (21 funções/métodos candidatos de teste). |
| `cli/medperf/tests/utils.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'cli/medperf/tests/utils.py' identificado (0 funções/métodos candidatos de teste). |
| `cli/medperf/tests/commands/__init__.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'cli/medperf/tests/commands/__init__.py' identificado (0 funções/métodos candidatos de teste). |
| `cli/medperf/tests/commands/test_list.py` | `TestEntityList.set_common_attributes` | 45–48 | `test_module` | Módulo de teste 'cli/medperf/tests/commands/test_list.py' identificado (3 funções/métodos candidatos de teste). |
| `cli/medperf/tests/commands/test_profile.py` | `test_activate_updates_active_profile` | 13–19 | `test_module` | Módulo de teste 'cli/medperf/tests/commands/test_profile.py' identificado (6 funções/métodos candidatos de teste). |
| `cli/medperf/tests/commands/test_utils_commands.py` | `DummyConfig.__init__` | 8–12 | `test_module` | Módulo de teste 'cli/medperf/tests/commands/test_utils_commands.py' identificado (6 funções/métodos candidatos de teste). |
| `cli/medperf/tests/commands/test_view.py` | `test_prepare_with_id_given` | 19–31 | `test_module` | Módulo de teste 'cli/medperf/tests/commands/test_view.py' identificado (4 funções/métodos candidatos de teste). |
| `cli/medperf/tests/commands/association/__init__.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'cli/medperf/tests/commands/association/__init__.py' identificado (0 funções/métodos candidatos de teste). |
| `cli/medperf/tests/commands/association/test_approve.py` | `test_run_calls_correct_comms_method` | 26–34 | `test_module` | Módulo de teste 'cli/medperf/tests/commands/association/test_approve.py' identificado (1 funções/métodos candidatos de teste). |
*... e mais 123 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência identificada: 10 configuração(ões) de CI/CD localizada(s) com comandos declarados para execução automatizada de testes (evidências de cobertura: não identificadas).
- **Justificativa de Rastreabilidade:** Arquivos de workflow CI/CD contendo etapas de execução de testes foram encontrados.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `.github/workflows/auth-ci.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/auth-ci.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/cla.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/cla.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/codeql-analysis.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/codeql-analysis.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/docker-ci.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/docker-ci.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/docs-ci.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/docs-ci.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/encrypted-containers-ci.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/encrypted-containers-ci.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/local-ci.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/local-ci.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/train-ci.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/train-ci.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/unittests.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/unittests.yml' (comandos de teste: pip install flake8 pytest, - name: Test with pytest, pytest; cobertura: False) |
| `.github/workflows/webui-ci.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/webui-ci.yml' (comandos de teste: - name: Run webUI tutorial E2E tests with pytest, run: pytest; cobertura: False) |

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
- **Descrição:** Evidência parcial: entre 530 operação(ões) candidatas de I/O, 9 possuem bloco try-except não vazio e 521 não possuem tratamento local observável. Foram identificados 17 bloco(s) except vazios ou com 'pass'.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: coexistem operações de I/O sem captura local de exceção ou blocos except que suprimem falhas com pass.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `cli/cli_tests_move_storage.py` | `update_yaml` | 6–6 | `ast_io_operation` | Operação candidata de I/O 'open' em 'update_yaml' (dentro de try-except não vazio: False) |
| `cli/cli_tests_move_storage.py` | `update_yaml` | 14–14 | `ast_io_operation` | Operação candidata de I/O 'open' em 'update_yaml' (dentro de try-except não vazio: False) |
| `cli/setup.py` | N/A | 4–4 | `ast_io_operation` | Operação candidata de I/O 'open' em '<module>' (dentro de try-except não vazio: False) |
| `cli/medperf/utils.py` | `get_file_hash` | 55–55 | `ast_io_operation` | Operação candidata de I/O 'open' em 'get_file_hash' (dentro de try-except não vazio: False) |
| `cli/medperf/utils.py` | `tar` | 191–191 | `ast_io_operation` | Operação candidata de I/O 'tarfile.open' em 'tar' (dentro de try-except não vazio: False) |
| `cli/medperf/utils.py` | `untar` | 216–216 | `ast_io_operation` | Operação candidata de I/O 'tarfile.open' em 'untar' (dentro de try-except não vazio: True) |
| `cli/medperf/utils.py` | `make_pretty_dict` | 271–271 | `ast_io_operation` | Operação candidata de I/O 'yaml.dump' em 'make_pretty_dict' (dentro de try-except não vazio: False) |
| `cli/medperf/utils.py` | `sanitize_json` | 423–423 | `ast_io_operation` | Operação candidata de I/O 'json.dumps' em 'sanitize_json' (dentro de try-except não vazio: False) |
| `cli/medperf/utils.py` | `sanitize_json` | 426–426 | `ast_io_operation` | Operação candidata de I/O 'json.loads' em 'sanitize_json' (dentro de try-except não vazio: False) |
| `cli/medperf/utils.py` | `run_command` | 603–603 | `ast_io_operation` | Operação candidata de I/O 'open' em 'run_command' (dentro de try-except não vazio: False) |
| `cli/medperf/utils.py` | `get_webui_properties` | 662–662 | `ast_io_operation` | Operação candidata de I/O 'open' em 'get_webui_properties' (dentro de try-except não vazio: False) |
| `cli/medperf/utils.py` | `secure_write_to_file` | 719–719 | `ast_io_operation` | Operação candidata de I/O 'open' em 'secure_write_to_file' (dentro de try-except não vazio: False) |
| `cli/medperf/utils.py` | `secure_write_to_file` | 722–722 | `ast_io_operation` | Operação candidata de I/O 'open' em 'secure_write_to_file' (dentro de try-except não vazio: False) |
| `cli/medperf/account_management/token_storage/filesystem.py` | `FilesystemTokenStore.read_tokens` | 38–38 | `ast_io_operation` | Operação candidata de I/O 'open' em 'FilesystemTokenStore.read_tokens' (dentro de try-except não vazio: False) |
| `cli/medperf/account_management/token_storage/filesystem.py` | `FilesystemTokenStore.read_tokens` | 40–40 | `ast_io_operation` | Operação candidata de I/O 'open' em 'FilesystemTokenStore.read_tokens' (dentro de try-except não vazio: False) |
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
- **Descrição:** Evidência identificada: 1436 sinal(is) estrutural(is) de validação de entrada localizado(s), incluindo 374 função(ões)/chamada(s) de validação e 409 guarda(s) condicional(is) com levantamento de exceção.
- **Justificativa de Rastreabilidade:** Foram identificados mecanismos explícitos de verificação de entrada no código. A presença estrutural não garante suficiência clínica ou completude da validação.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `cli/medperf/certificates.py` | `verify_certificate_authority` | 49–70 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'verify_certificate_authority' |
| `cli/medperf/certificates.py` | `verify_certificate_authority` | 53–57 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'verify_certificate_authority' |
| `cli/medperf/certificates.py` | `verify_certificate` | 73–93 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'verify_certificate' |
| `cli/medperf/certificates.py` | `verify_certificate_authority_by_id` | 96–98 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'verify_certificate_authority_by_id' |
| `cli/medperf/cli.py` | `version_callback` | 105–107 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'version_callback' |
| `cli/medperf/config.py` | N/A | 59–63 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em '<module>' |
| `cli/medperf/decorators.py` | `clean_except` | 13–45 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'clean_except' |
| `cli/medperf/encryption.py` | `SymmetricEncryption.check` | 21–28 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'SymmetricEncryption.check' |
| `cli/medperf/encryption.py` | `SymmetricEncryption.decrypt_file` | 37–40 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'SymmetricEncryption.decrypt_file' |
| `cli/medperf/encryption.py` | `SymmetricEncryption.encrypt_file` | 64–67 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'SymmetricEncryption.encrypt_file' |
| `cli/medperf/init.py` | `initialize` | 44–47 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'initialize' |
| `cli/medperf/init.py` | `initialize` | 44–44 | `validation_validation_call` | Sinal de validação (validation_call) em 'initialize' |
| `cli/medperf/utils.py` | `cleanup` | 106–122 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'cleanup' |
| `cli/medperf/utils.py` | `tar` | 187–188 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'tar' |
| `cli/medperf/utils.py` | `_MLCubeOutputFilter.check_line` | 297–316 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em '_MLCubeOutputFilter.check_line' |
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
- **Descrição:** Evidência parcial: foram identificados 44 sinal(is) de carregamento, salvamento ou referência a checkpoints de modelos (3 arquivo(s) de modelo no repositório). A existência de chamadas de carga ou arquivos .pt/.pth/.onnx não comprova proveniência completa nem controle de versão do modelo.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: artefatos de modelo exigem rastreabilidade documental de versão, dataset de treinamento, hiperparâmetros e verificação de integridade (hash).

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `examples/ChestXRay/xrv_densenet/project/models.py` | `DenseNet.__init__` | 194–194 | `model_model_load` | Operação/referência de modelo (model_load) em 'DenseNet.__init__' |
| `examples/ChestXRay/xrv_densenet/project/models.py` | `DenseNet.__init__` | 200–200 | `model_model_load` | Operação/referência de modelo (model_load) em 'DenseNet.__init__' |
| `examples/ChestXRay/xrv_resnet/project/models.py` | `ResNet.__init__` | 55–55 | `model_model_load` | Operação/referência de modelo (model_load) em 'ResNet.__init__' |
| `examples/ChestXRay/xrv_resnet/project/models.py` | `ResNet.__init__` | 55–55 | `model_model_load` | Operação/referência de modelo (model_load) em 'ResNet.__init__' |
| `examples/DFCI/model/project/coarse2fine_testing.py` | `coarse2fine_testing` | 22–22 | `model_model_load` | Operação/referência de modelo (model_load) em 'coarse2fine_testing' |
| `examples/DFCI/model/project/coarse2fine_testing.py` | `coarse2fine_testing` | 22–22 | `model_model_load` | Operação/referência de modelo (model_load) em 'coarse2fine_testing' |
| `examples/DFCI/model/project/coarse2fine_testing.py` | `coarse2fine_testing` | 25–27 | `model_model_load` | Operação/referência de modelo (model_load) em 'coarse2fine_testing' |
| `examples/DFCI/model/project/coarse2fine_testing.py` | `coarse2fine_testing` | 26–26 | `model_model_load` | Operação/referência de modelo (model_load) em 'coarse2fine_testing' |
| `examples/DFCI/model/project/coarse_testing.py` | `coarse_testing` | 25–25 | `model_model_load` | Operação/referência de modelo (model_load) em 'coarse_testing' |
| `examples/DFCI/model/project/coarse_testing.py` | `coarse_testing` | 25–25 | `model_model_load` | Operação/referência de modelo (model_load) em 'coarse_testing' |
| `examples/DFCI/model/project/coarse_testing.py` | `coarse_testing` | 28–28 | `model_model_load` | Operação/referência de modelo (model_load) em 'coarse_testing' |
| `examples/DFCI/model/project/coarse_testing.py` | `coarse_testing` | 28–28 | `model_model_load` | Operação/referência de modelo (model_load) em 'coarse_testing' |
| `examples/DFCI/model/project/infer.py` | `run_inference` | 15–15 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'run_inference' |
| `examples/cc/chestxray/implementation/benchmark/entrypoint.py` | N/A | 55–55 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `examples/cc/chestxray/implementation/benchmark/entrypoint.py` | N/A | 63–63 | `model_model_load` | Operação/referência de modelo (model_load) em '<module>' |
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
- **Descrição:** Evidência parcial: sinais estruturais de treinamento e de inferência coexistem no(s) mesmo(s) arquivo(s) (examples/flower/fl/project/src/task.py). Indicador técnico que merece investigação quanto à segregação arquitetural entre desenvolvimento/treino e produção/inferência.
- **Justificativa de Rastreabilidade:** Coexistência de sinais de treinamento e inferência em examples/flower/fl/project/src/task.py. Requer inspeção humana do fluxo de controle para verificar se o modelo é congelado em produção.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `cli/medperf/commands/dataset/dataset.py` | `train` | 186–215 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'train' |
| `cli/medperf/commands/dataset/prepare.py` | `DataPreparation.__generate_report_dict` | 289–307 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'DataPreparation.__generate_report_dict' |
| `cli/medperf/commands/dataset/train.py` | `TrainingExecution.prepare_training_cube` | 143–144 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'TrainingExecution.prepare_training_cube' |
| `cli/medperf/commands/execution/confidential_model_container_execution.py` | `ConfidentialModelContainerExecution.download_predictions` | 194–203 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'ConfidentialModelContainerExecution.download_predictions' |
| `cli/medperf/commands/execution/container_execution.py` | `ContainerExecution.__setup_predictions_path` | 77–92 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'ContainerExecution.__setup_predictions_path' |
| `cli/medperf/commands/execution/container_execution.py` | `ContainerExecution.run_inference` | 108–138 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'ContainerExecution.run_inference' |
| `cli/medperf/comms/rest.py` | `REST.get_training_exp` | 260–271 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'REST.get_training_exp' |
| `cli/medperf/comms/rest.py` | `REST.get_training_event` | 309–320 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'REST.get_training_event' |
| `cli/medperf/comms/rest.py` | `REST.get_training_exps` | 442–450 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'REST.get_training_exps' |
| `cli/medperf/comms/rest.py` | `REST.get_aggregator_training_experiments` | 462–475 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'REST.get_aggregator_training_experiments' |
| `cli/medperf/comms/rest.py` | `REST.get_training_events` | 487–495 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'REST.get_training_events' |
| `cli/medperf/comms/rest.py` | `REST.get_user_training_exps` | 578–586 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'REST.get_user_training_exps' |
| `cli/medperf/comms/rest.py` | `REST.get_user_training_events` | 643–651 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'REST.get_user_training_events' |
| `cli/medperf/comms/rest.py` | `REST.get_user_training_datasets_associations` | 674–682 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'REST.get_user_training_datasets_associations' |
| `cli/medperf/comms/rest.py` | `REST.upload_training_exp` | 749–760 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'REST.upload_training_exp' |
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
1. **TA-005 (R05 — Tratamento de erros e exceções em operações de I/O)** [Evidência parcial — indicador técnico que merece investigação]: Revisar cada operação de leitura/escrita sem tratamento de erro e eliminar blocos except vazios/pass que possam mascarar corrupção de arquivos ou dados clínicos.
1. **TA-007 (R07 — Proveniência, carregamento e versionamento de artefatos de modelos)** [Evidência parcial — indicador técnico que merece investigação]: Documentar formalmente a proveniência de cada modelo carregado (identificador de versão, hash SHA-256 do artefato, dataset de origem, hiperparâmetros e Relatório de Validação de Algoritmo).
1. **TA-008 (R08 — Sinais estruturais de separação entre treinamento e inferência)** [Evidência parcial — indicador técnico que merece investigação]: Revisar a arquitetura dos módulos listados para separar claramente os scripts de treinamento do pipeline de inferência clínica e documentar o controle de implantação (SOP Deployment).

### Prioridade de Revisão Média (`medium`)
1. **TA-002 (R02 — Gerenciamento de dependências e componentes externos (SOUP))** [Evidência parcial — indicador técnico que merece investigação]: Avaliar o congelamento de versões (pinning/lockfile), reconciliar bibliotecas importadas no código com o manifesto e manter a matriz de rastreabilidade de SOUP atualizada.
1. **TA-006 (R06 — Sinais estruturais de validação de entradas)** [Evidência identificada]: Revisão humana necessária para verificar se os critérios de validação cobrem formatos inválidos, valores ausentes, limites fisiológicos/dimensionais e proteção contra entradas malformadas.

### Prioridade de Revisão Baixa (`low`)
1. **TA-003 (R03 — Evidências de testes automatizados no repositório)** [Evidência identificada]: Revisão humana necessária para verificar a rastreabilidade entre os casos de teste automatizados, os requisitos de software e os controles de risco (IEC 62304 Seções 5.5, 5.6 e 5.7).
1. **TA-004 (R04 — Integração contínua (CI/CD) e automação de verificação)** [Evidência identificada]: Verificar se os registros de execução do CI/CD são arquivados como evidência de verificação e regressão a cada versão liberada (IEC 62304 Seção 5.6.6 e 5.8).

### Informativo (`informational`)
1. **TA-001 (R01 — Cobertura e integridade da inspeção estática)** [Evidência identificada]: Manter a verificação sintática íntegra no fluxo de desenvolvimento.
