"""
Document Ingestion Module

Handles loading, chunking, and indexing documents.
"""

import argparse
import hashlib
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Default settings
DEFAULT_CHUNK_SIZE = 500
DEFAULT_CHUNK_OVERLAP = 50
INDEX_PATH = Path("data/index.json")


def load_document(file_path: str) -> dict:
    """
    Load a document from file.

    Args:
        file_path: Path to document file

    Returns:
        Document dict with content and metadata
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Document not found: {file_path}")

    content = path.read_text(encoding="utf-8")

    return {
        "source": str(path),
        "filename": path.name,
        "content": content,
        "size": len(content),
    }


def chunk_document(
    text: str,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    overlap: int = DEFAULT_CHUNK_OVERLAP,
) -> list[str]:
    """
    Split document into overlapping chunks.

    Args:
        text: Document text
        chunk_size: Size of each chunk in characters
        overlap: Overlap between chunks

    Returns:
        List of text chunks
    """
    if not text:
        return []

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        # Try to break at sentence boundary
        if end < len(text):
            last_period = chunk.rfind(".")
            last_newline = chunk.rfind("\n")
            break_point = max(last_period, last_newline)

            if break_point > chunk_size // 2:
                chunk = chunk[: break_point + 1]
                end = start + break_point + 1

        chunks.append(chunk.strip())
        start = end - overlap

    return [c for c in chunks if c]  # Remove empty chunks


def generate_embedding(text: str) -> list[float]:
    """
    Generate embedding for text.

    This is a simple placeholder implementation using character hashing.
    Replace with actual embedding model in production.

    Args:
        text: Text to embed

    Returns:
        Embedding vector (simplified)
    """
    # Placeholder: Simple hash-based "embedding"
    # In production, use sentence-transformers, OpenAI, etc.
    hash_obj = hashlib.sha256(text.encode())
    hash_bytes = hash_obj.digest()

    # Convert to simple float vector
    embedding = [float(b) / 255.0 for b in hash_bytes[:64]]
    return embedding


def create_index_entry(
    chunk: str, doc_metadata: dict, chunk_index: int
) -> dict:
    """
    Create an index entry for a chunk.

    Args:
        chunk: Text chunk
        doc_metadata: Parent document metadata
        chunk_index: Index of chunk within document

    Returns:
        Index entry dict
    """
    return {
        "id": f"{doc_metadata['filename']}_{chunk_index}",
        "text": chunk,
        "embedding": generate_embedding(chunk),
        "metadata": {
            "source": doc_metadata["source"],
            "filename": doc_metadata["filename"],
            "chunk_index": chunk_index,
        },
    }


def ingest_documents(
    input_path: str,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    overlap: int = DEFAULT_CHUNK_OVERLAP,
) -> list[dict]:
    """
    Ingest documents from a directory.

    Args:
        input_path: Path to documents directory
        chunk_size: Size of each chunk
        overlap: Overlap between chunks

    Returns:
        List of index entries
    """
    path = Path(input_path)
    entries = []

    if path.is_file():
        files = [path]
    else:
        files = list(path.glob("**/*.txt")) + list(path.glob("**/*.md"))

    logger.info(f"Found {len(files)} documents to ingest")

    for file_path in files:
        logger.info(f"Processing: {file_path}")

        try:
            doc = load_document(str(file_path))
            chunks = chunk_document(doc["content"], chunk_size, overlap)

            logger.info(f"  Created {len(chunks)} chunks")

            for i, chunk in enumerate(chunks):
                entry = create_index_entry(chunk, doc, i)
                entries.append(entry)

        except Exception as e:
            logger.error(f"  Error processing {file_path}: {e}")

    logger.info(f"Total entries: {len(entries)}")
    return entries


def save_index(entries: list[dict], output_path: str = None) -> None:
    """
    Save index to file.

    Args:
        entries: List of index entries
        output_path: Path to save index
    """
    if output_path is None:
        output_path = INDEX_PATH

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w") as f:
        json.dump(entries, f, indent=2)

    logger.info(f"Index saved to {path}")


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Ingest documents into index")
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Input file or directory",
    )
    parser.add_argument(
        "--output",
        "-o",
        default=str(INDEX_PATH),
        help="Output index file",
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=DEFAULT_CHUNK_SIZE,
        help="Chunk size in characters",
    )
    parser.add_argument(
        "--overlap",
        type=int,
        default=DEFAULT_CHUNK_OVERLAP,
        help="Overlap between chunks",
    )

    args = parser.parse_args()

    entries = ingest_documents(
        args.input,
        chunk_size=args.chunk_size,
        overlap=args.overlap,
    )

    save_index(entries, args.output)


if __name__ == "__main__":
    main()
