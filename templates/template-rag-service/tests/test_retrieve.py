"""Tests for retrieval module."""

import json
import math
import tempfile
from pathlib import Path

import pytest

# Add rag directory to path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "rag"))

from retrieve import VectorRetriever, RetrievalResult, retrieve_context


class TestVectorRetriever:
    """Tests for VectorRetriever."""

    @pytest.fixture
    def temp_store(self, tmp_path):
        """Create a temporary vector store with test data."""
        # Create chunks file
        chunks_file = tmp_path / "chunks.jsonl"
        chunks = [
            {
                "content": "RAG stands for Retrieval-Augmented Generation.",
                "doc_id": "doc1",
                "chunk_index": 0,
                "metadata": {"source": "test.md"},
            },
            {
                "content": "Document chunking splits text into smaller pieces.",
                "doc_id": "doc1",
                "chunk_index": 1,
                "metadata": {"source": "test.md"},
            },
            {
                "content": "Embeddings are vector representations of text.",
                "doc_id": "doc2",
                "chunk_index": 0,
                "metadata": {"source": "embeddings.md"},
            },
        ]
        with open(chunks_file, "w") as f:
            for chunk in chunks:
                f.write(json.dumps(chunk) + "\n")

        # Create embeddings file (using placeholder embeddings)
        embeddings_file = tmp_path / "embeddings.json"
        embeddings = {}
        for chunk in chunks:
            chunk_id = f"{chunk['doc_id']}_{chunk['chunk_index']}"
            # Simple hash-based embedding for testing
            import hashlib
            hash_bytes = hashlib.sha256(chunk["content"].encode()).digest()
            embeddings[chunk_id] = [(b - 128) / 128.0 for b in hash_bytes[:128]]

        with open(embeddings_file, "w") as f:
            json.dump(embeddings, f)

        return tmp_path

    def test_load_store(self, temp_store):
        """Retriever should load chunks and embeddings."""
        retriever = VectorRetriever(temp_store)
        assert len(retriever.chunks) == 3
        assert len(retriever.embeddings) == 3

    def test_retrieve_returns_results(self, temp_store):
        """Retrieve should return relevant results."""
        retriever = VectorRetriever(temp_store)
        results = retriever.retrieve("What is RAG?", top_k=2)
        assert len(results) > 0
        assert all(isinstance(r, RetrievalResult) for r in results)

    def test_retrieve_respects_top_k(self, temp_store):
        """Retrieve should respect top_k parameter."""
        retriever = VectorRetriever(temp_store)
        results = retriever.retrieve("text", top_k=1)
        assert len(results) <= 1

    def test_retrieve_result_has_content(self, temp_store):
        """Results should have content and metadata."""
        retriever = VectorRetriever(temp_store)
        results = retriever.retrieve("RAG", top_k=1)
        if results:
            assert results[0].content
            assert results[0].score >= 0
            assert results[0].chunk_id

    def test_empty_store(self, tmp_path):
        """Empty store should return no results."""
        retriever = VectorRetriever(tmp_path)
        results = retriever.retrieve("anything")
        assert results == []


class TestCosineSimilarity:
    """Tests for cosine similarity calculation."""

    @pytest.fixture
    def retriever(self, tmp_path):
        """Create a retriever instance."""
        return VectorRetriever(tmp_path)

    def test_identical_vectors(self, retriever):
        """Identical vectors should have similarity 1.0."""
        vec = [1.0, 2.0, 3.0]
        similarity = retriever.cosine_similarity(vec, vec)
        assert abs(similarity - 1.0) < 0.001

    def test_orthogonal_vectors(self, retriever):
        """Orthogonal vectors should have similarity 0.0."""
        vec1 = [1.0, 0.0]
        vec2 = [0.0, 1.0]
        similarity = retriever.cosine_similarity(vec1, vec2)
        assert abs(similarity - 0.0) < 0.001

    def test_opposite_vectors(self, retriever):
        """Opposite vectors should have similarity -1.0."""
        vec1 = [1.0, 0.0]
        vec2 = [-1.0, 0.0]
        similarity = retriever.cosine_similarity(vec1, vec2)
        assert abs(similarity - (-1.0)) < 0.001

    def test_different_length_vectors(self, retriever):
        """Different length vectors should return 0.0."""
        vec1 = [1.0, 2.0]
        vec2 = [1.0, 2.0, 3.0]
        similarity = retriever.cosine_similarity(vec1, vec2)
        assert similarity == 0.0


class TestRetrieveContext:
    """Tests for the retrieve_context function."""

    @pytest.fixture
    def temp_store(self, tmp_path):
        """Create a temporary vector store."""
        chunks_file = tmp_path / "chunks.jsonl"
        chunk = {
            "content": "Test content",
            "doc_id": "test",
            "chunk_index": 0,
            "metadata": {"source": "test.md"},
        }
        with open(chunks_file, "w") as f:
            f.write(json.dumps(chunk) + "\n")

        embeddings_file = tmp_path / "embeddings.json"
        import hashlib
        hash_bytes = hashlib.sha256(chunk["content"].encode()).digest()
        embedding = [(b - 128) / 128.0 for b in hash_bytes[:128]]
        with open(embeddings_file, "w") as f:
            json.dump({"test_0": embedding}, f)

        return tmp_path

    def test_retrieve_context_returns_list(self, temp_store):
        """retrieve_context should return a list."""
        results = retrieve_context("test", store_path=str(temp_store))
        assert isinstance(results, list)

    def test_retrieve_context_dict_format(self, temp_store):
        """Results should be dictionaries with expected keys."""
        results = retrieve_context("test", store_path=str(temp_store))
        if results:
            assert "content" in results[0]
            assert "score" in results[0]
            assert "source" in results[0]
