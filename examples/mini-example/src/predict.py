"""Prediction Interface.

Load trained model and make predictions on new text.
"""

import argparse
import sys
from pathlib import Path

from model import load_model, MODEL_PATH


def predict(text: str, model_path: Path = MODEL_PATH) -> tuple[str, float]:
    """Predict sentiment for a text.

    Args:
        text: Input text to classify
        model_path: Path to trained model

    Returns:
        Tuple of (prediction label, confidence score)

    Example:
        >>> label, conf = predict("This is great!")
        >>> label in ["positive", "negative"]
        True
    """
    model = load_model(model_path)

    # Get prediction
    prediction = model.predict([text])[0]

    # Get confidence (probability of predicted class)
    probabilities = model.predict_proba([text])[0]
    confidence = max(probabilities)

    return prediction, confidence


def predict_batch(texts: list[str], model_path: Path = MODEL_PATH) -> list[tuple[str, float]]:
    """Predict sentiment for multiple texts.

    Args:
        texts: List of texts to classify
        model_path: Path to trained model

    Returns:
        List of (prediction, confidence) tuples
    """
    model = load_model(model_path)

    predictions = model.predict(texts)
    probabilities = model.predict_proba(texts)
    confidences = [max(p) for p in probabilities]

    return list(zip(predictions, confidences))


def main():
    """CLI for predictions."""
    parser = argparse.ArgumentParser(description="Predict sentiment")
    parser.add_argument(
        "text",
        type=str,
        help="Text to classify",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=str(MODEL_PATH),
        help="Path to model file",
    )
    args = parser.parse_args()

    try:
        label, confidence = predict(args.text, Path(args.model))
        print(f"Prediction: {label} (confidence: {confidence:.2f})")
        return 0
    except FileNotFoundError:
        print("Error: Model not found. Run 'python src/model.py' first to train.")
        return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
