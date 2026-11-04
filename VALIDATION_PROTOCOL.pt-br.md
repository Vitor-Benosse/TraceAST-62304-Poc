# Protocolo de Validação Científica — TraceAST-62304 v1.0 (Português)

[![en](https://img.shields.io/badge/lang-English%20(Main)-blue.svg)](./VALIDATION_PROTOCOL.md)
[![pt-br](https://img.shields.io/badge/lang-Portugu%C3%AAs%20(pt--BR)-green.svg)](./VALIDATION_PROTOCOL.pt-br.md)

> 🌐 **Language / Idioma:** **[Read in English (Primary) — `VALIDATION_PROTOCOL.md`](./VALIDATION_PROTOCOL.md)** | **Português (`VALIDATION_PROTOCOL.pt-br.md`)**
> 📖 **Portal Interativo:** [Documentação Completa (PT-BR)](./docs/index.pt-br.html) | [Full Documentation Portal (EN)](./docs/index.html)

**Estudo Alvo:** Submissão à *JMIR Medical Informatics*
**Posicionamento:** *AI-assisted, evidence-traceable pre-audit screening for medical software development repositories.*

---

## 1. Objetivo do Estudo de Validação

Avaliar a capacidade do **TraceAST-62304** de identificar indicadores técnicos rastreáveis (`R01`–`R08`) e recuperar referências normativas relevantes (ANVISA RDC 657/2022 e IEC 62304) em repositórios de software médico em Python, comparando o desempenho determinístico da ferramenta contra o padrão de referência (*reference standard*) estabelecido por especialistas humanos independentes.

---

## 2. Separação Estrita entre Conjunto de Desenvolvimento e Conjunto de Teste

Para garantir validade científica e evitar sobreajuste (*data leakage* / *rule overfitting*):

1. **Conjunto de Desenvolvimento (`development_split`):**
   - Inclui as *fixtures* sintéticas controladas (`tests/fixtures/`) e o repositório `Medical-Report-Generator-from-Chest-X-Ray-Images` utilizado na concepção inicial da Prova de Conceito.
   - O repositório `Medical-Report-Generator-from-Chest-X-Ray-Images` permanece bloqueado no conjunto de desenvolvimento em `evaluation_artifacts/dataset_split_manifest.json` e **não deve ser reportado como validação externa independente**.
2. **Conjunto de Teste Externo (`external_test_split`):**
   - Composto por pelo menos $N = 20$ repositórios públicos de software médico/IA médica em Python selecionados por critérios de inclusão pré-especificados.
   - **Regra de Congelamento:** O catálogo de regras (`RULE_CATALOG_VERSION = 1.0.0`, registrado via SHA-256 no `run_manifest.json`) deve ser congelado antes da execução no conjunto de teste. Nenhuma heurística pode ser ajustada após observar resultados do conjunto de teste.

---

## 3. Procedimento de Anotação por Especialistas Humanos (Padrão de Referência)

Os templates oficiais são gerados pelo comando:

```bash
python -m traceast evaluate --out ./evaluation_artifacts
```

Isso produz quatro arquivos JSON em `evaluation_artifacts/`:
- `expert_1_annotation_sheet.json` (Avaliador Independente 1)
- `expert_2_annotation_sheet.json` (Avaliador Independente 2)
- `expert_3_adjudication_sheet.json` (Avaliador 3 — Desempate/Adjudicação)
- `consensus_reference_standard.json` (Consenso Final Consolidado)

### Regras do Processo de Anotação Cega:
1. **Independência:** Os Avaliadores 1 e 2 inspecionam cada repositório de forma independente e cega em relação à saída do TraceAST-62304 e um ao outro.
2. **Registro Estruturado:** Para cada par `(repository_id, rule_id)`, o avaliador preenche:
   - Estado da evidência (`observed`, `partial`, `not_observed`, `unable_to_assess`, `not_applicable`);
   - Prioridade de revisão (`high`, `medium`, `low`, `informational`);
   - Arquivo e linha relacionados;
   - Justificativa técnica;
   - Se o ponto mereceria investigação em uma auditoria humana formal (`warrants_human_audit_investigation`).
3. **Concordância Inter-Avaliadores (*Cohen's Kappa*):** Antes da reconciliação, os rótulos originais dos Avaliadores 1 e 2 são preservados e submetidos a `compute_cohens_kappa` para relatar o coeficiente $\kappa$ no artigo.
4. **Adjudicação:** Divergências entre os Avaliadores 1 e 2 são resolvidas pelo Avaliador 3, gerando o arquivo `consensus_reference_standard.json`.

---

## 4. Métricas Estatísticas e Regras de Pontuação

O motor de pontuação (`traceast/evaluation.py`) compara os achados da ferramenta com o consenso humano seguindo estas definições:

- **Sinal Positivo de Indicador:** `observed` ou `partial`.
- **Sinal Negativo de Indicador:** `not_observed`.
- **Regra de Inaplicabilidade:** Quando o consenso humano classifica uma regra como `not_applicable` ou `unable_to_assess`, um resultado `not_observed` ou `not_applicable` da ferramenta é contabilizado como **True Negative (`TN`)**, e **nunca como False Negative (`FN`)**.
- **Métricas Calculadas (por regra e agregadas micro/macro):**
  - *True Positives* (TP), *False Positives* (FP), *False Negatives* (FN), *True Negatives* (TN)
  - $\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$
  - $\text{Recall (Sensitivity)} = \frac{\text{TP}}{\text{TP} + \text{FN}}$
  - $\text{F1-score} = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$
- **Intervalos de Confiança (95% CI):** Calculados por **Cluster Bootstrap** ($B = 1000$ reamostragens com reposição), utilizando o `repository_id` como unidade primária de reamostragem para respeitar a correlação intra-repositório entre as 8 regras.

---

## 5. Avaliação da Recuperação Documental (RAG `Recall@3`)

1. O arquivo de consultas de referência associa cada regra (`R01`–`R08`) aos documentos normativos relevantes esperados na base (`ANVISA_RDC_657_2022` e templates/mapeamentos `IEC62304`).
2. Para cada consulta, o sistema recupera os $k = 3$ fragmentos de maior similaridade e calcula:
   - **Hit Rate Recall@3:** Proporção de regras em que ao menos um documento de referência relevante está presente no top-3 recuperado.
   - **Fractional Recall@3:** Proporção média das referências relevantes esperadas recuperadas no top-3.

