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

- **Nome do Projeto:** TEST-003_fepegar__torchio
- **Commit SHA Analisado:** `9b1be95027567b8587b05f48c22122b1dcac6cc0`
- **Data e Horário da Execução (UTC):** `2026-11-04T22:14:41.287721+00:00`
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

- **Quantidade total de arquivos encontrados:** 340
- **Quantidade de arquivos Python (`.py`):** 166
- **Arquivos Python analisados com sucesso:** 166
- **Arquivos Python que falharam na análise:** 0
- **Percentual de cobertura da inspeção sintática:** 100.0%

*Nenhum arquivo Python falhou durante o parsing sintático AST.*

## C. Visão Geral dos Indicadores Técnicos

| Estado do Indicador | Expressão Padronizada | Quantidade |
|---|---|---|
| `observed` | Evidência identificada | 5 |
| `partial` | Evidência parcial — indicador técnico que merece investigação | 3 |
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
- **Descrição:** Evidência identificada: todos os 166 arquivos Python encontrados foram analisados com sucesso via AST (cobertura de inspeção: 100.0%).
- **Justificativa de Rastreabilidade:** Inspeção concluída sem falhas de parsing em 166/166 arquivos Python.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `print_system.py` | `<module>` | 1–18 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: b68f38967beb...) |
| `docs/gallery.py` | `<module>` | 1–439 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: ed50eced8afe...) |
| `docs/plot_directive.py` | `<module>` | 1–102 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 5335b5b5bff4...) |
| `docs/examples/plot_3d_to_2d.py` | `<module>` | 1–65 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 484280ebd53b...) |
| `docs/examples/plot_colin27.py` | `<module>` | 1–10 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 7d170d4905ff...) |
| `docs/examples/plot_custom_z_spacing.py` | `<module>` | 1–35 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 434ccb99848c...) |
| `docs/examples/plot_history.py` | `<module>` | 1–65 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: d8fad25f97b5...) |
| `docs/examples/plot_include_exclude.py` | `<module>` | 1–24 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 3a002afa1ef8...) |
| `docs/examples/plot_video.py` | `<module>` | 1–69 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 13c56b1bb8d1...) |
| `src/torchio/__init__.py` | `<module>` | 1–193 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e43e5fe9f786...) |
| `src/torchio/cli.py` | `<module>` | 1–268 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 8d53d4020a98...) |
| `src/torchio/download.py` | `<module>` | 1–200 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 906ece9e76b3...) |
| `src/torchio/io.py` | `<module>` | 1–119 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 235c26b917c8...) |
| `src/torchio/loader.py` | `<module>` | 1–95 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 41150f6a4c77...) |
| `src/torchio/logging.py` | `<module>` | 1–42 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: f09f9bc47ec2...) |

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
- **Descrição:** Evidência parcial: manifesto(s) de dependências localizado(s) (pyproject.toml), contendo 0 pacote(s) com versão fixada e 14 pacote(s) sem versão exata fixada. Imports externos não declarados no manifesto: IPython, PIL, affine, aggregator, axes, backends, batch, bboxes, colin, compose, cornucopia, cornucopia_adapter, crop, crop_or_pad, data, download, external, fpg, icbm, image, intensity, interpol, invertible, itk_snap, ixi, label, lambda_transform, loader, matplotlib, medmnist, mni, monai, monai_adapter, niizarr, pad, parameter_range, patch, pediatric, points, pytest, repr_html, sampler, sheep, slicer, spatial, subject, to, torchio, transform, transforms, visualization, zarr, zone_plate. Componentes de IA/ML: MONAI (Medical Open Network for AI), NiBabel, PyTorch, SimpleITK.
- **Justificativa de Rastreabilidade:** A presença de dependências sem versão fixada ou imports omitidos não representa automaticamente uma não conformidade, mas é um indicador técnico que merece investigação para controle de SOUP.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `pyproject.toml` | `einops` | 1–1 | `dependency_declaration` | Pacote 'einops' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `fsspec` | 1–1 | `dependency_declaration` | Pacote 'fsspec' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `humanize` | 1–1 | `dependency_declaration` | Pacote 'humanize' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `jaxtyping` | 1–1 | `dependency_declaration` | Pacote 'jaxtyping' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `loguru` | 1–1 | `dependency_declaration` | Pacote 'loguru' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `nibabel` | 1–1 | `dependency_declaration` | Pacote 'nibabel' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `numpy` | 1–1 | `dependency_declaration` | Pacote 'numpy' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `platformdirs` | 1–1 | `dependency_declaration` | Pacote 'platformdirs' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `rich` | 1–1 | `dependency_declaration` | Pacote 'rich' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `simpleitk` | 1–1 | `dependency_declaration` | Pacote 'simpleitk' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `torch` | 1–1 | `dependency_declaration` | Pacote 'torch' declarado em 'pyproject.toml' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `pyproject.toml` | `torch-interpol` | 1–1 | `dependency_declaration` | Pacote 'torch-interpol' declarado em 'pyproject.toml' (especificador: '>=0.3.0', fixado: False, importado no código: False) |
| `pyproject.toml` | `typing_extensions` | 1–1 | `dependency_declaration` | Pacote 'typing_extensions' declarado em 'pyproject.toml' (especificador: '>=4.15.0', fixado: False, importado no código: True) |
| `pyproject.toml` | `tyro` | 1–1 | `dependency_declaration` | Pacote 'tyro' declarado em 'pyproject.toml' (especificador: '>=1.0.15', fixado: False, importado no código: True) |
| `print_system.py` | `torchio` | 1–1 | `undeclared_import` | Módulo externo 'torchio' importado em 'print_system.py', mas não localizado nos manifestos de dependências inspecionados. |
*... e mais 341 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência identificada: 69 arquivo(s) de teste localizado(s) (diretórios: tests; frameworks: pytest, unittest; 1377 função(ões)/método(s) de teste).
- **Justificativa de Rastreabilidade:** Módulos e funções de teste automatizado foram observados no repositório.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `tests/__init__.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/__init__.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/conftest.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/conftest.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/test_affine.py` | `TestAffineCreation.test_identity` | 12–14 | `test_module` | Módulo de teste 'tests/test_affine.py' identificado (45 funções/métodos candidatos de teste). |
| `tests/test_anisotropy.py` | `TestAnisotropy.test_changes_data` | 23–27 | `test_module` | Módulo de teste 'tests/test_anisotropy.py' identificado (10 funções/métodos candidatos de teste). |
| `tests/test_axes.py` | `TestValidateAxes.test_all_voxel_permutations_valid` | 25–26 | `test_module` | Módulo de teste 'tests/test_axes.py' identificado (27 funções/métodos candidatos de teste). |
| `tests/test_backends.py` | `TestNibabelBackend.nifti_path` | 19–24 | `test_module` | Módulo de teste 'tests/test_backends.py' identificado (66 funções/métodos candidatos de teste). |
| `tests/test_batch.py` | `TestImagesBatch.test_from_images` | 14–17 | `test_module` | Módulo de teste 'tests/test_batch.py' identificado (32 funções/métodos candidatos de teste). |
| `tests/test_bboxes.py` | `TestBoundingBoxFormat.test_ijk_corners` | 19–22 | `test_module` | Módulo de teste 'tests/test_bboxes.py' identificado (48 funções/métodos candidatos de teste). |
| `tests/test_bias_field.py` | `TestBasic.test_changes_data` | 21–25 | `test_module` | Módulo de teste 'tests/test_bias_field.py' identificado (16 funções/métodos candidatos de teste). |
| `tests/test_blur.py` | `TestBlur.test_changes_data` | 22–26 | `test_module` | Módulo de teste 'tests/test_blur.py' identificado (9 funções/métodos candidatos de teste). |
| `tests/test_clamp.py` | `TestClamp.test_clamps_values` | 23–28 | `test_module` | Módulo de teste 'tests/test_clamp.py' identificado (3 funções/métodos candidatos de teste). |
| `tests/test_cli.py` | `TestInfo.test_prints_metadata` | 36–45 | `test_module` | Módulo de teste 'tests/test_cli.py' identificado (13 funções/métodos candidatos de teste). |
| `tests/test_compose.py` | `TestCompose.test_identity_compose` | 18–22 | `test_module` | Módulo de teste 'tests/test_compose.py' identificado (8 funções/métodos candidatos de teste). |
| `tests/test_contour.py` | `TestContour.test_basic_contour` | 22–26 | `test_module` | Módulo de teste 'tests/test_contour.py' identificado (4 funções/métodos candidatos de teste). |
| `tests/test_copy_affine.py` | `TestCopyAffine.test_copies_affine` | 23–32 | `test_module` | Módulo de teste 'tests/test_copy_affine.py' identificado (3 funções/métodos candidatos de teste). |
*... e mais 55 evidência(s) registrada(s) em `findings.json`.*

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
| `.github/workflows/check_pull_request_title.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/check_pull_request_title.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/code_quality.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/code_quality.yml' (comandos de teste: name: tox env ${{ matrix.tox_env }}, tox_env:, - name: Run check for tox env "${{ matrix.tox_env }}", run: uv run --locked --only-group dev tox -e ${{ matrix.tox_env }}; cobertura: False) |
| `.github/workflows/docs.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/docs.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/publish.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/publish.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/tests.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/tests.yml' (comandos de teste: pytest:, run: uv run --locked --only-group dev tox run -v --notest --skip-missing-interpreters false -e test, - name: Run pytest, uv run --locked --only-group dev tox -e test, uv run --locked --only-group dev tox -e test -- -m "not slow", run: uv run --locked --only-group dev tox -e docs-test; cobertura: False) |

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
- **Descrição:** Evidência parcial: entre 63 operação(ões) candidatas de I/O, 5 possuem bloco try-except não vazio e 58 não possuem tratamento local observável. Foram identificados 0 bloco(s) except vazios ou com 'pass'.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: coexistem operações de I/O sem captura local de exceção ou blocos except que suprimem falhas com pass.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `docs/gallery.py` | `_execute_example` | 168–168 | `ast_io_operation` | Operação candidata de I/O 'script_path.read_text' em '_execute_example' (dentro de try-except não vazio: False) |
| `docs/gallery.py` | `_make_thumbnail` | 364–364 | `ast_io_operation` | Operação candidata de I/O 'PILImage.open' em '_make_thumbnail' (dentro de try-except não vazio: True) |
| `docs/gallery.py` | `_load_cached_example` | 383–383 | `ast_io_operation` | Operação candidata de I/O 'md_path.read_text' em '_load_cached_example' (dentro de try-except não vazio: False) |
| `docs/gallery.py` | `_load_cached_example` | 386–386 | `ast_io_operation` | Operação candidata de I/O 'script.read_text' em '_load_cached_example' (dentro de try-except não vazio: False) |
| `docs/gallery.py` | `_process_script` | 400–400 | `ast_io_operation` | Operação candidata de I/O 'script.read_bytes' em '_process_script' (dentro de try-except não vazio: False) |
| `docs/gallery.py` | `_process_script` | 411–411 | `ast_io_operation` | Operação candidata de I/O 'md_path.write_text' em '_process_script' (dentro de try-except não vazio: False) |
| `docs/gallery.py` | `main` | 434–434 | `ast_io_operation` | Operação candidata de I/O 'index_path.write_text' em 'main' (dentro de try-except não vazio: False) |
| `docs/plot_directive.py` | `process_file` | 37–37 | `ast_io_operation` | Operação candidata de I/O 'md_path.read_text' em 'process_file' (dentro de try-except não vazio: False) |
| `docs/plot_directive.py` | `process_file` | 86–86 | `ast_io_operation` | Operação candidata de I/O 'md_path.write_text' em 'process_file' (dentro de try-except não vazio: False) |
| `docs/examples/plot_video.py` | `read_clip` | 22–22 | `ast_io_operation` | Operação candidata de I/O 'Image.open' em 'read_clip' (dentro de try-except não vazio: False) |
| `src/torchio/download.py` | `calculate_md5` | 33–33 | `ast_io_operation` | Operação candidata de I/O 'open' em 'calculate_md5' (dentro de try-except não vazio: False) |
| `src/torchio/download.py` | `extract_archive` | 129–129 | `ast_io_operation` | Operação candidata de I/O 'tarfile.open' em 'extract_archive' (dentro de try-except não vazio: False) |
| `src/torchio/download.py` | `extract_archive` | 132–132 | `ast_io_operation` | Operação candidata de I/O 'tarfile.open' em 'extract_archive' (dentro de try-except não vazio: False) |
| `src/torchio/download.py` | `extract_archive` | 135–135 | `ast_io_operation` | Operação candidata de I/O 'tarfile.open' em 'extract_archive' (dentro de try-except não vazio: False) |
| `src/torchio/download.py` | `extract_archive` | 140–140 | `ast_io_operation` | Operação candidata de I/O 'open' em 'extract_archive' (dentro de try-except não vazio: False) |
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
- **Descrição:** Evidência identificada: 2187 sinal(is) estrutural(is) de validação de entrada localizado(s), incluindo 349 função(ões)/chamada(s) de validação e 134 guarda(s) condicional(is) com levantamento de exceção.
- **Justificativa de Rastreabilidade:** Foram identificados mecanismos explícitos de verificação de entrada no código. A presença estrutural não garante suficiência clínica ou completude da validação.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `docs/gallery.py` | `_execute_example` | 218–233 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em '_execute_example' |
| `docs/gallery.py` | `_execute_example` | 218–218 | `validation_validation_call` | Sinal de validação (validation_call) em '_execute_example' |
| `docs/gallery.py` | `_process_script` | 404–405 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em '_process_script' |
| `src/torchio/cli.py` | `Clean.run` | 188–200 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'Clean.run' |
| `src/torchio/cli.py` | `main` | 260–262 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'main' |
| `src/torchio/download.py` | `check_integrity` | 39–45 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'check_integrity' |
| `src/torchio/download.py` | `check_integrity` | 43–44 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'check_integrity' |
| `src/torchio/download.py` | `download_url` | 107–109 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'download_url' |
| `src/torchio/download.py` | `extract_archive` | 125–126 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'extract_archive' |
| `src/torchio/download.py` | `download_and_extract_archive` | 173–174 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'download_and_extract_archive' |
| `src/torchio/download.py` | `compress` | 196–197 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'compress' |
| `src/torchio/io.py` | `_to_itk_convention` | 68–69 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em '_to_itk_convention' |
| `src/torchio/io.py` | `_to_itk_convention` | 68–68 | `validation_validation_call` | Sinal de validação (validation_call) em '_to_itk_convention' |
| `src/torchio/io.py` | `_write_niftyreg_matrix` | 116–117 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em '_write_niftyreg_matrix' |
| `src/torchio/io.py` | `_write_niftyreg_matrix` | 116–116 | `validation_validation_call` | Sinal de validação (validation_call) em '_write_niftyreg_matrix' |
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
- **Descrição:** Evidência parcial: foram identificados 3 sinal(is) de carregamento, salvamento ou referência a checkpoints de modelos (0 arquivo(s) de modelo no repositório). A existência de chamadas de carga ou arquivos .pt/.pth/.onnx não comprova proveniência completa nem controle de versão do modelo.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: artefatos de modelo exigem rastreabilidade documental de versão, dataset de treinamento, hiperparâmetros e verificação de integridade (hash).

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `src/torchio/transforms/intensity/histogram_standardization.py` | `_load_landmarks` | 241–241 | `model_model_load` | Operação/referência de modelo (model_load) em '_load_landmarks' |
| `tests/test_histogram_standardization.py` | `TestHistogramStandardizationEdgeCases.test_load_landmarks_from_pt` | 120–120 | `model_model_save` | Operação/referência de modelo (model_save) em 'TestHistogramStandardizationEdgeCases.test_load_landmarks_from_pt' |
| `tests/test_histogram_standardization.py` | `TestHistogramStandardizationEdgeCases.test_pt_with_wrong_type_raises` | 133–133 | `model_model_save` | Operação/referência de modelo (model_save) em 'TestHistogramStandardizationEdgeCases.test_pt_with_wrong_type_raises' |

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
- **Status:** `observed` (Evidência identificada)
- **Prioridade de Revisão Técnica:** `low` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `medium`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência identificada: sinais estruturais de treinamento (3 arquivo(s): tests/test_flip.py, tests/test_noise.py, tests/test_pad.py) e de inferência (7 arquivo(s): src/torchio/data/image.py, src/torchio/transforms/compose.py, src/torchio/transforms/cornucopia_adapter.py, src/torchio/transforms/monai_adapter.py, src/torchio/transforms/transform.py, src/torchio/transforms/spatial/crop_or_pad.py, src/torchio/transforms/spatial/ensure_shape_multiple.py) encontram-se distribuídos em módulos distintos.
- **Justificativa de Rastreabilidade:** Não foi observado acoplamento no mesmo arquivo entre sinais de treinamento e inferência. Isso não prova isolamento de ambiente em produção sem análise do fluxo de execução.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `src/torchio/data/image.py` | `Image._infer_affine_without_loading` | 620–637 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'Image._infer_affine_without_loading' |
| `src/torchio/transforms/compose.py` | `Compose.forward` | 84–93 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'Compose.forward' |
| `src/torchio/transforms/compose.py` | `OneOf.forward` | 142–159 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'OneOf.forward' |
| `src/torchio/transforms/compose.py` | `SomeOf.forward` | 236–247 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'SomeOf.forward' |
| `src/torchio/transforms/cornucopia_adapter.py` | `CornucopiaAdapter.forward` | 66–80 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'CornucopiaAdapter.forward' |
| `src/torchio/transforms/monai_adapter.py` | `MonaiAdapter.forward` | 70–94 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'MonaiAdapter.forward' |
| `src/torchio/transforms/transform.py` | `Transform.forward` | 194–194 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'Transform.forward' |
| `src/torchio/transforms/transform.py` | `Transform.forward` | 196–196 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'Transform.forward' |
| `src/torchio/transforms/transform.py` | `Transform.forward` | 198–198 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'Transform.forward' |
| `src/torchio/transforms/transform.py` | `Transform.forward` | 200–200 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'Transform.forward' |
| `src/torchio/transforms/transform.py` | `Transform.forward` | 202–202 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'Transform.forward' |
| `src/torchio/transforms/transform.py` | `Transform.forward` | 204–204 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'Transform.forward' |
| `src/torchio/transforms/transform.py` | `Transform.forward` | 206–206 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'Transform.forward' |
| `src/torchio/transforms/transform.py` | `Transform.forward` | 208–208 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'Transform.forward' |
| `src/torchio/transforms/transform.py` | `Transform.forward` | 210–210 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'Transform.forward' |
*... e mais 6 evidência(s) registrada(s) em `findings.json`.*

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
Revisão humana necessária para confirmar que o pacote de implantação em produção não executa rotinas de treinamento ou atualização não controlada de pesos.

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

