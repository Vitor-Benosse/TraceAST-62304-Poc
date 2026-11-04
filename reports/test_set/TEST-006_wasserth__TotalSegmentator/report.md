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

- **Nome do Projeto:** TEST-006_wasserth__TotalSegmentator
- **Commit SHA Analisado:** `c59be95b839252dd993e1e32ff3369168d9f4eab`
- **Data e Horário da Execução (UTC):** `2026-11-04T22:15:14.086069+00:00`
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

- **Quantidade total de arquivos encontrados:** 402
- **Quantidade de arquivos Python (`.py`):** 108
- **Arquivos Python analisados com sucesso:** 108
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
- **Descrição:** Evidência identificada: todos os 108 arquivos Python encontrados foram analisados com sucesso via AST (cobertura de inspeção: 100.0%).
- **Justificativa de Rastreabilidade:** Inspeção concluída sem falhas de parsing em 108/108 arquivos Python.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `setup.py` | `<module>` | 1–112 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 82b19f8467df...) |
| `resources/anonymise_lightning_yaml.py` | `<module>` | 1–79 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 2fb7359257aa...) |
| `resources/anonymise_nnunet_pkl_v2.py` | `<module>` | 1–42 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 6096323326f7...) |
| `resources/convert_dataset_to_nnunet.py` | `<module>` | 1–116 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: eb5d39fa0f6b...) |
| `resources/evaluate.py` | `<module>` | 1–82 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 00c1b3f160c4...) |
| `tests/test_aorta_report.py` | `<module>` | 1–156 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: a025b661d2ca...) |
| `tests/test_aorta_report_cpr.py` | `<module>` | 1–125 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: d99d80fc2396...) |
| `tests/test_aorta_report_geometry.py` | `<module>` | 1–174 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: a3ee2bc4bde5...) |
| `tests/test_aorta_report_io.py` | `<module>` | 1–303 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 7f4fd53d7f3f...) |
| `tests/test_aorta_report_pipeline.py` | `<module>` | 1–231 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 87d32b5069ec...) |
| `tests/test_cnn.py` | `<module>` | 1–150 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: ff54628c2e9c...) |
| `tests/test_config.py` | `<module>` | 1–48 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 4cda1ce1edc9...) |
| `tests/test_device_type.py` | `<module>` | 1–26 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: dafe7f05534e...) |
| `tests/test_end_to_end.py` | `<module>` | 1–190 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 4945d684dc40...) |
| `tests/test_locally.py` | `<module>` | 1–283 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 1c1cd0943574...) |

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
- **Descrição:** Evidência parcial: manifesto(s) de dependências localizado(s) (pyproject.toml), contendo 0 pacote(s) com versão fixada e 0 pacote(s) sem versão exata fixada. Imports externos não declarados no manifesto: PIL, acvl_utils, ants, batchgenerators, batchgeneratorsv2, blosc, config, cucim, cupy, dicom2nifti, fury, highdicom, imgkit, jinja2, joblib, libs, matplotlib, mcp, modal, monai, networkx, nibabel, nnunet, nnunetv2, numpy, openpyxl, p_tqdm, pandas, psutil, pydicom, pynora, pytest, radiomics, requests, resample_nnunet, rt_utils, scipy, setuptools, skimage, sklearn, surface_distance, threadpoolctl, timm, torch, tqdm, utils, uvicorn, xgboost, xmltodict, xvfbwrapper. Componentes de IA/ML: MONAI (Medical Open Network for AI), NiBabel, PyDICOM, PyTorch, XGBoost, scikit-learn.
- **Justificativa de Rastreabilidade:** A presença de dependências sem versão fixada ou imports omitidos não representa automaticamente uma não conformidade, mas é um indicador técnico que merece investigação para controle de SOUP.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `setup.py` | `setuptools` | 1–1 | `undeclared_import` | Módulo externo 'setuptools' importado em 'setup.py', mas não localizado nos manifestos de dependências inspecionados. |
| `resources/convert_dataset_to_nnunet.py` | `nibabel` | 1–1 | `undeclared_import` | Módulo externo 'nibabel' importado em 'resources/convert_dataset_to_nnunet.py', mas não localizado nos manifestos de dependências inspecionados. |
| `resources/convert_dataset_to_nnunet.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'resources/convert_dataset_to_nnunet.py', mas não localizado nos manifestos de dependências inspecionados. |
| `resources/convert_dataset_to_nnunet.py` | `pandas` | 1–1 | `undeclared_import` | Módulo externo 'pandas' importado em 'resources/convert_dataset_to_nnunet.py', mas não localizado nos manifestos de dependências inspecionados. |
| `resources/convert_dataset_to_nnunet.py` | `tqdm` | 1–1 | `undeclared_import` | Módulo externo 'tqdm' importado em 'resources/convert_dataset_to_nnunet.py', mas não localizado nos manifestos de dependências inspecionados. |
| `resources/evaluate.py` | `nibabel` | 1–1 | `undeclared_import` | Módulo externo 'nibabel' importado em 'resources/evaluate.py', mas não localizado nos manifestos de dependências inspecionados. |
| `resources/evaluate.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'resources/evaluate.py', mas não localizado nos manifestos de dependências inspecionados. |
| `resources/evaluate.py` | `p_tqdm` | 1–1 | `undeclared_import` | Módulo externo 'p_tqdm' importado em 'resources/evaluate.py', mas não localizado nos manifestos de dependências inspecionados. |
| `resources/evaluate.py` | `pandas` | 1–1 | `undeclared_import` | Módulo externo 'pandas' importado em 'resources/evaluate.py', mas não localizado nos manifestos de dependências inspecionados. |
| `resources/evaluate.py` | `surface_distance` | 1–1 | `undeclared_import` | Módulo externo 'surface_distance' importado em 'resources/evaluate.py', mas não localizado nos manifestos de dependências inspecionados. |
| `resources/evaluate.py` | `tqdm` | 1–1 | `undeclared_import` | Módulo externo 'tqdm' importado em 'resources/evaluate.py', mas não localizado nos manifestos de dependências inspecionados. |
| `tests/test_aorta_report.py` | `pytest` | 1–1 | `undeclared_import` | Módulo externo 'pytest' importado em 'tests/test_aorta_report.py', mas não localizado nos manifestos de dependências inspecionados. |
| `tests/test_aorta_report_cpr.py` | `nibabel` | 1–1 | `undeclared_import` | Módulo externo 'nibabel' importado em 'tests/test_aorta_report_cpr.py', mas não localizado nos manifestos de dependências inspecionados. |
| `tests/test_aorta_report_cpr.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'tests/test_aorta_report_cpr.py', mas não localizado nos manifestos de dependências inspecionados. |
| `tests/test_aorta_report_geometry.py` | `nibabel` | 1–1 | `undeclared_import` | Módulo externo 'nibabel' importado em 'tests/test_aorta_report_geometry.py', mas não localizado nos manifestos de dependências inspecionados. |
*... e mais 240 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência identificada: 22 arquivo(s) de teste localizado(s) (diretórios: tests; frameworks: pytest, unittest; 123 função(ões)/método(s) de teste).
- **Justificativa de Rastreabilidade:** Módulos e funções de teste automatizado foram observados no repositório.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `tests/test_aorta_report.py` | `test_aorta_report_logs` | 120–138 | `test_module` | Módulo de teste 'tests/test_aorta_report.py' identificado (3 funções/métodos candidatos de teste). |
| `tests/test_aorta_report_cpr.py` | `test_resample_centerline_uses_physical_distance` | 27–35 | `test_module` | Módulo de teste 'tests/test_aorta_report_cpr.py' identificado (6 funções/métodos candidatos de teste). |
| `tests/test_aorta_report_geometry.py` | `test_centerline_arc_length_lookup_and_endpoints` | 32–46 | `test_module` | Módulo de teste 'tests/test_aorta_report_geometry.py' identificado (10 funções/métodos candidatos de teste). |
| `tests/test_aorta_report_io.py` | `test_crop_to_masks_uses_binary_mask_without_promoting_input` | 32–41 | `test_module` | Módulo de teste 'tests/test_aorta_report_io.py' identificado (11 funções/métodos candidatos de teste). |
| `tests/test_aorta_report_pipeline.py` | `_Logger.__init__` | 19–20 | `test_module` | Módulo de teste 'tests/test_aorta_report_pipeline.py' identificado (13 funções/métodos candidatos de teste). |
| `tests/test_cnn.py` | `test_new_model_target_orders_are_modality_specific` | 17–23 | `test_module` | Módulo de teste 'tests/test_cnn.py' identificado (9 funções/métodos candidatos de teste). |
| `tests/test_config.py` | `test_set_license_number_skips_validation_for_existing_license` | 6–23 | `test_module` | Módulo de teste 'tests/test_config.py' identificado (2 funções/métodos candidatos de teste). |
| `tests/test_device_type.py` | `TestValidateDeviceType.test_valid_inputs` | 5–10 | `test_module` | Módulo de teste 'tests/test_device_type.py' identificado (2 funções/métodos candidatos de teste). |
| `tests/test_end_to_end.py` | `test_end_to_end.setUp` | 36–37 | `test_module` | Módulo de teste 'tests/test_end_to_end.py' identificado (21 funções/métodos candidatos de teste). |
| `tests/test_locally.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/test_locally.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/test_mcp.py` | `TestMCPValidation.test_valid_total_request` | 7–8 | `test_module` | Módulo de teste 'tests/test_mcp.py' identificado (2 funções/métodos candidatos de teste). |
| `tests/test_nnunet_crop.py` | `test_empty_crop_returns_empty_segmentation_with_output_path` | 25–31 | `test_module` | Módulo de teste 'tests/test_nnunet_crop.py' identificado (2 funções/métodos candidatos de teste). |
| `tests/test_postprocessing.py` | `test_vertebrae_pp_postprocessing_returns_unchanged_without_touching_labels` | 12–19 | `test_module` | Módulo de teste 'tests/test_postprocessing.py' identificado (6 funções/métodos candidatos de teste). |
| `tests/test_pulmonary_report.py` | `test_pulmonary_report_logs` | 88–98 | `test_module` | Módulo de teste 'tests/test_pulmonary_report.py' identificado (3 funções/métodos candidatos de teste). |
| `tests/test_registry.py` | `TestRegistry.test_tasks_unique` | 20–21 | `test_module` | Módulo de teste 'tests/test_registry.py' identificado (17 funções/métodos candidatos de teste). |
*... e mais 7 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência identificada: 6 configuração(ões) de CI/CD localizada(s) com comandos declarados para execução automatizada de testes (evidências de cobertura: não identificadas).
- **Justificativa de Rastreabilidade:** Arquivos de workflow CI/CD contendo etapas de execução de testes foram encontrados.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `.github/workflows/codespell.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/codespell.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/lint.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/lint.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/run_tests.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/run_tests.yml' (comandos de teste: pip install pytest fury "uharfbuzz>=0.52,<0.56.1" xgboost, run: pytest -v tests/test_spine_report.py, run: pytest -v tests/test_aorta_report.py, run: pytest -v tests/test_pulmonary_report.py, pytest_prefix: "xvfb-run -a", pytest_prefix: "", pip install pytest scipy pillow scikit-image "${{ matrix.numpy-version }}" "${{ matrix.fury-version }}" "uharfbuzz>=0.52,<0.56.1", run: ${{ matrix.pytest_prefix }} pytest -v tests/test_rendering.py; cobertura: False) |
| `.github/workflows/run_tests_nnunet.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/run_tests_nnunet.yml' (comandos de teste: pip install pytest, pip install pytest; cobertura: False) |
| `.github/workflows/run_tests_os.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/run_tests_os.yml' (comandos de teste: pip install pytest fury "uharfbuzz>=0.52,<0.56.1", pip install pytest; cobertura: False) |
| `.github/workflows/run_tests_subtasks.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/run_tests_subtasks.yml' (comandos de teste: pip install pytest fury "uharfbuzz>=0.52,<0.56.1"; cobertura: False) |

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
- **Descrição:** Evidência parcial: entre 299 operação(ões) candidatas de I/O, 10 possuem bloco try-except não vazio e 289 não possuem tratamento local observável. Foram identificados 9 bloco(s) except vazios ou com 'pass'.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: coexistem operações de I/O sem captura local de exceção ou blocos except que suprimem falhas com pass.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `resources/anonymise_lightning_yaml.py` | N/A | 74–74 | `ast_io_operation` | Operação candidata de I/O 'hparams_file.read_text' em '<module>' (dentro de try-except não vazio: False) |
| `resources/anonymise_lightning_yaml.py` | N/A | 78–78 | `ast_io_operation` | Operação candidata de I/O 'hparams_file.write_text' em '<module>' (dentro de try-except não vazio: False) |
| `resources/convert_dataset_to_nnunet.py` | `generate_json_from_dir_v2` | 31–31 | `ast_io_operation` | Operação candidata de I/O 'json.dump' em 'generate_json_from_dir_v2' (dentro de try-except não vazio: False) |
| `resources/convert_dataset_to_nnunet.py` | `generate_json_from_dir_v2` | 31–31 | `ast_io_operation` | Operação candidata de I/O 'open' em 'generate_json_from_dir_v2' (dentro de try-except não vazio: False) |
| `resources/convert_dataset_to_nnunet.py` | `generate_json_from_dir_v2` | 47–47 | `ast_io_operation` | Operação candidata de I/O 'json.dump' em 'generate_json_from_dir_v2' (dentro de try-except não vazio: False) |
| `resources/convert_dataset_to_nnunet.py` | `generate_json_from_dir_v2` | 47–47 | `ast_io_operation` | Operação candidata de I/O 'open' em 'generate_json_from_dir_v2' (dentro de try-except não vazio: False) |
| `resources/convert_dataset_to_nnunet.py` | `combine_labels` | 51–51 | `ast_io_operation` | Operação candidata de I/O 'nib.load' em 'combine_labels' (dentro de try-except não vazio: False) |
| `resources/convert_dataset_to_nnunet.py` | `combine_labels` | 56–56 | `ast_io_operation` | Operação candidata de I/O 'nib.load' em 'combine_labels' (dentro de try-except não vazio: False) |
| `resources/convert_dataset_to_nnunet.py` | N/A | 94–94 | `ast_io_operation` | Operação candidata de I/O 'pd.read_csv' em '<module>' (dentro de try-except não vazio: False) |
| `resources/evaluate.py` | `calc_metrics` | 29–29 | `ast_io_operation` | Operação candidata de I/O 'nib.load' em 'calc_metrics' (dentro de try-except não vazio: False) |
| `resources/evaluate.py` | `calc_metrics` | 30–30 | `ast_io_operation` | Operação candidata de I/O 'nib.load' em 'calc_metrics' (dentro de try-except não vazio: False) |
| `tests/test_aorta_report.py` | `test_aorta_report_logs` | 121–121 | `ast_io_operation` | Operação candidata de I/O 'read_text' em 'test_aorta_report_logs' (dentro de try-except não vazio: False) |
| `tests/test_aorta_report.py` | `test_aorta_report_json` | 142–142 | `ast_io_operation` | Operação candidata de I/O 'open' em 'test_aorta_report_json' (dentro de try-except não vazio: False) |
| `tests/test_aorta_report.py` | `test_aorta_report_json` | 143–143 | `ast_io_operation` | Operação candidata de I/O 'json.load' em 'test_aorta_report_json' (dentro de try-except não vazio: False) |
| `tests/test_aorta_report.py` | `test_aorta_report_json` | 144–144 | `ast_io_operation` | Operação candidata de I/O 'open' em 'test_aorta_report_json' (dentro de try-except não vazio: False) |
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
- **Descrição:** Evidência identificada: 700 sinal(is) estrutural(is) de validação de entrada localizado(s), incluindo 116 função(ões)/chamada(s) de validação e 98 guarda(s) condicional(is) com levantamento de exceção.
- **Justificativa de Rastreabilidade:** Foram identificados mecanismos explícitos de verificação de entrada no código. A presença estrutural não garante suficiência clínica ou completude da validação.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `tests/test_aorta_report.py` | `dicts_almost_equal` | 24–56 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'dicts_almost_equal' |
| `tests/test_aorta_report.py` | `dicts_almost_equal` | 24–24 | `validation_validation_call` | Sinal de validação (validation_call) em 'dicts_almost_equal' |
| `tests/test_aorta_report.py` | `dicts_almost_equal` | 24–24 | `validation_validation_call` | Sinal de validação (validation_call) em 'dicts_almost_equal' |
| `tests/test_aorta_report.py` | `dicts_almost_equal` | 34–56 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'dicts_almost_equal' |
| `tests/test_aorta_report.py` | `dicts_almost_equal` | 34–34 | `validation_validation_call` | Sinal de validação (validation_call) em 'dicts_almost_equal' |
| `tests/test_aorta_report.py` | `dicts_almost_equal` | 34–34 | `validation_validation_call` | Sinal de validação (validation_call) em 'dicts_almost_equal' |
| `tests/test_aorta_report.py` | `dicts_almost_equal` | 44–56 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'dicts_almost_equal' |
| `tests/test_aorta_report.py` | `dicts_almost_equal` | 44–44 | `validation_validation_call` | Sinal de validação (validation_call) em 'dicts_almost_equal' |
| `tests/test_aorta_report.py` | `dicts_almost_equal` | 44–44 | `validation_validation_call` | Sinal de validação (validation_call) em 'dicts_almost_equal' |
| `tests/test_aorta_report.py` | `dicts_almost_equal` | 49–56 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'dicts_almost_equal' |
| `tests/test_aorta_report.py` | `dicts_almost_equal` | 49–49 | `validation_validation_call` | Sinal de validação (validation_call) em 'dicts_almost_equal' |
| `tests/test_aorta_report.py` | `dicts_almost_equal` | 49–49 | `validation_validation_call` | Sinal de validação (validation_call) em 'dicts_almost_equal' |
| `tests/test_aorta_report.py` | `remove_keys_with_prefix` | 63–68 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'remove_keys_with_prefix' |
| `tests/test_aorta_report.py` | `remove_keys_with_prefix` | 63–63 | `validation_validation_call` | Sinal de validação (validation_call) em 'remove_keys_with_prefix' |
| `tests/test_aorta_report.py` | `remove_keys_with_prefix` | 69–70 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'remove_keys_with_prefix' |
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
- **Descrição:** Evidência parcial: foram identificados 10 sinal(is) de carregamento, salvamento ou referência a checkpoints de modelos (2 arquivo(s) de modelo no repositório). A existência de chamadas de carga ou arquivos .pt/.pth/.onnx não comprova proveniência completa nem controle de versão do modelo.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: artefatos de modelo exigem rastreabilidade documental de versão, dataset de treinamento, hiperparâmetros e verificação de integridade (hash).

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `totalsegmentator/cnn.py` | `_find_fold_checkpoint` | 530–530 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '_find_fold_checkpoint' |
| `totalsegmentator/cnn.py` | `_load_torch_checkpoint._load` | 563–563 | `model_model_load` | Operação/referência de modelo (model_load) em '_load_torch_checkpoint._load' |
| `totalsegmentator/cnn.py` | `_load_fold_model` | 753–753 | `model_model_load` | Operação/referência de modelo (model_load) em '_load_fold_model' |
| `totalsegmentator/nnunet.py` | `nnUNetv2_predict` | 349–349 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'nnUNetv2_predict' |
| `totalsegmentator/bin/totalseg_get_body_stats.py` | `load_xgboost_model` | 66–66 | `model_model_load` | Operação/referência de modelo (model_load) em 'load_xgboost_model' |
| `totalsegmentator/bin/totalseg_get_modality.py` | `get_modality` | 52–52 | `model_model_load` | Operação/referência de modelo (model_load) em 'get_modality' |
| `totalsegmentator/bin/totalseg_get_modality.py` | `get_modality_from_rois` | 99–99 | `model_model_load` | Operação/referência de modelo (model_load) em 'get_modality_from_rois' |
| `totalsegmentator/bin/totalseg_get_phase.py` | `get_ct_contrast_phase` | 197–197 | `model_model_load` | Operação/referência de modelo (model_load) em 'get_ct_contrast_phase' |
| `totalsegmentator/resources/contrast_phase_classifiers_2024_07_19.pkl` | `contrast_phase_classifiers_2024_07_19.pkl` | 1–1 | `standalone_model_file` | Arquivo binário/checkpoint de modelo localizado no repositório: 'totalsegmentator/resources/contrast_phase_classifiers_2024_07_19.pkl' |
| `totalsegmentator/resources/modality_classifiers_2024_10_04.pkl` | `modality_classifiers_2024_10_04.pkl` | 1–1 | `standalone_model_file` | Arquivo binário/checkpoint de modelo localizado no repositório: 'totalsegmentator/resources/modality_classifiers_2024_10_04.pkl' |

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
- **Descrição:** Evidência parcial: sinais estruturais de treinamento e de inferência coexistem no(s) mesmo(s) arquivo(s) (totalsegmentator/cnn.py, totalsegmentator/custom_trainers.py, totalsegmentator/nnunet.py). Indicador técnico que merece investigação quanto à segregação arquitetural entre desenvolvimento/treino e produção/inferência.
- **Justificativa de Rastreabilidade:** Coexistência de sinais de treinamento e inferência em totalsegmentator/cnn.py, totalsegmentator/custom_trainers.py, totalsegmentator/nnunet.py. Requer inspeção humana do fluxo de controle para verificar se o modelo é congelado em produção.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `tests/test_end_to_end.py` | `test_end_to_end.test_prediction_multilabel` | 39–46 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'test_end_to_end.test_prediction_multilabel' |
| `tests/test_end_to_end.py` | `test_end_to_end.test_prediction_multilabel_high_order` | 48–55 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'test_end_to_end.test_prediction_multilabel_high_order' |
| `tests/test_end_to_end.py` | `test_end_to_end.test_prediction_multilabel_mr` | 57–62 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'test_end_to_end.test_prediction_multilabel_mr' |
| `tests/test_end_to_end.py` | `test_end_to_end.test_prediction_liver_roi_subset` | 64–69 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'test_end_to_end.test_prediction_liver_roi_subset' |
| `tests/test_end_to_end.py` | `test_end_to_end.test_prediction_liver_roi_subset_mr` | 71–76 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'test_end_to_end.test_prediction_liver_roi_subset_mr' |
| `tests/test_end_to_end.py` | `test_end_to_end.test_prediction_fast` | 82–88 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'test_end_to_end.test_prediction_fast' |
| `tests/test_end_to_end.py` | `test_end_to_end.test_prediction_multilabel_fast` | 90–95 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'test_end_to_end.test_prediction_multilabel_fast' |
| `tests/test_end_to_end.py` | `test_end_to_end.test_prediction_multilabel_fast_force_split` | 97–102 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'test_end_to_end.test_prediction_multilabel_fast_force_split' |
| `tests/test_end_to_end.py` | `test_end_to_end.test_prediction_multilabel_fast_body_seg` | 104–109 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'test_end_to_end.test_prediction_multilabel_fast_body_seg' |
| `tests/test_end_to_end.py` | `test_end_to_end.test_prediction_dicom` | 167–172 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'test_end_to_end.test_prediction_dicom' |
| `tests/test_end_to_end.py` | `test_end_to_end.test_phase_prediction` | 174–177 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'test_end_to_end.test_phase_prediction' |
| `tests/test_end_to_end.py` | `test_end_to_end.test_body_stats_prediction` | 179–182 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'test_end_to_end.test_body_stats_prediction' |
| `tests/test_end_to_end.py` | `test_end_to_end.test_nnunet_prediction` | 184–186 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'test_end_to_end.test_nnunet_prediction' |
| `tests/test_nnunet_crop.py` | `_predict_with_empty_crop` | 13–22 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em '_predict_with_empty_crop' |
| `tests/test_research_utils.py` | `test_statistics_extra_prediction_paths` | 51–124 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'test_statistics_extra_prediction_paths' |
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
