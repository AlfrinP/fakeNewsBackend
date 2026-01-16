from langchain_mongodb import MongoDBAtlasVectorSearch
from embeddingModel import exported_embeddings
from envVariables import MONGODB_COLLECTION, ATLAS_VECTOR_SEARCH_INDEX_NAME, MONGODB_CONNECTION_STRING

vector_store = MongoDBAtlasVectorSearch(
    embedding=exported_embeddings,
    collection=MONGODB_COLLECTION,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
    relevance_score_fn="cosine",
    connection_string=MONGODB_CONNECTION_STRING
)          