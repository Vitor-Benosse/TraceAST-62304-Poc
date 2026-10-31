# TraceAST-62304: Arquitetura RegTech Autônoma para Auditoria de IA Médica (SaMD)
[![en](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/Vitor-Benosse/TraceAST-62304-Poc/blob/master/README.md)

**Prova de Conceito (PoC) Acadêmica e Declaração de *Prior Art***

Este repositório apresenta a fundação acadêmica e o núcleo tecnológico (Prova de Conceito) do projeto **TraceAST-62304**. O sistema consiste em um Agente Autônomo de rastreabilidade regulatória, projetado para auditar repositórios de Inteligência Artificial médica e gerar análises preliminares de conformidade e matrizes de risco.

O objetivo principal desta publicação é estabelecer o **Estado da Técnica (*Prior Art*)** para validação científica e proteção de propriedade intelectual.

---

## 1. Fundamentação Científica: Isenção de Comitê de Ética em Pesquisa (CEP)

A metodologia de pesquisa deste projeto adota a hipótese jurídica e científica de isenção de submissão a Comitês de Ética em Pesquisa (CEP), baseando-se nos seguintes pilares:

1. **Ausência de Dados Clínicos Reais:** A arquitetura não consome, armazena ou processa dados biomédicos nominais ou imagens médicas reais de pacientes.
2. **Avaliação Estritamente Sintática:** O pipeline de auditoria realiza exclusivamente a extração de **Árvores de Sintaxe Abstrata (AST)** a partir do código-fonte estrutural de repositórios de Inteligência Artificial abertos (Open-Source).
3. **Foco Regulatório:** O julgamento do sistema recai sobre a conformidade de *engenharia de software* perante as normas globais, avaliando a presença de salvaguardas no código (ex: blocos `try...except`), e não a acurácia diagnóstica do modelo médico em si.

Essa abordagem elimina os riscos associados à privacidade e LGPD/HIPAA, acelerando drasticamente o ciclo de validação regulatória ("RegTech").

---

## 2. Arquitetura Teórica e Tecnológica

O núcleo desta PoC contorna limitações tradicionais de Modelos de Linguagem de Grande Escala (LLMs) — como saturação da janela de contexto e alucinações — combinando duas técnicas avançadas:

### A. Fatiamento Semântico Inteligente (Módulo AST)
Enviar a base de código integral de um sistema hospitalar para um LLM é ineficiente e expõe propriedade intelectual. Para solucionar isso, utilizamos o módulo nativo `ast` do Python para extrair apenas o "esqueleto" semântico crítico:
* **Isolamento de Dados do Paciente:** Identifica ativamente nós de manipulação de dados (I/O) e mapeia salvaguardas (`ast.Try`), listando os tratamentos de erro. Isso valida a resiliência do algoritmo frente à corrupção da telemetria (ex: sensores de UTI falhos).
* **Separação de Ambientes (Treino vs. Produção):** O extrator busca por assinaturas de arquitetura de rede explícitas (como o método `forward` do PyTorch), permitindo que o Agente identifique se rotinas indevidas de treinamento estão acopladas no fluxo de inferência em tempo real.

### B. Motor de Raciocínio Clínico e Cérebro Vetorial (RAG)
* **Harmonização Regulatória:** As diretrizes da **FDA** (EUA), **ANVISA (RDC 657/2022)** e a norma internacional **IEC 62304** (via IMDRF) foram convertidas em vetores matemáticos (Embeddings) utilizando o modelo `sentence-transformers/all-MiniLM-L6-v2`.
* **ChromaDB:** Atua como o banco de dados vetorial de longo prazo, permitindo buscas espaciais precisas (Retrieval-Augmented Generation - RAG).
* **Agente LLM (Groq):** O modelo `qwen/qwen3.8-27b` (ou da família Llama3) é instanciado com temperatura `0.2` para garantir o rigor lógico, recebendo o código AST fatiado e a legislação recuperada para emitir o Dossiê Técnico de risco.

---

## 3. Estrutura do Repositório

* `analyzer.py`: Extrator sintático baseado no módulo `ast` para mapeamento de frameworks de IA, classes, métodos de arquitetura de rede (`forward`), funções de `I/O` e salvaguardas (`try...except`).
* `regulatory_db.py`: Pipeline de ingestão documental (`.pdf` e `.md`), fatiamento textual e geração do banco vetorial local no ChromaDB.
* `audit_agent.py`: Executor de auditoria que integra a busca espacial no ChromaDB ao motor de raciocínio na nuvem (Groq).
* `legal_documents/`: Diretório destinado aos arquivos normativos públicos (FDA, ANVISA RDC 657/2022 e templates IEC 62304 / ISO 14971).
* `.env.example`: Template de configuração para variáveis de ambiente.

---

## 4. Guia de Execução (Passo a Passo)

Para avaliadores, pesquisadores e revisores que desejam rodar a Prova de Conceito localmente, siga as instruções abaixo:

### Pré-requisitos
* Python 3.9 ou superior.
* Git.
* Uma chave de API gratuita da [Groq Cloud](https://console.groq.com/).

### Passo 1: Instalação e Configuração de Ambiente
Clone este repositório e crie um ambiente virtual:
```bash
git clone https://github.com/SEU_USUARIO/TraceAST-62304-PoC.git
cd TraceAST-62304-PoC
python -m venv venv

# Ativar no Windows:
venv\Scripts\activate
# Ativar no Linux/Mac:
source venv/bin/activate
```

Instale as dependências essenciais:
```bash
pip install langchain-chroma langchain-huggingface langchain-groq python-dotenv sentence-transformers
```

### Passo 2: Configuração de Credenciais
Crie um arquivo chamado `.env` na raiz do projeto e insira as suas chaves da Groq:
```env
GROQ_API_KEY="sua_chave_de_api_aqui"
GROQ_MODEL="qwen/qwen3.8-27b"
```

### Passo 3: Executando a Prova de Conceito
A PoC pública é composta por scripts de terminal de fácil execução que demonstram o fluxo ponta a ponta:

1. **Extração AST (Fatiamento Semântico):**
   Execute o analisador apontando para um repositório de IA médica público(sinta-se a vontade para alterar o link do repositório). Este script criará um resumo das classes, lógicas I/O e métodos de segurança.
   ```bash
   python analyzer.py https://github.com/anandr07/Medical-Report-Generator-from-Chest-X-Ray-Images
   ```

2. **Auditoria Regulatória (Cérebro Vetorial + LLM):**
   Crie o banco de dados vetorial que processa os documentos da pasta legal_documents/, gera os embeddings localmente e persiste o banco ChromaDB:
   ```bash
   python regulatory_db.py
   ```

   Execute o Agente para simular o recebimento do código AST e consultar a base de leis, retornando o Parecer de Risco do LLM:
   ```bash
   python audit_agent.py
   ```

---

## 5. Contato e Autoria
Desenvolvido como pesquisa acadêmica focada na otimização de validação legal para *Software as a Medical Device* (SaMD). Para discussões sobre a arquitetura e detalhes metodológicos, consulte o artigo científico associado a esta publicação ou abra uma *Issue* neste repositório.