import os
from dotenv import load_dotenv
from typing import List
from app.utils import get_collection, get_most_similar_chunk
from cohere import CohereClient
from langchain import Embeddings
from models import Chunk

# Cargar variables de entorno desde .env
load_dotenv()

def generate_response(user_name: str, question: str) -> str:
    try:
        # Obtener la clave de API de Cohere desde .env
        cohere_api_key = os.getenv("COHERE_API_KEY")
        if not cohere_api_key:
            raise Exception("No se ha proporcionado la clave de API de Cohere")

        embeddings = Embeddings()
        cohere = CohereClient(api_key=cohere_api_key)  # Inicializar Cohere con la API key
        collection = get_collection()
        chunks = collection.get_all_documents()

        question_encoding = embeddings.encode(question)
        most_similar_chunk = get_most_similar_chunk(chunks, question_encoding)

        # Construcción del prompt para el LLM
        prompt = f"{user_name} asks: {question}\n\n{most_similar_chunk}"

        # Obtención de la respuesta del LLM
        response = cohere.complete(prompt, max_tokens=50)["choices"][0]["text"].strip()

        return response
    except Exception as e:
        raise Exception("Error en la generación de respuesta")