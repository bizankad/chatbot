# required for get_wordnet_pos
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize
import numpy as np

def get_corpus(filepath):
    """ 
    load file 
    
    Parameters
    ----------
    filpath : string, 
        path to database containg corpus
    
    Returns
    -------
    corpus : string, shape: (n_documents)
        
    """
    
    with open(filepath, 'r') as f:
        corpus = f.read()
    return corpus


def get_wordnet_pos(pos_tag):
    """ 
    contruct mapping between pos_tag and tags as required by lemmatizer
    
    Parameters
    ----------
    pos_tag : array, 
    
    Returns
    -------
    output : array, 
        
    """

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
    """ 
    sentence tokenize corpus 
    
    Parameters
    ----------
    corpus : string, 
        string variable containing corpus
    
    Returns
    -------
    documents : array, shape: (n_documents)
        extracted sentences from the coprus
    """
    return sent_tokenize(corpus)