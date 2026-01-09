"""Vector retrieval for RAG."""

import json
import logging
import math
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class RetrievalResult:
    """Result from retrieval."""

    chunk_id: str
    content: str
    score: float
    metadata: dict


class MockEmbedder:
    """Mock embedder for demonstration.

    Replace with real embeddings (OpenAI, sentence-transformers, etc.)
    """

    def __init__(self, dimension: int = 64):
        """Initialize mock embedder."""
        self.dimension = dimension

    def embed(self, text: str) -> List[float]:
        """Generate mock embedding from text.

        This creates a deterministic embedding based on text content.
        Replace with actual embedding model in production.
        """
        # Simple hash-based mock embedding
        import hashlib

        hash_bytes = hashlib.sha256(text.encode()).digest()

        # Convert bytes to floats in [-1, 1]
        embedding = []
        for i in range(self.dimension):
            byte_val = hash_bytes[i % len(hash_bytes)]
            embedding.append((byte_val / 127.5) - 1.0)

        # Normalize
        norm = math.sqrt(sum(x * x for x in embedding))
        if norm > 0:
            embedding = [x / norm for x in embedding]

        return embedding

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Embed multiple texts."""
        return [self.embed(text) for text in texts]


class MockVectorStore:
    """Mock vector store for demonstration.

    Replace with real vector store (ChromaDB, Pinecone, etc.)
    """

    def __init__(self):
        """Initialize mock store."""
        self.vectors: List[tuple] = []  # (id, embedding, metadata)

    def add(
        self,
        ids: List[str],
        embeddings: List[List[float]],
        metadatas: List[dict],
    ) -> None:
        """Add vectors to store."""
        for id_, emb, meta in zip(ids, embeddings, metadatas):
            self.vectors.append((id_, emb, meta))
        logger.info(f"Added {len(ids)} vectors to store")

    def search(
        self,
        query_embedding: List[float],
        top_k: int = 5,
    ) -> List[tuple]:
        """Search for similar vectors.

        Returns:
            List of (id, score, metadata) tuples
        """
        results = []

        for id_, embedding, metadata in self.vectors:
            score = self._cosine_similarity(query_embedding, embedding)
            results.append((id_, score, metadata))

        # Sort by score descending
        results.sort(key=lambda x: x[1], reverse=True)

        return results[:top_k]

    def _cosine_similarity(self, a: List[float], b: List[float]) -> float:
        """Compute cosine similarity between two vectors."""
        dot = sum(x * y for x, y in zip(a, b))
        norm_a = math.sqrt(sum(x * x for x in a))
        norm_b = math.sqrt(sum(x * x for x in b))

        if norm_a == 0 or norm_b == 0:
            return 0.0

        return dot / (norm_a * norm_b)

    def save(self, path: str) -> None:
        """Save store to file."""
        with open(path, "w") as f:
            json.dump(self.vectors, f)

    def load(self, path: str) -> None:
        """Load store from file."""
        with open(path, "r") as f:
            self.vectors = json.load(f)


class Retriever:
    """Retrieves relevant chunks for queries."""

    def __init__(
        self,
        index_path: Optional[str] = None,
        embedder: Optional[MockEmbedder] = None,
        vector_store: Optional[MockVectorStore] = None,
    ):
        """Initialize retriever.

        Args:
            index_path: Path to load existing index
            embedder: Embedding model (defaults to MockEmbedder)
            vector_store: Vector store (defaults to MockVectorStore)
        """
        self.embedder = embedder or MockEmbedder()
        self.vector_store = vector_store or MockVectorStore()
        self.chunks: dict = {}  # id -> content mapping

        if index_path:
            self.load_index(index_path)

    def index_chunks(self, chunks_path: str) -> None:
        """Index chunks from JSONL file.

        Args:
            chunks_path: Path to chunks JSONL file
        """
        logger.info(f"Indexing chunks from {chunks_path}")

        path = Path(chunks_path)
        if not path.exists():
            raise FileNotFoundError(f"Chunks file not found: {chunks_path}")

        chunks = []
        with open(path, "r") as f:
            for line in f:
                chunk = json.loads(line)
                chunks.append(chunk)
                self.chunks[chunk["id"]] = chunk["content"]

        # Create embeddings
        contents = [c["content"] for c in chunks]
        embeddings = self.embedder.embed_batch(contents)

        # Add to vector store
        ids = [c["id"] for c in chunks]
        metadatas = [
            {"content": c["content"], "document_id": c["document_id"]}
            for c in chunks
        ]
        self.vector_store.add(ids, embeddings, metadatas)

        logger.info(f"Indexed {len(chunks)} chunks")

    def search(
        self,
        query: str,
        top_k: int = 5,
        min_score: float = 0.0,
    ) -> List[RetrievalResult]:
        """Search for relevant chunks.

        Args:
            query: Search query
            top_k: Number of results to return
            min_score: Minimum similarity score threshold

        Returns:
            List of RetrievalResult objects
        """
        logger.debug(f"Searching for: {query}")

        # Embed query
        query_embedding = self.embedder.embed(query)

        # Search vector store
        raw_results = self.vector_store.search(query_embedding, top_k)

        # Filter and convert results
        results = []
        for id_, score, metadata in raw_results:
            if score >= min_score:
                results.append(
                    RetrievalResult(
                        chunk_id=id_,
                        content=metadata.get("content", ""),
                        score=score,
                        metadata=metadata,
                    )
                )

        logger.info(f"Found {len(results)} results for query")
        return results

    def save_index(self, path: str) -> None:
        """Save index to directory."""
        dir_path = Path(path)
        dir_path.mkdir(parents=True, exist_ok=True)

        self.vector_store.save(str(dir_path / "vectors.json"))

        with open(dir_path / "chunks.json", "w") as f:
            json.dump(self.chunks, f)

        logger.info(f"Saved index to {path}")

    def load_index(self, path: str) -> None:
        """Load index from directory."""
        dir_path = Path(path)

        vectors_path = dir_path / "vectors.json"
        chunks_path = dir_path / "chunks.json"

        if vectors_path.exists():
            self.vector_store.load(str(vectors_path))

        if chunks_path.exists():
            with open(chunks_path, "r") as f:
                self.chunks = json.load(f)

        logger.info(f"Loaded index from {path}")
