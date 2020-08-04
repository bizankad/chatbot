from chatbot.utils import get_corpus, get_documents
from chatbot.preprocessing import CustomTextTransfromer
from chatbot.bot_answer import get_closest_sentence
import numpy as np

def update_model(filepath):
    # get corpus from file
    print("Fetching data from db ....")
    corpus = get_corpus(filepath)
    print("Data ready.")

    # database
    global documents_db 
    documents_db = get_documents(corpus)

    # preprocess corpus
    global cst_transfromer 
    cst_transfromer = CustomTextTransfromer()

    # fit
    print("Fiting the model....")
    cst_transfromer.fit(documents_db)
    print('Model fit DONE.')

def ask_bot(query):
    small_talks_good = ["Thanks for getting in touch with me", "I am so sorry I do not understand your point", 
                   "I'll make sure to understand you after my next update"]
    small_talks_bad = ["I can not understand a word of what you are saying", "Please be more specific"]

    # transform
    TF_IDF = cst_transfromer.transform(documents_db)

    bot_answer, score = get_closest_sentence(query, TF_IDF, cst_transfromer, documents_db)

    if score > .6:
        small_talk = bot_answer
    elif score > .3:
        small_talk = np.random.choice(small_talks_good)
    else:
        small_talk = np.random.choice(small_talks_bad)

    return small_talk

