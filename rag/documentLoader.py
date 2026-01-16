from langchain_community.document_loaders import PyPDFLoader

file_path = "./documents/"
loader = PyPDFLoader(file_path)

docs = loader.load()
docs[0]