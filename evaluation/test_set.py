test_cases = [
    # FACTUAL
    {"query": "What is the purpose of AI regulation?", "type": "FACTUAL"},
    {"query": "What risks are mentioned regarding AI?", "type": "FACTUAL"},
    {"query": "Who are the stakeholders in AI governance?", "type": "FACTUAL"},
    {"query": "What policies are discussed?", "type": "FACTUAL"},
    {"query": "What is the role of government in AI?", "type": "FACTUAL"},

    # SYNTHESIS
    {"query": "Compare different approaches to AI regulation", "type": "SYNTHESIS"},
    {"query": "How do risks and policies relate?", "type": "SYNTHESIS"},
    {"query": "Analyze stakeholder perspectives across documents", "type": "SYNTHESIS"},
    {"query": "What are the combined challenges in AI governance?", "type": "SYNTHESIS"},
    {"query": "How do documents differ in their recommendations?", "type": "SYNTHESIS"},

    # OUT OF SCOPE
    {"query": "Who won FIFA 2022?", "type": "OUT_OF_SCOPE"},
    {"query": "Explain quantum computing", "type": "OUT_OF_SCOPE"},
    {"query": "What is Python programming?", "type": "OUT_OF_SCOPE"},
    {"query": "Who is Elon Musk?", "type": "OUT_OF_SCOPE"},
    {"query": "Explain black holes", "type": "OUT_OF_SCOPE"},
]