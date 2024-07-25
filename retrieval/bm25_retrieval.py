# bm25_retrieval.py

from rank_bm25 import BM25Okapi

def setup_bm25(corpus):
    # Corpus should be a list of tokenized documents
    bm25 = BM25Okapi(corpus)
    return bm25

def search_bm25(query, bm25):
    query_tokens = query.split()
    scores = bm25.get_scores(query_tokens)
    return scores
