from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def answer_similarity(pred, truth):
    emb1 = model.encode([pred])
    emb2 = model.encode([truth])
    return cosine_similarity(emb1, emb2)[0][0]