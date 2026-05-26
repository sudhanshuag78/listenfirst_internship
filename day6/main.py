import os
from dotenv import load_dotenv
import google.generativeai as genai

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)

from langchain_community.vectorstores import Chroma

from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
# .env load karo
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Gemini configure
genai.configure(api_key=API_KEY)

# 1. PDF load karo
pages = PyPDFLoader("mypdf.pdf").load()
print(f"Pages loaded: {len(pages)}")

# 2. Chunks banao
chunks = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
).split_documents(pages)

print(f"Chunks bane: {len(chunks)}")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        google_api_key=API_KEY
    ),
    persist_directory="./db"
)

print("Vector DB ready!")

# 4. Prompt
PROMPT = PromptTemplate(
    template="""
Context ke basis par jawab do.
Agar jawab context mein nahi hai toh bol do "Document mein nahi mila."

Context:
{context}

Sawal:
{question}

Jawab:
""",
    input_variables=["context", "question"]
)

# 5. RAG chain
qa = RetrievalQA.from_chain_type(
    llm=ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=API_KEY,
        temperature=0
    ),
    retriever=vectorstore.as_retriever(
        search_kwargs={"k": 3}
    ),
    chain_type_kwargs={
        "prompt": PROMPT
    },
    return_source_documents=True
)

# 6. Question
que = input("Apna sawal likho: ")

result = qa.invoke({"query": que})

print("\nJawab:")
print(result["result"])

print("\nSources:")
for doc in result["source_documents"]:
    print(
        f"Page {doc.metadata['page'] + 1}: "
        f"{doc.page_content[:100]}..."
    )