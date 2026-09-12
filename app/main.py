from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="My First AI Agent API")


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "My first AI Agent API is running"}


@app.post("/chat")
def chat(request: ChatRequest):
    if request.message.lower() == "hello":
        answer = "Hello! How can I assist you today?"
    elif request.message.lower() == "bye":
        answer = "Goodbye! Have a great day!"
    else:
        answer = f"你说的是: {request.message}"
    return {
        "answer": answer,
        "is_agent": False,
    }
