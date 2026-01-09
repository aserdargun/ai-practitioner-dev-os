"""Training script for sentiment model."""

import json
import logging
from pathlib import Path

from model import SentimentModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sample training data (in real project, load from file/database)
SAMPLE_DATA = [
    # Positive examples
    ("I love this product, it's amazing!", "positive"),
    ("Great quality and fast shipping", "positive"),
    ("This is the best purchase I've made", "positive"),
    ("Excellent service, highly recommend", "positive"),
    ("Wonderful experience, will buy again", "positive"),
    ("Perfect, exactly what I needed", "positive"),
    ("Fantastic product, exceeded expectations", "positive"),
    ("Really happy with this purchase", "positive"),
    ("Outstanding quality and value", "positive"),
    ("Superb, couldn't be happier", "positive"),
    # Negative examples
    ("Terrible product, complete waste of money", "negative"),
    ("Very disappointed with the quality", "negative"),
    ("Worst purchase ever, do not buy", "negative"),
    ("Poor quality, broke after one day", "negative"),
    ("Horrible experience, terrible service", "negative"),
    ("Not worth the price, very bad", "negative"),
    ("Awful product, totally useless", "negative"),
    ("Really unhappy with this purchase", "negative"),
    ("Disappointing quality and slow shipping", "negative"),
    ("Bad experience, would not recommend", "negative"),
]


def create_sample_data(output_dir: str) -> str:
    """Create sample data file.

    Args:
        output_dir: Directory to save data

    Returns:
        Path to created data file
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    data_path = Path(output_dir) / "training_data.jsonl"

    with open(data_path, "w") as f:
        for text, label in SAMPLE_DATA:
            f.write(json.dumps({"text": text, "label": label}) + "\n")

    logger.info(f"Created sample data at {data_path}")
    return str(data_path)


def load_training_data(data_path: str) -> tuple:
    """Load training data from JSONL file.

    Args:
        data_path: Path to JSONL file

    Returns:
        Tuple of (texts, labels)
    """
    texts = []
    labels = []

    with open(data_path, "r") as f:
        for line in f:
            item = json.loads(line)
            texts.append(item["text"])
            labels.append(item["label"])

    return texts, labels


def train_model(texts: list, labels: list, model_path: str) -> dict:
    """Train and save the sentiment model.

    Args:
        texts: List of training texts
        labels: List of labels
        model_path: Path to save trained model

    Returns:
        Training metrics
    """
    logger.info("Training model...")
    model = SentimentModel()

    metrics = model.train(texts, labels)
    logger.info(f"Training accuracy: {metrics['accuracy']:.2f}")

    # Save model
    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    model.save(model_path)
    logger.info(f"Model saved to {model_path}")

    return metrics


def main():
    """Main training pipeline."""
    # Paths
    data_dir = "data"
    model_path = "models/sentiment_model.json"

    # Create sample data
    logger.info("Creating sample data...")
    data_path = create_sample_data(data_dir)

    # Load data
    logger.info(f"Loading data from {data_path}...")
    texts, labels = load_training_data(data_path)
    logger.info(f"Loaded {len(texts)} samples")

    # Train model
    metrics = train_model(texts, labels, model_path)

    # Summary
    logger.info("=" * 40)
    logger.info("Training Complete!")
    logger.info(f"  Samples: {metrics['num_samples']}")
    logger.info(f"  Accuracy: {metrics['accuracy']:.2%}")
    logger.info(f"  Model: {model_path}")
    logger.info("=" * 40)

    # Quick test
    logger.info("\nQuick test:")
    from model import load_model

    model = load_model(model_path)

    test_texts = [
        "This is great!",
        "I hate this",
        "Not bad, pretty good",
    ]

    for text in test_texts:
        pred = model.predict(text)
        logger.info(f"  '{text}' -> {pred.sentiment} ({pred.confidence:.2f})")


if __name__ == "__main__":
    main()
