from pydantic import BaseModel

class Chunk(BaseModel):
    # MOdelo de datos para solicitar preg
    id: int
    user_name: str
    question: str
