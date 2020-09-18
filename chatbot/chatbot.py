from chatbot.utils import get_corpus, get_documents
from chatbot.preprocessing import CustomTextTransfromer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class ChatBot:
    """
    A simple chatbot that handles basic queries from user and answers
    questions based on the similarity score between the question 
    and documents learned by the model. 

    Parameters
    -------
    db_path: string, path to file containing the corpus

    Attributes
    ----------
    documents_db: array, contains the bot answers
    TF_IDF: vectorized documents (tf-idf)

    """
    def __init__(self, db_path):
        print("Fetching data from db ....")
        corpus = get_corpus(db_path)
        self.documents_db = get_documents(corpus)
        print("Data ready.")

    def update_model(self):
        # preprocess corpus
        self.__cst_transfromer = CustomTextTransfromer()

        # fit
        print("Fiting the model....")
        self.__cst_transfromer.fit(self.documents_db)
        print('Model fit DONE.')

        self.TF_IDF = self.__cst_transfromer.transform(self.documents_db)

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
        sim = cosine_similarity(self.__cst_transfromer.transform(documents), self.TF_IDF)
        
        return self.documents_db[sim.argmax()], sim.max()