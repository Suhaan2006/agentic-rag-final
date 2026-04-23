import requests
from config import OPENAI_API_KEY, MODEL

def generate_answer(query, context, mode):
    if mode == "OUT_OF_SCOPE":
        return "The provided documents do not contain enough information to answer this question."

    prompt = f"""
Answer ONLY from the context below.
If sources disagree, present both perspectives.

Context:
{context}

Question:
{query}
"""

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}]
        },
        timeout=15
    )
    print(response.json())
    return response.json()["choices"][0]["message"]["content"]