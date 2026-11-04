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

- **Nome do Projeto:** TEST-018_ozan-oktay__Attention-Gated-Networks
- **Commit SHA Analisado:** `eee4881fdc31920efd873773e0b744df8dacbfb6`
- **Data e Horário da Execução (UTC):** `2026-11-04T22:17:00.456011+00:00`
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

- **Quantidade total de arquivos encontrados:** 60
- **Quantidade de arquivos Python (`.py`):** 49
- **Arquivos Python analisados com sucesso:** 49
- **Arquivos Python que falharam na análise:** 0
- **Percentual de cobertura da inspeção sintática:** 100.0%

*Nenhum arquivo Python falhou durante o parsing sintático AST.*

## C. Visão Geral dos Indicadores Técnicos

| Estado do Indicador | Expressão Padronizada | Quantidade |
|---|---|---|
| `observed` | Evidência identificada | 3 |
| `partial` | Evidência parcial — indicador técnico que merece investigação | 2 |
| `not_observed` | Evidência não identificada no repositório analisado | 3 |
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
- **Descrição:** Evidência identificada: todos os 49 arquivos Python encontrados foram analisados com sucesso via AST (cobertura de inspeção: 100.0%).
- **Justificativa de Rastreabilidade:** Inspeção concluída sem falhas de parsing em 49/49 arquivos Python.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `setup.py` | `<module>` | 1–33 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: aa34cf57295f...) |
| `test_classification.py` | `<module>` | 1–177 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 66e4c2f7265d...) |
| `train_classifaction.py` | `<module>` | 1–239 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: fbcee1f75914...) |
| `train_segmentation.py` | `<module>` | 1–107 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 8891e1a82110...) |
| `validation.py` | `<module>` | 1–89 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 1c6fd70b283e...) |
| `visualise_att_maps_epoch.py` | `<module>` | 1–92 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 1649fcf498bb...) |
| `visualise_attention.py` | `<module>` | 1–192 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: db3c5e587d6c...) |
| `visualise_fmaps.py` | `<module>` | 1–82 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: eb69bc0cef9b...) |
| `dataio/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `dataio/loader/__init__.py` | `<module>` | 1–32 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: bd5112a2a0d5...) |
| `dataio/loader/cmr_3D_dataset.py` | `<module>` | 1–54 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: c33eb8c94580...) |
| `dataio/loader/hms_dataset.py` | `<module>` | 1–7 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 6f5d40dadb6b...) |
| `dataio/loader/test_dataset.py` | `<module>` | 1–48 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: b29848c071c4...) |
| `dataio/loader/ukbb_dataset.py` | `<module>` | 1–58 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: ce9932f5bf62...) |
| `dataio/loader/us_dataset.py` | `<module>` | 1–75 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: f8e7241b8215...) |

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
- **Descrição:** Evidência não identificada no repositório analisado: não foram localizados arquivos de gerenciamento de dependências (requirements.txt, pyproject.toml, poetry.lock). Foram identificados 37 módulos externos importados no código (PIL, SimpleITK, aggregated_classifier, base_model, cv2, dominate, feedforward_classifier, feedforward_seg_model, h5py, layers). Possível lacuna documental de SOUP.
- **Justificativa de Rastreabilidade:** Ausência de manifesto de dependências observável no diretório inspecionado.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `setup.py` | `setuptools` | 1–1 | `undeclared_import` | Módulo externo 'setuptools' importado em 'setup.py', mas não localizado nos manifestos de dependências inspecionados. |
| `test_classification.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'test_classification.py', mas não localizado nos manifestos de dependências inspecionados. |
| `test_classification.py` | `torch` | 1–1 | `undeclared_import` | Módulo externo 'torch' importado em 'test_classification.py', mas não localizado nos manifestos de dependências inspecionados. |
| `test_classification.py` | `tqdm` | 1–1 | `undeclared_import` | Módulo externo 'tqdm' importado em 'test_classification.py', mas não localizado nos manifestos de dependências inspecionados. |
| `train_classifaction.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'train_classifaction.py', mas não localizado nos manifestos de dependências inspecionados. |
| `train_classifaction.py` | `torch` | 1–1 | `undeclared_import` | Módulo externo 'torch' importado em 'train_classifaction.py', mas não localizado nos manifestos de dependências inspecionados. |
| `train_classifaction.py` | `tqdm` | 1–1 | `undeclared_import` | Módulo externo 'tqdm' importado em 'train_classifaction.py', mas não localizado nos manifestos de dependências inspecionados. |
| `train_segmentation.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'train_segmentation.py', mas não localizado nos manifestos de dependências inspecionados. |
| `train_segmentation.py` | `torch` | 1–1 | `undeclared_import` | Módulo externo 'torch' importado em 'train_segmentation.py', mas não localizado nos manifestos de dependências inspecionados. |
| `train_segmentation.py` | `tqdm` | 1–1 | `undeclared_import` | Módulo externo 'tqdm' importado em 'train_segmentation.py', mas não localizado nos manifestos de dependências inspecionados. |
| `validation.py` | `SimpleITK` | 1–1 | `undeclared_import` | Módulo externo 'SimpleITK' importado em 'validation.py', mas não localizado nos manifestos de dependências inspecionados. |
| `validation.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'validation.py', mas não localizado nos manifestos de dependências inspecionados. |
| `validation.py` | `torch` | 1–1 | `undeclared_import` | Módulo externo 'torch' importado em 'validation.py', mas não localizado nos manifestos de dependências inspecionados. |
| `visualise_att_maps_epoch.py` | `matplotlib` | 1–1 | `undeclared_import` | Módulo externo 'matplotlib' importado em 'visualise_att_maps_epoch.py', mas não localizado nos manifestos de dependências inspecionados. |
| `visualise_att_maps_epoch.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'visualise_att_maps_epoch.py', mas não localizado nos manifestos de dependências inspecionados. |
*... e mais 96 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência identificada: 2 arquivo(s) de teste localizado(s) (diretórios: raiz/módulos; frameworks: não identificado explicitamente; 9 função(ões)/método(s) de teste).
- **Justificativa de Rastreabilidade:** Módulos e funções de teste automatizado foram observados no repositório.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `test_classification.py` | `HiddenPrints.__enter__` | 16–18 | `test_module` | Módulo de teste 'test_classification.py' identificado (6 funções/métodos candidatos de teste). |
| `dataio/loader/test_dataset.py` | `TestDataset.__init__` | 11–27 | `test_module` | Módulo de teste 'dataio/loader/test_dataset.py' identificado (3 funções/métodos candidatos de teste). |

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
- **Status:** `not_observed` (Evidência não identificada no repositório analisado)
- **Prioridade de Revisão Técnica:** `medium` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência não identificada no repositório analisado: nenhuma configuração de CI/CD (.github/workflows/*.yml ou .gitlab-ci.yml) foi encontrada no escopo inspecionado.
- **Justificativa de Rastreabilidade:** Ausência de arquivos de configuração de integração contínua no repositório.

#### Evidências Extraídas (Arquivos e Linhas)
*Nenhuma evidência positiva localizada no código; ver justificativa acima.*

#### Referências Regulatórias Relacionadas
- **IEC62304** (IEC) — Cláusula/Seção: `5.5.5; 5.6.4; 5.6.6` | Status da Validação: `pending_expert_review`
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 5.6.6, 5.6.7, 5.6.8` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s16` (Score: `0.5773`)
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 5.6.3, 5.6.4, 5.6.5` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s15` (Score: `0.5169`)
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 5.5.5, 5.6.1, 5.6.2` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s14` (Score: `0.3814`)

#### Limitações Técnicas
- Pipelines de CI/CD podem estar hospedados em servidores externos (Jenkins, Azure DevOps, GitLab externo) sem arquivo de configuração versionado na pasta .github/workflows.
- A presença do arquivo YAML não garante que o workflow esteja ativo ou aprovado nas branches protegidas.

#### Recomendação de Investigação ou Correção
Avaliar a adoção de pipeline de CI/CD versionado para automatizar testes de regressão ou documentar o ambiente externo utilizado para verificação.

### TA-005 (R05) — Tratamento de erros e exceções em operações de I/O
- **Categoria:** Confiabilidade e Tratamento de Falhas
- **Status:** `not_observed` (Evidência não identificada no repositório analisado)
- **Prioridade de Revisão Técnica:** `high` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência não identificada no repositório analisado: foram detectadas 18 operação(ões) candidatas de I/O sem nenhum bloco try-except não vazio associado (blocos except vazios/pass encontrados: 0).
- **Justificativa de Rastreabilidade:** Operações de leitura/escrita identificadas sem tratamento de exceções efetivo observável no escopo local.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `setup.py` | N/A | 5–5 | `ast_io_operation` | Operação candidata de I/O 'open' em '<module>' (dentro de try-except não vazio: False) |
| `test_classification.py` | `test` | 153–153 | `ast_io_operation` | Operação candidata de I/O 'open' em 'test' (dentro de try-except não vazio: False) |
| `test_classification.py` | `test` | 158–158 | `ast_io_operation` | Operação candidata de I/O 'pkl.dump' em 'test' (dentro de try-except não vazio: False) |
| `dataio/loader/utils.py` | `load_nifti_img` | 17–17 | `ast_io_operation` | Operação candidata de I/O 'nib.load' em 'load_nifti_img' (dentro de try-except não vazio: False) |
| `dataio/transformation/myImageTransformations.py` | N/A | 449–449 | `ast_io_operation` | Operação candidata de I/O 'Image.open' em '<module>' (dentro de try-except não vazio: False) |
| `dataio/transformation/myImageTransformations.py` | N/A | 450–450 | `ast_io_operation` | Operação candidata de I/O 'Image.open' em '<module>' (dentro de try-except não vazio: False) |
| `models/base_model.py` | `BaseModel.save_network` | 66–66 | `ast_io_operation` | Operação candidata de I/O 'torch.save' em 'BaseModel.save_network' (dentro de try-except não vazio: False) |
| `models/base_model.py` | `BaseModel.load_network` | 75–75 | `ast_io_operation` | Operação candidata de I/O 'torch.load' em 'BaseModel.load_network' (dentro de try-except não vazio: False) |
| `models/base_model.py` | `BaseModel.load_network_from_path` | 81–81 | `ast_io_operation` | Operação candidata de I/O 'torch.load' em 'BaseModel.load_network_from_path' (dentro de try-except não vazio: False) |
| `models/feedforward_classifier.py` | `FeedForwardClassifier.load_network_from_path` | 181–181 | `ast_io_operation` | Operação candidata de I/O 'torch.load' em 'FeedForwardClassifier.load_network_from_path' (dentro de try-except não vazio: False) |
| `utils/html.py` | `HTML.save` | 47–47 | `ast_io_operation` | Operação candidata de I/O 'open' em 'HTML.save' (dentro de try-except não vazio: False) |
| `utils/post_process_crf.py` | N/A | 79–79 | `ast_io_operation` | Operação candidata de I/O 'nib.load' em '<module>' (dentro de try-except não vazio: False) |
| `utils/post_process_crf.py` | N/A | 86–86 | `ast_io_operation` | Operação candidata de I/O 'nib.load' em '<module>' (dentro de try-except não vazio: False) |
| `utils/util.py` | `json_file_to_pyobj.json2obj` | 88–88 | `ast_io_operation` | Operação candidata de I/O 'json.loads' em 'json_file_to_pyobj.json2obj' (dentro de try-except não vazio: False) |
| `utils/util.py` | `json_file_to_pyobj` | 89–89 | `ast_io_operation` | Operação candidata de I/O 'open' em 'json_file_to_pyobj' (dentro de try-except não vazio: False) |
*... e mais 3 evidência(s) registrada(s) em `findings.json`.*

#### Referências Regulatórias Relacionadas
- **IEC62304** (IEC) — Cláusula/Seção: `5.1.12; 5.5.3; 7.1.2` | Status da Validação: `pending_expert_review`
- **IEC62304_OPENREG_MAPPING** (OpenRegulatory (referenciando cláusulas verificáveis da IEC 62304:2006)) — Cláusula/Seção: `IEC 62304 Sec. 5.1.12, 5.2.1, 5.2.2` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_MAPPING::s07` (Score: `0.4122`)
- **IEC62304_OPENREG_DEV_PLAN** (OpenRegulatory) — Cláusula/Seção: `IEC 62304 Sec. 5.1.5, 5.1.6, 5.1.7, 5.1.8` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_DEV_PLAN::s03` (Score: `0.3344`)
- **IEC62304_OPENREG_DEV_PLAN** (OpenRegulatory) — Cláusula/Seção: `IEC 62304 Sec. 5.1.12, 6.1` | Status da Validação: `pending_expert_review` | Fragmento: `IEC62304_OPENREG_DEV_PLAN::s04` (Score: `0.2835`)

#### Limitações Técnicas
- A presença de um bloco try-except NÃO comprova que o tratamento de erro é clinicamente seguro ou adequado aos controles de risco do dispositivo.
- O tratamento de exceções pode ocorrer em níveis superiores da pilha de chamadas (caller functions) não visíveis na inspeção intrafuncional.

#### Recomendação de Investigação ou Correção
Implementar tratamento estruturado de exceções para operações de leitura/escrita de dados e artefatos, vinculando o tratamento à análise de riscos do software.

### TA-006 (R06) — Sinais estruturais de validação de entradas
- **Categoria:** Verificação de Interfaces e Entradas
- **Status:** `observed` (Evidência identificada)
- **Prioridade de Revisão Técnica:** `medium` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `medium`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência identificada: 176 sinal(is) estrutural(is) de validação de entrada localizado(s), incluindo 74 função(ões)/chamada(s) de validação e 3 guarda(s) condicional(is) com levantamento de exceção.
- **Justificativa de Rastreabilidade:** Foram identificados mecanismos explícitos de verificação de entrada no código. A presença estrutural não garante suficiência clínica ou completude da validação.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `test_classification.py` | `test` | 134–134 | `validation_validation_call` | Sinal de validação (validation_call) em 'test' |
| `train_classifaction.py` | `check_warm_start` | 66–73 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'check_warm_start' |
| `train_classifaction.py` | `train` | 191–191 | `validation_validation_call` | Sinal de validação (validation_call) em 'train' |
| `train_segmentation.py` | `train` | 73–73 | `validation_validation_call` | Sinal de validação (validation_call) em 'train' |
| `visualise_attention.py` | N/A | 133–133 | `validation_validation_call` | Sinal de validação (validation_call) em '<module>' |
| `dataio/loader/cmr_3D_dataset.py` | `CMR3DDataset.__init__` | 17–17 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'CMR3DDataset.__init__' |
| `dataio/loader/test_dataset.py` | `TestDataset.__init__` | 21–21 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'TestDataset.__init__' |
| `dataio/loader/ukbb_dataset.py` | `UKBBDataset.__init__` | 17–17 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'UKBBDataset.__init__' |
| `dataio/loader/us_dataset.py` | `UltraSoundDataset.__init__` | 40–40 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'UltraSoundDataset.__init__' |
| `dataio/loader/utils.py` | `check_exceptions` | 44–55 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'check_exceptions' |
| `dataio/loader/utils.py` | `check_exceptions` | 45–50 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'check_exceptions' |
| `dataio/loader/utils.py` | `check_exceptions` | 46–50 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'check_exceptions' |
| `dataio/loader/utils.py` | `check_exceptions` | 52–55 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'check_exceptions' |
| `dataio/transformation/myImageTransformations.py` | `center_crop` | 12–12 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'center_crop' |
| `dataio/transformation/myImageTransformations.py` | `poisson_downsampling` | 37–40 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'poisson_downsampling' |
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
- **Descrição:** Evidência parcial: foram identificados 8 sinal(is) de carregamento, salvamento ou referência a checkpoints de modelos (0 arquivo(s) de modelo no repositório). A existência de chamadas de carga ou arquivos .pt/.pth/.onnx não comprova proveniência completa nem controle de versão do modelo.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: artefatos de modelo exigem rastreabilidade documental de versão, dataset de treinamento, hiperparâmetros e verificação de integridade (hash).

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `test_classification.py` | `test` | 152–152 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'test' |
| `models/base_model.py` | `BaseModel.save_network` | 66–66 | `model_model_save` | Operação/referência de modelo (model_save) em 'BaseModel.save_network' |
| `models/base_model.py` | `BaseModel.load_network` | 75–75 | `model_model_load` | Operação/referência de modelo (model_load) em 'BaseModel.load_network' |
| `models/base_model.py` | `BaseModel.load_network` | 75–75 | `model_model_load` | Operação/referência de modelo (model_load) em 'BaseModel.load_network' |
| `models/base_model.py` | `BaseModel.load_network_from_path` | 81–81 | `model_model_load` | Operação/referência de modelo (model_load) em 'BaseModel.load_network_from_path' |
| `models/base_model.py` | `BaseModel.load_network_from_path` | 81–81 | `model_model_load` | Operação/referência de modelo (model_load) em 'BaseModel.load_network_from_path' |
| `models/feedforward_classifier.py` | `FeedForwardClassifier.load_network_from_path` | 181–181 | `model_model_load` | Operação/referência de modelo (model_load) em 'FeedForwardClassifier.load_network_from_path' |
| `models/feedforward_classifier.py` | `FeedForwardClassifier.load_network_from_path` | 181–181 | `model_model_load` | Operação/referência de modelo (model_load) em 'FeedForwardClassifier.load_network_from_path' |

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
- **Descrição:** Evidência parcial: sinais estruturais de treinamento e de inferência coexistem no(s) mesmo(s) arquivo(s) (models/aggregated_classifier.py, models/base_model.py, models/feedforward_classifier.py, models/feedforward_seg_model.py, models/networks_other.py). Indicador técnico que merece investigação quanto à segregação arquitetural entre desenvolvimento/treino e produção/inferência.
- **Justificativa de Rastreabilidade:** Coexistência de sinais de treinamento e inferência em models/aggregated_classifier.py, models/base_model.py, models/feedforward_classifier.py, models/feedforward_seg_model.py, models/networks_other.py. Requer inspeção humana do fluxo de controle para verificar se o modelo é congelado em produção.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `train_classifaction.py` | `train` | 76–227 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'train' |
| `train_segmentation.py` | `train` | 14–95 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'train' |
| `models/aggregated_classifier.py` | `AggregatedClassifier.backward` | 70–70 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'AggregatedClassifier.backward' |
| `models/aggregated_classifier.py` | `AggregatedClassifier.forward` | 61–66 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'AggregatedClassifier.forward' |
| `models/aggregated_classifier.py` | `AggregatedClassifier.validate` | 73–73 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'AggregatedClassifier.validate' |
| `models/base_model.py` | `BaseModel.update_learning_rate` | 87–87 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'BaseModel.update_learning_rate' |
| `models/base_model.py` | `BaseModel.update_learning_rate` | 89–89 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'BaseModel.update_learning_rate' |
| `models/base_model.py` | `BaseModel.forward` | 36–37 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'BaseModel.forward' |
| `models/feedforward_classifier.py` | `FeedForwardClassifier.backward` | 101–101 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'FeedForwardClassifier.backward' |
| `models/feedforward_classifier.py` | `FeedForwardClassifier.optimize_parameters` | 104–104 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'FeedForwardClassifier.optimize_parameters' |
| `models/feedforward_classifier.py` | `FeedForwardClassifier.optimize_parameters` | 107–107 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'FeedForwardClassifier.optimize_parameters' |
| `models/feedforward_classifier.py` | `FeedForwardClassifier.optimize_parameters` | 108–108 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'FeedForwardClassifier.optimize_parameters' |
| `models/feedforward_classifier.py` | `FeedForwardClassifier.optimize_parameters` | 109–109 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'FeedForwardClassifier.optimize_parameters' |
| `models/feedforward_classifier.py` | `FeedForwardClassifier.forward` | 88–95 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'FeedForwardClassifier.forward' |
| `models/feedforward_classifier.py` | `FeedForwardClassifier.test` | 112–112 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'FeedForwardClassifier.test' |
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
1. **TA-005 (R05 — Tratamento de erros e exceções em operações de I/O)** [Evidência não identificada no repositório analisado]: Implementar tratamento estruturado de exceções para operações de leitura/escrita de dados e artefatos, vinculando o tratamento à análise de riscos do software.
1. **TA-007 (R07 — Proveniência, carregamento e versionamento de artefatos de modelos)** [Evidência parcial — indicador técnico que merece investigação]: Documentar formalmente a proveniência de cada modelo carregado (identificador de versão, hash SHA-256 do artefato, dataset de origem, hiperparâmetros e Relatório de Validação de Algoritmo).
1. **TA-008 (R08 — Sinais estruturais de separação entre treinamento e inferência)** [Evidência parcial — indicador técnico que merece investigação]: Revisar a arquitetura dos módulos listados para separar claramente os scripts de treinamento do pipeline de inferência clínica e documentar o controle de implantação (SOP Deployment).

### Prioridade de Revisão Média (`medium`)
1. **TA-004 (R04 — Integração contínua (CI/CD) e automação de verificação)** [Evidência não identificada no repositório analisado]: Avaliar a adoção de pipeline de CI/CD versionado para automatizar testes de regressão ou documentar o ambiente externo utilizado para verificação.
1. **TA-006 (R06 — Sinais estruturais de validação de entradas)** [Evidência identificada]: Revisão humana necessária para verificar se os critérios de validação cobrem formatos inválidos, valores ausentes, limites fisiológicos/dimensionais e proteção contra entradas malformadas.

### Prioridade de Revisão Baixa (`low`)
1. **TA-003 (R03 — Evidências de testes automatizados no repositório)** [Evidência identificada]: Revisão humana necessária para verificar a rastreabilidade entre os casos de teste automatizados, os requisitos de software e os controles de risco (IEC 62304 Seções 5.5, 5.6 e 5.7).

### Informativo (`informational`)
1. **TA-001 (R01 — Cobertura e integridade da inspeção estática)** [Evidência identificada]: Manter a verificação sintática íntegra no fluxo de desenvolvimento.
