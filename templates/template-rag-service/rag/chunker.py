"""Text chunking utilities."""

import os
import re

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "500"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "50"))


def chunk_text(
    text: str,
    chunk_size: int = CHUNK_SIZE,
    chunk_overlap: int = CHUNK_OVERLAP,
) -> list[str]:
    """Split text into overlapping chunks.

    Args:
        text: Text to chunk.
        chunk_size: Maximum characters per chunk.
        chunk_overlap: Characters to overlap between chunks.

    Returns:
        List of text chunks.
    """
    # Clean text
    text = text.strip()
    if not text:
        return []

    # Split by paragraphs first
    paragraphs = re.split(r"\n\n+", text)

    chunks = []
    current_chunk = ""

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        # If paragraph fits in current chunk, add it
        if len(current_chunk) + len(para) + 2 <= chunk_size:
            if current_chunk:
                current_chunk += "\n\n" + para
            else:
                current_chunk = para
        else:
            # Save current chunk if not empty
            if current_chunk:
                chunks.append(current_chunk)

            # If paragraph is too long, split it
            if len(para) > chunk_size:
                # Split by sentences
                sentences = re.split(r"(?<=[.!?])\s+", para)
                current_chunk = ""

                for sentence in sentences:
                    if len(current_chunk) + len(sentence) + 1 <= chunk_size:
                        if current_chunk:
                            current_chunk += " " + sentence
                        else:
                            current_chunk = sentence
                    else:
                        if current_chunk:
                            chunks.append(current_chunk)
                        current_chunk = sentence
            else:
                current_chunk = para

    # Don't forget the last chunk
    if current_chunk:
        chunks.append(current_chunk)

    # Apply overlap
    if chunk_overlap > 0 and len(chunks) > 1:
        overlapped_chunks = [chunks[0]]
        for i in range(1, len(chunks)):
            prev_chunk = chunks[i - 1]
            overlap_text = prev_chunk[-chunk_overlap:] if len(prev_chunk) > chunk_overlap else prev_chunk
            overlapped_chunks.append(overlap_text + " " + chunks[i])
        chunks = overlapped_chunks

    return chunks


def chunk_by_tokens(text: str, max_tokens: int = 256) -> list[str]:
    """Chunk text by approximate token count.

    Args:
        text: Text to chunk.
        max_tokens: Maximum tokens per chunk (approximate).

    Returns:
        List of text chunks.
    """
    # Rough approximation: 1 token ≈ 4 characters
    chunk_size = max_tokens * 4
    return chunk_text(text, chunk_size=chunk_size)
