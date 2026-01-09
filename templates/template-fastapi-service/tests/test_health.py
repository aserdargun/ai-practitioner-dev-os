"""Tests for the FastAPI service."""

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestHealthEndpoint:
    """Tests for the health check endpoint."""

    def test_health_returns_200(self):
        """Health endpoint should return 200 OK."""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_returns_healthy_status(self):
        """Health endpoint should return healthy status."""
        response = client.get("/health")
        data = response.json()
        assert data["status"] == "healthy"

    def test_health_includes_model_status(self):
        """Health endpoint should include model loaded status."""
        response = client.get("/health")
        data = response.json()
        assert "model_loaded" in data
        assert isinstance(data["model_loaded"], bool)


class TestPredictEndpoint:
    """Tests for the prediction endpoint."""

    def test_predict_returns_200(self):
        """Predict endpoint should return 200 for valid input."""
        response = client.post("/predict", json={"features": [1.0, 2.0, 3.0]})
        assert response.status_code == 200

    def test_predict_returns_prediction(self):
        """Predict endpoint should return prediction value."""
        response = client.post("/predict", json={"features": [1.0, 2.0, 3.0]})
        data = response.json()
        assert "prediction" in data
        assert isinstance(data["prediction"], float)

    def test_predict_returns_confidence(self):
        """Predict endpoint should return confidence score."""
        response = client.post("/predict", json={"features": [1.0, 2.0, 3.0]})
        data = response.json()
        assert "confidence" in data
        assert 0.0 <= data["confidence"] <= 1.0

    def test_predict_empty_features_fails(self):
        """Predict endpoint should reject empty features."""
        response = client.post("/predict", json={"features": []})
        assert response.status_code == 422

    def test_predict_missing_features_fails(self):
        """Predict endpoint should reject missing features."""
        response = client.post("/predict", json={})
        assert response.status_code == 422

    def test_predict_invalid_type_fails(self):
        """Predict endpoint should reject invalid feature types."""
        response = client.post("/predict", json={"features": ["not", "numbers"]})
        assert response.status_code == 422


class TestRootEndpoint:
    """Tests for the root endpoint."""

    def test_root_returns_200(self):
        """Root endpoint should return 200 OK."""
        response = client.get("/")
        assert response.status_code == 200

    def test_root_returns_service_info(self):
        """Root endpoint should return service information."""
        response = client.get("/")
        data = response.json()
        assert "service" in data
        assert "version" in data
        assert "docs" in data
