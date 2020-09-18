from flask import Flask, render_template, request, redirect
import requests 
import json

# instanciate flask app
app = Flask(__name__)

# chatbot micro service URL
chatbot_url = 'http://127.0.0.1:8000'
end_point = '/bot_answer'


message_record = []

@app.route('/')
def index():
    return render_template('index.html', message_record=message_record)

@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        user = request.form['user']
        question = request.form['question']
        answer = requests.post(chatbot_url+end_point, json={"question": question})
        message_record.append(dict(user=user, question=question, answer=answer.json()['answer']))
    
    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True)