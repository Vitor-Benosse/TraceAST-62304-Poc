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

- **Nome do Projeto:** TEST-017_282857341__nnFormer
- **Commit SHA Analisado:** `d48aaeb05612a09538f70c38a2357149ea3a7ac0`
- **Data e Horário da Execução (UTC):** `2026-11-04T22:16:56.271948+00:00`
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

- **Quantidade total de arquivos encontrados:** 175
- **Quantidade de arquivos Python (`.py`):** 165
- **Arquivos Python analisados com sucesso:** 165
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
- **Descrição:** Evidência identificada: todos os 165 arquivos Python encontrados foram analisados com sucesso via AST (cobertura de inspeção: 100.0%).
- **Justificativa de Rastreabilidade:** Inspeção concluída sem falhas de parsing em 165/165 arquivos Python.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `setup.py` | `<module>` | 1–43 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 495c39b6f8e0...) |
| `nnformer/__init__.py` | `<module>` | 1–2 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 90f1e5d52e69...) |
| `nnformer/configuration.py` | `<module>` | 1–5 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 28088adea4ea...) |
| `nnformer/inference_acdc.py` | `<module>` | 1–150 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: c46261d824a7...) |
| `nnformer/inference_synapse.py` | `<module>` | 1–185 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 6da57bbb407b...) |
| `nnformer/inference_tumor.py` | `<module>` | 1–111 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 17a0f5ab03c7...) |
| `nnformer/paths.py` | `<module>` | 1–58 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: b9e0b6b11695...) |
| `nnformer/dataset_conversion/Task017_BeyondCranialVaultAbdominalOrganSegmentation.py` | `<module>` | 1–94 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 4ab3b8891f4a...) |
| `nnformer/dataset_conversion/Task024_Promise2012.py` | `<module>` | 1–81 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: c8dc0bfb8778...) |
| `nnformer/dataset_conversion/Task027_AutomaticCardiacDetectionChallenge.py` | `<module>` | 1–106 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: ded98b54eb40...) |
| `nnformer/dataset_conversion/Task029_LiverTumorSegmentationChallenge.py` | `<module>` | 1–123 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 1f665f806a30...) |
| `nnformer/dataset_conversion/Task032_BraTS_2018.py` | `<module>` | 1–176 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 062e3c291642...) |
| `nnformer/dataset_conversion/Task035_ISBI_MSLesionSegmentationChallenge.py` | `<module>` | 1–162 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 7dd409245cd2...) |
| `nnformer/dataset_conversion/Task037_038_Chaos_Challenge.py` | `<module>` | 1–460 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: c5a049dbdbe6...) |
| `nnformer/dataset_conversion/Task040_KiTS.py` | `<module>` | 1–240 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: be439ed69768...) |

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
- **Descrição:** Evidência não identificada no repositório analisado: não foram localizados arquivos de gerenciamento de dependências (requirements.txt, pyproject.toml, poetry.lock). Foram identificados 23 módulos externos importados no código (PIL, SimpleITK, batchgenerators, cremi, dicom2nifti, einops, h5py, hiddenlayer, matplotlib, meddec). Possível lacuna documental de SOUP.
- **Justificativa de Rastreabilidade:** Ausência de manifesto de dependências observável no diretório inspecionado.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `setup.py` | `setuptools` | 1–1 | `undeclared_import` | Módulo externo 'setuptools' importado em 'setup.py', mas não localizado nos manifestos de dependências inspecionados. |
| `nnformer/inference_acdc.py` | `SimpleITK` | 1–1 | `undeclared_import` | Módulo externo 'SimpleITK' importado em 'nnformer/inference_acdc.py', mas não localizado nos manifestos de dependências inspecionados. |
| `nnformer/inference_acdc.py` | `medpy` | 1–1 | `undeclared_import` | Módulo externo 'medpy' importado em 'nnformer/inference_acdc.py', mas não localizado nos manifestos de dependências inspecionados. |
| `nnformer/inference_acdc.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'nnformer/inference_acdc.py', mas não localizado nos manifestos de dependências inspecionados. |
| `nnformer/inference_acdc.py` | `scipy` | 1–1 | `undeclared_import` | Módulo externo 'scipy' importado em 'nnformer/inference_acdc.py', mas não localizado nos manifestos de dependências inspecionados. |
| `nnformer/inference_acdc.py` | `sklearn` | 1–1 | `undeclared_import` | Módulo externo 'sklearn' importado em 'nnformer/inference_acdc.py', mas não localizado nos manifestos de dependências inspecionados. |
| `nnformer/inference_synapse.py` | `SimpleITK` | 1–1 | `undeclared_import` | Módulo externo 'SimpleITK' importado em 'nnformer/inference_synapse.py', mas não localizado nos manifestos de dependências inspecionados. |
| `nnformer/inference_synapse.py` | `medpy` | 1–1 | `undeclared_import` | Módulo externo 'medpy' importado em 'nnformer/inference_synapse.py', mas não localizado nos manifestos de dependências inspecionados. |
| `nnformer/inference_synapse.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'nnformer/inference_synapse.py', mas não localizado nos manifestos de dependências inspecionados. |
| `nnformer/inference_tumor.py` | `SimpleITK` | 1–1 | `undeclared_import` | Módulo externo 'SimpleITK' importado em 'nnformer/inference_tumor.py', mas não localizado nos manifestos de dependências inspecionados. |
| `nnformer/inference_tumor.py` | `medpy` | 1–1 | `undeclared_import` | Módulo externo 'medpy' importado em 'nnformer/inference_tumor.py', mas não localizado nos manifestos de dependências inspecionados. |
| `nnformer/inference_tumor.py` | `numpy` | 1–1 | `undeclared_import` | Módulo externo 'numpy' importado em 'nnformer/inference_tumor.py', mas não localizado nos manifestos de dependências inspecionados. |
| `nnformer/paths.py` | `batchgenerators` | 1–1 | `undeclared_import` | Módulo externo 'batchgenerators' importado em 'nnformer/paths.py', mas não localizado nos manifestos de dependências inspecionados. |
| `nnformer/dataset_conversion/Task017_BeyondCranialVaultAbdominalOrganSegmentation.py` | `batchgenerators` | 1–1 | `undeclared_import` | Módulo externo 'batchgenerators' importado em 'nnformer/dataset_conversion/Task017_BeyondCranialVaultAbdominalOrganSegmentation.py', mas não localizado nos manifestos de dependências inspecionados. |
| `nnformer/dataset_conversion/Task024_Promise2012.py` | `SimpleITK` | 1–1 | `undeclared_import` | Módulo externo 'SimpleITK' importado em 'nnformer/dataset_conversion/Task024_Promise2012.py', mas não localizado nos manifestos de dependências inspecionados. |
*... e mais 315 evidência(s) registrada(s) em `findings.json`.*

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
- **Status:** `not_observed` (Evidência não identificada no repositório analisado)
- **Prioridade de Revisão Técnica:** `high` *(Não representa classe de risco regulatório ou clínico)*
- **Confiança da Detecção Sintática:** `high`
- **Necessidade de Validação Humana:** `Sim`
- **Descrição:** Evidência não identificada no repositório analisado: não foram localizados diretórios de teste (tests/, test/) nem arquivos de teste (test_*.py, *_test.py). A ausência no repositório é relatada como ausência de evidência observável, e não como prova de que a organização não executa testes.
- **Justificativa de Rastreabilidade:** Nenhum arquivo ou diretório de testes automatizados encontrado no escopo inspecionado.

