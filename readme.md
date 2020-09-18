Very straigntforward chatbot that computes similarity between a user query and vectorized tf-idf documents stored in memory. The chatbot outputs the most similar document.
The corpus is taken from an article about artificial intelligence. 

The application is structured as follows:

- Flask-app: contains flask front end to query the chatbot
- Chatbot: contains sources file required to run the chatbot service


## Setup
To run the application, please follow these steps:

1. install dependancies
```bash
pip install -r requirements.txt
```
2. run fast api service 
```bash
uvicorn run_chatbot_api:app --reload
```
![alt text](https://i.ibb.co/ZghkbVc/Capture-d-cran-2020-09-18-20-44-35.png)

3. run flask app 
```bash
python flask-app/main.py
```
![alt text](https://i.ibb.co/XDJCfhS/Capture-d-cran-2020-09-18-20-47-26.png)


Chatbot app

![alt text](https://i.ibb.co/23P3jNs/Capture-d-cran-2020-09-18-20-45-19.png)




