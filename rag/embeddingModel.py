from langchain_huggingface import HuggingFaceEmbeddings
from textSplitters import texts

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

print(embeddings.embed_documents(texts))