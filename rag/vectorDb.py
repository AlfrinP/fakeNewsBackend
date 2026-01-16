from langchain_mongodb import MongoDBAtlasVectorSearch

MONGODB_COLLECTION = "documents"
ATLAS_VECTOR_SEARCH_INDEX_NAME = "default"

vector_store = MongoDBAtlasVectorSearch(
    embedding=embeddings,
    collection=MONGODB_COLLECTION,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
    relevance_score_fn="cosine",
)