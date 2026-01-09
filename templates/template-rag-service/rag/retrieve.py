"""Retrieval Module.

Handles similarity search and context retrieval.
"""

import argparse
import json
import logging
import math
import os
import sys
from dataclasses import dataclass
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@dataclass
class RetrievalResult:
    """A retrieval result with content and score."""

    content: str
    score: float
    metadata: dict
    chunk_id: str


class VectorRetriever:
    """Retrieves relevant chunks based on query similarity.

    Replace with production vector database:
    - Pinecone
    - Weaviate
    - Chroma
    - FAISS
    """

    def __init__(self, store_path: Path):
        self.store_path = store_path
        self.chunks: dict[str, dict] = {}
        self.embeddings: dict[str, list[float]] = {}
        self._load_store()

    def _load_store(self) -> None:
        """Load chunks and embeddings from store."""
        chunks_file = self.store_path / "chunks.jsonl"
        embeddings_file = self.store_path / "embeddings.json"

        if chunks_file.exists():
            with open(chunks_file) as f:
                for line in f:
                    chunk = json.loads(line)
                    chunk_id = f"{chunk['doc_id']}_{chunk['chunk_index']}"
                    self.chunks[chunk_id] = chunk
            logger.info(f"Loaded {len(self.chunks)} chunks")

        if embeddings_file.exists():
            with open(embeddings_file) as f:
                self.embeddings = json.load(f)
            logger.info(f"Loaded {len(self.embeddings)} embeddings")

    def get_embedding(self, text: str) -> list[float]:
        """Get embedding for query text.

        Replace with actual embedding API call.
        """
        import hashlib

        hash_bytes = hashlib.sha256(text.encode()).digest()
        embedding = [(b - 128) / 128.0 for b in hash_bytes[:128]]
        return embedding

    def cosine_similarity(
        self, vec1: list[float], vec2: list[float]
    ) -> float:
        """Calculate cosine similarity between two vectors."""
        if len(vec1) != len(vec2):
            return 0.0

        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        norm1 = math.sqrt(sum(a * a for a in vec1))
        norm2 = math.sqrt(sum(b * b for b in vec2))

        if norm1 == 0 or norm2 == 0:
            return 0.0

        return dot_product / (norm1 * norm2)

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        min_score: float = 0.0,
    ) -> list[RetrievalResult]:
        """Retrieve most relevant chunks for a query.

        Args:
            query: The search query
            top_k: Number of results to return
            min_score: Minimum similarity score threshold

        Returns:
            List of RetrievalResult objects
        """
        logger.info(f"Retrieving for query: {query[:50]}...")

        if not self.chunks or not self.embeddings:
            logger.warning("No chunks or embeddings loaded")
            return []

        # Get query embedding
        query_embedding = self.get_embedding(query)

        # Calculate similarities
        scores = []
        for chunk_id, chunk_embedding in self.embeddings.items():
            similarity = self.cosine_similarity(query_embedding, chunk_embedding)
            if similarity >= min_score:
                scores.append((chunk_id, similarity))

        # Sort by similarity
        scores.sort(key=lambda x: x[1], reverse=True)

        # Build results
        results = []
        for chunk_id, score in scores[:top_k]:
            if chunk_id in self.chunks:
                chunk = self.chunks[chunk_id]
                results.append(
                    RetrievalResult(
                        content=chunk["content"],
                        score=score,
                        metadata=chunk["metadata"],
                        chunk_id=chunk_id,
                    )
                )

        logger.info(f"Retrieved {len(results)} results")
        return results


def retrieve_context(
    query: str,
    store_path: str = "vectorstore",
    top_k: int = 5,
    min_score: float = 0.0,
) -> list[dict]:
    """Retrieve context for a query.

    Args:
        query: The search query
        store_path: Path to vector store
        top_k: Number of results to return
        min_score: Minimum similarity score

    Returns:
        List of context dictionaries
    """
    retriever = VectorRetriever(Path(store_path))
    results = retriever.retrieve(query, top_k=top_k, min_score=min_score)

    return [
        {
            "content": r.content,
            "score": r.score,
            "source": r.metadata.get("source", "unknown"),
            "chunk_id": r.chunk_id,
        }
        for r in results
    ]


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Retrieve context for RAG")
    parser.add_argument(
        "--query",
        type=str,
        required=True,
        help="Search query",
    )
    parser.add_argument(
        "--store",
        type=str,
        default="vectorstore",
        help="Vector store path",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Number of results to return",
    )
    parser.add_argument(
        "--min-score",
        type=float,
        default=0.0,
        help="Minimum similarity score",
    )
    args = parser.parse_args()

    results = retrieve_context(
        query=args.query,
        store_path=args.store,
        top_k=args.top_k,
        min_score=args.min_score,
    )

    print(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
