"""Tests for mini example."""

import tempfile
from pathlib import Path

import numpy as np
import pytest

from main import (
    evaluate,
    load_data,
    load_model,
    predict,
    preprocess,
    save_model,
    train,
)


def test_load_data():
    """Data loading returns correct shapes."""
    X, y, names = load_data()
    assert X.shape == (150, 4)
    assert y.shape == (150,)
    assert len(names) == 3


def test_preprocess():
    """Preprocessing splits and scales correctly."""
    X, y, _ = load_data()
    X_train, X_test, y_train, y_test, scaler = preprocess(X, y, test_size=0.2)

    # Check split sizes
    assert len(X_train) == 120
    assert len(X_test) == 30

    # Check scaling (mean ~0, std ~1 for train)
    assert np.abs(X_train.mean()) < 0.1
    assert np.abs(X_train.std() - 1.0) < 0.1


def test_train():
    """Model trains successfully."""
    X, y, _ = load_data()
    X_train, _, y_train, _, _ = preprocess(X, y)
    model = train(X_train, y_train)

    # Model should have predict method
    assert hasattr(model, "predict")
    assert hasattr(model, "predict_proba")


def test_evaluate():
    """Evaluation produces valid metrics."""
    X, y, names = load_data()
    X_train, X_test, y_train, y_test, _ = preprocess(X, y)
    model = train(X_train, y_train)

    accuracy, report, y_pred = evaluate(model, X_test, y_test, names)

    assert 0.0 <= accuracy <= 1.0
    assert len(y_pred) == len(y_test)
    assert isinstance(report, str)


def test_predict():
    """Prediction works on new data."""
    X, y, _ = load_data()
    X_train, _, y_train, _, scaler = preprocess(X, y)
    model = train(X_train, y_train)

    # Predict on sample
    sample = np.array([[5.1, 3.5, 1.4, 0.2]])
    prediction = predict(model, scaler, sample)

    assert len(prediction) == 1
    assert prediction[0] in [0, 1, 2]


def test_save_and_load_model():
    """Model saves and loads correctly."""
    X, y, _ = load_data()
    X_train, X_test, y_train, y_test, scaler = preprocess(X, y)
    model = train(X_train, y_train)

    # Get predictions before save
    original_preds = model.predict(X_test)

    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "model.pkl"
        save_model(model, scaler, path)

        assert path.exists()

        loaded_model, loaded_scaler = load_model(path)
        loaded_preds = loaded_model.predict(X_test)

        # Predictions should match
        assert np.array_equal(original_preds, loaded_preds)


def test_full_pipeline():
    """Full pipeline achieves reasonable accuracy."""
    X, y, names = load_data()
    X_train, X_test, y_train, y_test, scaler = preprocess(X, y)
    model = train(X_train, y_train)
    accuracy, _, _ = evaluate(model, X_test, y_test, names)

    # Iris should be easy - expect high accuracy
    assert accuracy >= 0.9
