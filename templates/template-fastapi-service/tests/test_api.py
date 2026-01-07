"""API endpoint tests."""

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    """Test health endpoint returns healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_model_info():
    """Test model info endpoint returns metadata."""
    response = client.get("/model/info")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "version" in data
    assert "description" in data
    assert "features_count" in data


def test_predict_single():
    """Test single prediction endpoint."""
    response = client.post(
        "/predict",
        json={"features": [1.0, 2.0, 3.0, 4.0]},
    )
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert isinstance(data["prediction"], (int, float))


def test_predict_batch():
    """Test batch prediction endpoint."""
    response = client.post(
        "/predict/batch",
        json={
            "instances": [
                {"features": [1.0, 2.0, 3.0, 4.0]},
                {"features": [5.0, 6.0, 7.0, 8.0]},
            ]
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert "predictions" in data
    assert len(data["predictions"]) == 2


def test_predict_invalid_input():
    """Test prediction with invalid input returns error."""
    response = client.post(
        "/predict",
        json={"features": []},
    )
    assert response.status_code == 422  # Validation error


def test_predict_missing_features():
    """Test prediction with missing features returns error."""
    response = client.post(
        "/predict",
        json={},
    )
    assert response.status_code == 422  # Validation error
