from chatbot.workflow import update_model, ask_bot
from fastapi import FastAPI
from pydantic import BaseModel
from chatbot.workflow import update_model, ask_bot

# database link
filepath = './input/chatbot_database.txt'

# train model
update_model(filepath)

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
    answer = ask_bot(question['question'])

    return {'answer': answer}