"""Model and data loading utilities."""

import pickle
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


def load_model(path: Path) -> Any:
    """Load a model from file.

    Supports:
    - Pickle files (.pkl, .pickle)
    - Joblib files (.joblib)

    Args:
        path: Path to model file.

    Returns:
        Loaded model object.

    Raises:
        ValueError: If file format is not supported.
    """
    path = Path(path)
    suffix = path.suffix.lower()

    if suffix in [".pkl", ".pickle"]:
        with open(path, "rb") as f:
            return pickle.load(f)
    elif suffix == ".joblib":
        try:
            import joblib

            return joblib.load(path)
        except ImportError:
            raise ImportError("joblib required for .joblib files")
    else:
        raise ValueError(f"Unsupported model format: {suffix}")


def load_data(
    path: Path,
    target_column: str = "target",
) -> tuple[np.ndarray, np.ndarray]:
    """Load data from file.

    Supports:
    - CSV files (.csv)
    - Parquet files (.parquet)
    - NPZ files (.npz) with 'X' and 'y' arrays

    Args:
        path: Path to data file.
        target_column: Name of target column (for tabular data).

    Returns:
        Tuple of (X, y) arrays.

    Raises:
        ValueError: If file format is not supported.
    """
    path = Path(path)
    suffix = path.suffix.lower()

    if suffix == ".csv":
        df = pd.read_csv(path)
        y = df[target_column].values
        X = df.drop(columns=[target_column]).values
        return X, y

    elif suffix == ".parquet":
        df = pd.read_parquet(path)
        y = df[target_column].values
        X = df.drop(columns=[target_column]).values
        return X, y

    elif suffix == ".npz":
        data = np.load(path)
        return data["X"], data["y"]

    else:
        raise ValueError(f"Unsupported data format: {suffix}")


def save_model(model: Any, path: Path) -> None:
    """Save a model to file.

    Args:
        model: Model object to save.
        path: Output path.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "wb") as f:
        pickle.dump(model, f)
