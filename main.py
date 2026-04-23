from ingestion.loader import load_documents
from ingestion.cleaner import clean_text
from ingestion.chunker import chunk_text
from ingestion.embedder import embed_texts
from retrieval.vector_store import VectorStore
from retrieval.retriever import retrieve
from agent.router import classify_query
from generation.generator import generate_answer

def build_pipeline(doc_path):
    docs = load_documents(doc_path)

    all_chunks = []

    for doc in docs:
        cleaned = clean_text(doc["text"])
        chunks = chunk_text(cleaned)
        all_chunks.extend(chunks)

    embeddings = embed_texts(all_chunks)

    vs = VectorStore(len(embeddings[0]))
    vs.add(embeddings, all_chunks)

    def pipeline(query):
        retrieved, scores = retrieve(query, vs)

        q_type = classify_query(query, scores)

        context = "\n".join(retrieved)

        answer = generate_answer(query, context, q_type)

        return {
            "type": q_type,
            "answer": answer,
            "context": retrieved
        }

    return pipeline


if __name__ == "__main__":
    pipeline = build_pipeline("data")

    query = input("Enter your query: ")
    result = pipeline(query)

    print("\nType:", result["type"])
    print("\nAnswer:\n", result["answer"])