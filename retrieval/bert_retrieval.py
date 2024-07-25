# bert_retrieval.py

from sentence_transformers import SentenceTransformer, util

def setup_bert_model():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model

def encode_texts(texts, model):
    return model.encode(texts, convert_to_tensor=True)

def search_bert(query, texts, model):
    query_embedding = model.encode([query], convert_to_tensor=True)
    text_embeddings = encode_texts(texts, model)
    scores = util.pytorch_cos_sim(query_embedding, text_embeddings)[0].tolist()
    return scores
