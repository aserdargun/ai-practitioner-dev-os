"""Embedding generation using sentence transformers."""

import os

import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")


class Embedder:
    """Wrapper for embedding generation."""

    def __init__(self, model_name: str = MODEL_NAME):
        """Initialize the embedder.

        Args:
            model_name: Name of the sentence transformer model.
        """
        self.model = SentenceTransformer(model_name)
        self.dimension = self.model.get_sentence_embedding_dimension()

    def embed(self, text: str) -> np.ndarray:
        """Generate embedding for a single text.

        Args:
            text: Text to embed.

        Returns:
            Embedding vector as numpy array.
        """
        return self.model.encode(text, convert_to_numpy=True)

    def embed_batch(self, texts: list[str]) -> np.ndarray:
        """Generate embeddings for multiple texts.

        Args:
            texts: List of texts to embed.

        Returns:
            2D numpy array of embeddings.
        """
        return self.model.encode(texts, convert_to_numpy=True)
