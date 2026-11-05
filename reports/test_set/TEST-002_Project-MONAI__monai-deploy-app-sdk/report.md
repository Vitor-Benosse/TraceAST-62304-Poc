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

- **Nome do Projeto:** TEST-002_Project-MONAI__monai-deploy-app-sdk
- **Commit SHA Analisado:** `3aee3dac70b70f4ec5e573e653eac4d149fc5812`
- **Data e Horário da Execução (UTC):** `2026-11-04T22:14:31.505449+00:00`
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

- **Quantidade total de arquivos encontrados:** 410
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
| `setup.py` | `<module>` | 1–38 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 81ece693df3f...) |
| `versioneer.py` | `<module>` | 1–2089 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 4d2f07c1be3f...) |
| `docs/source/conf.py` | `<module>` | 1–281 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 2f227f3af5f8...) |
| `examples/apps/convert_nnunet_ckpts.py` | `<module>` | 1–103 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 5d074f4e2838...) |
| `examples/apps/ai_livertumor_seg_app/__init__.py` | `<module>` | 1–18 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 1655ab465492...) |
| `examples/apps/ai_livertumor_seg_app/__main__.py` | `<module>` | 1–19 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 26755dd9a4b7...) |
| `examples/apps/ai_livertumor_seg_app/app.py` | `<module>` | 1–149 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 654d351d6727...) |
| `examples/apps/ai_livertumor_seg_app/livertumor_seg_operator.py` | `<module>` | 1–181 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: c7c5a0278d9b...) |
| `examples/apps/ai_multi_ai_app/__init__.py` | `<module>` | 1–7 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: c5b3e9f31fa8...) |
| `examples/apps/ai_multi_ai_app/__main__.py` | `<module>` | 1–8 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: cdeb32877b5b...) |
| `examples/apps/ai_multi_ai_app/app.py` | `<module>` | 1–258 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: d5bae7345d17...) |
| `examples/apps/ai_pancreas_seg_app/__init__.py` | `<module>` | 1–18 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 1655ab465492...) |
| `examples/apps/ai_pancreas_seg_app/__main__.py` | `<module>` | 1–19 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 69a3b7cd58b0...) |
| `examples/apps/ai_pancreas_seg_app/app.py` | `<module>` | 1–188 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 0c8628a6562f...) |
| `examples/apps/ai_remote_infer_app/__main__.py` | `<module>` | 1–15 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 30bc1ee6260b...) |

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
- **Descrição:** Evidência parcial: manifesto(s) de dependências localizado(s) (docs/requirements.txt, examples/apps/ai_multi_ai_app/requirements.txt, examples/apps/ai_spleen_seg_app/requirements.txt, examples/apps/breast_density_classifier_app/requirements.txt, examples/apps/cchmc-tcv-fast/my_app/requirements.txt, examples/apps/cchmc_nnunet_fifteen_ckpt_app/my_app/requirements.txt, examples/apps/cchmc_ped_abd_ct_seg_app/requirements.txt, examples/apps/mednist_classifier_monaideploy/requirements.txt, examples/apps/simple_imaging_app/requirements.txt, platforms/aidoc/restful_app/ai_spleen_seg_app/requirements.txt, platforms/aidoc/restful_app/requirements.txt, platforms/nuance_pin/requirements.txt, requirements-dev.txt, requirements-examples.txt, requirements-min.txt, requirements.txt, pyproject.toml), contendo 33 pacote(s) com versão fixada e 186 pacote(s) sem versão exata fixada. Imports externos não declarados no manifesto: abdomen_seg_operator, ai_service, app, app_context, app_generator, arg_parser, breast_density_classifier_operator, bundle_downloader, check_output_contract, clara_viz_operator, click, config, core, cupy, cupyx, cx_Freeze, datapath, datastore, diagnostic_report, dicom_data_loader_operator, dicom_encapsulated_pdf_writer_operator, dicom_sc_writer_operator, dicom_seg_writer_operator, dicom_series, dicom_series_selection, dicom_series_selector_operator, dicom_series_to_volume_operator, dicom_sop_instance, dicom_study, dicom_text_sr_writer_operator, dicom_utils, diffusers, distutils, domain, egress_operator, ensemble_average_operator, factory, fixtures, gaussian_operator, generator, google, gpu_bootstrap, gpu_util, grpc, grpc_ingress_operator, hub_client, huggingface_hub, image, inference_operator, io_type, jinja2, livertumor_seg_operator, main, map_service_pb2, map_service_pb2_grpc, median_operator, mem_budget, memory, model, model_registry, models, monai_bundle_inference_operator, monai_seg_inference_operator, monet_bundle_inference_operator, mongodb_entry_creator_operator, mongodb_writer_operator, my_app, named_model, nii_data_loader_operator, nnunet_bundle, nnunet_seg_operator, nvidia, odict, operators, pipeline_generator, png_converter_operator, post_transforms, postprocess_operator, postresample_operator, preprocess_operator, publisher_operator, py2exe, pynvml, pytest_lazyfixture, result, results_message, rich, rmm, run, runtime_env, sc_overlay, serve_client, serve_daemon, serve_folder_client, serve_publish, serve_release, serve_scratch, serve_state, serve_writers, settings, skimage, slidewindow_operator, sobel_operator, spleen_seg_operator, stl_conversion_operator, study_context, study_vram, torch_model, triton_model, unetr_seg_operator, yaml. Componentes de IA/ML: Hugging Face Diffusers, MONAI (Medical Open Network for AI), NiBabel, PyDICOM, PyTorch, SimpleITK.
- **Justificativa de Rastreabilidade:** A presença de dependências sem versão fixada ou imports omitidos não representa automaticamente uma não conformidade, mas é um indicador técnico que merece investigação para controle de SOUP.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `docs/requirements.txt` | `Sphinx` | 1–1 | `dependency_declaration` | Pacote 'Sphinx' declarado em 'docs/requirements.txt' (especificador: '>=5.3.0,<8.0.0', fixado: False, importado no código: True) |
| `docs/requirements.txt` | `sphinx-autobuild` | 2–2 | `dependency_declaration` | Pacote 'sphinx-autobuild' declarado em 'docs/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `myst-nb` | 3–3 | `dependency_declaration` | Pacote 'myst-nb' declarado em 'docs/requirements.txt' (especificador: '>=0.17.2', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `myst-parser` | 4–4 | `dependency_declaration` | Pacote 'myst-parser' declarado em 'docs/requirements.txt' (especificador: '>=0.18.0', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `lxml_html_clean` | 5–5 | `dependency_declaration` | Pacote 'lxml_html_clean' declarado em 'docs/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `linkify-it-py` | 6–6 | `dependency_declaration` | Pacote 'linkify-it-py' declarado em 'docs/requirements.txt' (especificador: '>=1.0.1', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `sphinx-togglebutton` | 7–7 | `dependency_declaration` | Pacote 'sphinx-togglebutton' declarado em 'docs/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `sphinx-copybutton` | 8–8 | `dependency_declaration` | Pacote 'sphinx-copybutton' declarado em 'docs/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `sphinxcontrib-bibtex` | 9–9 | `dependency_declaration` | Pacote 'sphinxcontrib-bibtex' declarado em 'docs/requirements.txt' (especificador: '>=2.4.1', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `sphinxcontrib-spelling` | 10–10 | `dependency_declaration` | Pacote 'sphinxcontrib-spelling' declarado em 'docs/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `sphinx-thebe` | 11–11 | `dependency_declaration` | Pacote 'sphinx-thebe' declarado em 'docs/requirements.txt' (especificador: '>=0.3.0', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `sphinx-design` | 12–12 | `dependency_declaration` | Pacote 'sphinx-design' declarado em 'docs/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `ablog` | 13–13 | `dependency_declaration` | Pacote 'ablog' declarado em 'docs/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `pydata_sphinx_theme` | 14–14 | `dependency_declaration` | Pacote 'pydata_sphinx_theme' declarado em 'docs/requirements.txt' (especificador: '>=0.13.0', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `sphinxemoji` | 15–15 | `dependency_declaration` | Pacote 'sphinxemoji' declarado em 'docs/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
*... e mais 257 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência identificada: 30 arquivo(s) de teste localizado(s) (diretórios: tests; frameworks: pytest, unittest; 178 função(ões)/método(s) de teste).
- **Justificativa de Rastreabilidade:** Módulos e funções de teste automatizado foram observados no repositório.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `examples/apps/cchmc-tcv-fast/scripts/test_contract_synthetic.py` | `test_contract_passes_on_valid_fixture` | 231–240 | `test_module` | Módulo de teste 'examples/apps/cchmc-tcv-fast/scripts/test_contract_synthetic.py' identificado (4 funções/métodos candidatos de teste). |
| `examples/apps/cchmc-tcv-fast/scripts/test_emit_npy.py` | `test_gate_convention_source` | 41–49 | `test_module` | Módulo de teste 'examples/apps/cchmc-tcv-fast/scripts/test_emit_npy.py' identificado (3 funções/métodos candidatos de teste). |
| `examples/apps/cchmc-tcv-fast/scripts/test_inference_params.py` | `test_inference_params_tcv` | 37–57 | `test_module` | Módulo de teste 'examples/apps/cchmc-tcv-fast/scripts/test_inference_params.py' identificado (2 funções/métodos candidatos de teste). |
| `examples/apps/cchmc-tcv-fast/scripts/test_scratch_orphan.py` | `test_orphan_sweep_removes_stale_root` | 35–39 | `test_module` | Módulo de teste 'examples/apps/cchmc-tcv-fast/scripts/test_scratch_orphan.py' identificado (3 funções/métodos candidatos de teste). |
| `examples/apps/cchmc-tcv-fast/scripts/test_serve_folder_client.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'examples/apps/cchmc-tcv-fast/scripts/test_serve_folder_client.py' identificado (0 funções/métodos candidatos de teste). |
| `examples/apps/cchmc-tcv-fast/scripts/test_serve_import.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'examples/apps/cchmc-tcv-fast/scripts/test_serve_import.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/__init__.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/__init__.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/conftest.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/conftest.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/fixtures/__init__.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/fixtures/__init__.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/fixtures/runner_fixtures.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/fixtures/runner_fixtures.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/integration/__init__.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/integration/__init__.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/performance/__init__.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/performance/__init__.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/system/packager/test_packager.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/system/packager/test_packager.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/unit/__init__.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/unit/__init__.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/unit/test_argparse_types.py` | `test_valid_dir_path_valid_args` | 22–32 | `test_module` | Módulo de teste 'tests/unit/test_argparse_types.py' identificado (7 funções/métodos candidatos de teste). |
*... e mais 17 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência identificada: 1 configuração(ões) de CI/CD localizada(s) com comandos declarados para execução automatizada de testes (evidências de cobertura: .coveragerc).
- **Justificativa de Rastreabilidade:** Arquivos de workflow CI/CD contendo etapas de execução de testes foram encontrados.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `.github/workflows/pr.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/pr.yml' (comandos de teste: uv run pytest; cobertura: False) |

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
- **Descrição:** Evidência parcial: entre 312 operação(ões) candidatas de I/O, 51 possuem bloco try-except não vazio e 261 não possuem tratamento local observável. Foram identificados 64 bloco(s) except vazios ou com 'pass'.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: coexistem operações de I/O sem captura local de exceção ou blocos except que suprimem falhas com pass.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `versioneer.py` | `get_config_from_root` | 338–338 | `ast_io_operation` | Operação candidata de I/O 'open' em 'get_config_from_root' (dentro de try-except não vazio: False) |
| `versioneer.py` | `git_get_keywords` | 1054–1054 | `ast_io_operation` | Operação candidata de I/O 'open' em 'git_get_keywords' (dentro de try-except não vazio: False) |
| `versioneer.py` | `do_vcs_install` | 1287–1287 | `ast_io_operation` | Operação candidata de I/O 'open' em 'do_vcs_install' (dentro de try-except não vazio: False) |
| `versioneer.py` | `do_vcs_install` | 1296–1296 | `ast_io_operation` | Operação candidata de I/O 'open' em 'do_vcs_install' (dentro de try-except não vazio: False) |
| `versioneer.py` | `versions_from_file` | 1350–1350 | `ast_io_operation` | Operação candidata de I/O 'open' em 'versions_from_file' (dentro de try-except não vazio: True) |
| `versioneer.py` | `versions_from_file` | 1359–1359 | `ast_io_operation` | Operação candidata de I/O 'json.loads' em 'versions_from_file' (dentro de try-except não vazio: False) |
| `versioneer.py` | `write_to_version_file` | 1365–1365 | `ast_io_operation` | Operação candidata de I/O 'json.dumps' em 'write_to_version_file' (dentro de try-except não vazio: False) |
| `versioneer.py` | `write_to_version_file` | 1366–1366 | `ast_io_operation` | Operação candidata de I/O 'open' em 'write_to_version_file' (dentro de try-except não vazio: False) |
| `versioneer.py` | `get_cmdclass.cmd_build_exe.run` | 1830–1830 | `ast_io_operation` | Operação candidata de I/O 'open' em 'get_cmdclass.cmd_build_exe.run' (dentro de try-except não vazio: False) |
| `versioneer.py` | `get_cmdclass.cmd_py2exe.run` | 1860–1860 | `ast_io_operation` | Operação candidata de I/O 'open' em 'get_cmdclass.cmd_py2exe.run' (dentro de try-except não vazio: False) |
| `versioneer.py` | `do_setup` | 1966–1966 | `ast_io_operation` | Operação candidata de I/O 'open' em 'do_setup' (dentro de try-except não vazio: True) |
| `versioneer.py` | `do_setup` | 1972–1972 | `ast_io_operation` | Operação candidata de I/O 'open' em 'do_setup' (dentro de try-except não vazio: False) |
| `versioneer.py` | `do_setup` | 1988–1988 | `ast_io_operation` | Operação candidata de I/O 'open' em 'do_setup' (dentro de try-except não vazio: True) |
| `versioneer.py` | `do_setup` | 1996–1996 | `ast_io_operation` | Operação candidata de I/O 'open' em 'do_setup' (dentro de try-except não vazio: False) |
| `versioneer.py` | `do_setup` | 2000–2000 | `ast_io_operation` | Operação candidata de I/O 'open' em 'do_setup' (dentro de try-except não vazio: False) |
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
- **Descrição:** Evidência identificada: 1456 sinal(is) estrutural(is) de validação de entrada localizado(s), incluindo 262 função(ões)/chamada(s) de validação e 327 guarda(s) condicional(is) com levantamento de exceção.
- **Justificativa de Rastreabilidade:** Foram identificados mecanismos explícitos de verificação de entrada no código. A presença estrutural não garante suficiência clínica ou completude da validação.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `versioneer.py` | `get_root` | 304–312 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'get_root' |
| `versioneer.py` | `run_command` | 382–382 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'run_command' |
| `versioneer.py` | `run_command` | 382–382 | `validation_validation_call` | Sinal de validação (validation_call) em 'run_command' |
| `versioneer.py` | `git_versions_from_keywords` | 1076–1077 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'git_versions_from_keywords' |
| `versioneer.py` | `git_versions_from_keywords` | 1079–1090 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'git_versions_from_keywords' |
| `versioneer.py` | `git_versions_from_keywords` | 1092–1095 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'git_versions_from_keywords' |
| `versioneer.py` | `git_pieces_from_vcs` | 1157–1160 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'git_pieces_from_vcs' |
| `versioneer.py` | `git_pieces_from_vcs` | 1168–1169 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'git_pieces_from_vcs' |
| `versioneer.py` | `git_pieces_from_vcs` | 1172–1173 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'git_pieces_from_vcs' |
| `versioneer.py` | `git_pieces_from_vcs` | 1183–1184 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'git_pieces_from_vcs' |
| `versioneer.py` | `git_pieces_from_vcs` | 1193–1194 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'git_pieces_from_vcs' |
| `versioneer.py` | `versions_from_file` | 1357–1358 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'versions_from_file' |
| `versioneer.py` | `get_versions` | 1624–1624 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'get_versions' |
| `versioneer.py` | `get_versions` | 1626–1626 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'get_versions' |
| `versioneer.py` | `get_versions` | 1628–1628 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'get_versions' |
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
- **Descrição:** Evidência parcial: foram identificados 49 sinal(is) de carregamento, salvamento ou referência a checkpoints de modelos (0 arquivo(s) de modelo no repositório). A existência de chamadas de carga ou arquivos .pt/.pth/.onnx não comprova proveniência completa nem controle de versão do modelo.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: artefatos de modelo exigem rastreabilidade documental de versão, dataset de treinamento, hiperparâmetros e verificação de integridade (hash).

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `examples/apps/cchmc-tcv-fast/my_app/config/__init__.py` | `load_torch_checkpoint` | 76–76 | `model_model_load` | Operação/referência de modelo (model_load) em 'load_torch_checkpoint' |
| `examples/apps/cchmc-tcv-fast/my_app/config/__init__.py` | `resolve_checkpoint_name` | 390–390 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'resolve_checkpoint_name' |
| `examples/apps/cchmc-tcv-fast/my_app/config/__init__.py` | `resolve_checkpoint_name` | 390–390 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'resolve_checkpoint_name' |
| `examples/apps/cchmc-tcv-fast/my_app/operators/postprocess_operator.py` | `load_postprocessing_rules` | 160–160 | `model_model_load` | Operação/referência de modelo (model_load) em 'load_postprocessing_rules' |
| `examples/apps/cchmc-tcv-fast/my_app/operators/postprocess_operator.py` | `PostprocessOperator._load_rules` | 598–598 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'PostprocessOperator._load_rules' |
| `examples/apps/cchmc-tcv-fast/my_app/operators/slidewindow_operator.py` | `build_network_from_params` | 210–210 | `model_model_load` | Operação/referência de modelo (model_load) em 'build_network_from_params' |
| `examples/apps/cchmc-tcv-fast/my_app/operators/slidewindow_operator.py` | `predict_logits` | 451–451 | `model_model_load` | Operação/referência de modelo (model_load) em 'predict_logits' |
| `examples/apps/cchmc-tcv-fast/scripts/load_verify.py` | `main` | 140–140 | `model_model_load` | Operação/referência de modelo (model_load) em 'main' |
| `examples/apps/cchmc-tcv-fast/scripts/load_verify.py` | `main` | 145–145 | `model_model_load` | Operação/referência de modelo (model_load) em 'main' |
| `examples/apps/cchmc-tcv-fast/scripts/sync_checkpoint_meta.py` | `main` | 87–87 | `model_model_save` | Operação/referência de modelo (model_save) em 'main' |
| `examples/apps/cchmc_nnunet_fifteen_ckpt_app/my_app/nnunet_bundle.py` | `_resolve_checkpoint_name` | 70–70 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '_resolve_checkpoint_name' |
| `examples/apps/cchmc_nnunet_fifteen_ckpt_app/my_app/nnunet_bundle.py` | `_resolve_checkpoint_name` | 71–71 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '_resolve_checkpoint_name' |
| `examples/apps/cchmc_nnunet_fifteen_ckpt_app/my_app/nnunet_bundle.py` | `convert_nnunet_to_monai_bundle` | 159–163 | `model_model_load` | Operação/referência de modelo (model_load) em 'convert_nnunet_to_monai_bundle' |
| `examples/apps/cchmc_nnunet_fifteen_ckpt_app/my_app/nnunet_bundle.py` | `convert_nnunet_to_monai_bundle` | 160–160 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'convert_nnunet_to_monai_bundle' |
| `examples/apps/cchmc_nnunet_fifteen_ckpt_app/my_app/nnunet_bundle.py` | `convert_nnunet_to_monai_bundle` | 167–171 | `model_model_load` | Operação/referência de modelo (model_load) em 'convert_nnunet_to_monai_bundle' |
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
- **Descrição:** Evidência parcial: sinais estruturais de treinamento e de inferência coexistem no(s) mesmo(s) arquivo(s) (examples/apps/cchmc_nnunet_fifteen_ckpt_app/my_app/nnunet_bundle.py, monai/deploy/core/models/torch_model.py). Indicador técnico que merece investigação quanto à segregação arquitetural entre desenvolvimento/treino e produção/inferência.
- **Justificativa de Rastreabilidade:** Coexistência de sinais de treinamento e inferência em examples/apps/cchmc_nnunet_fifteen_ckpt_app/my_app/nnunet_bundle.py, monai/deploy/core/models/torch_model.py. Requer inspeção humana do fluxo de controle para verificar se o modelo é congelado em produção.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `examples/apps/breast_density_classifier_app/breast_density_classifier_operator.py` | `ClassifierOperator.compute` | 163–163 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'ClassifierOperator.compute' |
| `examples/apps/cchmc-tcv-fast/my_app/config/__init__.py` | `load_inference_params` | 471–540 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'load_inference_params' |
| `examples/apps/cchmc-tcv-fast/my_app/operators/slidewindow_operator.py` | `build_network_from_params` | 212–212 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'build_network_from_params' |
| `examples/apps/cchmc-tcv-fast/my_app/operators/slidewindow_operator.py` | `mirror_and_predict` | 292–310 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'mirror_and_predict' |
| `examples/apps/cchmc-tcv-fast/my_app/operators/slidewindow_operator.py` | `sliding_window_predict` | 331–422 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'sliding_window_predict' |
| `examples/apps/cchmc-tcv-fast/my_app/operators/slidewindow_operator.py` | `predict_logits` | 425–469 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'predict_logits' |
| `examples/apps/cchmc-tcv-fast/my_app/operators/slidewindow_operator.py` | `SlideWindowOperator.compute` | 740–740 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'SlideWindowOperator.compute' |
| `examples/apps/cchmc-tcv-fast/scripts/test_inference_params.py` | `test_inference_params_tcv` | 37–57 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'test_inference_params_tcv' |
| `examples/apps/cchmc_nnunet_fifteen_ckpt_app/my_app/nnunet_bundle.py` | `get_nnunet_trainer` | 531–637 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'get_nnunet_trainer' |
| `examples/apps/cchmc_nnunet_fifteen_ckpt_app/my_app/nnunet_bundle.py` | `_resolve_predictor_device` | 94–99 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em '_resolve_predictor_device' |
| `examples/apps/cchmc_nnunet_fifteen_ckpt_app/my_app/nnunet_bundle.py` | `get_nnunet_monai_predictor` | 640–726 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'get_nnunet_monai_predictor' |
| `examples/apps/cchmc_nnunet_fifteen_ckpt_app/my_app/nnunet_bundle.py` | `get_nnunet_monai_predictors_for_ensemble` | 729–751 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'get_nnunet_monai_predictors_for_ensemble' |
| `examples/apps/cchmc_nnunet_fifteen_ckpt_app/my_app/nnunet_bundle.py` | `ModelnnUNetWrapper.forward` | 1035–1198 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'ModelnnUNetWrapper.forward' |
| `examples/apps/cchmc_nnunet_fifteen_ckpt_app/my_app/nnunet_seg_operator.py` | `NNUnetSegOperator._load_nnunet_models` | 195–195 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'NNUnetSegOperator._load_nnunet_models' |
| `examples/apps/cchmc_ped_abd_ct_seg_app/abdomen_seg_operator.py` | `AbdomenSegOperator._load_pytorch_model` | 125–125 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'AbdomenSegOperator._load_pytorch_model' |
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
