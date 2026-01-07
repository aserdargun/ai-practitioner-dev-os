"""Utility functions for the pipeline."""

import hashlib
from datetime import datetime
from pathlib import Path


def get_file_hash(path: Path) -> str:
    """Calculate MD5 hash of a file.

    Args:
        path: Path to file.

    Returns:
        MD5 hash string.
    """
    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def timestamp_filename(base_name: str, extension: str = "") -> str:
    """Generate timestamped filename.

    Args:
        base_name: Base filename.
        extension: File extension (without dot).

    Returns:
        Timestamped filename.
    """
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    if extension:
        return f"{base_name}_{ts}.{extension}"
    return f"{base_name}_{ts}"


def ensure_directory(path: Path) -> Path:
    """Ensure directory exists, create if needed.

    Args:
        path: Directory path.

    Returns:
        The path.
    """
    path.mkdir(parents=True, exist_ok=True)
    return path
