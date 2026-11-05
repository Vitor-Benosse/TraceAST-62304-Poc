# Relatório de Execução no Conjunto de Teste Externo (20 Repositórios) — TraceAST-62304 v1.0 (Português)

[![en](https://img.shields.io/badge/lang-English%20(Main)-blue.svg)](./TEST_SET_EXECUTION_REPORT.md)
[![pt-br](https://img.shields.io/badge/lang-Portugu%C3%AAs%20(pt--BR)-green.svg)](./TEST_SET_EXECUTION_REPORT.pt-br.md)

> 🌐 **Language / Idioma:** **[Read in English (Primary) — `TEST_SET_EXECUTION_REPORT.md`](./TEST_SET_EXECUTION_REPORT.md)** | **Português (`TEST_SET_EXECUTION_REPORT.pt-br.md`)**

## 1. Resumo da Execução Experimental

- **Total de Repositórios Analisados:** `20` (`10` `well_structured` + `10` `experimental_deficient`)
- **Total de Avaliações de Regras Geradas:** `160` (`20` repositórios $\times$ `8` regras)
- **Versão e Hash SHA-256 do Catálogo de Regras:** `v1.0.0` (`35cab4357bb9a065...`)
- **Total de Arquivos Python Inspecionados nos 20 Repositórios:** `4395` (`4390` analisados com sucesso)
- **Tempo Total de Execução (20 Repositórios):** `204.919s`

---

## 2. Matriz de Status por Repositório (`R01`–`R08`)

| ID | Repositório | Classe Esperada | Commit SHA | Arqs .py | Cobertura | R01 | R02 | R03 | R04 | R05 | R06 | R07 | R08 | Relatório |
|---|---|---|---|---:|---:|---|---|---|---|---|---|---|---|---|
| `TEST-001` | `Project-MONAI/MONAI` | `well_structured` | `c5bddb21` | 1353 | 100.0% | `observed` | `partial` | `observed` | `observed` | `partial` | `observed` | `partial` | `partial` | [report.md](../reports/test_set/TEST-001_Project-MONAI__MONAI/report.md) |
| `TEST-002` | `Project-MONAI/monai-deploy-app-sdk` | `well_structured` | `3aee3dac` | 212 | 100.0% | `observed` | `partial` | `observed` | `observed` | `partial` | `observed` | `partial` | `partial` | [report.md](../reports/test_set/TEST-002_Project-MONAI__monai-deploy-app-sdk/report.md) |
| `TEST-003` | `fepegar/torchio` | `well_structured` | `9b1be950` | 166 | 100.0% | `observed` | `partial` | `observed` | `observed` | `partial` | `observed` | `partial` | `observed` | [report.md](../reports/test_set/TEST-003_fepegar__torchio/report.md) |
| `TEST-004` | `microsoft/hi-ml` | `well_structured` | `b67c1d27` | 299 | 100.0% | `observed` | `partial` | `observed` | `observed` | `partial` | `observed` | `partial` | `partial` | [report.md](../reports/test_set/TEST-004_microsoft__hi-ml/report.md) |
| `TEST-005` | `microsoft/InnerEye-DeepLearning` | `well_structured` | `69a64d1d` | 265 | 100.0% | `observed` | `not_observed` | `observed` | `partial` | `partial` | `observed` | `partial` | `partial` | [report.md](../reports/test_set/TEST-005_microsoft__InnerEye-DeepLearning/report.md) |
| `TEST-006` | `wasserth/TotalSegmentator` | `well_structured` | `c59be95b` | 108 | 100.0% | `observed` | `partial` | `observed` | `observed` | `partial` | `observed` | `partial` | `partial` | [report.md](../reports/test_set/TEST-006_wasserth__TotalSegmentator/report.md) |
| `TEST-007` | `MIC-DKFZ/nnUNet` | `well_structured` | `517ddab5` | 235 | 100.0% | `observed` | `partial` | `observed` | `observed` | `partial` | `observed` | `partial` | `partial` | [report.md](../reports/test_set/TEST-007_MIC-DKFZ__nnUNet/report.md) |
| `TEST-008` | `mlcommons/medperf` | `well_structured` | `b73b1f26` | 781 | 100.0% | `observed` | `partial` | `observed` | `observed` | `partial` | `observed` | `partial` | `partial` | [report.md](../reports/test_set/TEST-008_mlcommons__medperf/report.md) |
| `TEST-009` | `mlcommons/GaNDLF` | `well_structured` | `3f9b7726` | 212 | 100.0% | `observed` | `partial` | `observed` | `observed` | `partial` | `observed` | `partial` | `partial` | [report.md](../reports/test_set/TEST-009_mlcommons__GaNDLF/report.md) |
| `TEST-010` | `SciKit-Surgery/scikit-surgeryimage` | `well_structured` | `543f639b` | 60 | 100.0% | `observed` | `partial` | `observed` | `observed` | `partial` | `observed` | `not_observed` | `not_observed` | [report.md](../reports/test_set/TEST-010_SciKit-Surgery__scikit-surgeryimage/report.md) |
| `TEST-011` | `arnoweng/CheXNet` | `experimental_deficient` | `3d45ee77` | 2 | 100.0% | `observed` | `not_observed` | `not_observed` | `not_observed` | `not_observed` | `partial` | `partial` | `partial` | [report.md](../reports/test_set/TEST-011_arnoweng__CheXNet/report.md) |
| `TEST-012` | `brucechou1983/CheXNet-Keras` | `experimental_deficient` | `b80afc83` | 10 | 100.0% | `observed` | `partial` | `not_observed` | `not_observed` | `partial` | `observed` | `partial` | `partial` | [report.md](../reports/test_set/TEST-012_brucechou1983__CheXNet-Keras/report.md) |
| `TEST-013` | `imlab-uiip/lung-segmentation-2d` | `experimental_deficient` | `128794bd` | 7 | 28.57% | `partial` | `not_observed` | `not_observed` | `not_observed` | `partial` | `observed` | `not_observed` | `not_observed` | [report.md](../reports/test_set/TEST-013_imlab-uiip__lung-segmentation-2d/report.md) |
| `TEST-014` | `MrGiovanni/UNetPlusPlus` | `experimental_deficient` | `e9153d42` | 293 | 100.0% | `observed` | `partial` | `observed` | `not_observed` | `partial` | `observed` | `partial` | `partial` | [report.md](../reports/test_set/TEST-014_MrGiovanni__UNetPlusPlus/report.md) |
| `TEST-015` | `jeya-maria-jose/Medical-Transformer` | `experimental_deficient` | `62f40a53` | 19 | 100.0% | `observed` | `partial` | `not_observed` | `not_observed` | `partial` | `observed` | `partial` | `observed` | [report.md](../reports/test_set/TEST-015_jeya-maria-jose__Medical-Transformer/report.md) |
| `TEST-016` | `MIC-DKFZ/medicaldetectiontoolkit` | `experimental_deficient` | `6753237c` | 49 | 100.0% | `observed` | `partial` | `not_observed` | `not_observed` | `partial` | `observed` | `partial` | `partial` | [report.md](../reports/test_set/TEST-016_MIC-DKFZ__medicaldetectiontoolkit/report.md) |
| `TEST-017` | `282857341/nnFormer` | `experimental_deficient` | `d48aaeb0` | 165 | 100.0% | `observed` | `not_observed` | `not_observed` | `not_observed` | `partial` | `observed` | `partial` | `partial` | [report.md](../reports/test_set/TEST-017_282857341__nnFormer/report.md) |
| `TEST-018` | `ozan-oktay/Attention-Gated-Networks` | `experimental_deficient` | `eee4881f` | 49 | 100.0% | `observed` | `not_observed` | `observed` | `not_observed` | `not_observed` | `observed` | `partial` | `partial` | [report.md](../reports/test_set/TEST-018_ozan-oktay__Attention-Gated-Networks/report.md) |
| `TEST-019` | `YerevaNN/mimic3-benchmarks` | `experimental_deficient` | `ea0314c7` | 66 | 100.0% | `observed` | `partial` | `partial` | `not_observed` | `partial` | `observed` | `partial` | `partial` | [report.md](../reports/test_set/TEST-019_YerevaNN__mimic3-benchmarks/report.md) |
| `TEST-020` | `deepmedic/deepmedic` | `experimental_deficient` | `e10ba7c3` | 44 | 100.0% | `observed` | `not_observed` | `partial` | `not_observed` | `partial` | `observed` | `not_observed` | `partial` | [report.md](../reports/test_set/TEST-020_deepmedic__deepmedic/report.md) |

---

## 3. Distribuição dos Status por Regra nos 20 Repositórios

| Rule ID | Observed | Partial | Not Observed | Not Applicable | Unable to Assess |
|---|---:|---:|---:|---:|---:|
| `R01` | 19 | 1 | 0 | 0 | 0 |
| `R02` | 0 | 14 | 6 | 0 | 0 |
| `R03` | 12 | 2 | 6 | 0 | 0 |
| `R04` | 9 | 1 | 10 | 0 | 0 |
| `R05` | 0 | 18 | 2 | 0 | 0 |
| `R06` | 19 | 1 | 0 | 0 | 0 |
| `R07` | 0 | 17 | 3 | 0 | 0 |
| `R08` | 2 | 16 | 2 | 0 | 0 |

---

## 4. Arquivos Gerados Prontos para Comparação com os Especialistas

- **CSV com as 160 Predições da Ferramenta:** [`test_set_160_tool_predictions.csv`](./test_set_160_tool_predictions.csv)
- **CSV Resumo dos 20 Repositórios:** [`test_set_tool_results_summary.csv`](./test_set_tool_results_summary.csv)
- **JSON Resumo dos 20 Repositórios:** [`test_set_tool_results_summary.json`](./test_set_tool_results_summary.json)
- **Planilha em Branco do Especialista 1 (160 linhas):** [`templates/expert_annotation_reviewer_1_template.csv`](./templates/expert_annotation_reviewer_1_template.csv)
- **Planilha em Branco do Especialista 2 (160 linhas):** [`templates/expert_annotation_reviewer_2_template.csv`](./templates/expert_annotation_reviewer_2_template.csv)
- **Planilha em Branco do Adjudicador 3 (160 linhas):** [`templates/expert_annotation_adjudicator_3_template.csv`](./templates/expert_annotation_adjudicator_3_template.csv)
- **Planilha em Branco do Consenso Final (160 linhas):** [`templates/expert_annotation_consensus_template.csv`](./templates/expert_annotation_consensus_template.csv)

### Como Calcular as Métricas Finais Assim que as Planilhas dos Especialistas Retornarem

```bash
python -m traceast score-consensus \
  --consensus-csv ./evaluation_artifacts/templates/expert_annotation_consensus_template.csv \
  --predictions-csv ./evaluation_artifacts/test_set_160_tool_predictions.csv \
  --reviewer1-csv ./evaluation_artifacts/templates/expert_annotation_reviewer_1_template.csv \
  --reviewer2-csv ./evaluation_artifacts/templates/expert_annotation_reviewer_2_template.csv \
  --out ./evaluation_artifacts
```
