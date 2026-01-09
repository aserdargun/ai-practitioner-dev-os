"""Integration tests for sentiment API."""

import pytest
from fastapi.testclient import TestClient
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from serve import app

client = TestClient(app)


class TestHealthEndpoint:
    """Tests for health check endpoint."""

    def test_health_returns_200(self):
        """Health endpoint should return 200."""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_returns_status(self):
        """Health endpoint should return status field."""
        response = client.get("/health")
        data = response.json()

        assert "status" in data
        assert data["status"] == "healthy"

    def test_health_returns_model_status(self):
        """Health endpoint should indicate model status."""
        response = client.get("/health")
        data = response.json()

        assert "model_loaded" in data
        assert isinstance(data["model_loaded"], bool)


class TestPredictEndpoint:
    """Tests for prediction endpoint."""

    def test_predict_returns_200(self):
        """Predict should return 200 for valid input."""
        response = client.post(
            "/predict",
            json={"text": "This is a test message"},
        )
        assert response.status_code == 200

    def test_predict_returns_sentiment(self):
        """Predict should return sentiment field."""
        response = client.post(
            "/predict",
            json={"text": "I love this product!"},
        )
        data = response.json()

        assert "sentiment" in data
        assert data["sentiment"] in ["positive", "negative"]

    def test_predict_returns_confidence(self):
        """Predict should return confidence field."""
        response = client.post(
            "/predict",
            json={"text": "Great experience"},
        )
        data = response.json()

        assert "confidence" in data
        assert isinstance(data["confidence"], float)
        assert 0 <= data["confidence"] <= 1

    def test_predict_positive_text(self):
        """Positive text should predict positive."""
        response = client.post(
            "/predict",
            json={"text": "I love this, it's amazing and wonderful!"},
        )
        data = response.json()

        assert data["sentiment"] == "positive"

    def test_predict_negative_text(self):
        """Negative text should predict negative."""
        response = client.post(
            "/predict",
            json={"text": "This is terrible and awful!"},
        )
        data = response.json()

        assert data["sentiment"] == "negative"

    def test_predict_empty_text_fails(self):
        """Empty text should fail validation."""
        response = client.post(
            "/predict",
            json={"text": ""},
        )
        assert response.status_code == 422

    def test_predict_missing_text_fails(self):
        """Missing text field should fail."""
        response = client.post(
            "/predict",
            json={},
        )
        assert response.status_code == 422

    def test_predict_invalid_json_fails(self):
        """Invalid JSON should fail."""
        response = client.post(
            "/predict",
            content="not json",
            headers={"Content-Type": "application/json"},
        )
        assert response.status_code == 422


class TestRootEndpoint:
    """Tests for root endpoint."""

    def test_root_returns_200(self):
        """Root should return 200."""
        response = client.get("/")
        assert response.status_code == 200

    def test_root_returns_api_info(self):
        """Root should return API information."""
        response = client.get("/")
        data = response.json()

        assert "name" in data
        assert "version" in data
        assert "endpoints" in data


class TestDocsEndpoint:
    """Tests for documentation endpoints."""

    def test_docs_available(self):
        """Swagger docs should be available."""
        response = client.get("/docs")
        assert response.status_code == 200

    def test_openapi_schema_available(self):
        """OpenAPI schema should be available."""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        data = response.json()
        assert "openapi" in data
        assert "paths" in data
