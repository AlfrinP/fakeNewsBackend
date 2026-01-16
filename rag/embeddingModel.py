from langchain_huggingface import HuggingFaceEmbeddings
from textSplitters import texts

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

exported_embeddings = embeddings.embed_documents(texts)