### Prioridade de Revisão Média (`medium`)
1. **TA-002 (R02 — Gerenciamento de dependências e componentes externos (SOUP))** [Evidência parcial — indicador técnico que merece investigação]: Avaliar o congelamento de versões (pinning/lockfile), reconciliar bibliotecas importadas no código com o manifesto e manter a matriz de rastreabilidade de SOUP atualizada.
1. **TA-006 (R06 — Sinais estruturais de validação de entradas)** [Evidência identificada]: Revisão humana necessária para verificar se os critérios de validação cobrem formatos inválidos, valores ausentes, limites fisiológicos/dimensionais e proteção contra entradas malformadas.

### Prioridade de Revisão Baixa (`low`)
1. **TA-003 (R03 — Evidências de testes automatizados no repositório)** [Evidência identificada]: Revisão humana necessária para verificar a rastreabilidade entre os casos de teste automatizados, os requisitos de software e os controles de risco (IEC 62304 Seções 5.5, 5.6 e 5.7).
1. **TA-004 (R04 — Integração contínua (CI/CD) e automação de verificação)** [Evidência identificada]: Verificar se os registros de execução do CI/CD são arquivados como evidência de verificação e regressão a cada versão liberada (IEC 62304 Seção 5.6.6 e 5.8).
1. **TA-008 (R08 — Sinais estruturais de separação entre treinamento e inferência)** [Evidência identificada]: Revisão humana necessária para confirmar que o pacote de implantação em produção não executa rotinas de treinamento ou atualização não controlada de pesos.

### Informativo (`informational`)
1. **TA-001 (R01 — Cobertura e integridade da inspeção estática)** [Evidência identificada]: Manter a verificação sintática íntegra no fluxo de desenvolvimento.
