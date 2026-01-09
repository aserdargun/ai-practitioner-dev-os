"""
Data Pipeline Runner

Main entry point for running the data pipeline.
"""

import argparse
import logging
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

from pipeline.validate import run_all_validations

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def load_data(input_path: str) -> pd.DataFrame:
    """
    Load data from input file.

    Args:
        input_path: Path to input file (CSV or JSON)

    Returns:
        Loaded DataFrame
    """
    path = Path(input_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    logger.info(f"Loading data from {input_path}")

    if path.suffix == ".csv":
        df = pd.read_csv(input_path)
    elif path.suffix == ".json":
        df = pd.read_json(input_path)
    else:
        raise ValueError(f"Unsupported file format: {path.suffix}")

    logger.info(f"Loaded {len(df)} rows, {len(df.columns)} columns")
    return df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply transformations to the data.

    Customize this function for your specific transformations.

    Args:
        df: Input DataFrame

    Returns:
        Transformed DataFrame
    """
    logger.info("Applying transformations")
    df = df.copy()

    # Example transformations (customize as needed):

    # 1. Add processing metadata
    df["_processed_at"] = datetime.now().isoformat()

    # 2. Handle missing values (example: fill with defaults)
    # df["column_name"] = df["column_name"].fillna("default")

    # 3. Type conversions (example)
    # df["date_column"] = pd.to_datetime(df["date_column"])

    # 4. Derived columns (example)
    # df["full_name"] = df["first_name"] + " " + df["last_name"]

    logger.info("Transformations complete")
    return df


def save_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Save processed data to output file.

    Args:
        df: DataFrame to save
        output_path: Path to output file
    """
    path = Path(output_path)

    # Create output directory if needed
    path.parent.mkdir(parents=True, exist_ok=True)

    logger.info(f"Saving data to {output_path}")

    if path.suffix == ".csv":
        df.to_csv(output_path, index=False)
    elif path.suffix == ".json":
        df.to_json(output_path, orient="records", indent=2)
    else:
        raise ValueError(f"Unsupported output format: {path.suffix}")

    logger.info(f"Saved {len(df)} rows to {output_path}")


def run_pipeline(
    input_path: str,
    output_path: str,
    skip_validation: bool = False,
    dry_run: bool = False,
) -> bool:
    """
    Run the full data pipeline.

    Args:
        input_path: Path to input file
        output_path: Path to output file
        skip_validation: Skip validation steps
        dry_run: Only validate, don't save output

    Returns:
        True if pipeline succeeded, False otherwise
    """
    logger.info("=" * 50)
    logger.info("Starting data pipeline")
    logger.info("=" * 50)

    try:
        # Stage 1: Load
        df = load_data(input_path)

        # Stage 2: Validate input
        if not skip_validation:
            logger.info("Validating input data")
            validation_result = run_all_validations(df)

            if not validation_result["passed"]:
                logger.error("Input validation failed:")
                for issue in validation_result["issues"]:
                    logger.error(f"  - {issue}")
                return False

            logger.info("Input validation passed")

        # Stage 3: Transform
        df = transform_data(df)

        # Stage 4: Validate output
        if not skip_validation:
            logger.info("Validating output data")
            validation_result = run_all_validations(df)

            if not validation_result["passed"]:
                logger.error("Output validation failed:")
                for issue in validation_result["issues"]:
                    logger.error(f"  - {issue}")
                return False

            logger.info("Output validation passed")

        # Stage 5: Save
        if not dry_run:
            save_data(df, output_path)
        else:
            logger.info("Dry run - skipping save")

        logger.info("=" * 50)
        logger.info("Pipeline completed successfully")
        logger.info("=" * 50)
        return True

    except Exception as e:
        logger.exception(f"Pipeline failed: {e}")
        return False


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Run the data pipeline")
    parser.add_argument(
        "--input",
        "-i",
        default="data/input.csv",
        help="Input file path",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="data/output.csv",
        help="Output file path",
    )
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="Skip validation steps",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate only, don't save output",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging",
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    success = run_pipeline(
        input_path=args.input,
        output_path=args.output,
        skip_validation=args.skip_validation,
        dry_run=args.dry_run,
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
