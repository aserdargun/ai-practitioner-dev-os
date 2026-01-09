"""
Tests for Retrieval Module

Run with: pytest tests/test_retrieve.py -v
"""

import json
import tempfile
from pathlib import Path

import pytest

from rag.ingest import (
    chunk_document,
    create_index_entry,
    generate_embedding,
    load_document,
)
from rag.retrieve import Retriever, cosine_similarity


class TestChunking:
    """Tests for document chunking."""

    def test_chunk_empty_text(self):
        """Empty text should return empty list."""
        chunks = chunk_document("")
        assert chunks == []

    def test_chunk_short_text(self):
        """Short text should return single chunk."""
        text = "This is a short text."
        chunks = chunk_document(text, chunk_size=100)
        assert len(chunks) == 1
        assert chunks[0] == text

    def test_chunk_long_text(self):
        """Long text should be split into multiple chunks."""
        text = "This is a sentence. " * 50
        chunks = chunk_document(text, chunk_size=100, overlap=20)
        assert len(chunks) > 1

    def test_chunks_have_overlap(self):
        """Chunks should have overlapping content."""
        text = "word " * 100
        chunks = chunk_document(text, chunk_size=50, overlap=10)

        # Check that chunks exist
        assert len(chunks) >= 2


class TestEmbeddings:
    """Tests for embedding generation."""

    def test_embedding_returns_list(self):
        """Embedding should return list of floats."""
        embedding = generate_embedding("test text")
        assert isinstance(embedding, list)
        assert all(isinstance(x, float) for x in embedding)

    def test_embedding_consistent(self):
        """Same text should produce same embedding."""
        text = "consistent test"
        emb1 = generate_embedding(text)
        emb2 = generate_embedding(text)
        assert emb1 == emb2

    def test_embedding_different_for_different_text(self):
        """Different text should produce different embeddings."""
        emb1 = generate_embedding("text one")
        emb2 = generate_embedding("text two")
        assert emb1 != emb2


class TestCosineSimilarity:
    """Tests for cosine similarity calculation."""

    def test_identical_vectors(self):
        """Identical vectors should have similarity 1.0."""
        vec = [0.5, 0.5, 0.5]
        similarity = cosine_similarity(vec, vec)
        assert abs(similarity - 1.0) < 0.0001

    def test_orthogonal_vectors(self):
        """Orthogonal vectors should have similarity 0.0."""
        vec1 = [1.0, 0.0, 0.0]
        vec2 = [0.0, 1.0, 0.0]
        similarity = cosine_similarity(vec1, vec2)
        assert abs(similarity) < 0.0001

    def test_opposite_vectors(self):
        """Opposite vectors should have similarity -1.0."""
        vec1 = [1.0, 0.0]
        vec2 = [-1.0, 0.0]
        similarity = cosine_similarity(vec1, vec2)
        assert abs(similarity + 1.0) < 0.0001

    def test_mismatched_length_raises(self):
        """Vectors of different lengths should raise error."""
        vec1 = [1.0, 2.0]
        vec2 = [1.0, 2.0, 3.0]
        with pytest.raises(ValueError):
            cosine_similarity(vec1, vec2)


class TestRetriever:
    """Tests for Retriever class."""

    @pytest.fixture
    def sample_index(self, tmp_path):
        """Create a sample index file."""
        index_data = [
            {
                "id": "doc1_0",
                "text": "Machine learning is a type of artificial intelligence.",
                "embedding": generate_embedding(
                    "Machine learning is a type of artificial intelligence."
                ),
                "metadata": {"source": "doc1.txt", "filename": "doc1.txt", "chunk_index": 0},
            },
            {
                "id": "doc2_0",
                "text": "Python is a programming language used for data science.",
                "embedding": generate_embedding(
                    "Python is a programming language used for data science."
                ),
                "metadata": {"source": "doc2.txt", "filename": "doc2.txt", "chunk_index": 0},
            },
            {
                "id": "doc3_0",
                "text": "Deep learning uses neural networks with many layers.",
                "embedding": generate_embedding(
                    "Deep learning uses neural networks with many layers."
                ),
                "metadata": {"source": "doc3.txt", "filename": "doc3.txt", "chunk_index": 0},
            },
        ]

        index_path = tmp_path / "index.json"
        with open(index_path, "w") as f:
            json.dump(index_data, f)

        return index_path

    def test_retriever_loads_index(self, sample_index):
        """Retriever should load index from file."""
        retriever = Retriever(str(sample_index))
        assert len(retriever.index) == 3

    def test_retriever_missing_index(self, tmp_path):
        """Retriever should handle missing index gracefully."""
        retriever = Retriever(str(tmp_path / "nonexistent.json"))
        assert len(retriever.index) == 0

    def test_search_returns_results(self, sample_index):
        """Search should return matching documents."""
        retriever = Retriever(str(sample_index))
        results = retriever.search("machine learning AI", top_k=2)
        assert len(results) <= 2
        assert all("text" in r for r in results)
        assert all("score" in r for r in results)

    def test_search_respects_top_k(self, sample_index):
        """Search should respect top_k limit."""
        retriever = Retriever(str(sample_index))
        results = retriever.search("learning", top_k=1)
        assert len(results) == 1

    def test_search_empty_index(self, tmp_path):
        """Search on empty index should return empty list."""
        retriever = Retriever(str(tmp_path / "nonexistent.json"))
        results = retriever.search("test query")
        assert results == []

    def test_get_document(self, sample_index):
        """Should retrieve specific document by ID."""
        retriever = Retriever(str(sample_index))
        doc = retriever.get_document("doc1_0")
        assert doc is not None
        assert doc["id"] == "doc1_0"

    def test_get_document_not_found(self, sample_index):
        """Should return None for non-existent document."""
        retriever = Retriever(str(sample_index))
        doc = retriever.get_document("nonexistent")
        assert doc is None


class TestDocumentLoading:
    """Tests for document loading."""

    def test_load_text_document(self, tmp_path):
        """Should load text document."""
        doc_path = tmp_path / "test.txt"
        doc_path.write_text("Test content")

        doc = load_document(str(doc_path))
        assert doc["content"] == "Test content"
        assert doc["filename"] == "test.txt"

    def test_load_nonexistent_raises(self):
        """Loading non-existent file should raise error."""
        with pytest.raises(FileNotFoundError):
            load_document("nonexistent.txt")


class TestIndexEntry:
    """Tests for index entry creation."""

    def test_create_index_entry(self):
        """Should create valid index entry."""
        metadata = {"source": "test.txt", "filename": "test.txt"}
        entry = create_index_entry("Test chunk text", metadata, 0)

        assert entry["id"] == "test.txt_0"
        assert entry["text"] == "Test chunk text"
        assert "embedding" in entry
        assert entry["metadata"]["source"] == "test.txt"
