def classify_query(query, scores):
    query_lower = query.lower()

    synthesis_keywords = ["compare", "difference", "impact", "analyze", "relationship"]

    if any(k in query_lower for k in synthesis_keywords):
        return "SYNTHESIS"

    if max(scores) < 0.3:
        return "OUT_OF_SCOPE"

    if len([s for s in scores if s < 0.5]) >= 2:
        return "SYNTHESIS"

    return "FACTUAL"