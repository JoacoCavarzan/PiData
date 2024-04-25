import chromadb
from chromadb.utils import embedding_functions


def get_collection() -> chromadb:
    return chromadb()  #entorno local

def get_most_similar_chunk(chunks: list, target_encoding: str) -> str:
    embeddings = Embeddings()
    target_embedding = embeddings.decode(target_encoding)
    most_similar_chunk = None
    min_distance = float("inf")

    for chunk in chunks:
        distance = embeddings.cosine_distance(target_embedding, embeddings.decode(chunk.encoding))
        if distance < min_distance:
            min_distance = distance
            most_similar_chunk = chunk.text

    return most_similar_chunk