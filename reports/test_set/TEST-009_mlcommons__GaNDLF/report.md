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

- **Nome do Projeto:** TEST-009_mlcommons__GaNDLF
- **Commit SHA Analisado:** `3f9b7726925be0f97a8a0eb108c8f35b19ff50dd`
- **Data e Horário da Execução (UTC):** `2026-11-04T22:15:51.714623+00:00`
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

- **Quantidade total de arquivos encontrados:** 345
- **Quantidade de arquivos Python (`.py`):** 212
- **Arquivos Python analisados com sucesso:** 212
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
- **Descrição:** Evidência identificada: todos os 212 arquivos Python encontrados foram analisados com sucesso via AST (cobertura de inspeção: 100.0%).
- **Justificativa de Rastreabilidade:** Inspeção concluída sem falhas de parsing em 212/212 arquivos Python.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `setup.py` | `<module>` | 1–150 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e2575689d84f...) |
| `update_version.py` | `<module>` | 1–83 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: b12396a69318...) |
| `GANDLF/__init__.py` | `<module>` | 1–5 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: ee825c82c89d...) |
| `GANDLF/config_manager.py` | `<module>` | 1–75 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: b342a7bcfa1d...) |
| `GANDLF/inference_manager.py` | `<module>` | 1–155 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: ff82dba6940d...) |
| `GANDLF/logger.py` | `<module>` | 1–84 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 005ef94dda1b...) |
| `GANDLF/parseConfig.py` | `<module>` | 1–21 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: c3e5afc79287...) |
| `GANDLF/training_manager.py` | `<module>` | 1–298 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 2eb1baf58b89...) |
| `GANDLF/version.py` | `<module>` | 1–5 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: af961471e6d3...) |
| `GANDLF/anonymize/__init__.py` | `<module>` | 1–53 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 4ef10f29fb2b...) |
| `GANDLF/anonymize/convert_to_nifti.py` | `<module>` | 1–40 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 2809a00b4af4...) |
| `GANDLF/cli/__init__.py` | `<module>` | 1–18 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: d110de9c518a...) |
| `GANDLF/cli/config_generator.py` | `<module>` | 1–125 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 5fa903fb974a...) |
| `GANDLF/cli/data_split_saver.py` | `<module>` | 1–49 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 85c828008f9f...) |

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
- **Descrição:** Evidência parcial: manifesto(s) de dependências localizado(s) (docs/requirements.txt, pyproject.toml), contendo 9 pacote(s) com versão fixada e 0 pacote(s) sem versão exata fixada. Imports externos não declarados no manifesto: ImagesFromDataFrame, MSDNet, PIL, SimpleITK, acsconv, ademamix, adopt, augmentation, base, blur_enhanced, brain_age, click, config_generator, config_manager, config_parsing, convert_to_nifti, crop_zero_planes, cv2, data_split_saver, data_splitter, deep_unet, densenet, deploy, deprecated, dicomanonymizer, docker, dynunet_wrapper, efficientnet, entrypoints, fcn, forward_pass, gandlf_logging, gdown, generate_metrics, generic, handle_collisions, hed_augs, histogram_matching, huggingface_hub, hybrid, imagenet_unet, imagenet_vgg, imaging, light_unet, light_unet_multilayer, lightning, lion, lion_pytorch, loss_and_metric, loss_interface, main_run, matplotlib, medcam, modelBase, model_handling, modelio, monai, morphology, nibabel, noise_enhanced, non_zero_normalize, normalize_rgb, numpy, opacus, openslide, openvino, packaging, pandas, panoptica, parameter_processing, patch, patch_extraction, pip, post_training_model_optimization, preprocess_and_save, preprocessing, psutil, pydantic, pydantic_core, pydicom, pytest, recover_config, regression, regression_new, resample_minimum, resnet, rgb_augs, rgb_conversion, rotations, scipy, sdnet, seaborn, segmentation, segmentation_models_pytorch, segmentation_new, segmentation_panoptica, setuptools, skimage, sklearn, stain_extractors, stain_normalizer, step, subcommands, synthesis, template_matching, tensor, test_full, thirdparty, threshold_and_clip, torch, torchinfo, torchio, torchmetrics, torchvision, tqdm, training_utils, transunet, typing_extensions, uinc, unet, unet_multilayer, unetr, utils, version, vgg, wrap_monai, wrap_torch, wrap_torchio, write_parse, yaml, zarr. Componentes de IA/ML: MONAI (Medical Open Network for AI), NiBabel, OpenCV, PyDICOM, PyTorch, SimpleITK, TorchVision, scikit-learn.
- **Justificativa de Rastreabilidade:** A presença de dependências sem versão fixada ou imports omitidos não representa automaticamente uma não conformidade, mas é um indicador técnico que merece investigação para controle de SOUP.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `docs/requirements.txt` | `mkdocs` | 1–1 | `dependency_declaration` | Pacote 'mkdocs' declarado em 'docs/requirements.txt' (especificador: '==1.4.1', fixado: True, importado no código: False) |
| `docs/requirements.txt` | `mkdocs-autorefs` | 2–2 | `dependency_declaration` | Pacote 'mkdocs-autorefs' declarado em 'docs/requirements.txt' (especificador: '==0.4.1', fixado: True, importado no código: False) |
| `docs/requirements.txt` | `mkdocs-gen-files` | 3–3 | `dependency_declaration` | Pacote 'mkdocs-gen-files' declarado em 'docs/requirements.txt' (especificador: '==0.4.0', fixado: True, importado no código: False) |
| `docs/requirements.txt` | `mkdocs-literate-nav` | 4–4 | `dependency_declaration` | Pacote 'mkdocs-literate-nav' declarado em 'docs/requirements.txt' (especificador: '==0.5.0', fixado: True, importado no código: False) |
| `docs/requirements.txt` | `mkdocs-material` | 5–5 | `dependency_declaration` | Pacote 'mkdocs-material' declarado em 'docs/requirements.txt' (especificador: '==8.5.7', fixado: True, importado no código: False) |
| `docs/requirements.txt` | `mkdocs-material-extensions` | 6–6 | `dependency_declaration` | Pacote 'mkdocs-material-extensions' declarado em 'docs/requirements.txt' (especificador: '==1.1', fixado: True, importado no código: False) |
| `docs/requirements.txt` | `mkdocstrings` | 7–7 | `dependency_declaration` | Pacote 'mkdocstrings' declarado em 'docs/requirements.txt' (especificador: '==0.19.0', fixado: True, importado no código: False) |
| `docs/requirements.txt` | `mkdocstrings-python` | 8–8 | `dependency_declaration` | Pacote 'mkdocstrings-python' declarado em 'docs/requirements.txt' (especificador: '==0.7.1', fixado: True, importado no código: False) |
| `docs/requirements.txt` | `mkdocs-macros-plugin` | 9–9 | `dependency_declaration` | Pacote 'mkdocs-macros-plugin' declarado em 'docs/requirements.txt' (especificador: '==0.7.0', fixado: True, importado no código: False) |
| `setup.py` | `setuptools` | 1–1 | `undeclared_import` | Módulo externo 'setuptools' importado em 'setup.py', mas não localizado nos manifestos de dependências inspecionados. |
| `GANDLF/__init__.py` | `version` | 1–1 | `undeclared_import` | Módulo externo 'version' importado em 'GANDLF/__init__.py', mas não localizado nos manifestos de dependências inspecionados. |
| `GANDLF/config_manager.py` | `panoptica` | 1–1 | `undeclared_import` | Módulo externo 'panoptica' importado em 'GANDLF/config_manager.py', mas não localizado nos manifestos de dependências inspecionados. |
| `GANDLF/config_manager.py` | `pydantic` | 1–1 | `undeclared_import` | Módulo externo 'pydantic' importado em 'GANDLF/config_manager.py', mas não localizado nos manifestos de dependências inspecionados. |
| `GANDLF/config_manager.py` | `yaml` | 1–1 | `undeclared_import` | Módulo externo 'yaml' importado em 'GANDLF/config_manager.py', mas não localizado nos manifestos de dependências inspecionados. |
| `GANDLF/inference_manager.py` | `lightning` | 1–1 | `undeclared_import` | Módulo externo 'lightning' importado em 'GANDLF/inference_manager.py', mas não localizado nos manifestos de dependências inspecionados. |
*... e mais 496 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência identificada: 20 arquivo(s) de teste localizado(s) (diretórios: raiz/módulos; frameworks: pytest; 101 função(ões)/método(s) de teste).
- **Justificativa de Rastreabilidade:** Módulos e funções de teste automatizado foram observados no repositório.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `testing/test_full.py` | `test_prepare_data_for_ci` | 227–231 | `test_module` | Módulo de teste 'testing/test_full.py' identificado (63 funções/métodos candidatos de teste). |
| `testing/test_lightning_components.py` | `TrainerTestsContextManager._clear_output_dir` | 60–63 | `test_module` | Módulo de teste 'testing/test_lightning_components.py' identificado (20 funções/métodos candidatos de teste). |
| `testing/test_update_version.py` | `test_case` | 42–51 | `test_module` | Módulo de teste 'testing/test_update_version.py' identificado (1 funções/métodos candidatos de teste). |
| `testing/entrypoints/test_anonymizer.py` | `test_case` | 115–124 | `test_module` | Módulo de teste 'testing/entrypoints/test_anonymizer.py' identificado (1 funções/métodos candidatos de teste). |
| `testing/entrypoints/test_cli_tool.py` | `test_version_command` | 6–10 | `test_module` | Módulo de teste 'testing/entrypoints/test_cli_tool.py' identificado (1 funções/métodos candidatos de teste). |
| `testing/entrypoints/test_collect_stats.py` | `test_case` | 108–117 | `test_module` | Módulo de teste 'testing/entrypoints/test_collect_stats.py' identificado (1 funções/métodos candidatos de teste). |
| `testing/entrypoints/test_config_generator.py` | `test_case` | 71–80 | `test_module` | Módulo de teste 'testing/entrypoints/test_config_generator.py' identificado (1 funções/métodos candidatos de teste). |
| `testing/entrypoints/test_construct_csv.py` | `test_case` | 172–181 | `test_module` | Módulo de teste 'testing/entrypoints/test_construct_csv.py' identificado (1 funções/métodos candidatos de teste). |
| `testing/entrypoints/test_debug_info.py` | `test_case` | 34–43 | `test_module` | Módulo de teste 'testing/entrypoints/test_debug_info.py' identificado (1 funções/métodos candidatos de teste). |
| `testing/entrypoints/test_deploy.py` | `test_case` | 324–334 | `test_module` | Módulo de teste 'testing/entrypoints/test_deploy.py' identificado (1 funções/métodos candidatos de teste). |
| `testing/entrypoints/test_entrypoints_existence.py` | `test_command_execution` | 33–46 | `test_module` | Módulo de teste 'testing/entrypoints/test_entrypoints_existence.py' identificado (1 funções/métodos candidatos de teste). |
| `testing/entrypoints/test_generate_metrics.py` | `test_case` | 107–116 | `test_module` | Módulo de teste 'testing/entrypoints/test_generate_metrics.py' identificado (1 funções/métodos candidatos de teste). |
| `testing/entrypoints/test_hf_cli.py` | `test_case` | 109–122 | `test_module` | Módulo de teste 'testing/entrypoints/test_hf_cli.py' identificado (1 funções/métodos candidatos de teste). |
| `testing/entrypoints/test_optimize_model.py` | `test_case` | 100–109 | `test_module` | Módulo de teste 'testing/entrypoints/test_optimize_model.py' identificado (1 funções/métodos candidatos de teste). |
| `testing/entrypoints/test_patch_miner.py` | `test_case` | 101–110 | `test_module` | Módulo de teste 'testing/entrypoints/test_patch_miner.py' identificado (1 funções/métodos candidatos de teste). |
*... e mais 5 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência identificada: 16 configuração(ões) de CI/CD localizada(s) com comandos declarados para execução automatizada de testes (evidências de cobertura: .github/workflows/devcontainer.yml:68, .github/workflows/openfl-test.yml:30, .github/workflows/python-test.yml:45, .github/workflows/python-test.yml:48, .github/workflows/python-test.yml:51, .github/workflows/python-test.yml:54, .github/workflows/python-test.yml:57, .github/workflows/python-test.yml:60, .github/workflows/python-test.yml:63, .github/workflows/python-test.yml:66, .github/workflows/python-test.yml:69, .github/workflows/python-test.yml:195, .github/workflows/python-test.yml:199, .github/workflows/python-test.yml:203, .github/workflows/python-test.yml:207, .github/workflows/python-test.yml:211, .github/workflows/python-test.yml:215, .github/workflows/python-test.yml:219, .github/workflows/python-test.yml:223).
- **Justificativa de Rastreabilidade:** Arquivos de workflow CI/CD contendo etapas de execução de testes foram encontrados.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `.github/workflows/black.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/black.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/check_pull_request_title.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/check_pull_request_title.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/cla.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/cla.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/codacy.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/codacy.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/codeql-analysis.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/codeql-analysis.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/devcontainer.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/devcontainer.yml' (comandos de teste: runCmd: pytest --cov=. --cov-report=xml -k "generic and not docker"; cobertura: True) |
| `.github/workflows/docker-image.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/docker-image.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/docs-ci.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/docs-ci.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/main.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/main.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/openfl-test.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/openfl-test.yml' (comandos de teste: pytest --cov=. --cov-report=xml -k "prepare_data_for_ci"; cobertura: True) |
| `.github/workflows/ossar-analysis.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/ossar-analysis.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/publish-nightly.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/publish-nightly.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/python-install-check.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/python-install-check.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/python-test.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/python-test.yml' (comandos de teste: pytest --cov=. --cov-report=xml:coverage-generic.xml -k "generic" --cov-context=test | tee pytest-generic.log, pytest --cov=. --cov-report=xml:coverage-classification-histology.xml -k "classification and histology" --cov-context=test | tee pytest-classification-histology.log, pytest --cov=. --cov-report=xml:coverage-classification-standard.xml -k "classification and not histology" --cov-context=test | tee pytest-classification-standard.log, pytest --cov=. --cov-report=xml:coverage-segmentation-2d.xml -k "segmentation and 2d and not transunet" --cov-context=test | tee pytest-segmentation-2d.log, pytest --cov=. --cov-report=xml:coverage-segmentation-3d.xml -k "segmentation and 3d and not transunet" --cov-context=test | tee pytest-segmentation-3d.log, pytest --cov=. --cov-report=xml:coverage-regression.xml -k "regression" --cov-context=test | tee pytest-regression.log, pytest --cov=. --cov-report=xml:coverage-transunet.xml -k "transunet" --cov-context=test | tee pytest-transunet.log, pytest --cov=. --cov-report=xml:coverage-entrypoints.xml -k "entrypoints" --cov-context=test | tee pytest-entrypoints.log, pytest --cov=. --cov-report=xml:coverage-update_version.xml -k "update_version" --cov-context=test | tee pytest-update_version.log, flags: unittests, pytest --cov=. --cov-report=xml -k "generic", pytest --cov=. --cov-report=xml --cov-append -k "classification and histology", pytest --cov=. --cov-report=xml --cov-append -k "classification and not histology", pytest --cov=. --cov-report=xml --cov-append -k "segmentation and not transunet", pytest --cov=. --cov-report=xml --cov-append -k "regression", pytest --cov=. --cov-report=xml --cov-append -k "transunet", pytest --cov=. --cov-report=xml --cov-append -k "entrypoints", pytest --cov=. --cov-report=xml --cov-append -k "update_version", flags: unittests; cobertura: True) |
| `.github/workflows/spellchecker.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/spellchecker.yml' (comandos de teste: nenhum detectado; cobertura: False) |
*... e mais 1 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência parcial: entre 154 operação(ões) candidatas de I/O, 11 possuem bloco try-except não vazio e 143 não possuem tratamento local observável. Foram identificados 0 bloco(s) except vazios ou com 'pass'.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: coexistem operações de I/O sem captura local de exceção ou blocos except que suprimem falhas com pass.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `setup.py` | N/A | 11–11 | `ast_io_operation` | Operação candidata de I/O 'open' em '<module>' (dentro de try-except não vazio: True) |
| `setup.py` | N/A | 19–19 | `ast_io_operation` | Operação candidata de I/O 'open' em '<module>' (dentro de try-except não vazio: True) |
| `GANDLF/config_manager.py` | `_parseConfig` | 27–27 | `ast_io_operation` | Operação candidata de I/O 'open' em '_parseConfig' (dentro de try-except não vazio: True) |
| `GANDLF/inference_manager.py` | `InferenceManager` | 155–155 | `ast_io_operation` | Operação candidata de I/O 'averaged_probs_df.to_csv' em 'InferenceManager' (dentro de try-except não vazio: False) |
| `GANDLF/logger.py` | `Logger.__init__` | 43–43 | `ast_io_operation` | Operação candidata de I/O 'open' em 'Logger.__init__' (dentro de try-except não vazio: False) |
| `GANDLF/logger.py` | `Logger.__init__` | 52–52 | `ast_io_operation` | Operação candidata de I/O 'open' em 'Logger.__init__' (dentro de try-except não vazio: False) |
| `GANDLF/logger.py` | `Logger.write` | 81–81 | `ast_io_operation` | Operação candidata de I/O 'open' em 'Logger.write' (dentro de try-except não vazio: False) |
| `GANDLF/training_manager.py` | `TrainingManager` | 52–52 | `ast_io_operation` | Operação candidata de I/O 'open' em 'TrainingManager' (dentro de try-except não vazio: False) |
| `GANDLF/training_manager.py` | `TrainingManager` | 53–53 | `ast_io_operation` | Operação candidata de I/O 'pickle.dump' em 'TrainingManager' (dentro de try-except não vazio: False) |
| `GANDLF/training_manager.py` | `TrainingManager` | 61–61 | `ast_io_operation` | Operação candidata de I/O 'pickle.load' em 'TrainingManager' (dentro de try-except não vazio: False) |
| `GANDLF/training_manager.py` | `TrainingManager` | 61–61 | `ast_io_operation` | Operação candidata de I/O 'open' em 'TrainingManager' (dentro de try-except não vazio: False) |
| `GANDLF/training_manager.py` | `TrainingManager` | 108–108 | `ast_io_operation` | Operação candidata de I/O 'data.to_csv' em 'TrainingManager' (dentro de try-except não vazio: False) |
| `GANDLF/training_manager.py` | `TrainingManager_split` | 216–216 | `ast_io_operation` | Operação candidata de I/O 'open' em 'TrainingManager_split' (dentro de try-except não vazio: False) |
| `GANDLF/training_manager.py` | `TrainingManager_split` | 217–217 | `ast_io_operation` | Operação candidata de I/O 'pickle.dump' em 'TrainingManager_split' (dentro de try-except não vazio: False) |
| `GANDLF/training_manager.py` | `TrainingManager_split` | 225–225 | `ast_io_operation` | Operação candidata de I/O 'pickle.load' em 'TrainingManager_split' (dentro de try-except não vazio: False) |
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
- **Descrição:** Evidência identificada: 809 sinal(is) estrutural(is) de validação de entrada localizado(s), incluindo 205 função(ões)/chamada(s) de validação e 33 guarda(s) condicional(is) com levantamento de exceção.
- **Justificativa de Rastreabilidade:** Foram identificados mecanismos explícitos de verificação de entrada no código. A presença estrutural não garante suficiência clínica ou completude da validação.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `GANDLF/config_manager.py` | `_parseConfig` | 26–27 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em '_parseConfig' |
| `GANDLF/config_manager.py` | `_parseConfig` | 26–26 | `validation_validation_call` | Sinal de validação (validation_call) em '_parseConfig' |
| `GANDLF/config_manager.py` | `ConfigManager` | 64–71 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'ConfigManager' |
| `GANDLF/config_manager.py` | `ConfigManager` | 64–64 | `validation_validation_call` | Sinal de validação (validation_call) em 'ConfigManager' |
| `GANDLF/config_manager.py` | `ConfigManager` | 69–71 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'ConfigManager' |
| `GANDLF/inference_manager.py` | `InferenceManager` | 29–34 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'InferenceManager' |
| `GANDLF/inference_manager.py` | `InferenceManager` | 50–52 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'InferenceManager' |
| `GANDLF/inference_manager.py` | `InferenceManager` | 56–58 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'InferenceManager' |
| `GANDLF/inference_manager.py` | `InferenceManager` | 71–73 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'InferenceManager' |
| `GANDLF/inference_manager.py` | `InferenceManager` | 130–131 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'InferenceManager' |
| `GANDLF/logger.py` | `Logger.__init__` | 45–49 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'Logger.__init__' |
| `GANDLF/training_manager.py` | `TrainingManager` | 101–111 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'TrainingManager' |
| `GANDLF/training_manager.py` | `TrainingManager` | 122–124 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'TrainingManager' |
| `GANDLF/training_manager.py` | `TrainingManager` | 128–130 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'TrainingManager' |
| `GANDLF/training_manager.py` | `TrainingManager` | 143–145 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'TrainingManager' |
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
- **Descrição:** Evidência parcial: foram identificados 37 sinal(is) de carregamento, salvamento ou referência a checkpoints de modelos (0 arquivo(s) de modelo no repositório). A existência de chamadas de carga ou arquivos .pt/.pth/.onnx não comprova proveniência completa nem controle de versão do modelo.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: artefatos de modelo exigem rastreabilidade documental de versão, dataset de treinamento, hiperparâmetros e verificação de integridade (hash).

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `GANDLF/training_manager.py` | `TrainingManager` | 50–50 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'TrainingManager' |
| `GANDLF/training_manager.py` | `TrainingManager` | 53–53 | `model_model_save` | Operação/referência de modelo (model_save) em 'TrainingManager' |
| `GANDLF/training_manager.py` | `TrainingManager` | 61–61 | `model_model_load` | Operação/referência de modelo (model_load) em 'TrainingManager' |
| `GANDLF/training_manager.py` | `TrainingManager` | 108–108 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'TrainingManager' |
| `GANDLF/training_manager.py` | `TrainingManager_split` | 212–212 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'TrainingManager_split' |
| `GANDLF/training_manager.py` | `TrainingManager_split` | 217–217 | `model_model_save` | Operação/referência de modelo (model_save) em 'TrainingManager_split' |
| `GANDLF/training_manager.py` | `TrainingManager_split` | 225–225 | `model_model_load` | Operação/referência de modelo (model_load) em 'TrainingManager_split' |
| `GANDLF/cli/post_training_model_optimization.py` | `post_training_model_optimization` | 24–24 | `model_model_load` | Operação/referência de modelo (model_load) em 'post_training_model_optimization' |
| `GANDLF/cli/post_training_model_optimization.py` | `post_training_model_optimization` | 46–46 | `model_model_load` | Operação/referência de modelo (model_load) em 'post_training_model_optimization' |
| `GANDLF/cli/preprocess_and_save.py` | `preprocess_and_save` | 48–48 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'preprocess_and_save' |
| `GANDLF/cli/preprocess_and_save.py` | `preprocess_and_save` | 50–50 | `model_model_load` | Operação/referência de modelo (model_load) em 'preprocess_and_save' |
| `GANDLF/cli/preprocess_and_save.py` | `preprocess_and_save` | 56–56 | `model_model_save` | Operação/referência de modelo (model_save) em 'preprocess_and_save' |
| `GANDLF/cli/recover_config.py` | `recover_config` | 21–21 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'recover_config' |
| `GANDLF/cli/recover_config.py` | `recover_config` | 27–27 | `model_model_load` | Operação/referência de modelo (model_load) em 'recover_config' |
| `GANDLF/compute/inference_loop.py` | `inference_loop` | 91–91 | `model_model_load` | Operação/referência de modelo (model_load) em 'inference_loop' |
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
- **Descrição:** Evidência parcial: sinais estruturais de treinamento e de inferência coexistem no(s) mesmo(s) arquivo(s) (GANDLF/compute/forward_pass.py, GANDLF/compute/training_loop.py, GANDLF/data/lightning_datamodule.py, GANDLF/models/lightning_module.py, testing/test_full.py, testing/test_lightning_components.py). Indicador técnico que merece investigação quanto à segregação arquitetural entre desenvolvimento/treino e produção/inferência.
- **Justificativa de Rastreabilidade:** Coexistência de sinais de treinamento e inferência em GANDLF/compute/forward_pass.py, GANDLF/compute/training_loop.py, GANDLF/data/lightning_datamodule.py, GANDLF/models/lightning_module.py, testing/test_full.py, testing/test_lightning_components.py. Requer inspeção humana do fluxo de controle para verificar se o modelo é congelado em produção.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `GANDLF/inference_manager.py` | `InferenceManager` | 13–155 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'InferenceManager' |
| `GANDLF/inference_manager.py` | `InferenceManager` | 120–120 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'InferenceManager' |
| `GANDLF/training_manager.py` | `TrainingManager` | 22–185 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'TrainingManager' |
| `GANDLF/training_manager.py` | `TrainingManager` | 181–181 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'TrainingManager' |
| `GANDLF/training_manager.py` | `TrainingManager_split` | 188–298 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'TrainingManager_split' |
| `GANDLF/training_manager.py` | `TrainingManager_split` | 295–295 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'TrainingManager_split' |
| `GANDLF/cli/post_training_model_optimization.py` | `post_training_model_optimization` | 9–56 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'post_training_model_optimization' |
| `GANDLF/compute/forward_pass.py` | `validate_network` | 281–281 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'validate_network' |
| `GANDLF/compute/forward_pass.py` | `validate_network` | 283–283 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'validate_network' |
| `GANDLF/compute/forward_pass.py` | `validate_network` | 496–496 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'validate_network' |
| `GANDLF/compute/forward_pass.py` | `validate_network` | 498–498 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'validate_network' |
| `GANDLF/compute/forward_pass.py` | `validate_network` | 88–88 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'validate_network' |
| `GANDLF/compute/inference_loop.py` | `inference_loop` | 32–368 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'inference_loop' |
| `GANDLF/compute/inference_loop.py` | `inference_loop` | 103–103 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'inference_loop' |
| `GANDLF/compute/training_loop.py` | `train_network` | 42–224 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'train_network' |
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
