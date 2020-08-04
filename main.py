from chatbot.workflow import update_model, ask_bot
from fastapi import FastAPI
from pydantic import BaseModel
from chatbot.workflow import update_model, ask_bot

# database link
filepath = './input/chatbot_database.txt'

# train model
update_model(filepath)

app = FastAPI()

@app.post("/bot_answer")
async def get_answer(question: str):
    # ask the bot
    answer = ask_bot(question)

    return answer