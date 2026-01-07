"""Data extraction stage."""

import json
from pathlib import Path

import pandas as pd

from pipeline.config import ExtractConfig


def extract_data(config: ExtractConfig) -> pd.DataFrame:
    """Extract data from source.

    Args:
        config: Extraction configuration.

    Returns:
        DataFrame with extracted data.

    Raises:
        ValueError: If format is not supported.
        FileNotFoundError: If source file doesn't exist.
    """
    source_path = Path(config.source)

    if not source_path.exists():
        raise FileNotFoundError(f"Source not found: {source_path}")

    if config.format == "csv":
        return pd.read_csv(source_path)
    elif config.format == "json":
        with open(source_path) as f:
            data = json.load(f)
        return pd.DataFrame(data)
    else:
        raise ValueError(f"Unsupported format: {config.format}")
