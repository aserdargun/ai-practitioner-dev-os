"""Tests for RAG retrieval."""

import pytest

from rag.ingest import Chunk, DocumentIngester
from rag.retrieve import MockEmbedder, MockVectorStore, Retriever


class TestMockEmbedder:
    """Tests for MockEmbedder."""

    def test_embed_returns_correct_dimension(self):
        """Embedding should have correct dimension."""
        embedder = MockEmbedder(dimension=64)
        embedding = embedder.embed("test text")
        assert len(embedding) == 64

    def test_embed_is_normalized(self):
        """Embedding should be approximately normalized."""
        embedder = MockEmbedder()
        embedding = embedder.embed("test text")

        import math

        norm = math.sqrt(sum(x * x for x in embedding))
        assert abs(norm - 1.0) < 0.01

    def test_embed_is_deterministic(self):
        """Same text should produce same embedding."""
        embedder = MockEmbedder()
        emb1 = embedder.embed("test text")
        emb2 = embedder.embed("test text")
        assert emb1 == emb2

    def test_different_text_different_embedding(self):
        """Different text should produce different embeddings."""
        embedder = MockEmbedder()
        emb1 = embedder.embed("first text")
        emb2 = embedder.embed("second text")
        assert emb1 != emb2

    def test_embed_batch(self):
        """Batch embedding should work correctly."""
        embedder = MockEmbedder()
        texts = ["text one", "text two", "text three"]
        embeddings = embedder.embed_batch(texts)
        assert len(embeddings) == 3
        assert all(len(e) == 64 for e in embeddings)


class TestMockVectorStore:
    """Tests for MockVectorStore."""

    def test_add_and_search(self):
        """Should be able to add and search vectors."""
        store = MockVectorStore()
        embedder = MockEmbedder()

        # Add vectors
        texts = ["hello world", "goodbye world", "hello there"]
        embeddings = embedder.embed_batch(texts)
        ids = ["1", "2", "3"]
        metadatas = [{"content": t} for t in texts]

        store.add(ids, embeddings, metadatas)

        # Search for similar
        query_emb = embedder.embed("hello world")
        results = store.search(query_emb, top_k=2)

        assert len(results) == 2
        # First result should be exact match
        assert results[0][0] == "1"
        assert results[0][1] > 0.99  # Very high similarity

    def test_search_respects_top_k(self):
        """Search should return at most top_k results."""
        store = MockVectorStore()
        embedder = MockEmbedder()

        # Add many vectors
        ids = [str(i) for i in range(10)]
        embeddings = embedder.embed_batch([f"text {i}" for i in range(10)])
        metadatas = [{"i": i} for i in range(10)]

        store.add(ids, embeddings, metadatas)

        # Search with top_k=3
        query_emb = embedder.embed("text 5")
        results = store.search(query_emb, top_k=3)

        assert len(results) == 3


class TestRetriever:
    """Tests for Retriever."""

    @pytest.fixture
    def sample_chunks(self, tmp_path):
        """Create sample chunks file."""
        chunks_path = tmp_path / "chunks.jsonl"

        chunks = [
            Chunk(id="1", content="RAG combines retrieval with generation", document_id="doc1", index=0),
            Chunk(id="2", content="Vector search uses embeddings for similarity", document_id="doc1", index=1),
            Chunk(id="3", content="Chunking splits documents into pieces", document_id="doc2", index=0),
        ]

        with open(chunks_path, "w") as f:
            for chunk in chunks:
                f.write(f'{{"id": "{chunk.id}", "content": "{chunk.content}", "document_id": "{chunk.document_id}", "index": {chunk.index}}}\n')

        return str(chunks_path)

    def test_index_chunks(self, sample_chunks):
        """Should index chunks from file."""
        retriever = Retriever()
        retriever.index_chunks(sample_chunks)

        assert len(retriever.chunks) == 3
        assert "1" in retriever.chunks

    def test_search_returns_results(self, sample_chunks):
        """Search should return relevant results."""
        retriever = Retriever()
        retriever.index_chunks(sample_chunks)

        results = retriever.search("What is RAG?", top_k=2)

        assert len(results) > 0
        assert all(hasattr(r, "content") for r in results)
        assert all(hasattr(r, "score") for r in results)

    def test_search_respects_min_score(self, sample_chunks):
        """Search should filter by minimum score."""
        retriever = Retriever()
        retriever.index_chunks(sample_chunks)

        # High min_score should filter most results
        results = retriever.search("random query", top_k=5, min_score=0.99)

        # Results may be empty or very few
        assert all(r.score >= 0.99 for r in results)

    def test_save_and_load_index(self, sample_chunks, tmp_path):
        """Should save and load index."""
        # Create and save index
        retriever1 = Retriever()
        retriever1.index_chunks(sample_chunks)

        index_path = str(tmp_path / "index")
        retriever1.save_index(index_path)

        # Load into new retriever
        retriever2 = Retriever(index_path=index_path)

        assert len(retriever2.chunks) == len(retriever1.chunks)


class TestDocumentIngester:
    """Tests for DocumentIngester."""

    def test_ingest_file(self, tmp_path):
        """Should ingest a text file."""
        # Create test file
        test_file = tmp_path / "test.txt"
        test_file.write_text("This is paragraph one.\n\nThis is paragraph two.")

        ingester = DocumentIngester(chunk_size=100, overlap=10)
        chunks = ingester.ingest_file(str(test_file))

        assert len(chunks) > 0
        assert all(isinstance(c, Chunk) for c in chunks)

    def test_chunk_size_respected(self, tmp_path):
        """Chunks should not exceed size limit."""
        # Create file with long content
        test_file = tmp_path / "test.txt"
        test_file.write_text("word " * 1000)

        ingester = DocumentIngester(chunk_size=100, overlap=10)
        chunks = ingester.ingest_file(str(test_file))

        # Most chunks should be close to but not exceed limit
        for chunk in chunks[:-1]:  # Exclude last chunk which may be smaller
            assert len(chunk.content) <= 150  # Allow some slack for word boundaries

    def test_file_not_found(self):
        """Should raise error for missing file."""
        ingester = DocumentIngester()

        with pytest.raises(FileNotFoundError):
            ingester.ingest_file("nonexistent.txt")
