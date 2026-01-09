"""Unit tests for sentiment model."""

import json
import pytest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from model import SentimentModel, Prediction, load_model


class TestSentimentModel:
    """Tests for SentimentModel class."""

    @pytest.fixture
    def sample_data(self):
        """Sample training data."""
        texts = [
            "I love this, it's great!",
            "Excellent product, amazing quality",
            "This is terrible, very bad",
            "Awful experience, horrible service",
        ]
        labels = ["positive", "positive", "negative", "negative"]
        return texts, labels

    @pytest.fixture
    def trained_model(self, sample_data):
        """Pre-trained model for testing."""
        texts, labels = sample_data
        model = SentimentModel()
        model.train(texts, labels)
        return model

    def test_model_initializes(self):
        """Model should initialize with empty word lists."""
        model = SentimentModel()
        assert model.positive_words == []
        assert model.negative_words == []
        assert not model.is_trained

    def test_train_updates_word_lists(self, sample_data):
        """Training should populate word lists."""
        texts, labels = sample_data
        model = SentimentModel()

        model.train(texts, labels)

        assert len(model.positive_words) > 0
        assert len(model.negative_words) > 0
        assert model.is_trained

    def test_train_returns_metrics(self, sample_data):
        """Training should return accuracy metrics."""
        texts, labels = sample_data
        model = SentimentModel()

        metrics = model.train(texts, labels)

        assert "accuracy" in metrics
        assert "num_samples" in metrics
        assert metrics["num_samples"] == len(texts)
        assert 0 <= metrics["accuracy"] <= 1

    def test_predict_returns_prediction(self, trained_model):
        """Predict should return Prediction object."""
        result = trained_model.predict("This is great!")

        assert isinstance(result, Prediction)
        assert result.sentiment in ["positive", "negative"]
        assert 0 <= result.confidence <= 1

    def test_predict_positive_text(self, trained_model):
        """Positive text should predict positive."""
        result = trained_model.predict("I love this, it's amazing and great!")
        assert result.sentiment == "positive"

    def test_predict_negative_text(self, trained_model):
        """Negative text should predict negative."""
        result = trained_model.predict("This is terrible and awful, very bad!")
        assert result.sentiment == "negative"

    def test_predict_neutral_text(self, trained_model):
        """Neutral text should still return a prediction."""
        result = trained_model.predict("The sky is blue")
        assert result.sentiment in ["positive", "negative"]
        # Low confidence for neutral text
        assert result.confidence >= 0

    def test_save_and_load(self, trained_model, tmp_path):
        """Model should save and load correctly."""
        model_path = str(tmp_path / "model.json")

        # Save
        trained_model.save(model_path)
        assert Path(model_path).exists()

        # Load
        loaded_model = SentimentModel()
        loaded_model.load(model_path)

        assert loaded_model.positive_words == trained_model.positive_words
        assert loaded_model.negative_words == trained_model.negative_words
        assert loaded_model.is_trained

    def test_load_model_function(self, trained_model, tmp_path):
        """load_model helper should work correctly."""
        model_path = str(tmp_path / "model.json")
        trained_model.save(model_path)

        loaded = load_model(model_path)

        assert loaded.is_trained
        assert loaded.positive_words == trained_model.positive_words

    def test_predictions_consistent(self, trained_model):
        """Same input should give same output."""
        text = "I love this product!"

        pred1 = trained_model.predict(text)
        pred2 = trained_model.predict(text)

        assert pred1.sentiment == pred2.sentiment
        assert pred1.confidence == pred2.confidence


class TestPrediction:
    """Tests for Prediction dataclass."""

    def test_prediction_creation(self):
        """Should create prediction with required fields."""
        pred = Prediction(sentiment="positive", confidence=0.9)

        assert pred.sentiment == "positive"
        assert pred.confidence == 0.9

    def test_prediction_attributes(self):
        """Should have correct attribute types."""
        pred = Prediction(sentiment="negative", confidence=0.75)

        assert isinstance(pred.sentiment, str)
        assert isinstance(pred.confidence, float)
