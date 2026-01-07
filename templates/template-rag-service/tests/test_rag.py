"""RAG service tests."""

import pytest
from fastapi.testclient import TestClient

from rag.api import app
from rag.chunker import chunk_text
from rag.embedder import Embedder
from rag.retriever import Retriever

client = TestClient(app)


class TestChunker:
    """Tests for text chunking."""

    def test_chunk_empty_text(self):
        """Empty text returns empty list."""
        assert chunk_text("") == []
        assert chunk_text("   ") == []

    def test_chunk_short_text(self):
        """Short text returns single chunk."""
        text = "This is a short text."
        chunks = chunk_text(text, chunk_size=100)
        assert len(chunks) == 1
        assert chunks[0] == text

    def test_chunk_long_text(self):
        """Long text is split into multiple chunks."""
        text = "First paragraph.\n\n" * 50
        chunks = chunk_text(text, chunk_size=100, chunk_overlap=0)
        assert len(chunks) > 1

    def test_chunk_preserves_paragraphs(self):
        """Chunking preserves paragraph boundaries when possible."""
        text = "Paragraph one.\n\nParagraph two.\n\nParagraph three."
        chunks = chunk_text(text, chunk_size=50, chunk_overlap=0)
        assert len(chunks) >= 2


class TestEmbedder:
    """Tests for embedding generation."""

    @pytest.fixture
    def embedder(self):
        """Create embedder instance."""
        return Embedder()

    def test_embed_single(self, embedder):
        """Single text embedding has correct shape."""
        embedding = embedder.embed("Test text")
        assert embedding.shape == (embedder.dimension,)

    def test_embed_batch(self, embedder):
        """Batch embedding has correct shape."""
        texts = ["Text one", "Text two", "Text three"]
        embeddings = embedder.embed_batch(texts)
        assert embeddings.shape == (3, embedder.dimension)

    def test_similar_texts_have_similar_embeddings(self, embedder):
        """Similar texts produce similar embeddings."""
        import numpy as np

        emb1 = embedder.embed("The cat sat on the mat")
        emb2 = embedder.embed("The cat was sitting on the mat")
        emb3 = embedder.embed("Quantum physics is complex")

        # Cosine similarity
        sim_12 = np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
        sim_13 = np.dot(emb1, emb3) / (np.linalg.norm(emb1) * np.linalg.norm(emb3))

        assert sim_12 > sim_13  # Similar texts should be more similar


class TestRetriever:
    """Tests for vector retrieval."""

    @pytest.fixture
    def retriever(self):
        """Create retriever instance."""
        embedder = Embedder()
        return Retriever(embedder)

    def test_add_document(self, retriever):
        """Adding document increases count."""
        assert retriever.document_count == 0
        retriever.add_document("Test document")
        assert retriever.document_count == 1

    def test_add_documents(self, retriever):
        """Adding multiple documents."""
        texts = ["Doc one", "Doc two", "Doc three"]
        indices = retriever.add_documents(texts)
        assert len(indices) == 3
        assert retriever.document_count == 3

    def test_search_returns_results(self, retriever):
        """Search returns relevant results."""
        retriever.add_documents(
            [
                "Python is a programming language",
                "Machine learning is a field of AI",
                "Cats are furry animals",
            ]
        )
        results = retriever.search("What is Python?", top_k=2)
        assert len(results) == 2
        assert "Python" in results[0]["text"]

    def test_search_empty_index(self, retriever):
        """Search on empty index returns empty list."""
        results = retriever.search("query")
        assert results == []

    def test_clear(self, retriever):
        """Clear removes all documents."""
        retriever.add_document("Test")
        retriever.clear()
        assert retriever.document_count == 0


class TestAPI:
    """Tests for API endpoints."""

    def test_health_check(self):
        """Health endpoint returns healthy status."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"

    def test_ingest_document(self):
        """Ingest endpoint accepts documents."""
        response = client.post(
            "/ingest",
            json={
                "text": "This is a test document for ingestion.",
                "metadata": {"source": "test"},
            },
        )
        assert response.status_code == 200
        assert response.json()["status"] == "success"

    def test_search(self):
        """Search endpoint returns results."""
        # First ingest a document
        client.post(
            "/ingest",
            json={"text": "Python is great for data science."},
        )

        response = client.post(
            "/search",
            json={"query": "Python", "top_k": 5},
        )
        assert response.status_code == 200
        assert "results" in response.json()

    def test_list_documents(self):
        """Documents endpoint lists indexed documents."""
        response = client.get("/documents")
        assert response.status_code == 200
        assert "count" in response.json()
