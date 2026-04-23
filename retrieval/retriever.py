from ingestion.embedder import model

def retrieve(query, vector_store, k=3):
    query_emb = model.encode([query])[0]
    chunks, scores = vector_store.search(query_emb, k)
    return chunks, scores