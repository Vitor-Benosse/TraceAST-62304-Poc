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

- **Nome do Projeto:** TEST-020_deepmedic__deepmedic
- **Commit SHA Analisado:** `e10ba7c3570d06194f5dadca91d99d5e7bba7de5`
- **Data e Horário da Execução (UTC):** `2026-11-04T22:17:11.279823+00:00`
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

- **Quantidade total de arquivos encontrados:** 120
- **Quantidade de arquivos Python (`.py`):** 44
- **Arquivos Python analisados com sucesso:** 44
- **Arquivos Python que falharam na análise:** 0
- **Percentual de cobertura da inspeção sintática:** 100.0%

*Nenhum arquivo Python falhou durante o parsing sintático AST.*

## C. Visão Geral dos Indicadores Técnicos

| Estado do Indicador | Expressão Padronizada | Quantidade |
|---|---|---|
| `observed` | Evidência identificada | 2 |
| `partial` | Evidência parcial — indicador técnico que merece investigação | 3 |
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
- **Descrição:** Evidência identificada: todos os 44 arquivos Python encontrados foram analisados com sucesso via AST (cobertura de inspeção: 100.0%).
- **Justificativa de Rastreabilidade:** Inspeção concluída sem falhas de parsing em 44/44 arquivos Python.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `plotTrainingProgress.py` | `<module>` | 1–608 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 606ebdea263b...) |
| `setup.py` | `<module>` | 1–34 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 81fd2b2bd86a...) |
| `deepmedic/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `deepmedic/dataManagement/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `deepmedic/dataManagement/augmentImage.py` | `<module>` | 1–226 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 9559aca18232...) |
| `deepmedic/dataManagement/augmentSample.py` | `<module>` | 1–104 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 22e35213d4b1...) |
| `deepmedic/dataManagement/io.py` | `<module>` | 1–177 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 33b26cf9581e...) |
| `deepmedic/dataManagement/preprocessing.py` | `<module>` | 1–284 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: d03bdb1bd4b6...) |
| `deepmedic/dataManagement/sampling.py` | `<module>` | 1–903 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 03cbb06e4ce9...) |
| `deepmedic/dataManagement/samplingType.py` | `<module>` | 1–168 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 5d7dfbc06733...) |
| `deepmedic/frontEnd/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `deepmedic/frontEnd/sessHelpers.py` | `<module>` | 1–156 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 36848727ba70...) |
| `deepmedic/frontEnd/session.py` | `<module>` | 1–57 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 866eeaa74ff2...) |
| `deepmedic/frontEnd/testSession.py` | `<module>` | 1–136 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 3a20a7ac9234...) |
| `deepmedic/frontEnd/trainSession.py` | `<module>` | 1–227 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 0dec29293b78...) |

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
- **Descrição:** Evidência não identificada no repositório analisado: não foram localizados arquivos de gerenciamento de dependências (requirements.txt, pyproject.toml, poetry.lock). Foram identificados 8 módulos externos importados no código (matplotlib, nibabel, numpy, pandas, scipy, setuptools, six, tensorflow). Possível lacuna documental de SOUP.
- **Justificativa de Rastreabilidade:** Ausência de manifesto de dependências observável no diretório inspecionado.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `plotTrainingProgress.py` | `matplotlib` | 1–1 | `undeclared_import` | Módulo externo 'matplotlib' importado em 'plotTrainingProgress.py', mas não localizado nos manifestos de dependências inspecionados. |
| `plotTrainingProgress.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'plotTrainingProgress.py', mas não localizado nos manifestos de dependências inspecionados. |
| `plotTrainingProgress.py` | `six` | 1–1 | `undeclared_import` | Módulo externo 'six' importado em 'plotTrainingProgress.py', mas não localizado nos manifestos de dependências inspecionados. |
| `setup.py` | `setuptools` | 1–1 | `undeclared_import` | Módulo externo 'setuptools' importado em 'setup.py', mas não localizado nos manifestos de dependências inspecionados. |
| `deepmedic/dataManagement/augmentImage.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'deepmedic/dataManagement/augmentImage.py', mas não localizado nos manifestos de dependências inspecionados. |
| `deepmedic/dataManagement/augmentImage.py` | `scipy` | 1–1 | `undeclared_import` | Módulo externo 'scipy' importado em 'deepmedic/dataManagement/augmentImage.py', mas não localizado nos manifestos de dependências inspecionados. |
| `deepmedic/dataManagement/augmentSample.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'deepmedic/dataManagement/augmentSample.py', mas não localizado nos manifestos de dependências inspecionados. |
| `deepmedic/dataManagement/io.py` | `nibabel` | 1–1 | `undeclared_import` | Módulo externo 'nibabel' importado em 'deepmedic/dataManagement/io.py', mas não localizado nos manifestos de dependências inspecionados. |
| `deepmedic/dataManagement/io.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'deepmedic/dataManagement/io.py', mas não localizado nos manifestos de dependências inspecionados. |
| `deepmedic/dataManagement/preprocessing.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'deepmedic/dataManagement/preprocessing.py', mas não localizado nos manifestos de dependências inspecionados. |
| `deepmedic/dataManagement/sampling.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'deepmedic/dataManagement/sampling.py', mas não localizado nos manifestos de dependências inspecionados. |
| `deepmedic/dataManagement/samplingType.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'deepmedic/dataManagement/samplingType.py', mas não localizado nos manifestos de dependências inspecionados. |
| `deepmedic/frontEnd/testSession.py` | `six` | 1–1 | `undeclared_import` | Módulo externo 'six' importado em 'deepmedic/frontEnd/testSession.py', mas não localizado nos manifestos de dependências inspecionados. |
| `deepmedic/frontEnd/testSession.py` | `tensorflow` | 1–1 | `undeclared_import` | Módulo externo 'tensorflow' importado em 'deepmedic/frontEnd/testSession.py', mas não localizado nos manifestos de dependências inspecionados. |
| `deepmedic/frontEnd/trainSession.py` | `tensorflow` | 1–1 | `undeclared_import` | Módulo externo 'tensorflow' importado em 'deepmedic/frontEnd/trainSession.py', mas não localizado nos manifestos de dependências inspecionados. |
*... e mais 21 evidência(s) registrada(s) em `findings.json`.*

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
- **Status:** `partial` (Evidência parcial — indicador técnico que merece investigação)
- **Prioridade de Revisão Técnica:** `medium` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência parcial: estrutura ou configuração de testes presente (diretórios: nenhum, arquivos: 0, configs: setup.cfg), mas sem funções de teste verificáveis.
- **Justificativa de Rastreabilidade:** Estrutura parcial de testes localizada sem casos de teste completos observáveis via AST.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `setup.cfg` | `<test_config>` | 1–1 | `test_configuration` | Arquivo de configuração de testes 'setup.cfg' identificado. |

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
Implementar e vincular os testes de unidade, integração e sistema aos requisitos do software.

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
- **Status:** `partial` (Evidência parcial — indicador técnico que merece investigação)
- **Prioridade de Revisão Técnica:** `high` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência parcial: entre 12 operação(ões) candidatas de I/O, 3 possuem bloco try-except não vazio e 9 não possuem tratamento local observável. Foram identificados 0 bloco(s) except vazios ou com 'pass'.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: coexistem operações de I/O sem captura local de exceção ou blocos except que suprimem falhas com pass.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `plotTrainingProgress.py` | `getFirstLineInLogWithCertainPattern` | 157–157 | `ast_io_operation` | Operação candidata de I/O 'open' em 'getFirstLineInLogWithCertainPattern' (dentro de try-except não vazio: False) |
| `plotTrainingProgress.py` | `parseBasicMetricsFromThisLog` | 273–273 | `ast_io_operation` | Operação candidata de I/O 'open' em 'parseBasicMetricsFromThisLog' (dentro de try-except não vazio: False) |
| `plotTrainingProgress.py` | `parseDetailedMetricsFromThisLog` | 335–335 | `ast_io_operation` | Operação candidata de I/O 'open' em 'parseDetailedMetricsFromThisLog' (dentro de try-except não vazio: False) |
| `setup.py` | `read` | 9–9 | `ast_io_operation` | Operação candidata de I/O 'open' em 'read' (dentro de try-except não vazio: False) |
| `deepmedic/dataManagement/io.py` | `load_volume` | 21–21 | `ast_io_operation` | Operação candidata de I/O 'nib.load' em 'load_volume' (dentro de try-except não vazio: False) |
| `deepmedic/dataManagement/io.py` | `saveImgToNiiWithOriginalHdr` | 47–47 | `ast_io_operation` | Operação candidata de I/O 'nib.load' em 'saveImgToNiiWithOriginalHdr' (dentro de try-except não vazio: False) |
| `deepmedic/frontEnd/configParsing/config.py` | `Config.__init__` | 17–17 | `ast_io_operation` | Operação candidata de I/O 'open' em 'Config.__init__' (dentro de try-except não vazio: False) |
| `deepmedic/frontEnd/configParsing/testSessionParams.py` | `TestSessionParameters.__init__` | 54–54 | `ast_io_operation` | Operação candidata de I/O 'pd.read_csv' em 'TestSessionParameters.__init__' (dentro de try-except não vazio: True) |
| `deepmedic/frontEnd/configParsing/trainSessionParams.py` | `TrainSessionParameters.__init__` | 210–210 | `ast_io_operation` | Operação candidata de I/O 'pd.read_csv' em 'TrainSessionParameters.__init__' (dentro de try-except não vazio: True) |
| `deepmedic/frontEnd/configParsing/trainSessionParams.py` | `TrainSessionParameters.__init__` | 320–320 | `ast_io_operation` | Operação candidata de I/O 'pd.read_csv' em 'TrainSessionParameters.__init__' (dentro de try-except não vazio: True) |
| `deepmedic/frontEnd/configParsing/utils.py` | `parse_filelist` | 38–38 | `ast_io_operation` | Operação candidata de I/O 'open' em 'parse_filelist' (dentro de try-except não vazio: False) |
| `deepmedic/logging/loggers.py` | `Logger.print3` | 30–30 | `ast_io_operation` | Operação candidata de I/O 'open' em 'Logger.print3' (dentro de try-except não vazio: False) |

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
- **Descrição:** Evidência identificada: 169 sinal(is) estrutural(is) de validação de entrada localizado(s), incluindo 21 função(ões)/chamada(s) de validação e 5 guarda(s) condicional(is) com levantamento de exceção.
- **Justificativa de Rastreabilidade:** Foram identificados mecanismos explícitos de verificação de entrada no código. A presença estrutural não garante suficiência clínica ou completude da validação.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `plotTrainingProgress.py` | `getSubepochsPerEpoch` | 59–59 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'getSubepochsPerEpoch' |
| `plotTrainingProgress.py` | `getEpochsBetweenFullInf` | 63–63 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'getEpochsBetweenFullInf' |
| `plotTrainingProgress.py` | `getNumberOfClasses` | 67–67 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'getNumberOfClasses' |
| `plotTrainingProgress.py` | `checkIfLineMatchesAnyRegExpr` | 238–246 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'checkIfLineMatchesAnyRegExpr' |
| `deepmedic/dataManagement/augmentImage.py` | `augment_imgs_of_case` | 22–30 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'augment_imgs_of_case' |
| `deepmedic/dataManagement/augmentImage.py` | `random_affine_deformation` | 35–36 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'random_affine_deformation' |
| `deepmedic/dataManagement/augmentImage.py` | `random_affine_deformation` | 43–43 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'random_affine_deformation' |
| `deepmedic/dataManagement/augmentImage.py` | `AugmenterParams._set_from_dict` | 81–83 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'AugmenterParams._set_from_dict' |
| `deepmedic/dataManagement/augmentImage.py` | `AugmenterAffine._apply_transformation` | 150–150 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'AugmenterAffine._apply_transformation' |
| `deepmedic/dataManagement/augmentImage.py` | `AugmenterAffine.__call__` | 180–181 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'AugmenterAffine.__call__' |
| `deepmedic/dataManagement/augmentImage.py` | `AugmenterAffine.__call__` | 182–183 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'AugmenterAffine.__call__' |
| `deepmedic/dataManagement/augmentImage.py` | `AugmenterAffine.__call__` | 184–185 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'AugmenterAffine.__call__' |
| `deepmedic/dataManagement/augmentImage.py` | `AugmenterAffine.__call__` | 184–184 | `validation_validation_call` | Sinal de validação (validation_call) em 'AugmenterAffine.__call__' |
| `deepmedic/dataManagement/augmentImage.py` | `AugmenterAffine.__call__` | 187–188 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'AugmenterAffine.__call__' |
| `deepmedic/dataManagement/augmentImage.py` | `AugmenterAffine.__call__` | 187–187 | `validation_validation_call` | Sinal de validação (validation_call) em 'AugmenterAffine.__call__' |
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
- **Status:** `partial` (Evidência parcial — indicador técnico que merece investigação)
- **Prioridade de Revisão Técnica:** `high` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `medium`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência parcial: sinais estruturais de treinamento e de inferência coexistem no(s) mesmo(s) arquivo(s) (deepmedic/frontEnd/configParsing/trainSessionParams.py, deepmedic/frontEnd/sessHelpers.py, deepmedic/neuralnet/cnn3d.py, deepmedic/neuralnet/trainer.py, deepmedic/routines/training.py). Indicador técnico que merece investigação quanto à segregação arquitetural entre desenvolvimento/treino e produção/inferência.
- **Justificativa de Rastreabilidade:** Coexistência de sinais de treinamento e inferência em deepmedic/frontEnd/configParsing/trainSessionParams.py, deepmedic/frontEnd/sessHelpers.py, deepmedic/neuralnet/cnn3d.py, deepmedic/neuralnet/trainer.py, deepmedic/routines/training.py. Requer inspeção humana do fluxo de controle para verificar se o modelo é congelado em produção.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `plotTrainingProgress.py` | `parseVariablesOfTrainingSessionsFromListOfLogs` | 82–94 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'parseVariablesOfTrainingSessionsFromListOfLogs' |
| `deepmedic/dataManagement/sampling.py` | `constrain_sampling_maps_near_edges` | 245–255 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'constrain_sampling_maps_near_edges' |
| `deepmedic/frontEnd/sessHelpers.py` | `make_folders_for_train_session` | 81–112 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'make_folders_for_train_session' |
| `deepmedic/frontEnd/sessHelpers.py` | `createFolderForPredictions` | 20–23 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'createFolderForPredictions' |
| `deepmedic/frontEnd/configParsing/modelParams.py` | `ModelParameters.errorRequireSegmentDimensionsTrain` | 148–153 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'ModelParameters.errorRequireSegmentDimensionsTrain' |
| `deepmedic/frontEnd/configParsing/trainSessionParams.py` | `TrainSessionParameters.errorRequireChannelsTraining` | 43–52 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'TrainSessionParameters.errorRequireChannelsTraining' |
| `deepmedic/frontEnd/configParsing/trainSessionParams.py` | `TrainSessionParameters.errorRequireGtLabelsTraining` | 57–65 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'TrainSessionParameters.errorRequireGtLabelsTraining' |
| `deepmedic/frontEnd/configParsing/trainSessionParams.py` | `TrainSessionParameters.errorRequireBatchsizeTrain` | 70–72 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'TrainSessionParameters.errorRequireBatchsizeTrain' |
| `deepmedic/frontEnd/configParsing/trainSessionParams.py` | `TrainSessionParameters.get_args_for_train_routine` | 693–750 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'TrainSessionParameters.get_args_for_train_routine' |
| `deepmedic/frontEnd/configParsing/trainSessionParams.py` | `TrainSessionParameters.get_args_for_trainer` | 752–763 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'TrainSessionParameters.get_args_for_trainer' |
| `deepmedic/frontEnd/configParsing/trainSessionParams.py` | `TrainSessionParameters.errorRequireNamesOfPredictionsVal` | 149–158 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'TrainSessionParameters.errorRequireNamesOfPredictionsVal' |
| `deepmedic/neuralnet/blocks.py` | `Block.trainable_params` | 87–93 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'Block.trainable_params' |
| `deepmedic/neuralnet/cnn3d.py` | `Cnn3d.get_trainable_params` | 88–97 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'Cnn3d.get_trainable_params' |
| `deepmedic/neuralnet/cnn3d.py` | `Cnn3d.setup_ops_n_feeds_to_train` | 114–135 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'Cnn3d.setup_ops_n_feeds_to_train' |
| `deepmedic/neuralnet/cnn3d.py` | `Cnn3d.calc_unpredicted_margin` | 417–422 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'Cnn3d.calc_unpredicted_margin' |
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
1. **TA-008 (R08 — Sinais estruturais de separação entre treinamento e inferência)** [Evidência parcial — indicador técnico que merece investigação]: Revisar a arquitetura dos módulos listados para separar claramente os scripts de treinamento do pipeline de inferência clínica e documentar o controle de implantação (SOP Deployment).

### Prioridade de Revisão Média (`medium`)
1. **TA-003 (R03 — Evidências de testes automatizados no repositório)** [Evidência parcial — indicador técnico que merece investigação]: Implementar e vincular os testes de unidade, integração e sistema aos requisitos do software.
1. **TA-004 (R04 — Integração contínua (CI/CD) e automação de verificação)** [Evidência não identificada no repositório analisado]: Avaliar a adoção de pipeline de CI/CD versionado para automatizar testes de regressão ou documentar o ambiente externo utilizado para verificação.
1. **TA-006 (R06 — Sinais estruturais de validação de entradas)** [Evidência identificada]: Revisão humana necessária para verificar se os critérios de validação cobrem formatos inválidos, valores ausentes, limites fisiológicos/dimensionais e proteção contra entradas malformadas.
1. **TA-007 (R07 — Proveniência, carregamento e versionamento de artefatos de modelos)** [Evidência não identificada no repositório analisado]: Caso o software utilize modelos de IA/ML, identificar onde os artefatos de modelo são armazenados, carregados e versionados.

### Informativo (`informational`)
1. **TA-001 (R01 — Cobertura e integridade da inspeção estática)** [Evidência identificada]: Manter a verificação sintática íntegra no fluxo de desenvolvimento.
