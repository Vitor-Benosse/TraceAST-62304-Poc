import os
from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

class ResilientTextLoader(BaseLoader):
    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def lazy_load(self):
        raw_text = self.file_path.read_bytes()
        try:
            text = raw_text.decode("utf-8-sig")
        except UnicodeDecodeError:
            text = raw_text.decode("cp1252", errors="replace")

        yield Document(
            page_content=text,
            metadata={"source": str(self.file_path)},
        )

project_directory = Path(__file__).resolve().parent
docs_directory = str(project_directory / "legal_documents")
print(f"Reading all the documents in the folder: {docs_directory}")

# 1. PDF loader (FDA and ANVISA)
loader_pdf = DirectoryLoader(docs_directory, glob="**/*.pdf", loader_cls=PyPDFLoader)
pdf_docs = loader_pdf.load()

# 2. Markdown loader (OpenRegulatory)
loader_md = DirectoryLoader(docs_directory, glob="**/*.md", loader_cls=ResilientTextLoader)
md_docs = loader_md.load()

# 3. Bring all the documents together in one list
all_docs = pdf_docs + md_docs
print(f"Total loaded documents: {len(all_docs)} pages/files.")

# 4. Slice the texts and store them in ChromaDB
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_texts = text_splitter.split_documents(all_docs)

print("Generating embeddings and creating the database...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma.from_documents(
    split_texts,
    embeddings,
    persist_directory=str(project_directory / "db_regulacao"),
)

print("✅ Regulatory database loaded with FDA, ANVISA, and OpenRegulatory!")

# 5. RAG search test
print("\n--- Search testing ---")

question = "Como o software é classificado como dispositivo médico (SaMD) de acordo com o risco?"

print(f"Searching for: '{question}'")

# The DB will search the entire folder and return the 3 most relevant pieces of law
results = db.similarity_search(question, k=3)

print("\nFound results in (FDA/ANVISA/OpenRegulatory):")
print("=" * 60)

# Print each of the 3 results of the search
for i, result in enumerate(results):
    print(f"\n--- Excerpt {i+1} ---")
    print(result.page_content)
    print("-" * 30)