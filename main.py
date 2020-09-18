from fastapi import FastAPI
from pydantic import BaseModel
from chatbot.chatbot import ChatBot

# database link
filepath = './input/chatbot_database.txt'

my_bot = ChatBot(filepath)

# train model
my_bot.update_model()

app = FastAPI()

class ModelOut(BaseModel):
    answer: str

class ModelIn(BaseModel):
    question: str

@app.post("/bot_answer", response_model=ModelOut)
async def get_answer(question: ModelIn):
    # cast object to dict
    question = question.dict()

    # ask the bot
    answer = my_bot.ask_bot(question['question'])

    return {'answer': answer}