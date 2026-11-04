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

- **Nome do Projeto:** TEST-010_SciKit-Surgery__scikit-surgeryimage
- **Commit SHA Analisado:** `543f639bb420ce87212f5016e12221cd090cc0d3`
- **Data e Horário da Execução (UTC):** `2026-11-04T22:16:11.766880+00:00`
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

- **Quantidade total de arquivos encontrados:** 358
- **Quantidade de arquivos Python (`.py`):** 60
- **Arquivos Python analisados com sucesso:** 60
- **Arquivos Python que falharam na análise:** 0
- **Percentual de cobertura da inspeção sintática:** 100.0%

*Nenhum arquivo Python falhou durante o parsing sintático AST.*

## C. Visão Geral dos Indicadores Técnicos

| Estado do Indicador | Expressão Padronizada | Quantidade |
|---|---|---|
| `observed` | Evidência identificada | 4 |
| `partial` | Evidência parcial — indicador técnico que merece investigação | 2 |
| `not_observed` | Evidência não identificada no repositório analisado | 2 |
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
- **Descrição:** Evidência identificada: todos os 60 arquivos Python encontrados foram analisados com sucesso via AST (cobertura de inspeção: 100.0%).
- **Justificativa de Rastreabilidade:** Inspeção concluída sem falhas de parsing em 60/60 arquivos Python.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `setup.py` | `<module>` | 1–64 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 083a80f83667...) |
| `sksurgeryimage.py` | `<module>` | 1–6 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: a47fa64e911c...) |
| `versioneer.py` | `<module>` | 1–2277 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 3ec63afc75b5...) |
| `docs/conf.py` | `<module>` | 1–254 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: b33c9da6e76e...) |
| `examples/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `examples/acquire/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `examples/acquire/save_camera_feeds.py` | `<module>` | 1–43 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 3126f3803f21...) |
| `sksurgeryimage/__init__.py` | `<module>` | 1–6 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: f1ed9e2d2fec...) |
| `sksurgeryimage/_version.py` | `<module>` | 1–683 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 036caa641dc8...) |
| `sksurgeryimage/acquire/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `sksurgeryimage/acquire/stereo_video.py` | `<module>` | 1–328 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 94e07c13e652...) |
| `sksurgeryimage/acquire/video_source.py` | `<module>` | 1–219 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 2babd5f00128...) |
| `sksurgeryimage/acquire/video_writer.py` | `<module>` | 1–233 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: ed7d4a3104c6...) |
| `sksurgeryimage/calibration/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `sksurgeryimage/calibration/aruco_point_detector.py` | `<module>` | 1–105 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 6c06159c73a4...) |

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
- **Descrição:** Evidência parcial: manifesto(s) de dependências localizado(s) (requirements-dev.txt, requirements.txt), contendo 0 pacote(s) com versão fixada e 14 pacote(s) sem versão exata fixada. Imports externos não declarados no manifesto: cv2, cx_Freeze, py2exe, setuptools, sksurgerycore, tomli. Componentes de IA/ML: OpenCV.
- **Justificativa de Rastreabilidade:** A presença de dependências sem versão fixada ou imports omitidos não representa automaticamente uma não conformidade, mas é um indicador técnico que merece investigação para controle de SOUP.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `requirements-dev.txt` | `coverage` | 2–2 | `dependency_declaration` | Pacote 'coverage' declarado em 'requirements-dev.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `requirements-dev.txt` | `coveralls` | 3–3 | `dependency_declaration` | Pacote 'coveralls' declarado em 'requirements-dev.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `requirements-dev.txt` | `mock` | 4–4 | `dependency_declaration` | Pacote 'mock' declarado em 'requirements-dev.txt' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `requirements-dev.txt` | `pyfakefs` | 5–5 | `dependency_declaration` | Pacote 'pyfakefs' declarado em 'requirements-dev.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `requirements-dev.txt` | `parameterized` | 6–6 | `dependency_declaration` | Pacote 'parameterized' declarado em 'requirements-dev.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `requirements-dev.txt` | `pylint` | 7–7 | `dependency_declaration` | Pacote 'pylint' declarado em 'requirements-dev.txt' (especificador: '<3.1.0', fixado: False, importado no código: False) |
| `requirements-dev.txt` | `sphinx` | 8–8 | `dependency_declaration` | Pacote 'sphinx' declarado em 'requirements-dev.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `requirements-dev.txt` | `sphinx_rtd_theme` | 9–9 | `dependency_declaration` | Pacote 'sphinx_rtd_theme' declarado em 'requirements-dev.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `requirements-dev.txt` | `pyinstaller` | 10–10 | `dependency_declaration` | Pacote 'pyinstaller' declarado em 'requirements-dev.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `requirements-dev.txt` | `pytest` | 11–11 | `dependency_declaration` | Pacote 'pytest' declarado em 'requirements-dev.txt' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `requirements-dev.txt` | `tox` | 12–12 | `dependency_declaration` | Pacote 'tox' declarado em 'requirements-dev.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `requirements.txt` | `numpy` | 1–1 | `dependency_declaration` | Pacote 'numpy' declarado em 'requirements.txt' (especificador: '>=2.0.0', fixado: False, importado no código: True) |
| `requirements.txt` | `opencv-contrib-python-headless` | 2–2 | `dependency_declaration` | Pacote 'opencv-contrib-python-headless' declarado em 'requirements.txt' (especificador: '>=4.10.0.84,<4.13.0.90', fixado: False, importado no código: False) |
| `requirements.txt` | `scikit-surgerycore` | 3–3 | `dependency_declaration` | Pacote 'scikit-surgerycore' declarado em 'requirements.txt' (especificador: '>=0.1.0', fixado: False, importado no código: False) |
| `setup.py` | `setuptools` | 1–1 | `undeclared_import` | Módulo externo 'setuptools' importado em 'setup.py', mas não localizado nos manifestos de dependências inspecionados. |
*... e mais 43 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência identificada: 31 arquivo(s) de teste localizado(s) (diretórios: tests; frameworks: pytest; 234 função(ões)/método(s) de teste).
- **Justificativa de Rastreabilidade:** Módulos e funções de teste automatizado foram observados no repositório.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `tests/__init__.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/__init__.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/conftest.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/conftest.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/test_requirements.py` | `test_requirements_vs_setup` | 7–51 | `test_module` | Módulo de teste 'tests/test_requirements.py' identificado (1 funções/métodos candidatos de teste). |
| `tests/acquire/test_integration.py` | `test_save_a_file_and_all_cameras` | 17–82 | `test_module` | Módulo de teste 'tests/acquire/test_integration.py' identificado (2 funções/métodos candidatos de teste). |
| `tests/acquire/stereo_video/conftest.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/acquire/stereo_video/conftest.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/acquire/stereo_video/test_stereo_video.py` | `test_create_video_from_png` | 10–17 | `test_module` | Módulo de teste 'tests/acquire/stereo_video/test_stereo_video.py' identificado (42 funções/métodos candidatos de teste). |
| `tests/acquire/video_source/conftest.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/acquire/video_source/conftest.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/acquire/video_source/test_video_source.py` | `test_validate_camera_input` | 8–16 | `test_module` | Módulo de teste 'tests/acquire/video_source/test_video_source.py' identificado (13 funções/métodos candidatos de teste). |
| `tests/acquire/video_writer/conftest.py` | `DummyFrameSource.__init__` | 11–12 | `test_module` | Módulo de teste 'tests/acquire/video_writer/conftest.py' identificado (4 funções/métodos candidatos de teste). |
| `tests/acquire/video_writer/test_video_writer.py` | `test_videowriter_invalid_filename_raises_error` | 14–18 | `test_module` | Módulo de teste 'tests/acquire/video_writer/test_video_writer.py' identificado (5 funções/métodos candidatos de teste). |
| `tests/calibration/test_aruco_point_detector.py` | `test_init_no_dictionary` | 31–34 | `test_module` | Módulo de teste 'tests/calibration/test_aruco_point_detector.py' identificado (7 funções/métodos candidatos de teste). |
| `tests/calibration/test_charuco.py` | `test_extract_points` | 12–31 | `test_module` | Módulo de teste 'tests/calibration/test_charuco.py' identificado (3 funções/métodos candidatos de teste). |
| `tests/calibration/test_charuco_plus_chessboard_point_detector.py` | `test_charuco_plus_chessboard_tutorial_stuff` | 38–69 | `test_module` | Módulo de teste 'tests/calibration/test_charuco_plus_chessboard_point_detector.py' identificado (12 funções/métodos candidatos de teste). |
| `tests/calibration/test_charuco_point_detector.py` | `test_charuco_detector` | 13–45 | `test_module` | Módulo de teste 'tests/calibration/test_charuco_point_detector.py' identificado (6 funções/métodos candidatos de teste). |
| `tests/calibration/test_chessboard_point_detector.py` | `test_chessboard_detector` | 13–47 | `test_module` | Módulo de teste 'tests/calibration/test_chessboard_point_detector.py' identificado (6 funções/métodos candidatos de teste). |
*... e mais 19 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência identificada: 1 configuração(ões) de CI/CD localizada(s) com comandos declarados para execução automatizada de testes (evidências de cobertura: .coveragerc, .github/workflows/ci.yml:33, .github/workflows/ci.yml:42).
- **Justificativa de Rastreabilidade:** Arquivos de workflow CI/CD contendo etapas de execução de testes foram encontrados.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `.github/workflows/ci.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/ci.yml' (comandos de teste: coverage run -a --source ./sksurgeryimage -m pytest, coverage run -a --source ./sksurgeryimage -m pytest -v -s ./tests/; cobertura: True) |

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
- **Descrição:** Evidência parcial: entre 111 operação(ões) candidatas de I/O, 5 possuem bloco try-except não vazio e 106 não possuem tratamento local observável. Foram identificados 12 bloco(s) except vazios ou com 'pass'.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: coexistem operações de I/O sem captura local de exceção ou blocos except que suprimem falhas com pass.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `setup.py` | N/A | 10–10 | `ast_io_operation` | Operação candidata de I/O 'open' em '<module>' (dentro de try-except não vazio: False) |
| `versioneer.py` | `get_config_from_root` | 406–406 | `ast_io_operation` | Operação candidata de I/O 'open' em 'get_config_from_root' (dentro de try-except não vazio: True) |
| `versioneer.py` | `get_config_from_root` | 407–407 | `ast_io_operation` | Operação candidata de I/O 'tomllib.load' em 'get_config_from_root' (dentro de try-except não vazio: True) |
| `versioneer.py` | `get_config_from_root` | 414–414 | `ast_io_operation` | Operação candidata de I/O 'open' em 'get_config_from_root' (dentro de try-except não vazio: False) |
| `versioneer.py` | `git_get_keywords` | 1203–1203 | `ast_io_operation` | Operação candidata de I/O 'open' em 'git_get_keywords' (dentro de try-except não vazio: False) |
| `versioneer.py` | `do_vcs_install` | 1451–1451 | `ast_io_operation` | Operação candidata de I/O 'open' em 'do_vcs_install' (dentro de try-except não vazio: False) |
| `versioneer.py` | `do_vcs_install` | 1460–1460 | `ast_io_operation` | Operação candidata de I/O 'open' em 'do_vcs_install' (dentro de try-except não vazio: False) |
| `versioneer.py` | `versions_from_file` | 1515–1515 | `ast_io_operation` | Operação candidata de I/O 'open' em 'versions_from_file' (dentro de try-except não vazio: True) |
| `versioneer.py` | `versions_from_file` | 1526–1526 | `ast_io_operation` | Operação candidata de I/O 'json.loads' em 'versions_from_file' (dentro de try-except não vazio: False) |
| `versioneer.py` | `write_to_version_file` | 1531–1532 | `ast_io_operation` | Operação candidata de I/O 'json.dumps' em 'write_to_version_file' (dentro de try-except não vazio: False) |
| `versioneer.py` | `write_to_version_file` | 1533–1533 | `ast_io_operation` | Operação candidata de I/O 'open' em 'write_to_version_file' (dentro de try-except não vazio: False) |
| `versioneer.py` | `get_cmdclass.cmd_build_exe.run` | 2016–2016 | `ast_io_operation` | Operação candidata de I/O 'open' em 'get_cmdclass.cmd_build_exe.run' (dentro de try-except não vazio: False) |
| `versioneer.py` | `get_cmdclass.cmd_py2exe.run` | 2045–2045 | `ast_io_operation` | Operação candidata de I/O 'open' em 'get_cmdclass.cmd_py2exe.run' (dentro de try-except não vazio: False) |
| `versioneer.py` | `get_cmdclass.cmd_egg_info.find_sources` | 2088–2088 | `ast_io_operation` | Operação candidata de I/O 'open' em 'get_cmdclass.cmd_egg_info.find_sources' (dentro de try-except não vazio: False) |
| `versioneer.py` | `do_setup` | 2183–2183 | `ast_io_operation` | Operação candidata de I/O 'open' em 'do_setup' (dentro de try-except não vazio: True) |
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
- **Descrição:** Evidência identificada: 519 sinal(is) estrutural(is) de validação de entrada localizado(s), incluindo 37 função(ões)/chamada(s) de validação e 85 guarda(s) condicional(is) com levantamento de exceção.
- **Justificativa de Rastreabilidade:** Foram identificados mecanismos explícitos de verificação de entrada no código. A presença estrutural não garante suficiência clínica ou completude da validação.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `versioneer.py` | `get_root` | 365–375 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'get_root' |
| `versioneer.py` | `get_config_from_root` | 430–431 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'get_config_from_root' |
| `versioneer.py` | `get_config_from_root` | 433–437 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'get_config_from_root' |
| `versioneer.py` | `get_config_from_root` | 433–433 | `validation_validation_call` | Sinal de validação (validation_call) em 'get_config_from_root' |
| `versioneer.py` | `run_command` | 469–469 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'run_command' |
| `versioneer.py` | `run_command` | 469–469 | `validation_validation_call` | Sinal de validação (validation_call) em 'run_command' |
| `versioneer.py` | `git_versions_from_keywords` | 1229–1230 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'git_versions_from_keywords' |
| `versioneer.py` | `git_versions_from_keywords` | 1232–1243 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'git_versions_from_keywords' |
| `versioneer.py` | `git_versions_from_keywords` | 1245–1248 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'git_versions_from_keywords' |
| `versioneer.py` | `git_pieces_from_vcs` | 1316–1319 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'git_pieces_from_vcs' |
| `versioneer.py` | `git_pieces_from_vcs` | 1328–1329 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'git_pieces_from_vcs' |
| `versioneer.py` | `git_pieces_from_vcs` | 1332–1333 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'git_pieces_from_vcs' |
| `versioneer.py` | `git_pieces_from_vcs` | 1344–1345 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'git_pieces_from_vcs' |
| `versioneer.py` | `git_pieces_from_vcs` | 1354–1355 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'git_pieces_from_vcs' |
| `versioneer.py` | `versions_from_file` | 1524–1525 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'versions_from_file' |
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
- **Status:** `not_observed` (Evidência não identificada no repositório analisado)
- **Prioridade de Revisão Técnica:** `medium` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência não identificada no repositório analisado: não foram localizadas chamadas explícitas de carregamento/salvamento de artefatos de modelos nem arquivos de checkpoint no escopo inspecionado.
- **Justificativa de Rastreabilidade:** Nenhum ponto observável de persistência ou carregamento de pesos de modelo foi encontrado na AST.

#### Evidências Extraídas (Arquivos e Linhas)
*Nenhuma evidência positiva localizada no código; ver justificativa acima.*

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
Caso o software utilize modelos de IA/ML, identificar onde os artefatos de modelo são armazenados, carregados e versionados.

### TA-008 (R08) — Sinais estruturais de separação entre treinamento e inferência
- **Categoria:** Arquitetura e Isolamento de Ambientes (IA/ML)
- **Status:** `not_observed` (Evidência não identificada no repositório analisado)
- **Prioridade de Revisão Técnica:** `medium` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `medium`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência não identificada no repositório analisado: não foram detectados sinais estruturais explícitos de rotinas de treinamento nem de inferência nos arquivos Python inspecionados.
- **Justificativa de Rastreabilidade:** Nenhuma função ou chamada típica de treinamento/inferência foi localizada pela AST.

#### Evidências Extraídas (Arquivos e Linhas)
*Nenhuma evidência positiva localizada no código; ver justificativa acima.*

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
Revisar manualmente os pontos de entrada do algoritmo e a arquitetura do software.

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

### Prioridade de Revisão Média (`medium`)
1. **TA-002 (R02 — Gerenciamento de dependências e componentes externos (SOUP))** [Evidência parcial — indicador técnico que merece investigação]: Avaliar o congelamento de versões (pinning/lockfile), reconciliar bibliotecas importadas no código com o manifesto e manter a matriz de rastreabilidade de SOUP atualizada.
1. **TA-006 (R06 — Sinais estruturais de validação de entradas)** [Evidência identificada]: Revisão humana necessária para verificar se os critérios de validação cobrem formatos inválidos, valores ausentes, limites fisiológicos/dimensionais e proteção contra entradas malformadas.
1. **TA-007 (R07 — Proveniência, carregamento e versionamento de artefatos de modelos)** [Evidência não identificada no repositório analisado]: Caso o software utilize modelos de IA/ML, identificar onde os artefatos de modelo são armazenados, carregados e versionados.
1. **TA-008 (R08 — Sinais estruturais de separação entre treinamento e inferência)** [Evidência não identificada no repositório analisado]: Revisar manualmente os pontos de entrada do algoritmo e a arquitetura do software.

### Prioridade de Revisão Baixa (`low`)
1. **TA-003 (R03 — Evidências de testes automatizados no repositório)** [Evidência identificada]: Revisão humana necessária para verificar a rastreabilidade entre os casos de teste automatizados, os requisitos de software e os controles de risco (IEC 62304 Seções 5.5, 5.6 e 5.7).
1. **TA-004 (R04 — Integração contínua (CI/CD) e automação de verificação)** [Evidência identificada]: Verificar se os registros de execução do CI/CD são arquivados como evidência de verificação e regressão a cada versão liberada (IEC 62304 Seção 5.6.6 e 5.8).

### Informativo (`informational`)
1. **TA-001 (R01 — Cobertura e integridade da inspeção estática)** [Evidência identificada]: Manter a verificação sintática íntegra no fluxo de desenvolvimento.
