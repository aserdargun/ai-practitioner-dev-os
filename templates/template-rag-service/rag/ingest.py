"""Document Ingestion Module.

Handles document loading, chunking, and embedding storage.
"""

import argparse
import hashlib
import json
import logging
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

# Configure logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@dataclass
class Document:
    """A document with content and metadata."""

    content: str
    metadata: dict
    doc_id: str | None = None

    def __post_init__(self):
        if self.doc_id is None:
            self.doc_id = hashlib.md5(self.content.encode()).hexdigest()[:12]


@dataclass
class Chunk:
    """A chunk of a document."""

    content: str
    doc_id: str
    chunk_index: int
    metadata: dict


class DocumentLoader:
    """Loads documents from various sources."""

    SUPPORTED_EXTENSIONS = {".txt", ".md", ".json"}

    def load_file(self, file_path: Path) -> Document | None:
        """Load a single file as a document."""
        if file_path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
            logger.warning(f"Unsupported file type: {file_path}")
            return None

        try:
            content = file_path.read_text(encoding="utf-8")
            return Document(
                content=content,
                metadata={
                    "source": str(file_path),
                    "filename": file_path.name,
                    "extension": file_path.suffix,
                },
            )
        except Exception as e:
            logger.error(f"Failed to load {file_path}: {e}")
            return None

    def load_directory(self, dir_path: Path) -> Iterator[Document]:
        """Load all supported documents from a directory."""
        for file_path in dir_path.rglob("*"):
            if file_path.is_file():
                doc = self.load_file(file_path)
                if doc:
                    yield doc


class TextChunker:
    """Chunks text into smaller pieces for embedding."""

    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 50,
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_document(self, document: Document) -> list[Chunk]:
        """Split a document into chunks."""
        text = document.content
        chunks = []

        start = 0
        chunk_index = 0

        while start < len(text):
            end = start + self.chunk_size

            # Try to break at sentence boundary
            if end < len(text):
                # Look for sentence-ending punctuation
                for punct in [". ", "! ", "? ", "\n\n", "\n"]:
                    last_punct = text.rfind(punct, start, end)
                    if last_punct > start:
                        end = last_punct + len(punct)
                        break

            chunk_text = text[start:end].strip()

            if chunk_text:
                chunks.append(
                    Chunk(
                        content=chunk_text,
                        doc_id=document.doc_id,
                        chunk_index=chunk_index,
                        metadata={
                            **document.metadata,
                            "chunk_start": start,
                            "chunk_end": end,
                        },
                    )
                )
                chunk_index += 1

            start = end - self.chunk_overlap

        return chunks


class VectorStore:
    """Simple vector store implementation.

    Replace with a real vector database in production:
    - Pinecone
    - Weaviate
    - Chroma
    - FAISS
    """

    def __init__(self, store_path: Path):
        self.store_path = store_path
        self.store_path.mkdir(parents=True, exist_ok=True)
        self.chunks_file = store_path / "chunks.jsonl"
        self.embeddings_file = store_path / "embeddings.json"

    def add_chunks(self, chunks: list[Chunk]) -> None:
        """Add chunks to the store."""
        with open(self.chunks_file, "a") as f:
            for chunk in chunks:
                record = {
                    "content": chunk.content,
                    "doc_id": chunk.doc_id,
                    "chunk_index": chunk.chunk_index,
                    "metadata": chunk.metadata,
                }
                f.write(json.dumps(record) + "\n")

        logger.info(f"Added {len(chunks)} chunks to store")

    def get_embedding(self, text: str) -> list[float]:
        """Get embedding for text.

        Replace with actual embedding API call:
        - OpenAI embeddings
        - Sentence transformers
        - Cohere embeddings
        """
        # Placeholder: Simple hash-based fake embedding
        # Replace with real embeddings in production
        import hashlib

        hash_bytes = hashlib.sha256(text.encode()).digest()
        # Convert to float values between -1 and 1
        embedding = [(b - 128) / 128.0 for b in hash_bytes[:128]]
        return embedding

    def save_embeddings(self, chunk_embeddings: dict[str, list[float]]) -> None:
        """Save embeddings to file."""
        with open(self.embeddings_file, "w") as f:
            json.dump(chunk_embeddings, f)

        logger.info(f"Saved {len(chunk_embeddings)} embeddings")


def ingest_documents(
    input_path: str,
    output_path: str,
    chunk_size: int = 500,
    chunk_overlap: int = 50,
) -> dict:
    """Ingest documents into vector store.

    Args:
        input_path: Path to documents (file or directory)
        output_path: Path to vector store output
        chunk_size: Size of text chunks
        chunk_overlap: Overlap between chunks

    Returns:
        Ingestion statistics
    """
    input_path = Path(input_path)
    output_path = Path(output_path)

    loader = DocumentLoader()
    chunker = TextChunker(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    store = VectorStore(output_path)

    stats = {
        "documents_processed": 0,
        "chunks_created": 0,
        "embeddings_created": 0,
    }

    chunk_embeddings = {}

    # Load documents
    if input_path.is_file():
        documents = [loader.load_file(input_path)]
    else:
        documents = list(loader.load_directory(input_path))

    documents = [d for d in documents if d is not None]
    stats["documents_processed"] = len(documents)

    # Process each document
    for doc in documents:
        logger.info(f"Processing: {doc.metadata.get('source', doc.doc_id)}")

        # Chunk document
        chunks = chunker.chunk_document(doc)
        stats["chunks_created"] += len(chunks)

        # Store chunks
        store.add_chunks(chunks)

        # Create embeddings
        for chunk in chunks:
            chunk_id = f"{chunk.doc_id}_{chunk.chunk_index}"
            embedding = store.get_embedding(chunk.content)
            chunk_embeddings[chunk_id] = embedding

    # Save embeddings
    store.save_embeddings(chunk_embeddings)
    stats["embeddings_created"] = len(chunk_embeddings)

    logger.info(f"Ingestion complete: {stats}")
    return stats


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Ingest documents for RAG")
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Input path (file or directory)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="vectorstore",
        help="Output vector store path",
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=int(os.getenv("CHUNK_SIZE", "500")),
        help="Chunk size in characters",
    )
    parser.add_argument(
        "--chunk-overlap",
        type=int,
        default=int(os.getenv("CHUNK_OVERLAP", "50")),
        help="Chunk overlap in characters",
    )
    args = parser.parse_args()

    stats = ingest_documents(
        input_path=args.input,
        output_path=args.output,
        chunk_size=args.chunk_size,
        chunk_overlap=args.chunk_overlap,
    )

    print(json.dumps(stats, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
