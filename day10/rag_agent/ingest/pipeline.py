from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_chroma import Chroma

# Paths
DOCS_DIR = Path(__file__).parent.parent / "docs"
CHROMA_DIR = Path(__file__).parent.parent / "chroma_db"

# Embeddings
def get_embeddings():
    return MistralAIEmbeddings(
        model="mistral-embed"
    )

# Ingest docs
def ingest(reset=False):
    print("Loading docs...")

    # load md
    md_docs = DirectoryLoader(
        str(DOCS_DIR),
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    ).load()

    # load txt
    txt_docs = DirectoryLoader(
        str(DOCS_DIR),
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    ).load()

    docs = md_docs + txt_docs

    if not docs:
        print("No docs found")
        return

    print(f"{len(docs)} docs loaded")

    # split
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=80,
    )

    chunks = splitter.split_documents(docs)

    print(f"{len(chunks)} chunks created")

    # reset old db
    if reset and CHROMA_DIR.exists():
        import shutil
        shutil.rmtree(CHROMA_DIR)

    # store
    Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=str(CHROMA_DIR),
        collection_name="rag_docs",
    )

    print("Ingest complete")

# Retriever
def get_retriever(k=4):
    db = Chroma(
        persist_directory=str(CHROMA_DIR),
        embedding_function=get_embeddings(),
        collection_name="rag_docs",
    )

    return db.as_retriever(
        search_kwargs={"k": k}
    )

# test
if __name__ == "__main__":
    ingest(reset=True)