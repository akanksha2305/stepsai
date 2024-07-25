# query_expansion.py

import nltk
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer

nltk.download('wordnet')
nltk.download('punkt')

def expand_query(query):
    synonyms = set()
    for word in query.split():
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())
    return ' '.join(synonyms)

def stem_query(query):
    ps = PorterStemmer()
    return ' '.join([ps.stem(word) for word in query.split()])

def enhance_query(query):
    expanded_query = expand_query(query)
    stemmed_query = stem_query(expanded_query)
    return stemmed_query
