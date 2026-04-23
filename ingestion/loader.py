import os

def load_documents(folder_path):
    docs = []

    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)

        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                docs.append({
                    "name": file,
                    "text": f.read()
                })

    return docs