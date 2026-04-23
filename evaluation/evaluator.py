import pandas as pd
from evaluation.test_set import test_cases

def evaluate(pipeline):
    results = []

    for case in test_cases:
        output = pipeline(case["query"])

        results.append({
            "query": case["query"],
            "true_type": case["type"],
            "predicted_type": output["type"],
            "correct_routing": case["type"] == output["type"]
        })

    df = pd.DataFrame(results)
    df.to_csv("results.csv", index=False)
    print(df)