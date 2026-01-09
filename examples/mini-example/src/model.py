"""Sentiment analysis model."""

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


@dataclass
class Prediction:
    """Model prediction result."""

    sentiment: str  # "positive" or "negative"
    confidence: float  # 0.0 to 1.0


class SentimentModel:
    """Simple rule-based sentiment classifier.

    This is a demonstration model. In production, replace with:
    - scikit-learn classifier (LogisticRegression, SVM)
    - Transformer model (BERT, DistilBERT)
    - Cloud API (OpenAI, Anthropic)
    """

    def __init__(self):
        """Initialize the model with default word lists."""
        self.positive_words: List[str] = []
        self.negative_words: List[str] = []
        self._trained = False

    def train(
        self,
        texts: List[str],
        labels: List[str],
    ) -> Dict[str, float]:
        """Train the model on labeled data.

        For this simple model, we extract positive/negative words
        from the training data.

        Args:
            texts: List of text samples
            labels: List of labels ("positive" or "negative")

        Returns:
            Dictionary with training metrics
        """
        positive_texts = [t for t, l in zip(texts, labels) if l == "positive"]
        negative_texts = [t for t, l in zip(texts, labels) if l == "negative"]

        # Extract frequent words from each class
        self.positive_words = self._extract_keywords(positive_texts)
        self.negative_words = self._extract_keywords(negative_texts)

        # Remove common words that appear in both
        common = set(self.positive_words) & set(self.negative_words)
        self.positive_words = [w for w in self.positive_words if w not in common]
        self.negative_words = [w for w in self.negative_words if w not in common]

        self._trained = True

        # Compute training accuracy
        correct = sum(
            1 for t, l in zip(texts, labels) if self.predict(t).sentiment == l
        )
        accuracy = correct / len(texts) if texts else 0.0

        return {"accuracy": accuracy, "num_samples": len(texts)}

    def predict(self, text: str) -> Prediction:
        """Predict sentiment for text.

        Args:
            text: Input text to classify

        Returns:
            Prediction with sentiment and confidence
        """
        words = self._tokenize(text)

        pos_count = sum(1 for w in words if w in self.positive_words)
        neg_count = sum(1 for w in words if w in self.negative_words)

        total = pos_count + neg_count
        if total == 0:
            # No signal, default to neutral-ish positive
            return Prediction(sentiment="positive", confidence=0.5)

        if pos_count >= neg_count:
            confidence = pos_count / total
            return Prediction(sentiment="positive", confidence=confidence)
        else:
            confidence = neg_count / total
            return Prediction(sentiment="negative", confidence=confidence)

    def save(self, path: str) -> None:
        """Save model to JSON file.

        Args:
            path: Output file path
        """
        model_data = {
            "positive_words": self.positive_words,
            "negative_words": self.negative_words,
            "trained": self._trained,
        }

        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(model_data, f, indent=2)

    def load(self, path: str) -> None:
        """Load model from JSON file.

        Args:
            path: Input file path
        """
        with open(path, "r") as f:
            model_data = json.load(f)

        self.positive_words = model_data["positive_words"]
        self.negative_words = model_data["negative_words"]
        self._trained = model_data["trained"]

    def _tokenize(self, text: str) -> List[str]:
        """Tokenize text into lowercase words."""
        text = text.lower()
        words = re.findall(r"\w+", text)
        return words

    def _extract_keywords(self, texts: List[str]) -> List[str]:
        """Extract frequent keywords from texts."""
        word_counts: Dict[str, int] = {}

        for text in texts:
            words = self._tokenize(text)
            for word in words:
                if len(word) > 2:  # Skip very short words
                    word_counts[word] = word_counts.get(word, 0) + 1

        # Sort by frequency and return top words
        sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        return [word for word, count in sorted_words[:50] if count >= 2]

    @property
    def is_trained(self) -> bool:
        """Check if model has been trained."""
        return self._trained


def load_model(path: str) -> SentimentModel:
    """Load a trained model from file.

    Args:
        path: Path to saved model

    Returns:
        Loaded SentimentModel
    """
    model = SentimentModel()
    model.load(path)
    return model
