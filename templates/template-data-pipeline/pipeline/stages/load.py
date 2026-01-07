"""Data loading stage."""

import json
from pathlib import Path

import pandas as pd

from pipeline.config import LoadConfig


def load_data(df: pd.DataFrame, config: LoadConfig) -> None:
    """Load data to destination.

    Args:
        df: DataFrame to save.
        config: Load configuration.

    Raises:
        ValueError: If format is not supported.
    """
    dest_path = Path(config.destination)

    # Create parent directories if needed
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    if config.format == "csv":
        df.to_csv(dest_path, index=False)
    elif config.format == "json":
        with open(dest_path, "w") as f:
            json.dump(df.to_dict(orient="records"), f, indent=2)
    else:
        raise ValueError(f"Unsupported format: {config.format}")
