import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

project_directory = Path(__file__).resolve().parent
load_dotenv(project_directory / ".env")

groq_api_key = os.getenv("GROQ_API_KEY")
groq_model = os.getenv("GROQ_MODEL")
if not groq_api_key:
    raise RuntimeError("GROQ_API_KEY missing. Configure the key in the .env file.")
if not groq_model:
    raise RuntimeError(
        "GROQ_MODEL missing. Configure an active and available model ID "
        "for your Groq account in the .env file."
    )

llm = ChatGroq(
    api_key=groq_api_key,
    model=groq_model,
    temperature=0.2,
    max_tokens=800,
)

print("Connecting to regulatory database...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(
    persist_directory=str(project_directory / "db_regulacao"),
    embedding_function=embeddings,
)

analyzed_code = """
[CLASS] MedicalReportGenerator
  [METHOD] __init__
  [NETWORK ARCHITECTURE] forward
  [METHOD] generate_report
    Docstring:
      Train the medical report generation model
"""

print("Searching for relevant legal guidelines...")
search_question = "Quais são os requisitos regulatórios para um software que gera laudos ou relatórios médicos (medical report generation) baseado em IA?"
relevant_docs = db.similarity_search(search_question, k=3)
legal_context = "\n\n".join([doc.page_content for doc in relevant_docs])

template = """Atue como um Auditor Técnico da ANVISA e especialista na norma IEC 62304.

CÓDIGO ANALISADO DO REPOSITÓRIO (AST):
{code}

DIRETRIZES LEGAIS EXTRAÍDAS (FDA/ANVISA/62304):
{laws}

INSTRUÇÃO:
Com base no código fornecido e nas leis, escreva um resumo de 3 parágrafos classificando o risco provável deste software e que documentos técnicos precisarão ser gerados para homologação.
"""
prompt = PromptTemplate.from_template(template)

print(f"Sending for analysis with model {groq_model}...")
chain = prompt | llm
response = chain.invoke({"code": analyzed_code, "laws": legal_context})

print("\n=== AUDITOR REPORT (LLM) ===")
print(response.content)