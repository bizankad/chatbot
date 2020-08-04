from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.base import  BaseEstimator, TransformerMixin
from chatbot.utils import get_wordnet_pos

class CustomTextTransfromer(BaseEstimator, TransformerMixin):

    def __init__(self, language='english'):
        self.vect = TfidfVectorizer(analyzer=lambda x: x)
        self.language = language
    
    def preproc(self, X):

        # tokenize documents
        tokens_list = [word_tokenize(doc) for doc in X]

        # get stop words
        stop_words = stopwords.words('english')

        # remove stop words
        tokens_stop_words = [[token for token in tokens if token.lower() not in stop_words] for tokens in tokens_list]

        # keep only alpha tokens
        tokens_list = [[token for token in tokens if token.isalpha()] for tokens in tokens_stop_words]

        # Lemmatize
        tokens_class_list = [pos_tag(tokens) for tokens in tokens_list]
        tokens_class_list = [get_wordnet_pos(tokens_class) for tokens_class in tokens_class_list]
        lemmatizer = WordNetLemmatizer()
        limmatized_tokens = [[lemmatizer.lemmatize(token, tkn_class) for token, tkn_class in tokens_class] for tokens_class in tokens_class_list]

        # recreate documents from tokens
        documents = [' '.join(tokens) for tokens in limmatized_tokens]

        return documents

    def fit(self, X, y=None):
        # get pre processed documents
        documents = self.preproc(X)

        # compute TF-IDF
        self.vect.fit(documents)

        return self

    def transform(self, X):
        # get pre processed documents
        documents = self.preproc(X)

        # compute TF-IDF
        TF_IDF = self.vect.transform(documents).toarray()

        return TF_IDF