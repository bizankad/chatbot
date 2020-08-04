from sklearn.metrics.pairwise import cosine_similarity

def get_closest_sentence(query, tf_idf, CustomTextTransfromer, database):
    # append query to an array
    documents = [query]

    # compute TF-IDF
    sim = cosine_similarity(CustomTextTransfromer.transform(documents), tf_idf)
    
    return database[sim.argmax()], sim.max()