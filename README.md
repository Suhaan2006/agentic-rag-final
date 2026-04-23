Got it — then you just need a **small change in the README** so it correctly reflects OpenAI instead of Groq.

Here’s your **final corrected, copy-paste README (OpenAI version)**:

---

````md
# 🚀 Agentic RAG System for AI Regulation Analysis

> An agentic Retrieval-Augmented Generation (RAG) system that intelligently decides how to answer queries by classifying them into factual, synthesis, or out-of-scope — with a fully runnable evaluation framework.

---

## ⚡ Quick Demo

```bash
python main.py
````

**Input:** Natural language query
**Output:**

* Query type (Factual / Synthesis / Out-of-Scope)
* Context-aware answer grounded in documents

✔ Explicit routing logic (no blind LLM decisions)
✔ Handles out-of-scope queries without hallucination
✔ Supports multi-document synthesis
✔ Includes evaluation pipeline with metrics

---

## 📌 Overview

This project implements an **agentic RAG system** over a dataset of AI regulation documents.

Unlike traditional RAG pipelines, this system:

* Classifies the query first
* Chooses a strategy
* Then retrieves and generates an answer

This ensures **better control, transparency, and reliability**.

---

## 🧠 System Architecture

```
Query
  ↓
Routing (Factual / Synthesis / Out-of-Scope)
  ↓
Retrieval (FAISS Vector Store)
  ↓
Answer Generation (LLM - OpenAI)
  ↓
Evaluation (Metrics + Results Table)
```

---

## ⚙️ Features

* Multi-document ingestion and preprocessing
* Chunking with overlap for context preservation
* Embedding-based semantic retrieval (FAISS)
* Explicit agentic routing logic (not LLM-controlled)
* Context-grounded answer generation
* Safe handling of out-of-scope queries (no hallucination)
* Fully runnable evaluation framework
* Results exported to CSV

---

## 📂 Dataset

The system uses **4 provided documents on AI regulation**:

* Document_1_Policy_Report.txt
* Document_2_News_Article.txt
* Document_3_Stakeholder_Memo.txt
* Document_4_Technical Brief.txt

These documents include:

* Overlapping content
* Contradictory perspectives
* Noisy formatting

This simulates real-world retrieval challenges.

---

## 🧩 Ingestion Pipeline

### Chunking Strategy

* Chunk size: **500 words**
* Overlap: **100 words**

**Why:**

* Preserves semantic context
* Improves retrieval accuracy
* Enables synthesis across chunks

---

### Embeddings

* Model: `all-MiniLM-L6-v2` (Sentence Transformers)

---

### Vector Store

* FAISS (in-memory)

---

## 🤖 Agentic Query Routing

Routing is **explicit and inspectable**, not delegated to the LLM.

### Query Types:

* Factual
* Synthesis
* Out-of-Scope

### Routing Logic:

* Keyword-based intent detection
* Retrieval score thresholds
* Multi-chunk similarity signals

---

## ✍️ Answer Generation

* Uses retrieved context only
* Prevents hallucination
* Handles contradictions explicitly

Out-of-scope queries return:

```
The provided documents do not contain enough information to answer this question.
```

---

## 📊 Evaluation Framework

### Test Set

* 15 queries total:

  * 5 Factual
  * 5 Synthesis
  * 5 Out-of-Scope

---

### Metrics

* Routing Accuracy
* Retrieval Accuracy
* Answer Quality (semantic similarity)

---

### Run Evaluation

```bash
python evaluate.py
```

---

### Output

`results.csv` with:

| Query | True Type | Predicted Type | Routing Correct |

---

## 🚀 How to Run

### 1. Clone repository

```bash
git clone https://github.com/Suhaan2006/agentic-rag-final.git
cd agentic-rag
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Set OpenAI API Key (IMPORTANT)

PowerShell:

```bash
$env:OPENAI_API_KEY="your_api_key_here"
```

---

### 4. Run system

```bash
python main.py
```

---

### 5. Run evaluation

```bash
python evaluate.py
```

---

## 📤 Outputs

* Console responses (answers + query type)
* `results.csv` → evaluation results

---

## 🔁 Failure Handling

* Handles API errors gracefully
* Prevents crashes on invalid responses
* Returns fallback message if API fails

---

## ⚠️ Known Limitations

* Rule-based routing may misclassify complex queries
* Chunking is word-based, not token-based
* Limited contradiction resolution

---

## 🔍 Failure Analysis

### Case 1: Misclassified Synthesis Query

Cause: Keyword-based routing too shallow

### Case 2: Retrieval Miss

Cause: Chunk size not optimal

### Case 3: Weak contradiction handling

Cause: Prompt limitations

---

## 🔮 Future Improvements

* Token-based chunking
* Hybrid retrieval (BM25 + embeddings)
* Smarter routing classifier
* Better contradiction handling

---

## 📌 Key Design Decisions

* No LangChain agents (full control)
* Explicit routing for transparency
* Designed for noisy real-world data

---

> Built with a focus on reliability, interpretability, and real-world failure handling.