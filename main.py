from fastapi import FastAPI
from models import UserMessage
from gemini_wrapper import generate_response

app = FastAPI()
@app.post("/chat")
async def chat_with_bot(message: str):
    response = generate_response(message)
    return {"response": response}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Gemini Chatbot API. Use the /chat endpoint to interact with the bot."}
  