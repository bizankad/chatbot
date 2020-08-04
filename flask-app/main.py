from flask import Flask
import requests 
import json

# instanciate flask app
app = Flask(__name__)

# chatbot micro service URL
chatbot_url = 'http://127.0.0.1:8000'
end_point = '/bot_answer'

@app.route('/')
def index():
    result = requests.post(chatbot_url+end_point, json={"question": "What is a chatbot?"})
    return result.json()['answer']

if __name__ == '__main__':
    app.debug = True
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True)