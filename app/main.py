from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.services import generate_response

app = FastAPI()

class Question(BaseModel):
    user_name: str
    question: str

@app.post("/ask/")
def ask_question(question: Question):
    try:
        response = generate_response(question.user_name, question.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))