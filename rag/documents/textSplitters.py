from langchain_text_splitters import CharacterTextSplitter
from rag.documents.documentLoader import docs

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base", chunk_size=100, chunk_overlap=0
)
texts = text_splitter.split_text(docs[0].page_content)