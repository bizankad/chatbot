from chatbot.utils import get_corpus, get_documents
from chatbot.preprocessing import CustomTextTransfromer
from chatbot.bot_answer import get_closest_sentence

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
    # transform
    TF_IDF = cst_transfromer.transform(documents_db)

    bot_answer, score = get_closest_sentence(query, TF_IDF, cst_transfromer, documents_db)

    print(bot_answer)