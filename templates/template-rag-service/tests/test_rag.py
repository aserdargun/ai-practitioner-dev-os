"""Tests for RAG service."""

import pytest
from fastapi.testclient import TestClient

from src.api import app

client = TestClient(app)


class TestAPI:
    """Tests for API endpoints."""

    def test_root(self):
        """Test root endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data

    def test_health(self):
        """Test health endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"

    def test_stats(self):
        """Test stats endpoint."""
        response = client.get("/stats")
        assert response.status_code == 200

    def test_query_without_index(self):
        """Test query without indexed documents."""
        response = client.post(
            "/query",
            json={"question": "What is the main topic?"},
        )
        assert response.status_code == 200
        data = response.json()
        assert "answer" in data


class TestModels:
    """Tests for Pydantic models."""

    def test_query_request_valid(self):
        """Test valid query request."""
        from src.models import QueryRequest

        request = QueryRequest(question="What is AI?", top_k=4)
        assert request.question == "What is AI?"
        assert request.top_k == 4

    def test_query_request_empty_question_fails(self):
        """Test that empty question fails validation."""
        from pydantic import ValidationError

        from src.models import QueryRequest

        with pytest.raises(ValidationError):
            QueryRequest(question="")

    def test_query_response(self):
        """Test query response model."""
        from src.models import QueryResponse

        response = QueryResponse(
            answer="Test answer",
            sources=["doc1.txt"],
            confidence=0.9,
        )
        assert response.answer == "Test answer"
        assert len(response.sources) == 1
