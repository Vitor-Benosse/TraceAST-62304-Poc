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

- **Nome do Projeto:** TEST-019_YerevaNN__mimic3-benchmarks
- **Commit SHA Analisado:** `ea0314c7cbd369f62e2237ace6f683740f867e3a`
- **Data e Horário da Execução (UTC):** `2026-11-04T22:17:05.648755+00:00`
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

- **Quantidade total de arquivos encontrados:** 101
- **Quantidade de arquivos Python (`.py`):** 66
- **Arquivos Python analisados com sucesso:** 66
- **Arquivos Python que falharam na análise:** 0
- **Percentual de cobertura da inspeção sintática:** 100.0%

*Nenhum arquivo Python falhou durante o parsing sintático AST.*

## C. Visão Geral dos Indicadores Técnicos

| Estado do Indicador | Expressão Padronizada | Quantidade |
|---|---|---|
| `observed` | Evidência identificada | 2 |
| `partial` | Evidência parcial — indicador técnico que merece investigação | 5 |
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
- **Descrição:** Evidência identificada: todos os 66 arquivos Python encontrados foram analisados com sucesso via AST (cobertura de inspeção: 100.0%).
- **Justificativa de Rastreabilidade:** Inspeção concluída sem falhas de parsing em 66/66 arquivos Python.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `mimic3benchmark/__init__.py` | `<module>` | 1–4 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 07dae31275ad...) |
| `mimic3benchmark/mimic3csv.py` | `<module>` | 1–197 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 15d304bb2ab5...) |
| `mimic3benchmark/preprocessing.py` | `<module>` | 1–291 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 8cc082e4e2c1...) |
| `mimic3benchmark/readers.py` | `<module>` | 1–345 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: ddd4ac0bb89e...) |
| `mimic3benchmark/subject.py` | `<module>` | 1–73 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 7da069c22972...) |
| `mimic3benchmark/util.py` | `<module>` | 1–5 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 91b37ce8a4be...) |
| `mimic3benchmark/evaluation/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `mimic3benchmark/evaluation/evaluate_decomp.py` | `<module>` | 1–66 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e2f574f1180c...) |
| `mimic3benchmark/evaluation/evaluate_ihm.py` | `<module>` | 1–66 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: f9f8edb99832...) |
| `mimic3benchmark/evaluation/evaluate_los.py` | `<module>` | 1–69 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 10ff1f1a816b...) |
| `mimic3benchmark/evaluation/evaluate_pheno.py` | `<module>` | 1–89 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 59c038092c3a...) |
| `mimic3benchmark/scripts/__init__.py` | `<module>` | 1–1 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: e3b0c44298fc...) |
| `mimic3benchmark/scripts/create_decompensation.py` | `<module>` | 1–110 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 897669295d2a...) |
| `mimic3benchmark/scripts/create_in_hospital_mortality.py` | `<module>` | 1–85 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: ce19a0485666...) |
| `mimic3benchmark/scripts/create_length_of_stay.py` | `<module>` | 1–93 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 663d88cdd544...) |

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
- **Descrição:** Evidência parcial: manifesto(s) de dependências localizado(s) (requirements.txt), contendo 7 pacote(s) com versão fixada e 1 pacote(s) sem versão exata fixada. Imports externos não declarados no manifesto: imp, scipy. Componentes de IA/ML: Keras, TensorFlow, scikit-learn.
- **Justificativa de Rastreabilidade:** A presença de dependências sem versão fixada ou imports omitidos não representa automaticamente uma não conformidade, mas é um indicador técnico que merece investigação para controle de SOUP.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `requirements.txt` | `Keras` | 1–1 | `dependency_declaration` | Pacote 'Keras' declarado em 'requirements.txt' (especificador: '==2.1.2', fixado: True, importado no código: True) |
| `requirements.txt` | `tensorflow` | 2–2 | `dependency_declaration` | Pacote 'tensorflow' declarado em 'requirements.txt' (especificador: '==1.15.0', fixado: True, importado no código: True) |
| `requirements.txt` | `protobuf` | 3–3 | `dependency_declaration` | Pacote 'protobuf' declarado em 'requirements.txt' (especificador: '==3.19.0', fixado: True, importado no código: False) |
| `requirements.txt` | `pandas` | 4–4 | `dependency_declaration` | Pacote 'pandas' declarado em 'requirements.txt' (especificador: '==1.2.5', fixado: True, importado no código: True) |
| `requirements.txt` | `scikit-learn` | 5–5 | `dependency_declaration` | Pacote 'scikit-learn' declarado em 'requirements.txt' (especificador: '==1.0.2', fixado: True, importado no código: True) |
| `requirements.txt` | `numpy` | 6–6 | `dependency_declaration` | Pacote 'numpy' declarado em 'requirements.txt' (especificador: '==1.16.5', fixado: True, importado no código: True) |
| `requirements.txt` | `pyyaml` | 7–7 | `dependency_declaration` | Pacote 'pyyaml' declarado em 'requirements.txt' (especificador: '==6.0', fixado: True, importado no código: True) |
| `requirements.txt` | `tqdm` | 8–8 | `dependency_declaration` | Pacote 'tqdm' declarado em 'requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `mimic3models/feature_extractor.py` | `scipy` | 1–1 | `undeclared_import` | Módulo externo 'scipy' importado em 'mimic3models/feature_extractor.py', mas não localizado nos manifestos de dependências inspecionados. |
| `mimic3models/decompensation/main.py` | `imp` | 1–1 | `undeclared_import` | Módulo externo 'imp' importado em 'mimic3models/decompensation/main.py', mas não localizado nos manifestos de dependências inspecionados. |
| `mimic3models/in_hospital_mortality/main.py` | `imp` | 1–1 | `undeclared_import` | Módulo externo 'imp' importado em 'mimic3models/in_hospital_mortality/main.py', mas não localizado nos manifestos de dependências inspecionados. |
| `mimic3models/length_of_stay/main.py` | `imp` | 1–1 | `undeclared_import` | Módulo externo 'imp' importado em 'mimic3models/length_of_stay/main.py', mas não localizado nos manifestos de dependências inspecionados. |
| `mimic3models/multitask/main.py` | `imp` | 1–1 | `undeclared_import` | Módulo externo 'imp' importado em 'mimic3models/multitask/main.py', mas não localizado nos manifestos de dependências inspecionados. |
| `mimic3models/phenotyping/main.py` | `imp` | 1–1 | `undeclared_import` | Módulo externo 'imp' importado em 'mimic3models/phenotyping/main.py', mas não localizado nos manifestos de dependências inspecionados. |

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
- **Status:** `partial` (Evidência parcial — indicador técnico que merece investigação)
- **Prioridade de Revisão Técnica:** `medium` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência parcial: estrutura ou configuração de testes presente (diretórios: nenhum, arquivos: 6, configs: nenhuma), mas sem funções de teste verificáveis.
- **Justificativa de Rastreabilidade:** Estrutura parcial de testes localizada sem casos de teste completos observáveis via AST.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `mimic3benchmark/scripts/split_train_and_test.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'mimic3benchmark/scripts/split_train_and_test.py' identificado (0 funções/métodos candidatos de teste). |
| `mimic3benchmark/tests/__init__.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'mimic3benchmark/tests/__init__.py' identificado (0 funções/métodos candidatos de teste). |
| `mimic3benchmark/tests/compare_dir_with_existing.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'mimic3benchmark/tests/compare_dir_with_existing.py' identificado (0 funções/métodos candidatos de teste). |
| `mimic3benchmark/tests/compare_hashes.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'mimic3benchmark/tests/compare_hashes.py' identificado (0 funções/métodos candidatos de teste). |
| `mimic3benchmark/tests/compare_listfiles.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'mimic3benchmark/tests/compare_listfiles.py' identificado (0 funções/métodos candidatos de teste). |
| `mimic3benchmark/tests/hash_tables.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'mimic3benchmark/tests/hash_tables.py' identificado (0 funções/métodos candidatos de teste). |

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
- **Descrição:** Evidência parcial: entre 129 operação(ões) candidatas de I/O, 0 possuem bloco try-except não vazio e 129 não possuem tratamento local observável. Foram identificados 5 bloco(s) except vazios ou com 'pass'.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: coexistem operações de I/O sem captura local de exceção ou blocos except que suprimem falhas com pass.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `mimic3benchmark/mimic3csv.py` | `read_events_table_by_row` | 45–45 | `ast_io_operation` | Operação candidata de I/O 'open' em 'read_events_table_by_row' (dentro de try-except não vazio: False) |
| `mimic3benchmark/mimic3csv.py` | `count_icd_codes` | 58–58 | `ast_io_operation` | Operação candidata de I/O 'codes.to_csv' em 'count_icd_codes' (dentro de try-except não vazio: False) |
| `mimic3benchmark/mimic3csv.py` | `break_up_stays_by_subject` | 125–126 | `ast_io_operation` | Operação candidata de I/O 'to_csv' em 'break_up_stays_by_subject' (dentro de try-except não vazio: False) |
| `mimic3benchmark/mimic3csv.py` | `break_up_diagnoses_by_subject` | 139–140 | `ast_io_operation` | Operação candidata de I/O 'to_csv' em 'break_up_diagnoses_by_subject' (dentro de try-except não vazio: False) |
| `mimic3benchmark/mimic3csv.py` | `read_events_table_and_break_up_by_subject.write_current_observations` | 166–166 | `ast_io_operation` | Operação candidata de I/O 'open' em 'read_events_table_and_break_up_by_subject.write_current_observations' (dentro de try-except não vazio: False) |
| `mimic3benchmark/mimic3csv.py` | `read_events_table_and_break_up_by_subject.write_current_observations` | 169–169 | `ast_io_operation` | Operação candidata de I/O 'open' em 'read_events_table_and_break_up_by_subject.write_current_observations' (dentro de try-except não vazio: False) |
| `mimic3benchmark/mimic3csv.py` | `break_up_stays_by_subject` | 120–123 | `ast_empty_or_pass_except` | Bloco try-except em 'break_up_stays_by_subject' possui handler vazio ou com instrução 'pass' (exceções: <bare_except>) |
| `mimic3benchmark/mimic3csv.py` | `break_up_diagnoses_by_subject` | 134–137 | `ast_empty_or_pass_except` | Bloco try-except em 'break_up_diagnoses_by_subject' possui handler vazio ou com instrução 'pass' (exceções: <bare_except>) |
| `mimic3benchmark/mimic3csv.py` | `read_events_table_and_break_up_by_subject.write_current_observations` | 160–163 | `ast_empty_or_pass_except` | Bloco try-except em 'read_events_table_and_break_up_by_subject.write_current_observations' possui handler vazio ou com instrução 'pass' (exceções: <bare_except>) |
| `mimic3benchmark/readers.py` | `Reader.__init__` | 14–14 | `ast_io_operation` | Operação candidata de I/O 'open' em 'Reader.__init__' (dentro de try-except não vazio: False) |
| `mimic3benchmark/readers.py` | `DecompensationReader._read_timeseries` | 51–51 | `ast_io_operation` | Operação candidata de I/O 'open' em 'DecompensationReader._read_timeseries' (dentro de try-except não vazio: False) |
| `mimic3benchmark/readers.py` | `InHospitalMortalityReader._read_timeseries` | 111–111 | `ast_io_operation` | Operação candidata de I/O 'open' em 'InHospitalMortalityReader._read_timeseries' (dentro de try-except não vazio: False) |
| `mimic3benchmark/readers.py` | `LengthOfStayReader._read_timeseries` | 166–166 | `ast_io_operation` | Operação candidata de I/O 'open' em 'LengthOfStayReader._read_timeseries' (dentro de try-except não vazio: False) |
| `mimic3benchmark/readers.py` | `PhenotypingReader._read_timeseries` | 224–224 | `ast_io_operation` | Operação candidata de I/O 'open' em 'PhenotypingReader._read_timeseries' (dentro de try-except não vazio: False) |
| `mimic3benchmark/readers.py` | `MultitaskReader._read_timeseries` | 300–300 | `ast_io_operation` | Operação candidata de I/O 'open' em 'MultitaskReader._read_timeseries' (dentro de try-except não vazio: False) |
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
- **Descrição:** Evidência identificada: 99 sinal(is) estrutural(is) de validação de entrada localizado(s), incluindo 14 função(ões)/chamada(s) de validação e 7 guarda(s) condicional(is) com levantamento de exceção.
- **Justificativa de Rastreabilidade:** Foram identificados mecanismos explícitos de verificação de entrada no código. A presença estrutural não garante suficiência clínica ou completude da validação.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `mimic3benchmark/mimic3csv.py` | `read_events_table_and_break_up_by_subject` | 146–147 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'read_events_table_and_break_up_by_subject' |
| `mimic3benchmark/mimic3csv.py` | `read_events_table_and_break_up_by_subject` | 148–149 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'read_events_table_and_break_up_by_subject' |
| `mimic3benchmark/mimic3csv.py` | `read_events_table_and_break_up_by_subject` | 179–180 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'read_events_table_and_break_up_by_subject' |
| `mimic3benchmark/mimic3csv.py` | `read_events_table_and_break_up_by_subject` | 181–182 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'read_events_table_and_break_up_by_subject' |
| `mimic3benchmark/preprocessing.py` | `make_phenotype_label_matrix` | 99–100 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'make_phenotype_label_matrix' |
| `mimic3benchmark/preprocessing.py` | `clean_sbp` | 150–154 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'clean_sbp' |
| `mimic3benchmark/preprocessing.py` | `clean_dbp` | 157–161 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'clean_dbp' |
| `mimic3benchmark/preprocessing.py` | `clean_crr` | 165–175 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'clean_crr' |
| `mimic3benchmark/preprocessing.py` | `clean_fio2` | 179–200 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'clean_fio2' |
| `mimic3benchmark/preprocessing.py` | `clean_lab` | 204–208 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'clean_lab' |
| `mimic3benchmark/preprocessing.py` | `clean_o2sat` | 212–221 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'clean_o2sat' |
| `mimic3benchmark/preprocessing.py` | `clean_temperature` | 225–229 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'clean_temperature' |
| `mimic3benchmark/preprocessing.py` | `clean_weight` | 234–242 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'clean_weight' |
| `mimic3benchmark/preprocessing.py` | `clean_height` | 247–251 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'clean_height' |
| `mimic3benchmark/preprocessing.py` | `clean_events` | 278–291 | `validation_validation_function_definition` | Sinal de validação (validation_function_definition) em 'clean_events' |
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
- **Descrição:** Evidência parcial: foram identificados 5 sinal(is) de carregamento, salvamento ou referência a checkpoints de modelos (0 arquivo(s) de modelo no repositório). A existência de chamadas de carga ou arquivos .pt/.pth/.onnx não comprova proveniência completa nem controle de versão do modelo.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: artefatos de modelo exigem rastreabilidade documental de versão, dataset de treinamento, hiperparâmetros e verificação de integridade (hash).

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `mimic3benchmark/tests/compare_hashes.py` | `main` | 12–12 | `model_model_load` | Operação/referência de modelo (model_load) em 'main' |
| `mimic3benchmark/tests/compare_hashes.py` | `main` | 15–15 | `model_model_load` | Operação/referência de modelo (model_load) em 'main' |
| `mimic3models/preprocessing.py` | `Normalizer._save_params` | 206–209 | `model_model_save` | Operação/referência de modelo (model_save) em 'Normalizer._save_params' |
| `mimic3models/preprocessing.py` | `Normalizer.load_params` | 214–214 | `model_model_load` | Operação/referência de modelo (model_load) em 'Normalizer.load_params' |
| `mimic3models/preprocessing.py` | `Normalizer.load_params` | 216–216 | `model_model_load` | Operação/referência de modelo (model_load) em 'Normalizer.load_params' |

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
- **Descrição:** Evidência parcial: sinais estruturais de treinamento e de inferência coexistem no(s) mesmo(s) arquivo(s) (mimic3models/decompensation/logistic/main.py, mimic3models/in_hospital_mortality/logistic/main.py, mimic3models/in_hospital_mortality/main.py, mimic3models/length_of_stay/logistic/main.py, mimic3models/length_of_stay/logistic/main_cf.py, mimic3models/phenotyping/logistic/main.py). Indicador técnico que merece investigação quanto à segregação arquitetural entre desenvolvimento/treino e produção/inferência.
- **Justificativa de Rastreabilidade:** Coexistência de sinais de treinamento e inferência em mimic3models/decompensation/logistic/main.py, mimic3models/in_hospital_mortality/logistic/main.py, mimic3models/in_hospital_mortality/main.py, mimic3models/length_of_stay/logistic/main.py, mimic3models/length_of_stay/logistic/main_cf.py, mimic3models/phenotyping/logistic/main.py. Requer inspeção humana do fluxo de controle para verificar se o modelo é congelado em produção.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `mimic3benchmark/mimic3csv.py` | `read_icd_diagnoses_table` | 34–40 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'read_icd_diagnoses_table' |
| `mimic3benchmark/mimic3csv.py` | `filter_diagnoses_on_stays` | 110–112 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'filter_diagnoses_on_stays' |
| `mimic3benchmark/mimic3csv.py` | `break_up_diagnoses_by_subject` | 129–140 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'break_up_diagnoses_by_subject' |
| `mimic3benchmark/subject.py` | `read_diagnoses` | 19–20 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'read_diagnoses' |
| `mimic3models/keras_utils.py` | `DecompensationMetrics.calc_metrics` | 36–36 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'DecompensationMetrics.calc_metrics' |
| `mimic3models/keras_utils.py` | `InHospitalMortalityMetrics.calc_metrics` | 89–89 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'InHospitalMortalityMetrics.calc_metrics' |
| `mimic3models/keras_utils.py` | `PhenotypingMetrics.calc_metrics` | 135–135 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'PhenotypingMetrics.calc_metrics' |
| `mimic3models/keras_utils.py` | `LengthOfStayMetrics.calc_metrics` | 182–182 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'LengthOfStayMetrics.calc_metrics' |
| `mimic3models/keras_utils.py` | `MultitaskMetrics.calc_metrics` | 254–254 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'MultitaskMetrics.calc_metrics' |
| `mimic3models/decompensation/main.py` | N/A | 181–181 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em '<module>' |
| `mimic3models/decompensation/logistic/main.py` | `main` | 80–80 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'main' |
| `mimic3models/decompensation/logistic/main.py` | `main` | 87–87 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'main' |
| `mimic3models/decompensation/logistic/main.py` | `main` | 99–99 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'main' |
| `mimic3models/decompensation/logistic/main.py` | `main` | 102–102 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'main' |
| `mimic3models/decompensation/logistic/main.py` | `main` | 107–107 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'main' |
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
1. **TA-003 (R03 — Evidências de testes automatizados no repositório)** [Evidência parcial — indicador técnico que merece investigação]: Implementar e vincular os testes de unidade, integração e sistema aos requisitos do software.
1. **TA-004 (R04 — Integração contínua (CI/CD) e automação de verificação)** [Evidência não identificada no repositório analisado]: Avaliar a adoção de pipeline de CI/CD versionado para automatizar testes de regressão ou documentar o ambiente externo utilizado para verificação.
1. **TA-006 (R06 — Sinais estruturais de validação de entradas)** [Evidência identificada]: Revisão humana necessária para verificar se os critérios de validação cobrem formatos inválidos, valores ausentes, limites fisiológicos/dimensionais e proteção contra entradas malformadas.

### Informativo (`informational`)
1. **TA-001 (R01 — Cobertura e integridade da inspeção estática)** [Evidência identificada]: Manter a verificação sintática íntegra no fluxo de desenvolvimento.
