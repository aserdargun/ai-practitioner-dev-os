"""Sentiment Classification Model.

A simple sentiment classifier using TF-IDF and Logistic Regression.
"""

import json
import logging
import pickle
from pathlib import Path
from typing import Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Paths
DATA_PATH = Path(__file__).parent.parent / "data" / "sample_reviews.json"
MODEL_PATH = Path(__file__).parent.parent / "model.pkl"


def load_data(data_path: Path = DATA_PATH) -> tuple[list[str], list[str]]:
    """Load training data from JSON file.

    Args:
        data_path: Path to JSON data file

    Returns:
        Tuple of (texts, labels)

    Example:
        >>> texts, labels = load_data()
        >>> len(texts) == len(labels)
        True
    """
    logger.info(f"Loading data from {data_path}")

    with open(data_path) as f:
        data = json.load(f)

    texts = [item["text"] for item in data]
    labels = [item["label"] for item in data]

    logger.info(f"Loaded {len(texts)} samples")
    return texts, labels


def create_pipeline() -> Pipeline:
    """Create the ML pipeline.

    Returns:
        Scikit-learn Pipeline with TF-IDF and LogisticRegression
    """
    return Pipeline([
        ("tfidf", TfidfVectorizer(
            max_features=1000,
            ngram_range=(1, 2),
            stop_words="english",
        )),
        ("classifier", LogisticRegression(
            max_iter=1000,
            random_state=42,
        )),
    ])


def train_model(
    texts: list[str],
    labels: list[str],
    test_size: float = 0.2,
) -> tuple[Pipeline, dict[str, float]]:
    """Train the sentiment classifier.

    Args:
        texts: List of text samples
        labels: List of labels (positive/negative)
        test_size: Proportion of data for testing

    Returns:
        Tuple of (trained pipeline, evaluation metrics)
    """
    logger.info("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=test_size, random_state=42, stratify=labels
    )

    logger.info(f"Training on {len(X_train)} samples...")
    pipeline = create_pipeline()
    pipeline.fit(X_train, y_train)

    logger.info("Evaluating...")
    y_pred = pipeline.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, pos_label="positive"),
        "recall": recall_score(y_test, y_pred, pos_label="positive"),
        "f1": f1_score(y_test, y_pred, pos_label="positive"),
    }

    return pipeline, metrics


def save_model(pipeline: Pipeline, model_path: Path = MODEL_PATH) -> None:
    """Save trained model to disk.

    Args:
        pipeline: Trained sklearn pipeline
        model_path: Path to save model
    """
    with open(model_path, "wb") as f:
        pickle.dump(pipeline, f)

    logger.info(f"Model saved to {model_path}")


def load_model(model_path: Path = MODEL_PATH) -> Pipeline:
    """Load trained model from disk.

    Args:
        model_path: Path to model file

    Returns:
        Trained sklearn pipeline
    """
    with open(model_path, "rb") as f:
        return pickle.load(f)


def main():
    """Train and evaluate the model."""
    print("Loading data...")
    texts, labels = load_data()

    print("Training model...")
    pipeline, metrics = train_model(texts, labels)

    print("\nEvaluation Results:")
    print(f"  Accuracy:  {metrics['accuracy']:.2f}")
    print(f"  Precision: {metrics['precision']:.2f}")
    print(f"  Recall:    {metrics['recall']:.2f}")
    print(f"  F1 Score:  {metrics['f1']:.2f}")

    print("\nSaving model...")
    save_model(pipeline)
    print(f"Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    main()
