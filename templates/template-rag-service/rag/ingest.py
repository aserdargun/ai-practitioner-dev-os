"""Document ingestion and chunking for RAG."""

import hashlib
import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class Document:
    """Represents a source document."""

    id: str
    content: str
    metadata: dict = field(default_factory=dict)
    source: str = ""


@dataclass
class Chunk:
    """Represents a document chunk."""

    id: str
    content: str
    document_id: str
    index: int
    metadata: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "content": self.content,
            "document_id": self.document_id,
            "index": self.index,
            "metadata": self.metadata,
        }


class DocumentIngester:
    """Ingests documents and creates chunks for RAG."""

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 50,
    ):
        """Initialize the ingester.

        Args:
            chunk_size: Maximum characters per chunk
            overlap: Characters to overlap between chunks
        """
        self.chunk_size = chunk_size
        self.overlap = overlap

    def ingest_file(self, file_path: str) -> List[Chunk]:
        """Ingest a single file into chunks.

        Args:
            file_path: Path to the file to ingest

        Returns:
            List of Chunk objects
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        logger.info(f"Ingesting file: {file_path}")

        content = path.read_text(encoding="utf-8")
        doc_id = self._generate_id(str(path))

        document = Document(
            id=doc_id,
            content=content,
            source=str(path),
            metadata={"filename": path.name, "size": len(content)},
        )

        chunks = self._chunk_document(document)
        logger.info(f"Created {len(chunks)} chunks from {file_path}")

        return chunks

    def ingest_directory(
        self,
        dir_path: str,
        extensions: Optional[List[str]] = None,
    ) -> List[Chunk]:
        """Ingest all files in a directory.

        Args:
            dir_path: Path to directory
            extensions: File extensions to include (e.g., ['.txt', '.md'])

        Returns:
            List of all Chunk objects
        """
        extensions = extensions or [".txt", ".md"]
        path = Path(dir_path)

        if not path.exists():
            raise FileNotFoundError(f"Directory not found: {dir_path}")

        all_chunks = []
        for ext in extensions:
            for file_path in path.glob(f"**/*{ext}"):
                chunks = self.ingest_file(str(file_path))
                all_chunks.extend(chunks)

        logger.info(f"Total chunks created: {len(all_chunks)}")
        return all_chunks

    def _chunk_document(self, document: Document) -> List[Chunk]:
        """Split document into overlapping chunks.

        Args:
            document: Document to chunk

        Returns:
            List of Chunk objects
        """
        content = document.content
        chunks = []

        # Split by paragraphs first for better boundaries
        paragraphs = content.split("\n\n")
        current_chunk = ""
        chunk_index = 0

        for para in paragraphs:
            # If adding paragraph exceeds chunk size, save current chunk
            if len(current_chunk) + len(para) > self.chunk_size and current_chunk:
                chunk = self._create_chunk(
                    current_chunk.strip(),
                    document.id,
                    chunk_index,
                    document.source,
                )
                chunks.append(chunk)

                # Keep overlap from end of current chunk
                if self.overlap > 0 and len(current_chunk) > self.overlap:
                    current_chunk = current_chunk[-self.overlap :] + "\n\n" + para
                else:
                    current_chunk = para
                chunk_index += 1
            else:
                current_chunk += ("\n\n" if current_chunk else "") + para

        # Don't forget the last chunk
        if current_chunk.strip():
            chunk = self._create_chunk(
                current_chunk.strip(),
                document.id,
                chunk_index,
                document.source,
            )
            chunks.append(chunk)

        return chunks

    def _create_chunk(
        self,
        content: str,
        document_id: str,
        index: int,
        source: str,
    ) -> Chunk:
        """Create a chunk with generated ID."""
        chunk_id = self._generate_id(f"{document_id}:{index}")
        return Chunk(
            id=chunk_id,
            content=content,
            document_id=document_id,
            index=index,
            metadata={"source": source},
        )

    def _generate_id(self, content: str) -> str:
        """Generate a deterministic ID from content."""
        return hashlib.md5(content.encode()).hexdigest()[:12]

    def save_chunks(self, chunks: List[Chunk], output_path: str) -> None:
        """Save chunks to JSONL file.

        Args:
            chunks: List of chunks to save
            output_path: Path to output file
        """
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w") as f:
            for chunk in chunks:
                f.write(json.dumps(chunk.to_dict()) + "\n")

        logger.info(f"Saved {len(chunks)} chunks to {output_path}")


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Ingest documents for RAG")
    parser.add_argument("--input", "-i", required=True, help="Input file or directory")
    parser.add_argument("--output", "-o", required=True, help="Output JSONL file")
    parser.add_argument("--chunk-size", type=int, default=500, help="Chunk size")
    parser.add_argument("--overlap", type=int, default=50, help="Chunk overlap")

    args = parser.parse_args()

    ingester = DocumentIngester(
        chunk_size=args.chunk_size,
        overlap=args.overlap,
    )

    input_path = Path(args.input)
    if input_path.is_dir():
        chunks = ingester.ingest_directory(args.input)
    else:
        chunks = ingester.ingest_file(args.input)

    ingester.save_chunks(chunks, args.output)


if __name__ == "__main__":
    main()
