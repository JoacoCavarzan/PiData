from pydantic import BaseModel


class Question(BaseModel):
    user_name: str
    question: str
