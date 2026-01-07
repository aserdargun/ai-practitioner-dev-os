"""Tests for the main FastAPI application."""

import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


class TestRoot:
    """Tests for the root endpoint."""

    def test_root_returns_welcome_message(self):
        """Test that root endpoint returns welcome message."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data


class TestHealth:
    """Tests for health check endpoints."""

    def test_health_check_returns_healthy(self):
        """Test that health endpoint returns healthy status."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"

    def test_readiness_check_returns_ready(self):
        """Test that readiness endpoint returns ready status."""
        response = client.get("/ready")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ready"
        assert "checks" in data


class TestPredict:
    """Tests for prediction endpoint."""

    def test_predict_with_valid_features(self):
        """Test prediction with valid feature input."""
        response = client.post(
            "/predict",
            json={"features": [1.0, 2.0, 3.0, 4.0]},
        )
        assert response.status_code == 200
        data = response.json()
        assert "prediction" in data
        assert "confidence" in data
        assert "model_version" in data

    def test_predict_with_single_feature(self):
        """Test prediction with single feature."""
        response = client.post(
            "/predict",
            json={"features": [5.0]},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["prediction"] == 5.0

    def test_predict_with_empty_features_fails(self):
        """Test that empty features returns validation error."""
        response = client.post(
            "/predict",
            json={"features": []},
        )
        assert response.status_code == 422  # Validation error

    def test_predict_with_invalid_type_fails(self):
        """Test that invalid feature type returns validation error."""
        response = client.post(
            "/predict",
            json={"features": "not a list"},
        )
        assert response.status_code == 422
