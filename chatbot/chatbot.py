from chatbot.utils import get_corpus, get_documents
from chatbot.preprocessing import CustomTextTransfromer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class ChatBot:
    def __init__(self, db_path):
        print("Fetching data from db ....")
        corpus = get_corpus(db_path)
        self.documents_db = get_documents(corpus)
        print("Data ready.")

    def update_model(self):
        # preprocess corpus
        self.cst_transfromer = CustomTextTransfromer()

        # fit
        print("Fiting the model....")
        self.cst_transfromer.fit(self.documents_db)
        print('Model fit DONE.')

        self.TF_IDF = self.cst_transfromer.transform(self.documents_db)

    def ask_bot(self, query):
        small_talks_good = ["Thanks for getting in touch with me", "I am so sorry I do not understand your point", 
                    "I'll make sure to understand you after my next update"]
        small_talks_bad = ["I can not understand a word of what you are saying", "Please be more specific"]

        # transform
        
        bot_answer, score = self.get_closest_sentence(query)

        if score > .6:
            small_talk = bot_answer
        elif score > .3:
            small_talk = np.random.choice(small_talks_good)
        else:
            small_talk = np.random.choice(small_talks_bad)

        return small_talk

    def get_closest_sentence(self, query):
        # append query to an array
        documents = [query]

        # compute TF-IDF
        sim = cosine_similarity(self.cst_transfromer.transform(documents), self.TF_IDF)
        
        return self.documents_db[sim.argmax()], sim.max()