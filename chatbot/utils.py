# required for get_wordnet_pos
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize
import numpy as np

def get_corpus(filepath):
    '''
    TODO: describe function
    '''
    with open(filepath, 'r') as f:
        corpus = f.read()
    return corpus


def get_wordnet_pos(pos_tag):
    output = np.asarray(pos_tag)
    for i in range(len(pos_tag)):
        if pos_tag[i][1].startswith('J'):
            output[i][1] = wordnet.ADJ
        elif pos_tag[i][1].startswith('V'):
            output[i][1] = wordnet.VERB
        elif pos_tag[i][1].startswith('R'):
            output[i][1] = wordnet.ADV
        else:
            output[i][1] = wordnet.NOUN
    return output


def get_documents(corpus):
    return sent_tokenize(corpus)