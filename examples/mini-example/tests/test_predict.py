"""
Tests for Prediction Module

Run with: pytest tests/test_predict.py -v
"""

import tempfile
from pathlib import Path

import numpy as np
import pytest

from src.data import load_iris_data
from src.predict import (
    load_model,
    predict,
    predict_batch,
    predict_proba,
)
from src.train import save_model, train_model


@pytest.fixture
def trained_model():
    """Create and return a trained model."""
    X, y, _, _ = load_iris_data()
    return train_model(X, y)


@pytest.fixture
def model_path(trained_model):
    """Save model and return path."""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "model.pkl"
        save_model(trained_model, str(path))
        yield str(path)


class TestLoadModel:
    """Tests for load_model function."""

    def test_load_existing_model(self, model_path):
        """Should load an existing model."""
        model = load_model(model_path)
        assert hasattr(model, "predict")

    def test_load_nonexistent_raises(self):
        """Should raise FileNotFoundError for missing model."""
        with pytest.raises(FileNotFoundError):
            load_model("/nonexistent/path/model.pkl")


class TestPredict:
    """Tests for predict function."""

    # Typical feature values for each class
    SETOSA_FEATURES = [5.0, 3.4, 1.5, 0.2]
    VERSICOLOR_FEATURES = [5.9, 2.8, 4.5, 1.3]
    VIRGINICA_FEATURES = [6.7, 3.0, 5.5, 2.1]

    def test_predict_setosa(self, trained_model):
        """Should predict setosa correctly."""
        result = predict(trained_model, self.SETOSA_FEATURES)
        assert result == "setosa"

    def test_predict_versicolor(self, trained_model):
        """Should predict versicolor correctly."""
        result = predict(trained_model, self.VERSICOLOR_FEATURES)
        assert result == "versicolor"

    def test_predict_virginica(self, trained_model):
        """Should predict virginica correctly."""
        result = predict(trained_model, self.VIRGINICA_FEATURES)
        assert result == "virginica"

    def test_predict_returns_string(self, trained_model):
        """Prediction should be a string."""
        result = predict(trained_model, self.SETOSA_FEATURES)
        assert isinstance(result, str)

    def test_predict_valid_class(self, trained_model):
        """Prediction should be a valid class name."""
        valid_classes = {"setosa", "versicolor", "virginica"}
        result = predict(trained_model, self.SETOSA_FEATURES)
        assert result in valid_classes

    def test_predict_wrong_feature_count_raises(self, trained_model):
        """Should raise ValueError for wrong number of features."""
        with pytest.raises(ValueError, match="Expected 4 features"):
            predict(trained_model, [1.0, 2.0, 3.0])  # Only 3 features

    def test_predict_too_many_features_raises(self, trained_model):
        """Should raise ValueError for too many features."""
        with pytest.raises(ValueError, match="Expected 4 features"):
            predict(trained_model, [1.0, 2.0, 3.0, 4.0, 5.0])  # 5 features


class TestPredictProba:
    """Tests for predict_proba function."""

    SAMPLE_FEATURES = [5.0, 3.4, 1.5, 0.2]

    def test_returns_dict(self, trained_model):
        """Should return a dictionary."""
        result = predict_proba(trained_model, self.SAMPLE_FEATURES)
        assert isinstance(result, dict)

    def test_contains_all_classes(self, trained_model):
        """Should contain all class names."""
        result = predict_proba(trained_model, self.SAMPLE_FEATURES)

        assert "setosa" in result
        assert "versicolor" in result
        assert "virginica" in result

    def test_probabilities_sum_to_one(self, trained_model):
        """Probabilities should sum to 1."""
        result = predict_proba(trained_model, self.SAMPLE_FEATURES)

        total = sum(result.values())
        assert abs(total - 1.0) < 0.0001

    def test_probabilities_between_zero_and_one(self, trained_model):
        """Each probability should be between 0 and 1."""
        result = predict_proba(trained_model, self.SAMPLE_FEATURES)

        for prob in result.values():
            assert 0 <= prob <= 1

    def test_highest_prob_matches_prediction(self, trained_model):
        """Highest probability class should match prediction."""
        result = predict_proba(trained_model, self.SAMPLE_FEATURES)
        prediction = predict(trained_model, self.SAMPLE_FEATURES)

        highest_prob_class = max(result, key=result.get)
        assert highest_prob_class == prediction

    def test_wrong_feature_count_raises(self, trained_model):
        """Should raise ValueError for wrong number of features."""
        with pytest.raises(ValueError, match="Expected 4 features"):
            predict_proba(trained_model, [1.0, 2.0])


class TestPredictBatch:
    """Tests for predict_batch function."""

    def test_batch_prediction(self, trained_model):
        """Should predict multiple samples at once."""
        samples = [
            [5.0, 3.4, 1.5, 0.2],  # setosa
            [5.9, 2.8, 4.5, 1.3],  # versicolor
            [6.7, 3.0, 5.5, 2.1],  # virginica
        ]

        results = predict_batch(trained_model, samples)

        assert len(results) == 3
        assert results[0] == "setosa"
        assert results[1] == "versicolor"
        assert results[2] == "virginica"

    def test_batch_returns_list(self, trained_model):
        """Should return a list of predictions."""
        samples = [[5.0, 3.4, 1.5, 0.2]]
        results = predict_batch(trained_model, samples)

        assert isinstance(results, list)

    def test_empty_batch(self, trained_model):
        """Should handle empty batch."""
        results = predict_batch(trained_model, [])
        assert results == []


class TestEndToEnd:
    """End-to-end integration tests."""

    def test_full_workflow(self):
        """Test complete workflow: load data, train, save, load, predict."""
        # Load data
        X, y, _, _ = load_iris_data()

        # Train
        model = train_model(X, y)

        # Save
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "model.pkl"
            save_model(model, str(path))

            # Load
            loaded_model = load_model(str(path))

            # Predict
            sample = [5.0, 3.4, 1.5, 0.2]
            result = predict(loaded_model, sample)

            assert result in {"setosa", "versicolor", "virginica"}
