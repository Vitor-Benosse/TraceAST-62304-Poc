"""Versioned catalog of the 8 deterministic pre-audit rules (R01-R08) for TraceAST-62304."""

from __future__ import annotations

import hashlib
import json
from typing import Dict, List

from traceast.models import (
    MappingStatus,
    RegulatoryReference,
    ReviewPriority,
    RuleDefinition,
)

RULE_CATALOG_VERSION = "1.0.0"

RULE_DEFINITIONS: List[RuleDefinition] = [
    RuleDefinition(
        rule_id="R01",
        version=RULE_CATALOG_VERSION,
        title="Cobertura e integridade da inspeção estática",
        description=(
            "Contabiliza todos os arquivos inspecionados no repositório, a proporção de arquivos Python "
            "analisados sintaticamente com sucesso via AST e registra explicitamente qualquer falha de parsing."
        ),
        objective=(
            "Garantir transparência sobre o escopo efetivamente inspecionado e impedir que arquivos com "
            "erros de sintaxe ou codificação sejam ignorados silenciosamente."
        ),
        category="Integridade da Inspeção",
        evidence_sought=(
            "Inventário completo de arquivos Python (.py), hashes SHA-256 e registro de exceções "
            "(SyntaxError, UnicodeDecodeError, OSError) durante o parsing AST."
        ),
        detection_method="Varredura recursiva determinística de diretórios e tentativa controlada de ast.parse.",
        analyzed_files_scope="Todos os arquivos .py do repositório (excluindo ambientes virtuais e caches).",
        identification_criteria=(
            "observed quando 100% dos arquivos .py são analisados com sucesso; partial quando há arquivos "
            "com falha de parsing; unable_to_assess quando não há arquivos .py ou todos falham."
        ),
        limitations=[
            "Cobertura de 100% no parsing sintático significa apenas que a árvore AST pôde ser construída, "
            "não que o código está livre de defeitos lógicos ou em conformidade normativa.",
            "Arquivos em outras linguagens de programação (C++, JavaScript, etc.) não são analisados na V1.0.",
        ],
        default_review_priority=ReviewPriority.HIGH,
        normative_references=[
            RegulatoryReference(
                document_id="IEC62304",
                document_name="IEC 62304:2006/Amd 1:2015 Medical device software — Software life cycle processes",
                issuing_body="IEC",
                clause="5.5.5",
                section_or_page="Seção 5.5 — Implementação e verificação de unidades de software",
                mapping_status=MappingStatus.PENDING_EXPERT_REVIEW,
                source="legal_documents/templates_openregulatory/techdoc/62304/62304-mapping.md",
            ),
            RegulatoryReference(
                document_id="ANVISA_RDC_657_2022",
                document_name="Resolução RDC Nº 657, de 24 de março de 2022 (Regularização de SaMD)",
                issuing_body="ANVISA",
                clause="Art. 14",
                section_or_page="Capítulo II — Dos Requisitos Gerais e Documentação Técnica",
                mapping_status=MappingStatus.PENDING_EXPERT_REVIEW,
                source="legal_documents/RDC_657_2022.pdf",
            ),
        ],
        regulatory_validation_status=MappingStatus.PENDING_EXPERT_REVIEW,
        rag_query_pt=(
            "verificação de unidades de software inspeção de código-fonte documentação técnica "
            "arquitetura ciclo de vida software médico RDC 657 IEC 62304"
        ),
        rag_query_en=(
            "software unit verification source code inspection software configuration items IEC 62304 5.5"
        ),
    ),
    RuleDefinition(
        rule_id="R02",
        version=RULE_CATALOG_VERSION,
        title="Gerenciamento de dependências e componentes externos (SOUP)",
        description=(
            "Identifica arquivos de declaração de dependências (requirements.txt, pyproject.toml, poetry.lock), "
            "versões fixadas versus abertas, bibliotecas de IA/ML e dependências importadas no código."
        ),
        objective=(
            "Apoiar o inventário preliminar de Software of Unknown Provenance (SOUP) e a rastreabilidade "
            "de bibliotecas de terceiros utilizadas no software médico."
        ),
        category="Gerenciamento de Configuração e SOUP",
        evidence_sought=(
            "Presença de arquivos de manifesto de pacotes, especificadores de versão (== vs >= ou sem versão) "
            "e cruzamento com instruções import/from no código Python."
        ),
        detection_method="Parsing estático de manifestos de dependências cruzado com nós ast.Import e ast.ImportFrom.",
        analyzed_files_scope="requirements*.txt, pyproject.toml, poetry.lock e arquivos .py.",
        identification_criteria=(
            "observed quando há manifesto de dependências com todas as versões fixadas e sem imports de terceiros "
            "omitidos; partial quando há dependências sem versão exata fixada ou imports não listados; "
            "not_observed quando nenhum manifesto é encontrado."
        ),
        limitations=[
            "Uma dependência sem versão fixada no repositório não representa automaticamente uma não conformidade, "
            "pois o congelamento de versões pode ocorrer em artefatos de build ou containers externos.",
            "A listagem em requirements.txt não substitui a documentação formal de SOUP (requisitos funcionais, "
            "nível de risco e verificação de anomalias conhecidas).",
        ],
        default_review_priority=ReviewPriority.MEDIUM,
        normative_references=[
            RegulatoryReference(
                document_id="IEC62304",
                document_name="IEC 62304:2006/Amd 1:2015 Medical device software — Software life cycle processes",
                issuing_body="IEC",
                clause="5.3.3; 5.3.4; 7.1.2; 7.1.3; 8.1.2",
                section_or_page="Controle e identificação de SOUP (Software of Unknown Provenance)",
                mapping_status=MappingStatus.PENDING_EXPERT_REVIEW,
                source="legal_documents/templates_openregulatory/techdoc/62304/soup-list.md",
            ),
            RegulatoryReference(
                document_id="ANVISA_RDC_657_2022",
                document_name="Resolução RDC Nº 657, de 24 de março de 2022",
                issuing_body="ANVISA",
                clause="Art. 14",
                section_or_page="Documentação técnica e arquitetura de software",
                mapping_status=MappingStatus.PENDING_EXPERT_REVIEW,
                source="legal_documents/RDC_657_2022.pdf",
            ),
        ],
        regulatory_validation_status=MappingStatus.PENDING_EXPERT_REVIEW,
        rag_query_pt=(
            "SOUP Software of Unknown Provenance bibliotecas de terceiros gerenciamento de configuração "
            "versão dependências IEC 62304 8.1.2 5.3.3"
        ),
        rag_query_en=(
            "SOUP list Software of Unknown Provenance third-party libraries version requirements.txt IEC 62304 8.1.2"
        ),
    ),
    RuleDefinition(
        rule_id="R03",
        version=RULE_CATALOG_VERSION,
        title="Evidências de testes automatizados no repositório",
        description=(
            "Verifica a presença de diretórios de testes, arquivos de teste (test_*.py, *_test.py), "
            "frameworks utilizados (pytest, unittest) e arquivos de configuração de testes."
        ),
        objective=(
            "Identificar indicadores observáveis de verificação de unidades e testes de sistema "
            "mantidos junto ao código-fonte."
        ),
        category="Verificação e Testes de Software",
        evidence_sought=(
            "Diretórios tests/ ou test/, módulos de teste Python, funções test_* e importação de pytest/unittest."
        ),
        detection_method="Inspeção da estrutura de diretórios e AST dos módulos de teste.",
        analyzed_files_scope="Diretórios de teste, arquivos test_*.py / *_test.py, pytest.ini, tox.ini, .coveragerc.",
        identification_criteria=(
            "observed quando existem arquivos de teste contendo funções/métodos de teste; "
            "partial quando há estrutura ou configuração de teste sem funções verificáveis; "
            "not_observed quando não há diretórios ou arquivos de teste no repositório."
        ),
        limitations=[
            "A ausência de um diretório de testes no repositório analisado indica apenas ausência de evidência "
            "observável neste repositório, e NÃO prova que o fabricante não realiza testes em outro ambiente.",
            "A presença de arquivos de teste não comprova que os testes cobrem os requisitos de segurança ou passam.",
        ],
        default_review_priority=ReviewPriority.HIGH,
        normative_references=[
            RegulatoryReference(
                document_id="IEC62304",
                document_name="IEC 62304:2006/Amd 1:2015 Medical device software — Software life cycle processes",
                issuing_body="IEC",
                clause="5.5.5; 5.6.3; 5.7",
                section_or_page="Verificação de unidade, testes de integração e testes de sistema de software",
                mapping_status=MappingStatus.PENDING_EXPERT_REVIEW,
                source="legal_documents/templates_openregulatory/techdoc/62304/software-system-test-plan.md",
            ),
            RegulatoryReference(
                document_id="ANVISA_RDC_657_2022",
                document_name="Resolução RDC Nº 657, de 24 de março de 2022",
                issuing_body="ANVISA",
                clause="Art. 14",
                section_or_page="Evidências de verificação e validação do software",
                mapping_status=MappingStatus.PENDING_EXPERT_REVIEW,
                source="legal_documents/RDC_657_2022.pdf",
            ),
        ],
        regulatory_validation_status=MappingStatus.PENDING_EXPERT_REVIEW,
        rag_query_pt=(
            "plano de testes de sistema de software verificação de unidade testes de integração "
            "validação RDC 657 IEC 62304 5.7"
        ),
        rag_query_en=(
            "software system test plan unit verification integration testing regression tests IEC 62304 5.5 5.6 5.7"
        ),
    ),
    RuleDefinition(
        rule_id="R04",
        version=RULE_CATALOG_VERSION,
        title="Integração contínua (CI/CD) e automação de verificação",
        description=(
            "Inspeciona workflows de integração contínua (.github/workflows, .gitlab-ci.yml) em busca de "
            "execução automatizada de testes e coleta de cobertura."
        ),
        objective=(
            "Verificar se existem evidências no repositório de execução automatizada e repetível "
            "de testes de regressão e verificação."
        ),
        category="Verificação e Integração Contínua",
        evidence_sought="Arquivos YAML de CI/CD e etapas contendo comandos pytest, unittest, tox ou coverage.",
        detection_method="Inspeção de arquivos de workflow em .github/workflows/*.yml e .gitlab-ci.yml.",
        analyzed_files_scope=".github/workflows/*.yml, .github/workflows/*.yaml, .gitlab-ci.yml.",
        identification_criteria=(
            "observed quando há workflow de CI com comando explícito de execução de testes; "
            "partial quando há workflow de CI sem comando explícito de teste; "
            "not_observed quando nenhum arquivo de CI/CD é encontrado."
        ),
        limitations=[
            "Pipelines de CI/CD podem estar hospedados em servidores externos (Jenkins, Azure DevOps, GitLab externo) "
            "sem arquivo de configuração versionado na pasta .github/workflows.",
            "A presença do arquivo YAML não garante que o workflow esteja ativo ou aprovado nas branches protegidas.",
        ],
        default_review_priority=ReviewPriority.LOW,
        normative_references=[
            RegulatoryReference(
                document_id="IEC62304",
                document_name="IEC 62304:2006/Amd 1:2015 Medical device software — Software life cycle processes",
                issuing_body="IEC",
                clause="5.5.5; 5.6.4; 5.6.6",
                section_or_page="Verificação contínua e testes de regressão na integração de software",
                mapping_status=MappingStatus.PENDING_EXPERT_REVIEW,
                source="legal_documents/templates_openregulatory/techdoc/62304/62304-mapping.md",
            ),
        ],
        regulatory_validation_status=MappingStatus.PENDING_EXPERT_REVIEW,
        rag_query_pt=(
            "integração contínua CI/CD testes de regressão verificação de integração pull requests IEC 62304 5.6.6"
        ),
        rag_query_en=(
            "CI/CD in GitHub Pull Requests software integration testing conduct regression tests IEC 62304 5.6.6"
        ),
    ),
    RuleDefinition(
        rule_id="R05",
        version=RULE_CATALOG_VERSION,
        title="Tratamento de erros e exceções em operações de I/O",
        description=(
            "Identifica operações candidatas de leitura e escrita de dados/arquivos e examina a presença e "
            "estrutura de blocos try-except-finally, sinalizando blocos except vazios ou com pass."
        ),
        objective=(
            "Localizar pontos de entrada/saída desprotegidos ou capturas silenciosas de exceções que "
            "possam mascarar falhas de leitura de dados ou artefatos."
        ),
        category="Confiabilidade e Tratamento de Falhas",
        evidence_sought=(
            "Chamadas de I/O (open, read_csv, dcmread, load, etc.), nós ast.Try, tipos de exceção capturados "
            "e manipuladores except vazios ou contendo apenas pass."
        ),
        detection_method="Análise AST correlacionando linhas de ast.Call de I/O com escopos ast.Try e ast.ExceptHandler.",
        analyzed_files_scope="Todos os arquivos .py analisados com sucesso.",
        identification_criteria=(
            "observed quando todas as operações de I/O detectadas estão em blocos try-except não vazios e não há "
            "except vazio/pass; partial quando parte das operações de I/O não possui try-except ou há blocos except "
            "vazios/pass; not_observed quando não há operações de I/O ou nenhuma possui tratamento."
        ),
        limitations=[
            "A presença de um bloco try-except NÃO comprova que o tratamento de erro é clinicamente seguro ou "
            "adequado aos controles de risco do dispositivo.",
            "O tratamento de exceções pode ocorrer em níveis superiores da pilha de chamadas (caller functions) "
            "não visíveis na inspeção intrafuncional.",
        ],
        default_review_priority=ReviewPriority.HIGH,
        normative_references=[
            RegulatoryReference(
                document_id="IEC62304",
                document_name="IEC 62304:2006/Amd 1:2015 Medical device software — Software life cycle processes",
                issuing_body="IEC",
                clause="5.1.12; 5.5.3; 7.1.2",
                section_or_page="Identificação de defeitos comuns e controle de falhas em unidades de software",
                mapping_status=MappingStatus.PENDING_EXPERT_REVIEW,
                source="legal_documents/templates_openregulatory/techdoc/62304/62304-mapping.md",
            ),
        ],
        regulatory_validation_status=MappingStatus.PENDING_EXPERT_REVIEW,
        rag_query_pt=(
            "identificação e prevenção de defeitos de software controle de risco falhas tratamento de erros IEC 62304 7.1"
        ),
        rag_query_en=(
            "identification and avoidance of common software defects risk control measures software units IEC 62304 5.1.12 7.1.2"
        ),
    ),
    RuleDefinition(
        rule_id="R06",
        version=RULE_CATALOG_VERSION,
        title="Sinais estruturais de validação de entradas",
        description=(
            "Identifica mecanismos candidatos de validação de dados de entrada (funções de validação, "
            "verificações de tipo/None com levantamento de exceção, schemas e asserts)."
        ),
        objective=(
            "Auxiliar a equipe técnica a mapear onde os dados recebidos pelo software ou pelo modelo "
            "passam por verificação estrutural antes do processamento."
        ),
        category="Verificação de Interfaces e Entradas",
        evidence_sought=(
            "Funções com semântica de validação (validate_*, check_*, verify_*), condicionais que verificam "
            "isinstance/None e levantam exceção, chamadas de validação de schema e instruções assert."
        ),
        detection_method="Inspeção AST de definições de função, nós ast.If com ast.Raise, ast.Assert e chamadas de validação.",
        analyzed_files_scope="Todos os arquivos .py analisados com sucesso.",
        identification_criteria=(
            "observed quando há funções dedicadas de validação ou guardas condicionais que levantam exceção; "
            "partial quando há apenas verificações genéricas (como assert simples); "
            "not_observed quando nenhum sinal estrutural de validação é encontrado."
        ),
        limitations=[
            "A presença de uma condição if ou função de validação NÃO garante que os limites fisiológicos, "
            "formatos DICOM ou restrições clínicas de entrada foram devidamente validados.",
            "Instruções assert em Python podem ser desabilitadas em execução otimizada (python -O).",
        ],
        default_review_priority=ReviewPriority.MEDIUM,
        normative_references=[
            RegulatoryReference(
                document_id="IEC62304",
                document_name="IEC 62304:2006/Amd 1:2015 Medical device software — Software life cycle processes",
                issuing_body="IEC",
                clause="5.2.2; 5.3.2; 5.4.3",
                section_or_page="Requisitos de interfaces entre itens de software e validação de entradas",
                mapping_status=MappingStatus.PENDING_EXPERT_REVIEW,
                source="legal_documents/templates_openregulatory/techdoc/62304/software-architecture-checklist.md",
            ),
        ],
        regulatory_validation_status=MappingStatus.PENDING_EXPERT_REVIEW,
        rag_query_pt=(
            "requisitos de software interfaces dados de entrada arquitetura de interfaces verificação IEC 62304 5.3.2"
        ),
        rag_query_en=(
            "develop an architecture for the interfaces of software items input validation software requirements IEC 62304 5.3.2"
        ),
    ),
    RuleDefinition(
        rule_id="R07",
        version=RULE_CATALOG_VERSION,
        title="Proveniência, carregamento e versionamento de artefatos de modelos",
        description=(
            "Identifica chamadas de carregamento e salvamento de modelos (torch.load, from_pretrained, "
            "save_pretrained, onnx.load, etc.) e referências a arquivos de checkpoint (.pt, .pth, .onnx, .h5)."
        ),
        objective=(
            "Mapear onde artefatos de modelos de aprendizado de máquina são consumidos ou gerados, "
            "destacando a necessidade de controle de versão e proveniência documental."
        ),
        category="Rastreabilidade de Modelos de IA/ML",
        evidence_sought=(
            "Chamadas AST de carregamento/salvamento de modelos, strings literais referenciando extensões "
            "de checkpoints e arquivos de pesos presentes no repositório."
        ),
        detection_method="Inspeção AST de chamadas de função e argumentos constantes + inventário de arquivos de modelo.",
        analyzed_files_scope="Todos os arquivos .py e arquivos de artefato de modelo no repositório.",
        identification_criteria=(
            "not_applicable quando o perfil declara ai_components=False e não há bibliotecas/sinais de IA; "
            "partial quando artefatos ou chamadas de carregamento/salvamento são identificados (pois a proveniência "
            "completa depende de registros externos de dados de treino e hiperparâmetros); "
            "not_observed quando o projeto utiliza IA mas nenhum ponto de carregamento/salvamento é localizado."
        ),
        limitations=[
            "A existência de um arquivo .pt, .pth ou .onnx NÃO comprova a proveniência do modelo, a qualidade dos "
            "dados de treinamento nem a reprodutibilidade dos hiperparâmetros.",
            "Pesos de modelos frequentemente são armazenados fora do repositório Git (DVC, MLflow, S3, HuggingFace Hub).",
        ],
        default_review_priority=ReviewPriority.HIGH,
        normative_references=[
            RegulatoryReference(
                document_id="IEC62304",
                document_name="IEC 62304:2006/Amd 1:2015 Medical device software — Software life cycle processes",
                issuing_body="IEC",
                clause="8.1.1; 8.3",
                section_or_page="Identificação de itens de configuração e rastreabilidade de versão",
                mapping_status=MappingStatus.PENDING_EXPERT_REVIEW,
                source="legal_documents/templates_openregulatory/techdoc/62304/sop-machine-learning-model-development.md",
            ),
            RegulatoryReference(
                document_id="OPENREGULATORY_ML_SOP",
                document_name="SOP Machine Learning Model Development (OpenRegulatory Template)",
                issuing_body="OpenRegulatory",
                clause="Section 1.2; Section 2.5",
                section_or_page="Version control for ML projects and Algorithm Validation Report",
                mapping_status=MappingStatus.PENDING_EXPERT_REVIEW,
                source="legal_documents/templates_openregulatory/techdoc/62304/sop-machine-learning-model-development.md",
            ),
        ],
        regulatory_validation_status=MappingStatus.PENDING_EXPERT_REVIEW,
        rag_query_pt=(
            "desenvolvimento de modelos de aprendizado de máquina controle de versão hiperparâmetros "
            "relatório de validação de algoritmo itens de configuração IEC 62304 8.1.1"
        ),
        rag_query_en=(
            "machine learning model development version control hyperparameters Algorithm Validation Report "
            "configuration items IEC 62304 8.1.1"
        ),
    ),
    RuleDefinition(
        rule_id="R08",
        version=RULE_CATALOG_VERSION,
        title="Sinais estruturais de separação entre treinamento e inferência",
        description=(
            "Identifica funções e chamadas associadas ao treinamento (backward, optimizer.step, fit, model.train) "
            "e à inferência (forward, predict, model.eval, no_grad) e verifica se coexistem no mesmo módulo/escopo."
        ),
        objective=(
            "Sinalizar possíveis acoplamentos estruturais entre rotinas de treinamento/ajuste de modelos "
            "e rotinas de inferência destinadas ao uso operacional."
        ),
        category="Arquitetura e Isolamento de Ambientes (IA/ML)",
        evidence_sought=(
            "Funções e chamadas AST de treinamento vs. funções e chamadas AST de inferência, "
            "comparando os arquivos e símbolos onde ocorrem."
        ),
        detection_method="Correlação estrutural por arquivo e escopo de símbolo entre training_signals e inference_signals.",
        analyzed_files_scope="Todos os arquivos .py analisados com sucesso.",
        identification_criteria=(
            "not_applicable quando ai_components=False e não há bibliotecas/sinais de IA; "
            "observed quando sinais de treinamento e inferência estão alocados em módulos distintos; "
            "partial quando sinais de treinamento e inferência coexistem no mesmo arquivo/classe ou quando apenas "
            "uma das fases está presente; not_observed quando nenhum sinal de treino ou inferência é detectado."
        ),
        limitations=[
            "A análise estática AST NÃO consegue provar separação efetiva em tempo de execução nem isolamento "
            "de infraestrutura entre servidores de desenvolvimento e produção.",
            "Classes de modelos (como torch.nn.Module) naturalmente definem o método forward usado tanto no treino "
            "quanto na inferência; portanto, a presença no mesmo arquivo exige análise humana do fluxo de execução.",
        ],
        default_review_priority=ReviewPriority.MEDIUM,
        normative_references=[
            RegulatoryReference(
                document_id="IEC62304",
                document_name="IEC 62304:2006/Amd 1:2015 Medical device software — Software life cycle processes",
                issuing_body="IEC",
                clause="5.3.1; 5.3.5",
                section_or_page="Arquitetura de software e segregação entre itens de software",
                mapping_status=MappingStatus.PENDING_EXPERT_REVIEW,
                source="legal_documents/templates_openregulatory/techdoc/62304/sop-machine-learning-model-development.md",
            ),
            RegulatoryReference(
                document_id="OPENREGULATORY_ML_SOP",
                document_name="SOP Machine Learning Model Development (OpenRegulatory Template)",
                issuing_body="OpenRegulatory",
                clause="Section 2.1; Section 2.6",
                section_or_page="Separation between development environment and production environment",
                mapping_status=MappingStatus.PENDING_EXPERT_REVIEW,
                source="legal_documents/templates_openregulatory/techdoc/62304/sop-machine-learning-model-development.md",
            ),
        ],
        regulatory_validation_status=MappingStatus.PENDING_EXPERT_REVIEW,
        rag_query_pt=(
            "separação entre ambiente de desenvolvimento treinamento e ambiente de produção inferência "
            "arquitetura de software segregação IEC 62304 5.3"
        ),
        rag_query_en=(
            "configuration of development environment separated from the production environment "
            "production deployment of ML model IEC 62304 5.3"
        ),
    ),
]


def get_rule_catalog_dict() -> Dict[str, RuleDefinition]:
    return {r.rule_id: r for r in RULE_DEFINITIONS}


def compute_rule_catalog_hash() -> str:
    """Compute a deterministic SHA-256 hash of the entire versioned rule catalog."""
    payload = [r.model_dump(mode="json") for r in RULE_DEFINITIONS]
    canonical = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()

