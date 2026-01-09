"""
Retrieval Module

Handles searching the document index for relevant content.
"""

import json
import logging
import math
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEFAULT_INDEX_PATH = Path("data/index.json")
DEFAULT_TOP_K = 5


def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    """
    Calculate cosine similarity between two vectors.

    Args:
        vec1: First vector
        vec2: Second vector

    Returns:
        Cosine similarity score (0 to 1)
    """
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must have same length")

    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot_product / (norm1 * norm2)


def generate_query_embedding(query: str) -> list[float]:
    """
    Generate embedding for a query.

    Uses the same method as document embeddings for consistency.
    Replace with your embedding model in production.

    Args:
        query: Query text

    Returns:
        Query embedding vector
    """
    # Import from ingest to ensure consistency
    from rag.ingest import generate_embedding

    return generate_embedding(query)


class Retriever:
    """Document retriever using vector similarity search."""

    def __init__(self, index_path: str = None):
        """
        Initialize retriever.

        Args:
            index_path: Path to index file
        """
        self.index_path = Path(index_path) if index_path else DEFAULT_INDEX_PATH
        self.index = []
        self._load_index()

    def _load_index(self) -> None:
        """Load index from file."""
        if not self.index_path.exists():
            logger.warning(f"Index not found at {self.index_path}")
            return

        with open(self.index_path) as f:
            self.index = json.load(f)

        logger.info(f"Loaded {len(self.index)} entries from index")

    def search(
        self,
        query: str,
        top_k: int = DEFAULT_TOP_K,
        min_score: float = 0.0,
    ) -> list[dict]:
        """
        Search index for relevant documents.

        Args:
            query: Query text
            top_k: Number of results to return
            min_score: Minimum similarity score

        Returns:
            List of matching documents with scores
        """
        if not self.index:
            logger.warning("Index is empty")
            return []

        query_embedding = generate_query_embedding(query)

        # Calculate similarities
        results = []
        for entry in self.index:
            score = cosine_similarity(query_embedding, entry["embedding"])

            if score >= min_score:
                results.append(
                    {
                        "id": entry["id"],
                        "text": entry["text"],
                        "score": score,
                        "metadata": entry["metadata"],
                    }
                )

        # Sort by score descending
        results.sort(key=lambda x: x["score"], reverse=True)

        # Return top k
        return results[:top_k]

    def get_document(self, doc_id: str) -> dict | None:
        """
        Get a specific document by ID.

        Args:
            doc_id: Document ID

        Returns:
            Document dict or None if not found
        """
        for entry in self.index:
            if entry["id"] == doc_id:
                return {
                    "id": entry["id"],
                    "text": entry["text"],
                    "metadata": entry["metadata"],
                }
        return None


def search(query: str, top_k: int = DEFAULT_TOP_K) -> list[dict]:
    """
    Convenience function for one-off searches.

    Args:
        query: Query text
        top_k: Number of results

    Returns:
        List of matching documents
    """
    retriever = Retriever()
    return retriever.search(query, top_k)


if __name__ == "__main__":
    # Simple CLI for testing
    import sys

    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        results = search(query)

        print(f"\nQuery: {query}")
        print(f"Found {len(results)} results:\n")

        for i, result in enumerate(results, 1):
            print(f"{i}. [{result['score']:.3f}] {result['metadata']['source']}")
            print(f"   {result['text'][:100]}...")
            print()
    else:
        print("Usage: python -m rag.retrieve <query>")
