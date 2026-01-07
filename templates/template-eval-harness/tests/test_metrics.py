"""Tests for evaluation metrics."""

import pytest

from src.metrics import accuracy, f1_score, mean_absolute_error, precision, recall


class TestAccuracy:
    """Tests for accuracy metric."""

    def test_perfect_accuracy(self):
        """Test perfect predictions."""
        predictions = [1, 0, 1, 0, 1]
        ground_truth = [1, 0, 1, 0, 1]
        assert accuracy(predictions, ground_truth) == 1.0

    def test_zero_accuracy(self):
        """Test all wrong predictions."""
        predictions = [1, 1, 1, 1, 1]
        ground_truth = [0, 0, 0, 0, 0]
        assert accuracy(predictions, ground_truth) == 0.0

    def test_partial_accuracy(self):
        """Test partial accuracy."""
        predictions = [1, 0, 1, 0]
        ground_truth = [1, 1, 0, 0]
        assert accuracy(predictions, ground_truth) == 0.5

    def test_empty_input(self):
        """Test empty input returns 0."""
        assert accuracy([], []) == 0.0


class TestPrecision:
    """Tests for precision metric."""

    def test_perfect_precision(self):
        """Test perfect precision."""
        predictions = [1, 1, 0, 0]
        ground_truth = [1, 1, 0, 0]
        assert precision(predictions, ground_truth) == 1.0

    def test_all_false_positives(self):
        """Test all false positives."""
        predictions = [1, 1, 1, 1]
        ground_truth = [0, 0, 0, 0]
        assert precision(predictions, ground_truth) == 0.0

    def test_no_positive_predictions(self):
        """Test no positive predictions."""
        predictions = [0, 0, 0, 0]
        ground_truth = [1, 1, 1, 1]
        assert precision(predictions, ground_truth) == 0.0


class TestRecall:
    """Tests for recall metric."""

    def test_perfect_recall(self):
        """Test perfect recall."""
        predictions = [1, 1, 0, 0]
        ground_truth = [1, 1, 0, 0]
        assert recall(predictions, ground_truth) == 1.0

    def test_all_false_negatives(self):
        """Test all false negatives."""
        predictions = [0, 0, 0, 0]
        ground_truth = [1, 1, 1, 1]
        assert recall(predictions, ground_truth) == 0.0


class TestF1Score:
    """Tests for F1 score metric."""

    def test_perfect_f1(self):
        """Test perfect F1 score."""
        predictions = [1, 1, 0, 0]
        ground_truth = [1, 1, 0, 0]
        assert f1_score(predictions, ground_truth) == 1.0

    def test_zero_f1(self):
        """Test zero F1 score."""
        predictions = [0, 0, 0, 0]
        ground_truth = [1, 1, 1, 1]
        assert f1_score(predictions, ground_truth) == 0.0


class TestMAE:
    """Tests for mean absolute error."""

    def test_perfect_predictions(self):
        """Test perfect predictions."""
        predictions = [1.0, 2.0, 3.0]
        ground_truth = [1.0, 2.0, 3.0]
        assert mean_absolute_error(predictions, ground_truth) == 0.0

    def test_known_mae(self):
        """Test known MAE value."""
        predictions = [1.0, 2.0, 3.0]
        ground_truth = [2.0, 3.0, 4.0]
        assert mean_absolute_error(predictions, ground_truth) == 1.0
