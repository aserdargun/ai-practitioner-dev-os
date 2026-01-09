"""Tests for sentiment model."""

import json
import tempfile
from pathlib import Path

import pytest

# Add src to path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from model import load_data, create_pipeline, train_model, save_model, load_model


class TestDataLoading:
    """Tests for data loading."""

    @pytest.fixture
    def sample_data_file(self, tmp_path):
        """Create a sample data file."""
        data = [
            {"text": "Great product!", "label": "positive"},
            {"text": "Terrible service.", "label": "negative"},
            {"text": "Love it!", "label": "positive"},
            {"text": "Waste of money.", "label": "negative"},
        ]
        data_file = tmp_path / "test_data.json"
        with open(data_file, "w") as f:
            json.dump(data, f)
        return data_file

    def test_load_data_returns_texts_and_labels(self, sample_data_file):
        """load_data should return texts and labels."""
        texts, labels = load_data(sample_data_file)
        assert len(texts) == 4
        assert len(labels) == 4

    def test_load_data_correct_content(self, sample_data_file):
        """load_data should return correct content."""
        texts, labels = load_data(sample_data_file)
        assert "Great product!" in texts
        assert "positive" in labels
        assert "negative" in labels

    def test_load_data_file_not_found(self):
        """load_data should raise error for missing file."""
        with pytest.raises(FileNotFoundError):
            load_data(Path("/nonexistent/file.json"))


class TestPipeline:
    """Tests for ML pipeline."""

    def test_create_pipeline_has_components(self):
        """Pipeline should have tfidf and classifier."""
        pipeline = create_pipeline()
        assert "tfidf" in pipeline.named_steps
        assert "classifier" in pipeline.named_steps

    def test_pipeline_can_fit(self):
        """Pipeline should fit on sample data."""
        pipeline = create_pipeline()
        texts = ["good product", "bad product", "excellent", "terrible"]
        labels = ["positive", "negative", "positive", "negative"]
        pipeline.fit(texts, labels)
        # Should not raise

    def test_pipeline_can_predict(self):
        """Pipeline should make predictions after fitting."""
        pipeline = create_pipeline()
        texts = ["good product", "bad product", "excellent", "terrible"]
        labels = ["positive", "negative", "positive", "negative"]
        pipeline.fit(texts, labels)

        predictions = pipeline.predict(["amazing product"])
        assert len(predictions) == 1
        assert predictions[0] in ["positive", "negative"]


class TestTraining:
    """Tests for model training."""

    @pytest.fixture
    def training_data(self):
        """Sample training data."""
        texts = [
            "Great product, love it!",
            "Excellent quality",
            "Amazing experience",
            "Highly recommend",
            "Best purchase ever",
            "Terrible product",
            "Waste of money",
            "Very disappointed",
            "Would not recommend",
            "Horrible quality",
        ]
        labels = ["positive"] * 5 + ["negative"] * 5
        return texts, labels

    def test_train_model_returns_pipeline_and_metrics(self, training_data):
        """train_model should return pipeline and metrics."""
        texts, labels = training_data
        pipeline, metrics = train_model(texts, labels)

        assert pipeline is not None
        assert isinstance(metrics, dict)

    def test_train_model_metrics_keys(self, training_data):
        """Metrics should have expected keys."""
        texts, labels = training_data
        _, metrics = train_model(texts, labels)

        assert "accuracy" in metrics
        assert "precision" in metrics
        assert "recall" in metrics
        assert "f1" in metrics

    def test_train_model_metrics_values(self, training_data):
        """Metrics should be valid values."""
        texts, labels = training_data
        _, metrics = train_model(texts, labels)

        for key, value in metrics.items():
            assert 0 <= value <= 1, f"{key} should be between 0 and 1"


class TestModelPersistence:
    """Tests for save/load model."""

    @pytest.fixture
    def trained_model(self):
        """Train a simple model."""
        texts = ["good", "bad", "great", "terrible"] * 3
        labels = ["positive", "negative", "positive", "negative"] * 3
        pipeline = create_pipeline()
        pipeline.fit(texts, labels)
        return pipeline

    def test_save_and_load_model(self, trained_model, tmp_path):
        """Model should be saveable and loadable."""
        model_path = tmp_path / "model.pkl"
        save_model(trained_model, model_path)

        loaded = load_model(model_path)
        assert loaded is not None

    def test_loaded_model_predicts_same(self, trained_model, tmp_path):
        """Loaded model should give same predictions."""
        model_path = tmp_path / "model.pkl"
        save_model(trained_model, model_path)
        loaded = load_model(model_path)

        test_text = ["this is good"]
        original_pred = trained_model.predict(test_text)
        loaded_pred = loaded.predict(test_text)

        assert original_pred[0] == loaded_pred[0]


class TestEdgeCases:
    """Tests for edge cases."""

    def test_empty_text_prediction(self):
        """Empty text should still return prediction."""
        pipeline = create_pipeline()
        texts = ["good", "bad"] * 5
        labels = ["positive", "negative"] * 5
        pipeline.fit(texts, labels)

        # Empty string
        pred = pipeline.predict([""])
        assert len(pred) == 1

    def test_very_long_text(self):
        """Very long text should work."""
        pipeline = create_pipeline()
        texts = ["good product"] * 5 + ["bad product"] * 5
        labels = ["positive"] * 5 + ["negative"] * 5
        pipeline.fit(texts, labels)

        long_text = "good " * 1000
        pred = pipeline.predict([long_text])
        assert len(pred) == 1

    def test_special_characters(self):
        """Special characters should be handled."""
        pipeline = create_pipeline()
        texts = ["good!!!", "bad???", "great...", "terrible!!!"]
        labels = ["positive", "negative", "positive", "negative"]
        pipeline.fit(texts * 3, labels * 3)

        pred = pipeline.predict(["amazing!!! 🎉"])
        assert len(pred) == 1
