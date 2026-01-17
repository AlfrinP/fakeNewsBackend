from langchain_community.document_loaders import PyPDFLoader
from rag.vectorDb import vector_store

file_path = "./documents/demo.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()

result = vector_store.add_documents(docs)