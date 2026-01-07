"""Document ingestion CLI."""

import argparse
import logging
from pathlib import Path

from rag.chunker import chunk_text
from rag.embedder import Embedder
from rag.retriever import Retriever

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def ingest_file(path: Path, retriever: Retriever) -> int:
    """Ingest a single file.

    Args:
        path: Path to the file.
        retriever: Retriever instance.

    Returns:
        Number of chunks created.
    """
    logger.info(f"Ingesting: {path}")

    # Read file content
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        logger.warning(f"Skipping binary file: {path}")
        return 0

    # Chunk the content
    chunks = chunk_text(content)

    # Add to retriever
    for i, chunk in enumerate(chunks):
        metadata = {
            "source": str(path),
            "filename": path.name,
            "chunk_index": i,
            "total_chunks": len(chunks),
        }
        retriever.add_document(chunk, metadata)

    logger.info(f"Created {len(chunks)} chunks from {path.name}")
    return len(chunks)


def ingest_directory(
    docs_dir: Path,
    retriever: Retriever,
    extensions: list[str] | None = None,
) -> int:
    """Ingest all documents in a directory.

    Args:
        docs_dir: Path to documents directory.
        retriever: Retriever instance.
        extensions: File extensions to include (default: .txt, .md).

    Returns:
        Total number of chunks created.
    """
    if extensions is None:
        extensions = [".txt", ".md", ".rst"]

    total_chunks = 0

    for ext in extensions:
        for path in docs_dir.rglob(f"*{ext}"):
            total_chunks += ingest_file(path, retriever)

    return total_chunks


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Ingest documents into RAG service")
    parser.add_argument(
        "--docs-dir",
        type=Path,
        default=Path("./documents"),
        help="Directory containing documents",
    )
    parser.add_argument(
        "--extensions",
        nargs="+",
        default=[".txt", ".md"],
        help="File extensions to process",
    )
    args = parser.parse_args()

    if not args.docs_dir.exists():
        logger.error(f"Directory not found: {args.docs_dir}")
        return 1

    # Initialize components
    embedder = Embedder()
    retriever = Retriever(embedder)

    # Ingest documents
    total_chunks = ingest_directory(args.docs_dir, retriever, args.extensions)

    logger.info(f"Ingestion complete: {total_chunks} total chunks")
    logger.info(f"Total documents indexed: {retriever.document_count}")

    return 0


if __name__ == "__main__":
    exit(main())
