from langchain_mongodb import MongoDBAtlasVectorSearch
from embeddingModel import embeddings
from envVariables import MONGODB_COLLECTION, ATLAS_VECTOR_SEARCH_INDEX_NAME

vector_store = MongoDBAtlasVectorSearch(
    embedding=embeddings,
    collection=MONGODB_COLLECTION,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
    relevance_score_fn="cosine",
)          