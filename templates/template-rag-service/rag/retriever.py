"""Vector store and retrieval using FAISS."""

import os
from typing import Any

import faiss
import numpy as np

from rag.embedder import Embedder

VECTOR_STORE_PATH = os.getenv("VECTOR_STORE_PATH", "./vector_store")
TOP_K = int(os.getenv("TOP_K", "5"))


class Retriever:
    """FAISS-based vector retriever."""

    def __init__(self, embedder: Embedder):
        """Initialize the retriever.

        Args:
            embedder: Embedder instance for generating embeddings.
        """
        self.embedder = embedder
        self.dimension = embedder.dimension

        # Initialize FAISS index
        self.index = faiss.IndexFlatIP(self.dimension)  # Inner product (cosine sim)

        # Store documents and metadata
        self.documents: list[str] = []
        self.metadata: list[dict[str, Any]] = []

    @property
    def document_count(self) -> int:
        """Return number of indexed documents."""
        return len(self.documents)

    def add_document(self, text: str, metadata: dict[str, Any] | None = None) -> int:
        """Add a document to the index.

        Args:
            text: Document text.
            metadata: Optional metadata.

        Returns:
            Index of the added document.
        """
        # Generate embedding
        embedding = self.embedder.embed(text)

        # Normalize for cosine similarity
        embedding = embedding / np.linalg.norm(embedding)

        # Add to FAISS index
        self.index.add(embedding.reshape(1, -1).astype("float32"))

        # Store document and metadata
        self.documents.append(text)
        self.metadata.append(metadata or {})

        return len(self.documents) - 1

    def add_documents(
        self, texts: list[str], metadatas: list[dict[str, Any]] | None = None
    ) -> list[int]:
        """Add multiple documents to the index.

        Args:
            texts: List of document texts.
            metadatas: Optional list of metadata dicts.

        Returns:
            List of indices of added documents.
        """
        if metadatas is None:
            metadatas = [{}] * len(texts)

        indices = []
        for text, meta in zip(texts, metadatas):
            idx = self.add_document(text, meta)
            indices.append(idx)

        return indices

    def search(self, query: str, top_k: int = TOP_K) -> list[dict[str, Any]]:
        """Search for similar documents.

        Args:
            query: Search query.
            top_k: Number of results to return.

        Returns:
            List of results with text, score, and metadata.
        """
        if self.document_count == 0:
            return []

        # Generate query embedding
        query_embedding = self.embedder.embed(query)
        query_embedding = query_embedding / np.linalg.norm(query_embedding)

        # Search
        k = min(top_k, self.document_count)
        scores, indices = self.index.search(
            query_embedding.reshape(1, -1).astype("float32"), k
        )

        # Build results
        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx >= 0:  # FAISS returns -1 for empty results
                results.append(
                    {
                        "text": self.documents[idx],
                        "score": float(score),
                        "metadata": self.metadata[idx],
                    }
                )

        return results

    def get_all_metadata(self) -> list[dict[str, Any]]:
        """Get metadata for all documents.

        Returns:
            List of metadata dicts.
        """
        return self.metadata.copy()

    def clear(self) -> None:
        """Clear all documents from the index."""
        self.index = faiss.IndexFlatIP(self.dimension)
        self.documents = []
        self.metadata = []
