import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o-mini"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
TOP_K = 3