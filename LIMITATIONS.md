# Declaração de Limitações Técnicas e Regulatórias — TraceAST-62304 v1.0

O **TraceAST-62304** é um instrumento técnico de triagem pré-auditoria (*pre-audit screening*) e deve ser utilizado com pleno conhecimento de suas fronteiras metodológicas.

---

## 1. Limitações Regulatórias e Clínicas

1. **Não Substituição de Auditores Humanos:** O sistema não substitui engenheiros de qualidade, especialistas na norma IEC 62304, avaliadores clínicos ou inspetores da ANVISA.
2. **Ausência de Declaração de Conformidade ou Certificação:** Nenhum resultado (`observed`, `partial`, etc.) pode ser interpretado como certificado de conformidade regulatória.
3. **Não Determinação de Classe de Risco:** O sistema não classifica automaticamente dispositivos segundo a RDC 657/2022 (Classes I a IV) nem determina a Classe de Segurança do Software segundo a IEC 62304 (Classes A, B ou C). O campo `review_priority` refere-se exclusivamente à prioridade técnica de investigação pela equipe de engenharia.
4. **Ausência de Avaliação Clínica:** A inspeção estática do código-fonte não avalia eficácia clínica, sensibilidade/especificidade diagnóstica, viés populacional de datasets ou segurança clínica do modelo em mundo real.
5. **Significado de `not_observed`:** Quando uma evidência não é encontrada no repositório (`not_observed`), isso significa apenas que o indicador não foi localizado nos arquivos inspecionados. Documentos do Sistema de Gestão da Qualidade (SGQ), planos de validação, matrizes de risco (ISO 14971) e relatórios de testes frequentemente residem em sistemas externos de gestão documental.

---

## 2. Limitações da Análise Estática via AST (Python V1.0)

1. **Escopo de Linguagem:** A versão V1.0 analisa exclusivamente arquivos Python (`.py`). Repositórios híbridos contendo C/C++, CUDA, JavaScript/TypeScript ou R têm apenas sua camada Python inspecionada.
2. **Ausência de Execução Dinâmica:** Por segurança e reprodutibilidade, o código do repositório analisado nunca é executado. Portanto, a ferramenta não resolve tipos dinâmicos em tempo de execução, reflexão (`getattr` dinâmico) ou configurações carregadas de servidores externos.
3. **Limites das Heurísticas (`R01`–`R08`):**
   - **Tratamento de Exceções (`R05`):** Verificar que uma operação de leitura está dentro de um bloco `try-except` não prova que a exceção é tratada de modo seguro para o paciente, nem detecta se a captura de erro é feita em uma função chamadora de nível superior (*caller*).
   - **Validação de Entradas (`R06`):** Identificar uma função `validate_*` ou uma checagem `isinstance` não comprova que os intervalos fisiológicos, metadados DICOM ou invariantes clínicas estão devidamente verificados.
   - **Proveniência de Modelos (`R07`):** Detectar `torch.load` ou um arquivo `.pt` não comprova que o modelo possui rastreabilidade de versão, dataset de treinamento auditado ou hiperparâmetros documentados.
   - **Separação Treino/Inferência (`R08`):** Verificar que funções de treinamento e de inferência estão em arquivos distintos não garante isolamento de ambiente em produção; inversamente, classes PyTorch (`nn.Module`) definem `forward` usado tanto no treino quanto na inferência, exigindo revisão humana do fluxo de controle.

---

## 3. Limitações do Módulo RAG e do LLM Opcional

1. **Escopo Normativo Inicial:** A base documental da V1.0 contempla a **ANVISA RDC 657/2022** (texto oficial em português) e referências/templates mapeados da **IEC 62304**. Diretrizes da FDA não estão implementadas na V1.0.
2. **Direitos Autorais da IEC 62304:** O repositório público não distribui o texto integral protegido por direitos autorais da norma IEC 62304; utiliza referências de seções verificáveis e templates abertos (*OpenRegulatory*), cujos mapeamentos requerem revisão e aprovação por especialista (`pending_expert_review`).
3. **Recuperação por Similaridade:** Retornar 3 fragmentos no RAG não garante que o trecho recuperado esgote os requisitos aplicáveis ao produto específico.
4. **LLM Opcional:** Quando habilitado pelo usuário, o LLM atua apenas como redator de explicações acessíveis sobre achados já determinados pelas regras estáticas. Ele não tem permissão arquitetural para alterar estados, criar evidências ou emitir juízo regulatório.

