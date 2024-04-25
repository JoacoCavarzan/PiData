import os

from cohere import CohereClient
from dotenv import load_dotenv
from langchain import Embeddings

from app.database import get_collection

load_dotenv()


def generate_response(user_name: str, question: str) -> str:
    """
    respuesta del LLM a la pregunta del usuario.

    Args:
        user_name (str): Nombre del usuario .
        question (str): Pregunta del usuario.

    Returns:
        str: Respuestapor el LLM.
    """
    try:
        cohere_api_key = os.getenv("COHERE_API_KEY")
        if not cohere_api_key:
            raise Exception("No se ha proporcionado la clave de API de Cohere")

        cohere = CohereClient(api_key=cohere_api_key)
        collection = get_collection()
        context = collection.query(query_texts=[question], n_results=1)["documents"][0]
        embeddings = Embeddings()
        target_encoding = embeddings.encode(question.strip())
        response = cohere.generate_response(context, target_encoding)
        return response
    except Exception as e:
        raise Exception(f"Error generando la respuesta: {str(e)}")


def store_chunks_in_chromadb(document_content: str) -> None:
    """
    Almacena los chunks del documento en ChromaDB.

    Args:
        document_content (str): Contenido del documento.
    """
    try:
        # chunks, realizar el encoding y almacenar en ChromaDB
        # ...
        pass
    except Exception as e:
        raise Exception(f"Error al almacenar chunks en ChromaDB: {str(e)}")
