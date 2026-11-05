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

- **Nome do Projeto:** TEST-001_Project-MONAI__MONAI
- **Commit SHA Analisado:** `c5bddb21ccaaf3654a87c65ede6d2c7bd82e4128`
- **Data e Horário da Execução (UTC):** `2026-11-04T22:14:22.555361+00:00`
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

- **Quantidade total de arquivos encontrados:** 1602
- **Quantidade de arquivos Python (`.py`):** 1353
- **Arquivos Python analisados com sucesso:** 1353
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
- **Descrição:** Evidência identificada: todos os 1353 arquivos Python encontrados foram analisados com sucesso via AST (cobertura de inspeção: 100.0%).
- **Justificativa de Rastreabilidade:** Inspeção concluída sem falhas de parsing em 1353/1353 arquivos Python.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `setup.py` | `<module>` | 1–170 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 64757806598d...) |
| `versioneer.py` | `<module>` | 1–2277 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 3ec63afc75b5...) |
| `docs/source/conf.py` | `<module>` | 1–223 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: b804b053aa63...) |
| `monai/__init__.py` | `<module>` | 1–139 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 77ea24bac7dd...) |
| `monai/_version.py` | `<module>` | 1–683 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 17ab6eb3a246...) |
| `monai/_extensions/__init__.py` | `<module>` | 1–14 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 4d183805c9d5...) |
| `monai/_extensions/loader.py` | `<module>` | 1–95 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: d4cb9da483e7...) |
| `monai/apps/__init__.py` | `<module>` | 1–25 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 618d313b56c6...) |
| `monai/apps/datasets.py` | `<module>` | 1–745 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 7487ae5c6cbd...) |
| `monai/apps/utils.py` | `<module>` | 1–471 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 55cda53ed492...) |
| `monai/apps/auto3dseg/__init__.py` | `<module>` | 1–25 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 24e4b15dc6e0...) |
| `monai/apps/auto3dseg/__main__.py` | `<module>` | 1–35 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 6894ac70405c...) |
| `monai/apps/auto3dseg/auto_runner.py` | `<module>` | 1–921 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 86daedffe9d5...) |
| `monai/apps/auto3dseg/bundle_gen.py` | `<module>` | 1–757 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: cd5691b51f75...) |
| `monai/apps/auto3dseg/data_analyzer.py` | `<module>` | 1–386 | `parsed_python_file` | Arquivo Python analisado com sucesso (SHA-256: 2ddd9f6fc321...) |

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
- **Descrição:** Evidência parcial: manifesto(s) de dependências localizado(s) (docs/requirements.txt, pyproject.toml), contendo 4 pacote(s) com versão fixada e 41 pacote(s) sem versão exata fixada. Imports externos não declarados no manifesto: PIL, absolute_volume_difference, acti_norm, activation, active_learning_metrics, adaptors, adversarial_loss, ahnet, algo_gen, analyzer, aspp, attentionunet, aucm_loss, auto_runner, autoencoder, autoencoderkl, average_precision, backbone_fpn_utils, barlow_twins, basic_unet, basic_unetplusplus, batchgenerators, boundary_loss, box_ops, box_utils, bundle_gen, cProfile, cablock, calibration, checkpoint_loader, checkpoint_saver, class_activation_maps, classification_saver, classifier, cldice, clearml_handlers, client_algo, compare_sources, component_store, compose, config_item, config_parser, confusion_matrix, conjugate_gradient, contrastive, controlnet, convnext, convolutions, convutils, crf, croppad, crossattention, csv_saver, cumulative_average, cupy, cx_Freeze, daf3d, data_analyzer, dataloader, dataset, dataset_summary, datasets, ddim, ddpm, decathlon_datalist, decollate_batch, decorators, deform, denseblock, densenet, deprecate_utils, deviceconfig, dice, dictionary, diffusion_model_unet, dints, dints_block, dist, downsample, drop_path, ds_loss, dynunet, dynunet_block, earlystop_handler, efficientnet, embedding_collapse, encoder, ensemble_builder, enums, evaluator, f_beta_score, factories, fcn, feature_pyramid_network, fid, filtering, flexible_unet, focal_loss, folder_layout, froc, fullyconnectednet, garbage_collector, generalized_dice, generator, giou_loss, gmm, gradient_based, grid_dataset, hausdorff_distance, hausdorff_loss, highresnet, hovernet, hovernet_loss, hpo_gen, hyena, hyena_nd_unetr, ignite, ignite_metric, image_dataset, image_dissimilarity, image_reader, image_writer, img2tensorboard, inferer, intensity, inverse, inverse_batch_transform, iterable_dataset, itk_torch_bridge, jupyter_utils, label_desc, layer_norm_nd, lazy, lesion_froc, loader, localnet_block, logfile_handler, loss_metric, losses, lr_finder, lr_schedule_handler, lr_scheduler, masked_autoencoder_vit, matplotlib, mcc_loss, mean_dice, mean_iou, meandice, meaniou, mednext, mednext_block, merger, meta_obj, meta_tensor, meta_utility, metric, metric_logger, metrics, metrics_reloaded_handler, metrics_saver, milmodel, min_classes, misc, mlflow_handler, mlp, mmars, mmd, model_desc, module, monai_algo, multi_scale, nacl_loss, navit, netadapter, nnunet_bundle, nnunetv2, nnunetv2_runner, novograd, nrrd, nvtx, nvtx_handlers, occlusion_sensitivity, odict, operations, ordering, panoptic_quality, parameter_scheduler, patchembedding, patchgan_discriminator, perceptual, pndm, post, postprocessing, pretrainedmodels, probability_maps, profiling, properties, py2exe, quicknat, rectified_flow, reference_resolver, regression, regression_metrics, regressor, regularization, regunet, regunet_block, resnet, roc_auc, rocauc, safeeval, samplers, scheduler, scripts, seg_summarizer, segresnet, segresnet_block, segresnet_ds, selfattention, senet, setuptools, simplelayers, skimage, sklearn, smartcache_handler, smooth_field, spade_autoencoderkl, spade_diffusion_model_unet, spade_network, spade_norm, spatial, spatial_mask, spatial_transforms, spatialattention, spectral_loss, splitter, sqlalchemy, squeeze_and_excitation, ssim_loss, stain, state_cacher, stats_handler, sure_loss, surface_dice, surface_distance, swin_unetr, synthetic, tensorboard_handlers, test_time_augmentation, tf32, thread_buffer, tomli, torchscript_utils, torchvision, torchvision_fc, tqdm, trainer, traits, transchex, transform, transformer, transformerblock, transforms, trt_compiler, trt_handler, tversky, type_conversion, type_definitions, ultrasound_confidence_map, unet, unetr, unetr_block, unified_focal_loss, upsample, utility, utils, utils_morphological_ops, utils_pytorch_numpy_unification, validation_handler, varautoencoder, vector_quantizer, vista3d, visualizer, vit, vitautoenc, vnet, voxelmorph, vqvae, warp, weight_init, workflow, workflows, wrapper, wsi_datasets, wsi_reader. Componentes de IA/ML: Hugging Face Transformers, MONAI (Medical Open Network for AI), NiBabel, ONNX, ONNX Runtime, OpenCV, PyDICOM, PyTorch, TorchVision, opencv-python-headless, scikit-learn.
- **Justificativa de Rastreabilidade:** A presença de dependências sem versão fixada ou imports omitidos não representa automaticamente uma não conformidade, mas é um indicador técnico que merece investigação para controle de SOUP.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `docs/requirements.txt` | `torch` | 1–1 | `dependency_declaration` | Pacote 'torch' declarado em 'docs/requirements.txt' (especificador: '>=2.8.0', fixado: False, importado no código: True) |
| `docs/requirements.txt` | `numpy` | 2–2 | `dependency_declaration` | Pacote 'numpy' declarado em 'docs/requirements.txt' (especificador: '>=1.24,<3.0', fixado: False, importado no código: True) |
| `docs/requirements.txt` | `pytorch-ignite` | 3–3 | `dependency_declaration` | Pacote 'pytorch-ignite' declarado em 'docs/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `itk` | 4–4 | `dependency_declaration` | Pacote 'itk' declarado em 'docs/requirements.txt' (especificador: '>=5.2', fixado: False, importado no código: True) |
| `docs/requirements.txt` | `nibabel` | 5–5 | `dependency_declaration` | Pacote 'nibabel' declarado em 'docs/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `docs/requirements.txt` | `parameterized` | 6–6 | `dependency_declaration` | Pacote 'parameterized' declarado em 'docs/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `docs/requirements.txt` | `scikit-image` | 7–7 | `dependency_declaration` | Pacote 'scikit-image' declarado em 'docs/requirements.txt' (especificador: '>=0.19.0', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `scipy` | 8–8 | `dependency_declaration` | Pacote 'scipy' declarado em 'docs/requirements.txt' (especificador: '>=1.12.0', fixado: False, importado no código: True) |
| `docs/requirements.txt` | `tensorboard` | 9–9 | `dependency_declaration` | Pacote 'tensorboard' declarado em 'docs/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: True) |
| `docs/requirements.txt` | `commonmark` | 10–10 | `dependency_declaration` | Pacote 'commonmark' declarado em 'docs/requirements.txt' (especificador: '==0.9.1', fixado: True, importado no código: False) |
| `docs/requirements.txt` | `recommonmark` | 11–11 | `dependency_declaration` | Pacote 'recommonmark' declarado em 'docs/requirements.txt' (especificador: '==0.6.0', fixado: True, importado no código: False) |
| `docs/requirements.txt` | `Sphinx` | 12–12 | `dependency_declaration` | Pacote 'Sphinx' declarado em 'docs/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `pydata-sphinx-theme` | 13–13 | `dependency_declaration` | Pacote 'pydata-sphinx-theme' declarado em 'docs/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `sphinxcontrib-applehelp` | 14–14 | `dependency_declaration` | Pacote 'sphinxcontrib-applehelp' declarado em 'docs/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
| `docs/requirements.txt` | `sphinxcontrib-devhelp` | 15–15 | `dependency_declaration` | Pacote 'sphinxcontrib-devhelp' declarado em 'docs/requirements.txt' (especificador: 'sem versão', fixado: False, importado no código: False) |
*... e mais 454 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência identificada: 909 arquivo(s) de teste localizado(s) (diretórios: tests; frameworks: unittest; 3858 função(ões)/método(s) de teste).
- **Justificativa de Rastreabilidade:** Módulos e funções de teste automatizado foram observados no repositório.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `monai/data/test_time_augmentation.py` | `TestTimeAugmentation.__init__` | 115–157 | `test_module` | Módulo de teste 'monai/data/test_time_augmentation.py' identificado (3 funções/métodos candidatos de teste). |
| `tests/__init__.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/__init__.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/clang_format_utils.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/clang_format_utils.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/croppers.py` | `CropTest.get_arr` | 28–29 | `test_module` | Módulo de teste 'tests/croppers.py' identificado (6 funções/métodos candidatos de teste). |
| `tests/hvd_evenly_divisible_all_gather.py` | `HvdEvenlyDivisibleAllGather.test_data` | 24–29 | `test_module` | Módulo de teste 'tests/hvd_evenly_divisible_all_gather.py' identificado (2 funções/métodos candidatos de teste). |
| `tests/lazy_transforms_utils.py` | `test_resampler_lazy` | 34–91 | `test_module` | Módulo de teste 'tests/lazy_transforms_utils.py' identificado (1 funções/métodos candidatos de teste). |
| `tests/min_tests.py` | `<test_module>` | 1–1 | `test_module` | Módulo de teste 'tests/min_tests.py' identificado (0 funções/métodos candidatos de teste). |
| `tests/nonconfig_workflow.py` | `NonConfigWorkflow.__init__` | 40–57 | `test_module` | Módulo de teste 'tests/nonconfig_workflow.py' identificado (13 funções/métodos candidatos de teste). |
| `tests/padders.py` | `PadTest.get_arr` | 55–56 | `test_module` | Módulo de teste 'tests/padders.py' identificado (5 funções/métodos candidatos de teste). |
| `tests/runner.py` | `TimeLoggingTestResult.__init__` | 45–47 | `test_module` | Módulo de teste 'tests/runner.py' identificado (3 funções/métodos candidatos de teste). |
| `tests/test_call_dist.py` | `DistributedCallTest.test_constructor` | 20–27 | `test_module` | Módulo de teste 'tests/test_call_dist.py' identificado (1 funções/métodos candidatos de teste). |
| `tests/test_query_memory.py` | `TestQueryMemory.test_output_str` | 20–24 | `test_module` | Módulo de teste 'tests/test_query_memory.py' identificado (1 funções/métodos candidatos de teste). |
| `tests/test_segresnet_ds.py` | `TestSegResNetDSShapeLogic.test_shape_factor_isotropic` | 34–47 | `test_module` | Módulo de teste 'tests/test_segresnet_ds.py' identificado (5 funções/métodos candidatos de teste). |
| `tests/test_timedcall_dist.py` | `TestTimedCall.test_good_call` | 53–55 | `test_module` | Módulo de teste 'tests/test_timedcall_dist.py' identificado (5 funções/métodos candidatos de teste). |
| `tests/test_utils.py` | `test_pretrained_networks` | 191–193 | `test_module` | Módulo de teste 'tests/test_utils.py' identificado (27 funções/métodos candidatos de teste). |
*... e mais 894 evidência(s) registrada(s) em `findings.json`.*

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
- **Descrição:** Evidência identificada: 15 configuração(ões) de CI/CD localizada(s) com comandos declarados para execução automatizada de testes (evidências de cobertura: .github/workflows/cron.yml:67, .github/workflows/cron.yml:115, .github/workflows/cron.yml:219, .github/workflows/pythonapp-gpu.yml:114, .github/workflows/pythonapp-gpu.yml:126, .github/workflows/setupapp.yml:78, .github/workflows/setupapp.yml:123, .github/workflows/setupapp.yml:126).
- **Justificativa de Rastreabilidade:** Arquivos de workflow CI/CD contendo etapas de execução de testes foram encontrados.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `.github/workflows/blossom-ci.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/blossom-ci.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/build_docs.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/build_docs.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/chatops.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/chatops.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/cicd_tests.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/cicd_tests.yml' (comandos de teste: python -m unittest -v, python -m pip install --upgrade pip wheel tomli pytest, python -m pytest -v \; cobertura: False) |
| `.github/workflows/codeql-analysis.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/codeql-analysis.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/conda.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/conda.yml' (comandos de teste: $(pwd)/runtests.sh --build --unittests; cobertura: False) |
| `.github/workflows/cron-ngc-bundle.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/cron-ngc-bundle.yml' (comandos de teste: PYTHONPATH=. python -m unittest tests.bundle.test_bundle_download.TestNgcBundleDownload; cobertura: False) |
| `.github/workflows/cron.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/cron.yml' (comandos de teste: BUILD_MONAI=1 ./runtests.sh --build --coverage --unittests --disttests  # unit tests with coverage report, BUILD_MONAI=1 ./runtests.sh --build --coverage --unittests --disttests  # unit tests with coverage report, BUILD_MONAI=1 ./runtests.sh --build --coverage --pyrefly --unittests --disttests  # unit tests with pyrefly checks, coverage report; cobertura: True) |
| `.github/workflows/docker.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/docker.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/integration.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/integration.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/pythonapp-gpu.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/pythonapp-gpu.yml' (comandos de teste: export CUDA_VISIBLE_DEVICES=$(coverage run -m tests.utils | tail -n 1), ./runtests.sh --quick --unittests, coverage run -m tests.clang_format_utils; cobertura: True) |
| `.github/workflows/pythonapp-hyena-gpu.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/pythonapp-hyena-gpu.yml' (comandos de teste: python -m pytest -v \; cobertura: False) |
| `.github/workflows/release.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/release.yml' (comandos de teste: nenhum detectado; cobertura: False) |
| `.github/workflows/setupapp.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/setupapp.yml' (comandos de teste: #       BUILD_MONAI=1 ./runtests.sh --build --coverage --unittests --disttests  # unit tests with coverage report, #       ./runtests.sh --coverage --quick --unittests --disttests, #       #BUILD_MONAI=0 ./runtests.sh --build --coverage --quick --unittests; cobertura: True) |
| `.github/workflows/weekly-preview.yml` | `ci_workflow` | 1–1 | `ci_workflow` | Workflow CI '.github/workflows/weekly-preview.yml' (comandos de teste: nenhum detectado; cobertura: False) |

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
- **Descrição:** Evidência parcial: entre 479 operação(ões) candidatas de I/O, 16 possuem bloco try-except não vazio e 463 não possuem tratamento local observável. Foram identificados 37 bloco(s) except vazios ou com 'pass'.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: coexistem operações de I/O sem captura local de exceção ou blocos except que suprimem falhas com pass.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `setup.py` | `get_extensions` | 117–122 | `ast_empty_or_pass_except` | Bloco try-except em 'get_extensions' possui handler vazio ou com instrução 'pass' (exceções: ValueError) |
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
- **Descrição:** Evidência identificada: 5853 sinal(is) estrutural(is) de validação de entrada localizado(s), incluindo 1965 função(ões)/chamada(s) de validação e 1513 guarda(s) condicional(is) com levantamento de exceção.
- **Justificativa de Rastreabilidade:** Foram identificados mecanismos explícitos de verificação de entrada no código. A presença estrutural não garante suficiência clínica ou completude da validação.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `setup.py` | N/A | 50–51 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em '<module>' |
| `setup.py` | `torch_parallel_backend` | 65–66 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'torch_parallel_backend' |
| `setup.py` | `get_extensions` | 128–129 | `validation_conditional_guard` | Sinal de validação (conditional_guard) em 'get_extensions' |
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
- **Descrição:** Evidência parcial: foram identificados 187 sinal(is) de carregamento, salvamento ou referência a checkpoints de modelos (0 arquivo(s) de modelo no repositório). A existência de chamadas de carga ou arquivos .pt/.pth/.onnx não comprova proveniência completa nem controle de versão do modelo.
- **Justificativa de Rastreabilidade:** Indicador técnico que merece investigação: artefatos de modelo exigem rastreabilidade documental de versão, dataset de treinamento, hiperparâmetros e verificação de integridade (hash).

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `monai/apps/auto3dseg/utils.py` | `import_bundle_algo_history` | 47–47 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em 'import_bundle_algo_history' |
| `monai/apps/mmars/model_desc.py` | N/A | 63–63 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `monai/apps/mmars/model_desc.py` | N/A | 73–73 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `monai/apps/mmars/model_desc.py` | N/A | 83–83 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `monai/apps/mmars/model_desc.py` | N/A | 92–92 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `monai/apps/mmars/model_desc.py` | N/A | 102–102 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `monai/apps/mmars/model_desc.py` | N/A | 111–111 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `monai/apps/mmars/model_desc.py` | N/A | 120–120 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `monai/apps/mmars/model_desc.py` | N/A | 130–130 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `monai/apps/mmars/model_desc.py` | N/A | 139–139 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `monai/apps/mmars/model_desc.py` | N/A | 148–148 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `monai/apps/mmars/model_desc.py` | N/A | 158–158 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `monai/apps/mmars/model_desc.py` | N/A | 168–168 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `monai/apps/mmars/model_desc.py` | N/A | 177–177 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
| `monai/apps/mmars/model_desc.py` | N/A | 187–187 | `model_checkpoint_reference` | Operação/referência de modelo (checkpoint_reference) em '<module>' |
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
- **Descrição:** Evidência parcial: sinais estruturais de treinamento e de inferência coexistem no(s) mesmo(s) arquivo(s) (monai/apps/auto3dseg/auto_runner.py, monai/apps/auto3dseg/bundle_gen.py, monai/apps/auto3dseg/hpo_gen.py, monai/apps/detection/networks/retinanet_detector.py, monai/apps/nnunet/nnunet_bundle.py, monai/apps/nnunet/nnunetv2_runner.py, monai/auto3dseg/algo_gen.py, monai/inferers/inferer.py, monai/metrics/embedding_collapse.py, monai/networks/nets/hovernet.py, monai/networks/nets/resnet.py, monai/networks/nets/transchex.py, monai/networks/utils.py, monai/visualize/class_activation_maps.py, tests/bundle/test_bundle_workflow.py, tests/integration/test_auto3dseg_ensemble.py, tests/integration/test_integration_classification_2d.py, tests/integration/test_integration_fast_train.py, tests/integration/test_integration_gpu_customization.py, tests/integration/test_integration_lazy_samples.py, tests/integration/test_integration_segmentation_3d.py, tests/integration/test_integration_stn.py, tests/integration/test_integration_workflows.py, tests/integration/test_reg_loss_integration.py, tests/integration/test_seg_loss_integration.py, tests/losses/test_aucm_loss.py, tests/losses/test_generalized_wasserstein_dice_loss.py, tests/networks/blocks/test_hyena_block.py, tests/networks/layers/test_layer_norm_nd.py, tests/networks/layers/test_vector_quantizer.py, tests/networks/nets/test_dynunet.py, tests/networks/nets/test_fullyconnectednet.py, tests/networks/nets/test_mednext.py, tests/networks/nets/test_navit.py, tests/networks/nets/test_segresnet_ds.py, tests/networks/nets/test_swin_unetr.py, tests/networks/nets/test_varautoencoder.py, tests/networks/schedulers/test_scheduler_ddim.py, tests/networks/schedulers/test_scheduler_ddpm.py, tests/networks/schedulers/test_scheduler_pndm.py, tests/networks/schedulers/test_scheduler_rflow.py, tests/networks/utils/test_train_mode.py, tests/optimizers/test_lr_scheduler.py). Indicador técnico que merece investigação quanto à segregação arquitetural entre desenvolvimento/treino e produção/inferência.
- **Justificativa de Rastreabilidade:** Coexistência de sinais de treinamento e inferência em monai/apps/auto3dseg/auto_runner.py, monai/apps/auto3dseg/bundle_gen.py, monai/apps/auto3dseg/hpo_gen.py, monai/apps/detection/networks/retinanet_detector.py, monai/apps/nnunet/nnunet_bundle.py, monai/apps/nnunet/nnunetv2_runner.py, monai/auto3dseg/algo_gen.py, monai/inferers/inferer.py, monai/metrics/embedding_collapse.py, monai/networks/nets/hovernet.py, monai/networks/nets/resnet.py, monai/networks/nets/transchex.py, monai/networks/utils.py, monai/visualize/class_activation_maps.py, tests/bundle/test_bundle_workflow.py, tests/integration/test_auto3dseg_ensemble.py, tests/integration/test_integration_classification_2d.py, tests/integration/test_integration_fast_train.py, tests/integration/test_integration_gpu_customization.py, tests/integration/test_integration_lazy_samples.py, tests/integration/test_integration_segmentation_3d.py, tests/integration/test_integration_stn.py, tests/integration/test_integration_workflows.py, tests/integration/test_reg_loss_integration.py, tests/integration/test_seg_loss_integration.py, tests/losses/test_aucm_loss.py, tests/losses/test_generalized_wasserstein_dice_loss.py, tests/networks/blocks/test_hyena_block.py, tests/networks/layers/test_layer_norm_nd.py, tests/networks/layers/test_vector_quantizer.py, tests/networks/nets/test_dynunet.py, tests/networks/nets/test_fullyconnectednet.py, tests/networks/nets/test_mednext.py, tests/networks/nets/test_navit.py, tests/networks/nets/test_segresnet_ds.py, tests/networks/nets/test_swin_unetr.py, tests/networks/nets/test_varautoencoder.py, tests/networks/schedulers/test_scheduler_ddim.py, tests/networks/schedulers/test_scheduler_ddpm.py, tests/networks/schedulers/test_scheduler_pndm.py, tests/networks/schedulers/test_scheduler_rflow.py, tests/networks/utils/test_train_mode.py, tests/optimizers/test_lr_scheduler.py. Requer inspeção humana do fluxo de controle para verificar se o modelo é congelado em produção.

#### Evidências Extraídas (Arquivos e Linhas)
| Arquivo | Símbolo | Linhas | Tipo | Descrição |
|---|---|---|---|---|
| `monai/apps/auto3dseg/auto_runner.py` | `AutoRunner.set_training_params` | 532–552 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'AutoRunner.set_training_params' |
| `monai/apps/auto3dseg/auto_runner.py` | `AutoRunner._train_algo_in_sequence` | 732–755 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'AutoRunner._train_algo_in_sequence' |
| `monai/apps/auto3dseg/auto_runner.py` | `AutoRunner._train_algo_in_sequence` | 749–749 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'AutoRunner._train_algo_in_sequence' |
| `monai/apps/auto3dseg/auto_runner.py` | `AutoRunner._train_algo_in_sequence` | 751–751 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'AutoRunner._train_algo_in_sequence' |
| `monai/apps/auto3dseg/auto_runner.py` | `AutoRunner._train_algo_in_nni` | 757–824 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'AutoRunner._train_algo_in_nni' |
| `monai/apps/auto3dseg/auto_runner.py` | `AutoRunner.set_prediction_params` | 651–667 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'AutoRunner.set_prediction_params' |
| `monai/apps/auto3dseg/auto_runner.py` | `AutoRunner.run` | 864–870 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'AutoRunner.run' |
| `monai/apps/auto3dseg/auto_runner.py` | `AutoRunner.run` | 872–872 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'AutoRunner.run' |
| `monai/apps/auto3dseg/bundle_gen.py` | `BundleAlgo.train` | 337–358 | `ast_training_signal` | Sinal estrutural de treinamento (training_function) em 'BundleAlgo.train' |
| `monai/apps/auto3dseg/bundle_gen.py` | `BundleAlgo.get_inferer` | 373–409 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'BundleAlgo.get_inferer' |
| `monai/apps/auto3dseg/bundle_gen.py` | `BundleAlgo.predict` | 411–422 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'BundleAlgo.predict' |
| `monai/apps/auto3dseg/ensemble_builder.py` | `AlgoEnsemble.set_infer_files` | 86–107 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'AlgoEnsemble.set_infer_files' |
| `monai/apps/auto3dseg/ensemble_builder.py` | `AlgoEnsemble.__call__` | 214–214 | `ast_inference_signal` | Sinal estrutural de inferência (inference_call) em 'AlgoEnsemble.__call__' |
| `monai/apps/auto3dseg/ensemble_builder.py` | `AlgoEnsembleBuilder.add_inferer` | 361–375 | `ast_inference_signal` | Sinal estrutural de inferência (inference_function) em 'AlgoEnsembleBuilder.add_inferer' |
| `monai/apps/auto3dseg/hpo_gen.py` | `NNIGen.run_algo` | 313–313 | `ast_training_signal` | Sinal estrutural de treinamento (training_call) em 'NNIGen.run_algo' |
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
