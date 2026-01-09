"""
Tests for Model Training Module

Run with: pytest tests/test_train.py -v
"""

import tempfile
from pathlib import Path

import numpy as np
import pytest

from src.data import load_iris_data, split_data
from src.train import (
    evaluate_model,
    get_feature_importance,
    save_model,
    train_model,
)


@pytest.fixture
def iris_data():
    """Load Iris dataset for tests."""
    return load_iris_data()


@pytest.fixture
def split_iris_data(iris_data):
    """Split Iris data for tests."""
    X, y, feature_names, target_names = iris_data
    X_train, X_test, y_train, y_test = split_data(X, y)
    return X_train, X_test, y_train, y_test, feature_names, target_names


@pytest.fixture
def trained_model(split_iris_data):
    """Train a model for tests."""
    X_train, X_test, y_train, y_test, _, _ = split_iris_data
    return train_model(X_train, y_train)


class TestTrainModel:
    """Tests for train_model function."""

    def test_train_model_returns_classifier(self, iris_data):
        """Training should return a classifier."""
        X, y, _, _ = iris_data
        model = train_model(X, y)

        assert hasattr(model, "predict")
        assert hasattr(model, "predict_proba")

    def test_train_model_is_fitted(self, iris_data):
        """Model should be fitted after training."""
        X, y, _, _ = iris_data
        model = train_model(X, y)

        # Fitted models have classes_ attribute
        assert hasattr(model, "classes_")
        assert len(model.classes_) == 3

    def test_train_model_reproducible(self, iris_data):
        """Training with same seed should be reproducible."""
        X, y, _, _ = iris_data

        model1 = train_model(X, y, random_state=42)
        model2 = train_model(X, y, random_state=42)

        # Predictions should be identical
        pred1 = model1.predict(X[:5])
        pred2 = model2.predict(X[:5])

        assert np.array_equal(pred1, pred2)

    def test_train_model_custom_estimators(self, iris_data):
        """Should accept custom number of estimators."""
        X, y, _, _ = iris_data
        model = train_model(X, y, n_estimators=10)

        assert model.n_estimators == 10


class TestEvaluateModel:
    """Tests for evaluate_model function."""

    def test_evaluate_returns_accuracy(self, trained_model, split_iris_data):
        """Evaluation should return accuracy."""
        X_train, X_test, y_train, y_test, _, _ = split_iris_data
        metrics = evaluate_model(trained_model, X_test, y_test)

        assert "accuracy" in metrics
        assert 0 <= metrics["accuracy"] <= 1

    def test_evaluate_returns_confusion_matrix(self, trained_model, split_iris_data):
        """Evaluation should return confusion matrix."""
        X_train, X_test, y_train, y_test, _, _ = split_iris_data
        metrics = evaluate_model(trained_model, X_test, y_test)

        assert "confusion_matrix" in metrics
        assert len(metrics["confusion_matrix"]) == 3  # 3 classes

    def test_evaluate_high_accuracy(self, trained_model, split_iris_data):
        """Model should achieve high accuracy on Iris."""
        X_train, X_test, y_train, y_test, _, _ = split_iris_data
        metrics = evaluate_model(trained_model, X_test, y_test)

        # Iris is easy - should get >90% accuracy
        assert metrics["accuracy"] > 0.9

    def test_evaluate_with_target_names(self, trained_model, split_iris_data):
        """Evaluation with target names should return classification report."""
        X_train, X_test, y_train, y_test, _, target_names = split_iris_data
        metrics = evaluate_model(trained_model, X_test, y_test, target_names)

        assert "classification_report" in metrics


class TestSaveModel:
    """Tests for save_model function."""

    def test_save_model_creates_file(self, trained_model):
        """Saving should create a file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "model.pkl"
            save_model(trained_model, str(path))

            assert path.exists()

    def test_save_model_creates_directory(self, trained_model):
        """Saving should create parent directories."""
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "nested" / "dir" / "model.pkl"
            save_model(trained_model, str(path))

            assert path.exists()

    def test_save_and_load_model(self, trained_model, iris_data):
        """Saved model should load correctly."""
        X, y, _, _ = iris_data

        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "model.pkl"
            save_model(trained_model, str(path))

            # Load with predict module
            from src.predict import load_model

            loaded = load_model(str(path))

            # Predictions should match
            pred_original = trained_model.predict(X[:5])
            pred_loaded = loaded.predict(X[:5])

            assert np.array_equal(pred_original, pred_loaded)


class TestFeatureImportance:
    """Tests for get_feature_importance function."""

    def test_returns_all_features(self, trained_model, iris_data):
        """Should return importance for all features."""
        _, _, feature_names, _ = iris_data
        importance = get_feature_importance(trained_model, feature_names)

        assert len(importance) == len(feature_names)

    def test_importances_sum_to_one(self, trained_model, iris_data):
        """Feature importances should sum to approximately 1."""
        _, _, feature_names, _ = iris_data
        importance = get_feature_importance(trained_model, feature_names)

        total = sum(importance.values())
        assert abs(total - 1.0) < 0.01

    def test_petal_features_important(self, trained_model, iris_data):
        """Petal features should be more important than sepal."""
        _, _, feature_names, _ = iris_data
        importance = get_feature_importance(trained_model, feature_names)

        petal_importance = sum(
            v for k, v in importance.items() if "petal" in k.lower()
        )
        sepal_importance = sum(
            v for k, v in importance.items() if "sepal" in k.lower()
        )

        # Petal features are typically more discriminative
        assert petal_importance > sepal_importance
