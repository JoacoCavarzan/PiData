import chromadb


def get_collection() -> chromadb.Collection:
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name="my_collection")
    return collection
