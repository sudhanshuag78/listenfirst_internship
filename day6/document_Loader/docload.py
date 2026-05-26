from langchain_community.document_loaders import PyPDFLoader

# PDF path
pdf_path = "document_Loader/sample_langchain_test.pdf"

# loader
loader = PyPDFLoader(pdf_path)

# load all pages
documents = loader.load()

# total pages
print(f"Total pages: {len(documents)}")

# first page content
print("\nFirst page text:\n")
print(documents[0].page_content)