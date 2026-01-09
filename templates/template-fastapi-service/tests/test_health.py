"""Tests for the FastAPI ML service."""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """Create a test client."""
    return TestClient(app)


class TestHealthEndpoint:
    """Tests for the health check endpoint."""

    def test_health_returns_200(self, client):
        """Health endpoint should return 200 OK."""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_returns_status(self, client):
        """Health endpoint should return status field."""
        response = client.get("/health")
        data = response.json()
        assert "status" in data
        assert data["status"] == "healthy"

    def test_health_returns_model_loaded(self, client):
        """Health endpoint should indicate model loading status."""
        response = client.get("/health")
        data = response.json()
        assert "model_loaded" in data
        assert isinstance(data["model_loaded"], bool)


class TestRootEndpoint:
    """Tests for the root endpoint."""

    def test_root_returns_200(self, client):
        """Root endpoint should return 200 OK."""
        response = client.get("/")
        assert response.status_code == 200

    def test_root_returns_api_info(self, client):
        """Root endpoint should return API information."""
        response = client.get("/")
        data = response.json()
        assert "message" in data
        assert "docs" in data


class TestPredictEndpoint:
    """Tests for the prediction endpoint."""

    def test_predict_returns_200(self, client):
        """Predict endpoint should return 200 OK for valid input."""
        response = client.post("/predict", json={"data": [1.0, 2.0, 3.0]})
        assert response.status_code == 200

    def test_predict_returns_prediction(self, client):
        """Predict endpoint should return prediction field."""
        response = client.post("/predict", json={"data": [1.0, 2.0, 3.0]})
        data = response.json()
        assert "prediction" in data

    def test_predict_returns_confidence(self, client):
        """Predict endpoint should return confidence field."""
        response = client.post("/predict", json={"data": [1.0, 2.0, 3.0]})
        data = response.json()
        assert "confidence" in data

    def test_predict_validates_input(self, client):
        """Predict endpoint should validate input schema."""
        response = client.post("/predict", json={"invalid": "data"})
        assert response.status_code == 422

    def test_predict_handles_empty_data(self, client):
        """Predict endpoint should handle empty data gracefully."""
        response = client.post("/predict", json={"data": []})
        # Either returns prediction or handles gracefully
        assert response.status_code in [200, 400]
