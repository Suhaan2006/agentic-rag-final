from main import build_pipeline
from evaluation.evaluator import evaluate

pipeline = build_pipeline("data")

evaluate(pipeline)