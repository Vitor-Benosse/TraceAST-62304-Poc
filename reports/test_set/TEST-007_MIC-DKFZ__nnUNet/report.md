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

- **Nome do Projeto:** TEST-007_MIC-DKFZ__nnUNet
- **Commit SHA Analisado:** `517ddab5794f5c4e9083d4341fd99cdcb4d7c1ce`
- **Data e Horário da Execução (UTC):** `2026-11-04T22:15:22.987423+00:00`
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

- **Quantidade total de arquivos encontrados:** 322
- **Quantidade de arquivos Python (`.py`):** 235
- **Arquivos Python analisados com sucesso:** 235
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
- **Descrição:** Evidência identificada: todos os 235 arquivos Python encontrados foram analisados com sucesso via AST (cobertura de inspeção: 100.0%).
- **Justificativa de Rastreabilidade:** Inspeção concluída sem falhas de parsing em 235/235 arquivos Python.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `setup.py` | `<module>` | 1–4 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 269f762f9492...) |
| `documentation/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `documentation/competitions/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `documentation/competitions/FLARE24/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `documentation/competitions/FLARE24/Task_1/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `<module>` | 1–209 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: b35c072a975d...) |
| `documentation/competitions/FLARE24/Task_2/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `<module>` | 1–467 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 49a19b738ac7...) |
| `documentation/competitions/Toothfairy2/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `documentation/competitions/Toothfairy2/inference_script_semseg_only_customInf2.py` | `<module>` | 1–359 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 9c63dd4f6ab2...) |
| `nnunetv2/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `nnunetv2/configuration.py` | `<module>` | 1–10 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 019f8b794c17...) |
| `nnunetv2/paths.py` | `<module>` | 1–79 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 2f8ab98a8947...) |
| `nnunetv2/batch_running/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `nnunetv2/batch_running/collect_results_custom_Decathlon.py` | `<module>` | 1–121 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 1ce7dea519ca...) |

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
- **Descrição:** Evidência parcial: manifesto(s) de dependências localizado(s) (pyproject.toml), contendo 0 pacote(s) com versão fixada e 24 pacote(s) sem versão exata fixada. Imports externos não declarados no manifesto: PIL, adan_pytorch, dicom2nifti, hiddenlayer, huggingface_hub, openvino, pydicom, pytest, setuptools, skimage, threadpoolctl, wandb. Componentes de IA/ML: NiBabel, PyDICOM, PyTorch, SimpleITK, scikit-learn.
- **Justificativa de Rastreabilidade:** A presença de dependências sem versão fixada ou imports omitidos não representa automaticamente uma não conformidade, mas é um indicador técnico que merece investigação para controle de SOUP.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `pyproject.toml` | `torch` | 1–1 | `dependency_declaration` | Pacote 'torch' declarado em 'pyproject.toml' (especificador: '>=2.1.2,!=2.9.*', fixado: False, importado no código: True) |
| `pyproject.toml` | `acvl-utils` | 1–1 | `dependency_declaration` | Pacote 'acvl-utils' declarado em 'pyproject.toml' (especificador: '>=0.2.6,<0.3', fixado: False, importado no código: True) |
| `pyproject.toml` | `dynamic-network-architectures` | 1–1 | `dependency_declaration` | Pacote 'dynamic-network-architectures' declarado em 'pyproject.toml' (especificador: '>=0.4.4,<0.5', fixado: False, importado no código: True) |
| `pyproject.toml` | `tqdm` | 1–1 | `dependency_declaration` | Pacote 'tqdm' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `scipy` | 1–1 | `dependency_declaration` | Pacote 'scipy' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `batchgenerators` | 1–1 | `dependency_declaration` | Pacote 'batchgenerators' declarado em 'pyproject.toml' (especificador: '>=0.25.6', fixado: False, importado no código: True) |
| `pyproject.toml` | `numpy` | 1–1 | `dependency_declaration` | Pacote 'numpy' declarado em 'pyproject.toml' (especificador: '>=1.24', fixado: False, importado no código: True) |
| `pyproject.toml` | `scikit-learn` | 1–1 | `dependency_declaration` | Pacote 'scikit-learn' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `scikit-image` | 1–1 | `dependency_declaration` | Pacote 'scikit-image' declarado em 'pyproject.toml' (especificador: '>=0.19.3', fixado: False, importado no código: False) |
| `pyproject.toml` | `SimpleITK` | 1–1 | `dependency_declaration` | Pacote 'SimpleITK' declarado em 'pyproject.toml' (especificador: '>=2.2.1', fixado: False, importado no código: True) |
| `pyproject.toml` | `pandas` | 1–1 | `dependency_declaration` | Pacote 'pandas' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `graphviz` | 1–1 | `dependency_declaration` | Pacote 'graphviz' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `pyproject.toml` | `tifffile` | 1–1 | `dependency_declaration` | Pacote 'tifffile' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `requests` | 1–1 | `dependency_declaration` | Pacote 'requests' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `nibabel` | 1–1 | `dependency_declaration` | Pacote 'nibabel' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
*... e mais 28 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência identificada: 25 arquivo(s) de teste localizado(s) (diretórios: raiz/módulos; frameworks: pytest, unittest; 245 função(ões)/método(s) de teste).
- **Justificativa de Rastreabilidade:** Módulos e funções de teste automatizado foram observados no repositório.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `nnunetv2/tests/__init__.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'nnunetv2/tests/__init__.py' identificado (0 funções/métodos candidatos de teste). |
| `nnunetv2/tests/test_blosc2_read_ahead.py` | `TestBlosc2ReadAhead.setUp` | 28–29 | `test_module` | Módulo de teste 'nnunetv2/tests/test_blosc2_read_ahead.py' identificado (8 funções/métodos candidatos de teste). |
| `nnunetv2/tests/test_checkpoints.py` | `_TmpDirTestCase.setUp` | 92–94 | `test_module` | Módulo de teste 'nnunetv2/tests/test_checkpoints.py' identificado (60 funções/métodos candidatos de teste). |
| `nnunetv2/tests/test_compile_helpers.py` | `TestCompileHelpers.test_inductor_cache_dir` | 11–22 | `test_module` | Módulo de teste 'nnunetv2/tests/test_compile_helpers.py' identificado (2 funções/métodos candidatos de teste). |
| `nnunetv2/tests/test_copy_file_if_newer.py` | `TestCopyFileIfNewer._write` | 9–12 | `test_module` | Módulo de teste 'nnunetv2/tests/test_copy_file_if_newer.py' identificado (6 funções/métodos candidatos de teste). |
| `nnunetv2/tests/test_data_loader_bbox.py` | `_OneVoxelLocations.__init__` | 14–16 | `test_module` | Módulo de teste 'nnunetv2/tests/test_data_loader_bbox.py' identificado (9 funções/métodos candidatos de teste). |
| `nnunetv2/tests/test_dataset_fingerprint.py` | `TestDatasetFingerprintExtractor.test_collect_foreground_intensities_excludes_ignore_label` | 9–34 | `test_module` | Módulo de teste 'nnunetv2/tests/test_dataset_fingerprint.py' identificado (2 funções/métodos candidatos de teste). |
| `nnunetv2/tests/test_do_split.py` | `_FakeDataset.__init__` | 18–19 | `test_module` | Módulo de teste 'nnunetv2/tests/test_do_split.py' identificado (5 funções/métodos candidatos de teste). |
| `nnunetv2/tests/test_evaluate_predictions.py` | `TestConfusionMatrix.test_matches_brute_force` | 79–87 | `test_module` | Módulo de teste 'nnunetv2/tests/test_evaluate_predictions.py' identificado (21 funções/métodos candidatos de teste). |
| `nnunetv2/tests/test_find_objects.py` | `TestFindObjects.test_external_trainer_lookup_handles_multiple_directories_with_same_package_name` | 18–54 | `test_module` | Módulo de teste 'nnunetv2/tests/test_find_objects.py' identificado (4 funções/métodos candidatos de teste). |
| `nnunetv2/tests/test_foreground_locations.py` | `TestForegroundLocationsStore.setUp` | 45–48 | `test_module` | Módulo de teste 'nnunetv2/tests/test_foreground_locations.py' identificado (35 funções/métodos candidatos de teste). |
| `nnunetv2/tests/test_model_download.py` | `_BrokenOffResponse.__enter__` | 13–14 | `test_module` | Módulo de teste 'nnunetv2/tests/test_model_download.py' identificado (5 funções/métodos candidatos de teste). |
| `nnunetv2/tests/test_natural_image_tiff_compression.py` | `TestNaturalImage2DIOTiffCompression.test_supported_file_endings_include_tiff` | 16–18 | `test_module` | Módulo de teste 'nnunetv2/tests/test_natural_image_tiff_compression.py' identificado (9 funções/métodos candidatos de teste). |
| `nnunetv2/tests/test_no_resample.py` | `test_preprocessing_resolves_spacing` | 125–166 | `test_module` | Módulo de teste 'nnunetv2/tests/test_no_resample.py' identificado (6 funções/métodos candidatos de teste). |
| `nnunetv2/tests/test_paths.py` | `TestPaths.test_missing_env_var_only_raises_when_converted_to_path` | 10–15 | `test_module` | Módulo de teste 'nnunetv2/tests/test_paths.py' identificado (4 funções/métodos candidatos de teste). |
*... e mais 10 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência identificada: 5 configuração(ões) de CI/CD localizada(s) com comandos declarados para execução automatizada de testes (evidências de cobertura: não identificadas).
- **Justificativa de Rastreabilidade:** Arquivos de workflow CI/CD contendo etapas de execução de testes foram encontrados.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `.github/workflows/bug-fix-pr.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/bug-fix-pr.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/issue-agent.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/issue-agent.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/pr-agent.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/pr-agent.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/publish.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/publish.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/run_tests_nnunet.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/run_tests_nnunet.yml' (comandos de teste: pip install pytest Cython, pip install pytest Cython, pip install pytest Cython; cobertura: False) |

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
- **Descrição:** Evidência parcial: entre 155 operação(ões) candidatas de I/O, 9 possuem bloco try-except não vazio e 146 não possuem tratamento local observável. Foram identificados 10 bloco(s) except vazios ou com 'pass'.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: coexistem operações de I/O sem captura local de exceção ou blocos except que suprimem falhas com pass.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `FlarePredictor.initialize_from_trained_model_folder` | 47–48 | `ast_io_operation` | Operação candidata de I/O 'torch.load' em 'FlarePredictor.initialize_from_trained_model_folder' (dentro de try-except não vazio: False) |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.initialize_from_trained_model_folder` | 74–75 | `ast_io_operation` | Operação candidata de I/O 'torch.load' em 'FlarePredictor.initialize_from_trained_model_folder' (dentro de try-except não vazio: False) |
| `documentation/competitions/Toothfairy2/inference_script_semseg_only_customInf2.py` | `CustomPredictor.initialize_from_trained_model_folder` | 75–76 | `ast_io_operation` | Operação candidata de I/O 'torch.load' em 'CustomPredictor.initialize_from_trained_model_folder' (dentro de try-except não vazio: False) |
| `documentation/competitions/Toothfairy2/inference_script_semseg_only_customInf2.py` | `CustomPredictor.predict_preprocessed_image` | 164–164 | `ast_io_operation` | Operação candidata de I/O 'torch.load' em 'CustomPredictor.predict_preprocessed_image' (dentro de try-except não vazio: False) |
| `nnunetv2/batch_running/collect_results_custom_Decathlon.py` | `collect_results` | 17–17 | `ast_io_operation` | Operação candidata de I/O 'open' em 'collect_results' (dentro de try-except não vazio: False) |
| `nnunetv2/batch_running/collect_results_custom_Decathlon.py` | `summarize` | 54–54 | `ast_io_operation` | Operação candidata de I/O 'open' em 'summarize' (dentro de try-except não vazio: False) |
| `nnunetv2/batch_running/generate_lsf_runs_customDecathlon.py` | N/A | 102–102 | `ast_io_operation` | Operação candidata de I/O 'open' em '<module>' (dentro de try-except não vazio: False) |
| `nnunetv2/batch_running/benchmarking/generate_benchmarking_commands.py` | N/A | 30–30 | `ast_io_operation` | Operação candidata de I/O 'open' em '<module>' (dentro de try-except não vazio: False) |
| `nnunetv2/batch_running/benchmarking/summarize_benchmark_results.py` | N/A | 47–47 | `ast_io_operation` | Operação candidata de I/O 'open' em '<module>' (dentro de try-except não vazio: False) |
| `nnunetv2/batch_running/release_trainings/nnunetv2_v1/collect_results.py` | `collect_results` | 17–17 | `ast_io_operation` | Operação candidata de I/O 'open' em 'collect_results' (dentro de try-except não vazio: False) |
| `nnunetv2/batch_running/release_trainings/nnunetv2_v1/collect_results.py` | `summarize` | 54–54 | `ast_io_operation` | Operação candidata de I/O 'open' em 'summarize' (dentro de try-except não vazio: False) |
| `nnunetv2/batch_running/release_trainings/nnunetv2_v1/generate_lsf_commands.py` | N/A | 82–82 | `ast_io_operation` | Operação candidata de I/O 'open' em '<module>' (dentro de try-except não vazio: False) |
| `nnunetv2/dataset_conversion/Dataset015_018_RibFrac_RibSeg.py` | `load_ribfrac_info` | 30–30 | `ast_io_operation` | Operação candidata de I/O 'open' em 'load_ribfrac_info' (dentro de try-except não vazio: False) |
| `nnunetv2/dataset_conversion/Dataset015_018_RibFrac_RibSeg.py` | `write_fracture_types_csv` | 38–38 | `ast_io_operation` | Operação candidata de I/O 'open' em 'write_fracture_types_csv' (dentro de try-except não vazio: False) |
| `nnunetv2/dataset_conversion/Dataset015_018_RibFrac_RibSeg.py` | `migrate_existing_dataset015` | 77–77 | `ast_io_operation` | Operação candidata de I/O 'sitk.ReadImage' em 'migrate_existing_dataset015' (dentro de try-except não vazio: False) |
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
- **Descrição:** Evidência identificada: 950 sinal(is) estrutural(is) de validação de entrada localizado(s), incluindo 229 função(ões)/chamada(s) de validação e 134 guarda(s) condicional(is) com levantamento de exceção.
- **Justificativa de Rastreabilidade:** Foram identificados mecanismos explícitos de verificação de entrada no código. A presença estrutural não garante suficiência clínica ou completude da validação.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `FlarePredictor.initialize_from_trained_model_folder` | 34–35 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `FlarePredictor.initialize_from_trained_model_folder` | 41–42 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `FlarePredictor.initialize_from_trained_model_folder` | 41–41 | `validation_validation_call` | Sinal de validação (validation_call) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `FlarePredictor.initialize_from_trained_model_folder` | 62–64 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `FlarePredictor.initialize_from_trained_model_folder` | 99–101 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `FlarePredictor.initialize_from_trained_model_folder` | 100–100 | `validation_validation_call` | Sinal de validação (validation_call) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `convert_predicted_logits_to_segmentation_with_correct_shape` | 131–132 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'convert_predicted_logits_to_segmentation_with_correct_shape' |
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `convert_predicted_logits_to_segmentation_with_correct_shape` | 131–131 | `validation_validation_call` | Sinal de validação (validation_call) em 'convert_predicted_logits_to_segmentation_with_correct_shape' |
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `export_prediction_from_logits` | 153–154 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'export_prediction_from_logits' |
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `export_prediction_from_logits` | 153–153 | `validation_validation_call` | Sinal de validação (validation_call) em 'export_prediction_from_logits' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.__init__` | 50–51 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'FlarePredictor.__init__' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.initialize_from_trained_model_folder` | 60–61 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.initialize_from_trained_model_folder` | 67–68 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.initialize_from_trained_model_folder` | 67–67 | `validation_validation_call` | Sinal de validação (validation_call) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.initialize_from_trained_model_folder` | 69–69 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'FlarePredictor.initialize_from_trained_model_folder' |
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
- **Descrição:** Evidência parcial: foram identificados 132 sinal(is) de carregamento, salvamento ou referência a checkpoints de modelos (0 arquivo(s) de modelo no repositório). A existência de chamadas de carga ou arquivos .pt/.pth/.onnx não comprova proveniência completa nem controle de versão do modelo.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: artefatos de modelo exigem rastreabilidade documental de versão, dataset de treinamento, hiperparâmetros e verificação de integridade (hash).

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `FlarePredictor.initialize_from_trained_model_folder` | 47–48 | `model_model_load` | Operação/referência de modelo (model_load) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.initialize_from_trained_model_folder` | 74–75 | `model_model_load` | Operação/referência de modelo (model_load) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.initialize_from_trained_model_folder` | 127–127 | `model_model_load` | Operação/referência de modelo (model_load) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.initialize_from_trained_model_folder` | 129–129 | `model_model_load` | Operação/referência de modelo (model_load) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.initialize_from_trained_model_folder` | 143–143 | `model_model_save` | Operação/referência de modelo (model_save) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.predict_logits_from_preprocessed_data` | 275–275 | `model_model_load` | Operação/referência de modelo (model_load) em 'FlarePredictor.predict_logits_from_preprocessed_data' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.predict_logits_from_preprocessed_data` | 277–277 | `model_model_load` | Operação/referência de modelo (model_load) em 'FlarePredictor.predict_logits_from_preprocessed_data' |
| `documentation/competitions/Toothfairy2/inference_script_semseg_only_customInf2.py` | `CustomPredictor.initialize_from_trained_model_folder` | 75–76 | `model_model_load` | Operação/referência de modelo (model_load) em 'CustomPredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/Toothfairy2/inference_script_semseg_only_customInf2.py` | `CustomPredictor.predict_preprocessed_image` | 164–164 | `model_model_load` | Operação/referência de modelo (model_load) em 'CustomPredictor.predict_preprocessed_image' |
| `documentation/competitions/Toothfairy2/inference_script_semseg_only_customInf2.py` | `CustomPredictor.predict_preprocessed_image` | 164–164 | `model_model_load` | Operação/referência de modelo (model_load) em 'CustomPredictor.predict_preprocessed_image' |
| `nnunetv2/evaluation/find_best_configuration.py` | `find_best_configuration` | 173–173 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'find_best_configuration' |
| `nnunetv2/experiment_planning/like_nnssl.py` | `preprocess_like_nnssl` | 148–148 | `model_model_load` | Operação/referência de modelo (model_load) em 'preprocess_like_nnssl' |
| `nnunetv2/experiment_planning/like_nnssl.py` | `plan_like_dynamic` | 422–422 | `model_model_load` | Operação/referência de modelo (model_load) em 'plan_like_dynamic' |
| `nnunetv2/inference/JHU_inference.py` | N/A | 176–180 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `nnunetv2/inference/predict_from_raw_data.py` | `nnUNetPredictor.initialize_from_trained_model_folder` | 136–136 | `model_model_load` | Operação/referência de modelo (model_load) em 'nnUNetPredictor.initialize_from_trained_model_folder' |
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
- **Descrição:** Evidência parcial: sinais estruturais de treinamento e de inferência coexistem no(s) mesmo(s) arquivo(s) (documentation/competitions/FLARE24/Task_1/inference_flare_task1.py, documentation/competitions/FLARE24/Task_2/inference_flare_task2.py, documentation/competitions/Toothfairy2/inference_script_semseg_only_customInf2.py, nnunetv2/evaluation/find_best_configuration.py, nnunetv2/inference/predict_from_raw_data.py, nnunetv2/tests/test_checkpoints.py, nnunetv2/tests/test_pretrained_trainers.py, nnunetv2/training/dataloading/data_loader.py, nnunetv2/training/nnUNetTrainer/nnUNetTrainer.py, nnunetv2/training/nnUNetTrainer/variants/benchmarking/nnUNetTrainerBenchmark_5epochs_noDataLoading.py). Indicador técnico que merece investigação quanto à segregação arquitetural entre desenvolvimento/treino e produção/inferência.
- **Justificativa de Rastreabilidade:** Coexistência de sinais de treinamento e inferência em documentation/competitions/FLARE24/Task_1/inference_flare_task1.py, documentation/competitions/FLARE24/Task_2/inference_flare_task2.py, documentation/competitions/Toothfairy2/inference_script_semseg_only_customInf2.py, nnunetv2/evaluation/find_best_configuration.py, nnunetv2/inference/predict_from_raw_data.py, nnunetv2/tests/test_checkpoints.py, nnunetv2/tests/test_pretrained_trainers.py, nnunetv2/training/dataloading/data_loader.py, nnunetv2/training/nnUNetTrainer/nnUNetTrainer.py, nnunetv2/training/nnUNetTrainer/variants/benchmarking/nnUNetTrainerBenchmark_5epochs_noDataLoading.py. Requer inspeção humana do fluxo de controle para verificar se o modelo é congelado em produção.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `FlarePredictor.initialize_from_trained_model_folder` | 28–101 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `convert_predicted_logits_to_segmentation_with_correct_shape` | 104–144 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'convert_predicted_logits_to_segmentation_with_correct_shape' |
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `export_prediction_from_logits` | 147–167 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'export_prediction_from_logits' |
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `predict_flare` | 170–198 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'predict_flare' |
| `documentation/competitions/FLARE24/Task_1/inference_flare_task1.py` | `predict_flare` | 183–183 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'predict_flare' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.initialize_from_trained_model_folder` | 53–147 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.initialize_from_trained_model_folder` | 130–130 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'FlarePredictor.initialize_from_trained_model_folder' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.predict_from_files` | 149–177 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'FlarePredictor.predict_from_files' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor._internal_maybe_mirror_and_predict` | 179–201 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'FlarePredictor._internal_maybe_mirror_and_predict' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor._internal_predict_sliding_window_return_logits` | 203–258 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'FlarePredictor._internal_predict_sliding_window_return_logits' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.predict_logits_from_preprocessed_data` | 260–298 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'FlarePredictor.predict_logits_from_preprocessed_data' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.predict_sliding_window_return_logits` | 301–348 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'FlarePredictor.predict_sliding_window_return_logits' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.predict_sliding_window_return_logits` | 306–306 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'FlarePredictor.predict_sliding_window_return_logits' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.predict_sliding_window_return_logits` | 300–300 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'FlarePredictor.predict_sliding_window_return_logits' |
| `documentation/competitions/FLARE24/Task_2/inference_flare_task2.py` | `FlarePredictor.convert_predicted_logits_to_segmentation_with_correct_shape` | 350–383 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'FlarePredictor.convert_predicted_logits_to_segmentation_with_correct_shape' |
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