#### Evidências Extraídas (Arquivos e Linhas)
*Nenhuma evidência positiva localizada no código; ver justificativa acima.*

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
Investigar onde os artefatos de verificação de unidades e testes de sistema estão mantidos e incorporar suíte de testes automatizados reproduzível ao controle de versão.

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
- **Descrição:** Evidência parcial: entre 233 operação(ões) candidatas de I/O, 11 possuem bloco try-except não vazio e 222 não possuem tratamento local observável. Foram identificados 1 bloco(s) except vazios ou com 'pass'.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: coexistem operações de I/O sem captura local de exceção ou blocos except que suprimem falhas com pass.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `nnformer/inference_acdc.py` | `read_nii` | 12–12 | `ast_io_operation` | Operação candidata de I/O 'sitk.ReadImage' em 'read_nii' (dentro de try-except não vazio: False) |
| `nnformer/inference_acdc.py` | `test` | 78–78 | `ast_io_operation` | Operação candidata de I/O 'open' em 'test' (dentro de try-except não vazio: False) |
| `nnformer/inference_synapse.py` | `read_nii` | 9–9 | `ast_io_operation` | Operação candidata de I/O 'sitk.ReadImage' em 'read_nii' (dentro de try-except não vazio: False) |
| `nnformer/inference_synapse.py` | `test` | 63–63 | `ast_io_operation` | Operação candidata de I/O 'open' em 'test' (dentro de try-except não vazio: False) |
| `nnformer/inference_tumor.py` | `read_nii` | 9–9 | `ast_io_operation` | Operação candidata de I/O 'sitk.ReadImage' em 'read_nii' (dentro de try-except não vazio: False) |
| `nnformer/inference_tumor.py` | `test` | 52–52 | `ast_io_operation` | Operação candidata de I/O 'open' em 'test' (dentro de try-except não vazio: False) |
| `nnformer/dataset_conversion/Task024_Promise2012.py` | `export_for_submission` | 30–30 | `ast_io_operation` | Operação candidata de I/O 'sitk.ReadImage' em 'export_for_submission' (dentro de try-except não vazio: False) |
| `nnformer/dataset_conversion/Task024_Promise2012.py` | N/A | 47–47 | `ast_io_operation` | Operação candidata de I/O 'sitk.ReadImage' em '<module>' (dentro de try-except não vazio: False) |
| `nnformer/dataset_conversion/Task024_Promise2012.py` | N/A | 50–50 | `ast_io_operation` | Operação candidata de I/O 'sitk.ReadImage' em '<module>' (dentro de try-except não vazio: False) |
| `nnformer/dataset_conversion/Task024_Promise2012.py` | N/A | 57–57 | `ast_io_operation` | Operação candidata de I/O 'sitk.ReadImage' em '<module>' (dentro de try-except não vazio: False) |
| `nnformer/dataset_conversion/Task029_LiverTumorSegmentationChallenge.py` | `export_segmentations` | 29–29 | `ast_io_operation` | Operação candidata de I/O 'sitk.ReadImage' em 'export_segmentations' (dentro de try-except não vazio: False) |
| `nnformer/dataset_conversion/Task029_LiverTumorSegmentationChallenge.py` | `export_segmentations_postprocess` | 40–40 | `ast_io_operation` | Operação candidata de I/O 'sitk.ReadImage' em 'export_segmentations_postprocess' (dentro de try-except não vazio: False) |
| `nnformer/dataset_conversion/Task029_LiverTumorSegmentationChallenge.py` | `load_save_train` | 73–73 | `ast_io_operation` | Operação candidata de I/O 'sitk.ReadImage' em 'load_save_train' (dentro de try-except não vazio: False) |
| `nnformer/dataset_conversion/Task029_LiverTumorSegmentationChallenge.py` | `load_save_train` | 76–76 | `ast_io_operation` | Operação candidata de I/O 'sitk.ReadImage' em 'load_save_train' (dentro de try-except não vazio: False) |
| `nnformer/dataset_conversion/Task029_LiverTumorSegmentationChallenge.py` | `load_save_test` | 85–85 | `ast_io_operation` | Operação candidata de I/O 'sitk.ReadImage' em 'load_save_test' (dentro de try-except não vazio: False) |
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
- **Descrição:** Evidência identificada: 953 sinal(is) estrutural(is) de validação de entrada localizado(s), incluindo 158 função(ões)/chamada(s) de validação e 72 guarda(s) condicional(is) com levantamento de exceção.
- **Justificativa de Rastreabilidade:** Foram identificados mecanismos explícitos de verificação de entrada no código. A presença estrutural não garante suficiência clínica ou completude da validação.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `nnformer/paths.py` | N/A | 33–42 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em '<module>' |
| `nnformer/paths.py` | N/A | 44–49 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em '<module>' |
| `nnformer/paths.py` | N/A | 51–58 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em '<module>' |
| `nnformer/dataset_conversion/Task027_AutomaticCardiacDetectionChallenge.py` | `convert_to_submission` | 28–28 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'convert_to_submission' |
| `nnformer/dataset_conversion/Task032_BraTS_2018.py` | N/A | 91–97 | `validation_assert_statement` | Sinal de validação (assert_statement) em '<module>' |
| `nnformer/dataset_conversion/Task032_BraTS_2018.py` | N/A | 144–149 | `validation_assert_statement` | Sinal de validação (assert_statement) em '<module>' |
| `nnformer/dataset_conversion/Task032_BraTS_2018.py` | N/A | 166–171 | `validation_assert_statement` | Sinal de validação (assert_statement) em '<module>' |
| `nnformer/dataset_conversion/Task040_KiTS.py` | `copy_npz_fom_valsets` | 124–124 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'copy_npz_fom_valsets' |
| `nnformer/dataset_conversion/Task043_BraTS_2019.py` | `copy_BraTS_segmentation_and_convert_labels` | 33–34 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'copy_BraTS_segmentation_and_convert_labels' |
| `nnformer/dataset_conversion/Task043_BraTS_2019.py` | N/A | 77–83 | `validation_assert_statement` | Sinal de validação (assert_statement) em '<module>' |
| `nnformer/dataset_conversion/Task043_BraTS_2019.py` | N/A | 130–135 | `validation_assert_statement` | Sinal de validação (assert_statement) em '<module>' |
| `nnformer/dataset_conversion/Task056_VerSe2019.py` | `load_corr_save` | 31–31 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'load_corr_save' |
| `nnformer/dataset_conversion/Task056_VerSe2019.py` | `evaluate_verse_folder` | 69–69 | `validation_assert_statement` | Sinal de validação (assert_statement) em 'evaluate_verse_folder' |
| `nnformer/dataset_conversion/Task056_Verse_normalize_orientation.py` | `save_image` | 52–55 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'save_image' |
| `nnformer/dataset_conversion/Task056_Verse_normalize_orientation.py` | `save_image` | 52–52 | `validation_validation_call` | Sinal de validação (validation_call) em 'save_image' |
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
- **Descrição:** Evidência parcial: foram identificados 137 sinal(is) de carregamento, salvamento ou referência a checkpoints de modelos (1 arquivo(s) de modelo no repositório). A existência de chamadas de carga ou arquivos .pt/.pth/.onnx não comprova proveniência completa nem controle de versão do modelo.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: artefatos de modelo exigem rastreabilidade documental de versão, dataset de treinamento, hiperparâmetros e verificação de integridade (hash).

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `nnformer/dataset_conversion/Task027_AutomaticCardiacDetectionChallenge.py` | N/A | 106–106 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `nnformer/dataset_conversion/Task035_ISBI_MSLesionSegmentationChallenge.py` | N/A | 162–162 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `nnformer/dataset_conversion/Task037_038_Chaos_Challenge.py` | `convert_variant2_predicted_test_to_submission_format` | 102–102 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'convert_variant2_predicted_test_to_submission_format' |
| `nnformer/dataset_conversion/Task037_038_Chaos_Challenge.py` | `convert_variant2_predicted_test_to_submission_format` | 102–102 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'convert_variant2_predicted_test_to_submission_format' |
| `nnformer/dataset_conversion/Task037_038_Chaos_Challenge.py` | `convert_variant2_predicted_test_to_submission_format` | 103–103 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'convert_variant2_predicted_test_to_submission_format' |
| `nnformer/dataset_conversion/Task037_038_Chaos_Challenge.py` | `convert_variant2_predicted_test_to_submission_format` | 103–103 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'convert_variant2_predicted_test_to_submission_format' |
| `nnformer/dataset_conversion/Task037_038_Chaos_Challenge.py` | `convert_variant2_predicted_test_to_submission_format` | 112–112 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'convert_variant2_predicted_test_to_submission_format' |
| `nnformer/dataset_conversion/Task037_038_Chaos_Challenge.py` | `convert_variant2_predicted_test_to_submission_format` | 112–112 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'convert_variant2_predicted_test_to_submission_format' |
| `nnformer/dataset_conversion/Task037_038_Chaos_Challenge.py` | N/A | 448–448 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `nnformer/dataset_conversion/Task037_038_Chaos_Challenge.py` | N/A | 459–459 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `nnformer/dataset_conversion/Task040_KiTS.py` | `copy_npz_fom_valsets` | 119–119 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'copy_npz_fom_valsets' |
| `nnformer/dataset_conversion/Task040_KiTS.py` | `pretent_to_be_nnFormerTrainer` | 155–155 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'pretent_to_be_nnFormerTrainer' |
| `nnformer/dataset_conversion/Task040_KiTS.py` | `reset_trainerName` | 165–165 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'reset_trainerName' |
| `nnformer/dataset_conversion/Task061_CREMI.py` | N/A | 146–146 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `nnformer/dataset_conversion/Task075_Fluo_C3DH_A549_ManAndSim.py` | N/A | 136–136 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
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
- **Descrição:** Evidência parcial: sinais estruturais de treinamento e de inferência coexistem no(s) mesmo(s) arquivo(s) (nnformer/network_architecture/generic_UNet.py, nnformer/training/network_training/network_trainer.py, nnformer/training/network_training/network_trainer_synapse.py, nnformer/training/network_training/nnFormerTrainer.py, nnformer/training/network_training/nnFormerTrainerCascadeFullRes.py, nnformer/training/network_training/nnFormerTrainerV2.py, nnformer/training/network_training/nnFormerTrainerV2_CascadeFullRes.py, nnformer/training/network_training/nnFormerTrainerV2_nnformer_acdc.py, nnformer/training/network_training/nnFormerTrainerV2_nnformer_synapse.py, nnformer/training/network_training/nnFormerTrainerV2_nnformer_tumor.py, nnformer/training/network_training/nnFormerTrainer_synapse.py, nnformer/utilities/distributed.py). Indicador técnico que merece investigação quanto à segregação arquitetural entre desenvolvimento/treino e produção/inferência.
- **Justificativa de Rastreabilidade:** Coexistência de sinais de treinamento e inferência em nnformer/network_architecture/generic_UNet.py, nnformer/training/network_training/network_trainer.py, nnformer/training/network_training/network_trainer_synapse.py, nnformer/training/network_training/nnFormerTrainer.py, nnformer/training/network_training/nnFormerTrainerCascadeFullRes.py, nnformer/training/network_training/nnFormerTrainerV2.py, nnformer/training/network_training/nnFormerTrainerV2_CascadeFullRes.py, nnformer/training/network_training/nnFormerTrainerV2_nnformer_acdc.py, nnformer/training/network_training/nnFormerTrainerV2_nnformer_synapse.py, nnformer/training/network_training/nnFormerTrainerV2_nnformer_tumor.py, nnformer/training/network_training/nnFormerTrainer_synapse.py, nnformer/utilities/distributed.py. Requer inspeção humana do fluxo de controle para verificar se o modelo é congelado em produção.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `nnformer/dataset_conversion/Task029_LiverTumorSegmentationChallenge.py` | `load_save_train` | 68–78 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'load_save_train' |
| `nnformer/dataset_conversion/Task037_038_Chaos_Challenge.py` | `convert_variant2_predicted_test_to_submission_format` | 76–152 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'convert_variant2_predicted_test_to_submission_format' |
| `nnformer/dataset_conversion/Task040_KiTS.py` | `pretent_to_be_nnFormerTrainer` | 147–159 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'pretent_to_be_nnFormerTrainer' |
| `nnformer/dataset_conversion/Task040_KiTS.py` | `reset_trainerName` | 162–169 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'reset_trainerName' |
| `nnformer/dataset_conversion/Task040_KiTS.py` | `nnFormerTrainer_these` | 172–183 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'nnFormerTrainer_these' |
| `nnformer/dataset_conversion/Task040_KiTS.py` | `reset_trainerName_these` | 186–197 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'reset_trainerName_these' |
| `nnformer/dataset_conversion/Task082_BraTS_2020.py` | `summarize_validation_set_predictions` | 276–298 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'summarize_validation_set_predictions' |
| `nnformer/evaluation/metrics.py` | `negative_predictive_value` | 264–267 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'negative_predictive_value' |
| `nnformer/inference/change_trainer.py` | `pretend_to_be_nnFormerTrainer` | 19–20 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'pretend_to_be_nnFormerTrainer' |
| `nnformer/inference/change_trainer.py` | `pretend_to_be_other_trainer` | 23–35 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'pretend_to_be_other_trainer' |
| `nnformer/inference/predict.py` | `predict_cases` | 133–286 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'predict_cases' |
| `nnformer/inference/predict.py` | `predict_cases_fast` | 289–424 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'predict_cases_fast' |
| `nnformer/inference/predict.py` | `predict_cases_fastest` | 427–540 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'predict_cases_fastest' |
| `nnformer/inference/predict.py` | `predict_from_folder` | 579–662 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'predict_from_folder' |
| `nnformer/inference/pretrained_models/change_trainer.py` | `pretend_to_be_nnFormerTrainer` | 19–20 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'pretend_to_be_nnFormerTrainer' |
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
1. **TA-003 (R03 — Evidências de testes automatizados no repositório)** [Evidência não identificada no repositório analisado]: Investigar onde os artefatos de verificação de unidades e testes de sistema estão mantidos e incorporar suíte de testes automatizados reproduzível ao controle de versão.
1. **TA-005 (R05 — Tratamento de erros e exceções em operações de I/O)** [Evidência parcial — indicador técnico que merece investigação]: Revisar cada operação de leitura/escrita sem tratamento de erro e eliminar blocos except vazios/pass que possam mascarar corrupção de arquivos ou dados clínicos.
1. **TA-007 (R07 — Proveniência, carregamento e versionamento de artefatos de modelos)** [Evidência parcial — indicador técnico que merece investigação]: Documentar formalmente a proveniência de cada modelo carregado (identificador de versão, hash SHA-256 do artefato, dataset de origem, hiperparâmetros e Relatório de Validação de Algoritmo).
1. **TA-008 (R08 — Sinais estruturais de separação entre treinamento e inferência)** [Evidência parcial — indicador técnico que merece investigação]: Revisar a arquitetura dos módulos listados para separar claramente os scripts de treinamento do pipeline de inferência clínica e documentar o controle de implantação (SOP Deployment).

### Prioridade de Revisão Média (`medium`)
1. **TA-004 (R04 — Integração contínua (CI/CD) e automação de verificação)** [Evidência não identificada no repositório analisado]: Avaliar a adoção de pipeline de CI/CD versionado para automatizar testes de regressão ou documentar o ambiente externo utilizado para verificação.
1. **TA-006 (R06 — Sinais estruturais de validação de entradas)** [Evidência identificada]: Revisão humana necessária para verificar se os critérios de validação cobrem formatos inválidos, valores ausentes, limites fisiológicos/dimensionais e proteção contra entradas malformadas.

### Informativo (`informational`)
1. **TA-001 (R01 — Cobertura e integridade da inspeção estática)** [Evidência identificada]: Manter a verificação sintática íntegra no fluxo de desenvolvimento.
