# hybrid_retrieval.py

from bm25_retrieval import setup_bm25, search_bm25
from bert_retrieval import setup_bert_model, search_bert
from query_expansion import enhance_query
import numpy as np

def load_documents(file_paths):
    """Load and preprocess documents from file paths."""
    documents = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            documents.append(file.read())
    return documents

def preprocess_documents(documents):
    """Tokenize and preprocess documents."""
    return [doc.split() for doc in documents]

def normalize_scores(scores):
    """Normalize scores to a range of [0, 1]."""
    scores = np.array(scores)
    max_score = np.max(scores) if scores.size > 0 else 1
    return (scores / max_score).tolist()

def hybrid_search(query, texts, bm25, bert_model):
    """Perform hybrid search using BM25 and BERT models."""
    query_tokens = query.split()
    bm25_scores = search_bm25(query, bm25)
    bert_scores = search_bert(query, texts, bert_model)
    
    # Normalize and combine BM25 and BERT scores
    bm25_scores = normalize_scores(bm25_scores)
    bert_scores = normalize_scores(bert_scores)
    combined_scores = [0.5 * bm25 + 0.5 * bert for bm25, bert in zip(bm25_scores, bert_scores)]
    
    return combined_scores

def re_rank_results(results, scores):
    """Re-rank results based on scores."""
    sorted_results = [result for _, result in sorted(zip(scores, results), reverse=True)]
    return sorted_results

if __name__ == "__main__":
    query = "example query"
    
    # Load and preprocess documents
    file_paths = [
        "Introduction-to-Data-Science-AAgah-20240620-1.txt", 
        "Dynamicsl.txt",
        "Research-Data-Management-in-the-Canadian-Context-1712778191.txt"
    ]
    documents = load_documents(file_paths)
    corpus = preprocess_documents(documents)
    
    # Setup BM25 and BERT
    bm25 = setup_bm25(corpus)
    bert_model = setup_bert_model()
    
    # Enhance query and perform search
    enhanced_query = enhance_query(query)
    scores = hybrid_search(enhanced_query, documents, bm25, bert_model)
    ranked_results = re_rank_results(documents, scores)
    
    # Display top results (adjust the number if needed)
    top_n = 5
    for result in ranked_results[:top_n]:
        print(result)
