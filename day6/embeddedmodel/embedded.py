from dotenv import load_dotenv
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings
)

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

vector = embeddings.embed_query(
    "You are going to learn Gen AI"
)

vector_64 = vector[:64]

print(vector_64)
print("Dimensions:", len(vector_64))