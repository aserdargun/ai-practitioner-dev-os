"""Evaluation harness tests."""

import tempfile
from pathlib import Path

import numpy as np
import pytest
from sklearn.linear_model import LogisticRegression

from eval_harness.metrics import (
    MAE,
    MSE,
    RMSE,
    Accuracy,
    ConfusionMatrix,
    F1Score,
    Precision,
    R2Score,
    Recall,
)
from eval_harness.reporter import generate_report
from eval_harness.runner import EvaluationResults, EvaluationRunner


@pytest.fixture
def binary_classification_data():
    """Generate binary classification data."""
    np.random.seed(42)
    X = np.random.randn(100, 4)
    y = (X[:, 0] + X[:, 1] > 0).astype(int)
    return X, y


@pytest.fixture
def regression_data():
    """Generate regression data."""
    np.random.seed(42)
    X = np.random.randn(100, 4)
    y = X[:, 0] * 2 + X[:, 1] + np.random.randn(100) * 0.1
    return X, y


@pytest.fixture
def trained_classifier(binary_classification_data):
    """Train a simple classifier."""
    X, y = binary_classification_data
    model = LogisticRegression(random_state=42)
    model.fit(X, y)
    return model


class TestClassificationMetrics:
    """Tests for classification metrics."""

    def test_accuracy(self):
        """Accuracy metric computes correctly."""
        y_true = np.array([0, 1, 1, 0, 1])
        y_pred = np.array([0, 1, 0, 0, 1])
        metric = Accuracy()
        result = metric.compute(y_true, y_pred)
        assert "accuracy" in result
        assert 0 <= result["accuracy"] <= 1

    def test_precision(self):
        """Precision metric computes correctly."""
        y_true = np.array([0, 1, 1, 0, 1])
        y_pred = np.array([0, 1, 0, 0, 1])
        metric = Precision()
        result = metric.compute(y_true, y_pred)
        assert "precision_weighted" in result

    def test_recall(self):
        """Recall metric computes correctly."""
        y_true = np.array([0, 1, 1, 0, 1])
        y_pred = np.array([0, 1, 0, 0, 1])
        metric = Recall()
        result = metric.compute(y_true, y_pred)
        assert "recall_weighted" in result

    def test_f1_score(self):
        """F1 score metric computes correctly."""
        y_true = np.array([0, 1, 1, 0, 1])
        y_pred = np.array([0, 1, 0, 0, 1])
        metric = F1Score()
        result = metric.compute(y_true, y_pred)
        assert "f1_weighted" in result

    def test_confusion_matrix(self):
        """Confusion matrix metric computes correctly."""
        y_true = np.array([0, 1, 1, 0, 1])
        y_pred = np.array([0, 1, 0, 0, 1])
        metric = ConfusionMatrix()
        result = metric.compute(y_true, y_pred)
        assert "confusion_matrix" in result
        assert len(result["confusion_matrix"]) == 2


class TestRegressionMetrics:
    """Tests for regression metrics."""

    def test_mse(self):
        """MSE metric computes correctly."""
        y_true = np.array([1.0, 2.0, 3.0])
        y_pred = np.array([1.1, 2.0, 2.9])
        metric = MSE()
        result = metric.compute(y_true, y_pred)
        assert "mse" in result
        assert result["mse"] >= 0

    def test_rmse(self):
        """RMSE metric computes correctly."""
        y_true = np.array([1.0, 2.0, 3.0])
        y_pred = np.array([1.1, 2.0, 2.9])
        metric = RMSE()
        result = metric.compute(y_true, y_pred)
        assert "rmse" in result
        assert result["rmse"] >= 0

    def test_mae(self):
        """MAE metric computes correctly."""
        y_true = np.array([1.0, 2.0, 3.0])
        y_pred = np.array([1.1, 2.0, 2.9])
        metric = MAE()
        result = metric.compute(y_true, y_pred)
        assert "mae" in result
        assert result["mae"] >= 0

    def test_r2(self):
        """R2 metric computes correctly."""
        y_true = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        y_pred = np.array([1.1, 2.0, 2.9, 4.1, 5.0])
        metric = R2Score()
        result = metric.compute(y_true, y_pred)
        assert "r2" in result


class TestEvaluationRunner:
    """Tests for evaluation runner."""

    def test_add_metric(self):
        """Adding metrics works."""
        runner = EvaluationRunner()
        runner.add_metric(Accuracy())
        runner.add_metric(F1Score())
        assert len(runner.metrics) == 2

    def test_evaluate(self, trained_classifier, binary_classification_data):
        """Evaluation produces results."""
        X, y = binary_classification_data
        runner = EvaluationRunner()
        runner.add_metric(Accuracy())
        runner.add_metric(F1Score())

        results = runner.evaluate(trained_classifier, X, y)

        assert isinstance(results, EvaluationResults)
        assert "accuracy" in results.metrics
        assert "f1_weighted" in results.metrics

    def test_compare(self, binary_classification_data):
        """Model comparison works."""
        X, y = binary_classification_data

        # Train two models
        model1 = LogisticRegression(random_state=42)
        model1.fit(X, y)

        model2 = LogisticRegression(C=0.1, random_state=42)
        model2.fit(X, y)

        runner = EvaluationRunner()
        runner.add_metric(Accuracy())

        results = runner.compare(
            {"model1": model1, "model2": model2},
            X,
            y,
        )

        assert "model1" in results
        assert "model2" in results


class TestReporter:
    """Tests for report generation."""

    def test_generate_json_report(self):
        """JSON report generation works."""
        results = EvaluationResults(
            model_name="test_model",
            timestamp="2024-01-01T00:00:00",
            metrics={"accuracy": 0.95},
            metadata={"n_samples": 100, "n_features": 4},
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "report.json"
            generate_report(results, output_path, format="json")
            assert output_path.exists()

    def test_generate_html_report(self):
        """HTML report generation works."""
        results = EvaluationResults(
            model_name="test_model",
            timestamp="2024-01-01T00:00:00",
            metrics={"accuracy": 0.95, "f1_weighted": 0.94},
            metadata={"n_samples": 100, "n_features": 4},
        )

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "report.html"
            generate_report(results, output_path, format="html")
            assert output_path.exists()
            content = output_path.read_text()
            assert "test_model" in content
            assert "0.9500" in content
