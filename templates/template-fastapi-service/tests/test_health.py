"""
Tests for FastAPI Service

Run with: pytest tests/test_health.py -v
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestHealthEndpoint:
    """Tests for health check endpoint."""

    def test_health_returns_200(self):
        """Health endpoint should return 200 OK."""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_returns_healthy_status(self):
        """Health endpoint should return healthy status."""
        response = client.get("/health")
        data = response.json()
        assert data["status"] == "healthy"

    def test_health_returns_version(self):
        """Health endpoint should include version."""
        response = client.get("/health")
        data = response.json()
        assert "version" in data
        assert data["version"] == "1.0.0"


class TestRootEndpoint:
    """Tests for root endpoint."""

    def test_root_returns_200(self):
        """Root endpoint should return 200 OK."""
        response = client.get("/")
        assert response.status_code == 200

    def test_root_returns_message(self):
        """Root endpoint should return welcome message."""
        response = client.get("/")
        data = response.json()
        assert "message" in data


class TestPredictEndpoint:
    """Tests for prediction endpoint."""

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
        assert 0 <= data["confidence"] <= 1

    def test_predict_calculates_mean(self):
        """Predict endpoint should calculate mean of features (template behavior)."""
        response = client.post("/predict", json={"features": [2.0, 4.0, 6.0]})
        data = response.json()
        assert data["prediction"] == 4.0  # Mean of [2, 4, 6]

    def test_predict_empty_features_returns_400(self):
        """Predict endpoint should return 400 for empty features."""
        response = client.post("/predict", json={"features": []})
        assert response.status_code == 400

    def test_predict_invalid_input_returns_422(self):
        """Predict endpoint should return 422 for invalid input."""
        response = client.post("/predict", json={"wrong_field": [1.0]})
        assert response.status_code == 422


class TestOpenAPIDocumentation:
    """Tests for API documentation."""

    def test_docs_endpoint_available(self):
        """OpenAPI docs should be available at /docs."""
        response = client.get("/docs")
        assert response.status_code == 200

    def test_openapi_json_available(self):
        """OpenAPI JSON schema should be available."""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        data = response.json()
        assert data["info"]["title"] == "ML Service"
