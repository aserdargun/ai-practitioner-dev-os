"""
Evaluation Runner

Main entry point for running evaluations.
"""

import argparse
import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Callable

from evals.graders import GRADERS, exact_match

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_dataset(dataset_path: str) -> list[dict]:
    """
    Load golden dataset from JSONL file.

    Args:
        dataset_path: Path to JSONL file

    Returns:
        List of evaluation examples
    """
    path = Path(dataset_path)

    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    examples = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                examples.append(json.loads(line))

    logger.info(f"Loaded {len(examples)} examples from {dataset_path}")
    return examples


def placeholder_model(input_text: str) -> str:
    """
    Placeholder model function.

    Replace this with your actual model inference.

    Args:
        input_text: Input to the model

    Returns:
        Model output
    """
    # This is a placeholder - replace with your model
    # Example: return my_model.predict(input_text)
    return f"Response to: {input_text}"


class EvalRunner:
    """Evaluation runner for ML models and AI systems."""

    def __init__(
        self,
        model_fn: Callable[[str], str] = None,
        grader: str | Callable = "exact_match",
        pass_threshold: float = 0.5,
    ):
        """
        Initialize evaluation runner.

        Args:
            model_fn: Function that takes input and returns output
            grader: Grader name or function
            pass_threshold: Score threshold for passing
        """
        self.model_fn = model_fn or placeholder_model

        if isinstance(grader, str):
            if grader not in GRADERS:
                raise ValueError(f"Unknown grader: {grader}. Available: {list(GRADERS.keys())}")
            self.grader = GRADERS[grader]
        else:
            self.grader = grader

        self.pass_threshold = pass_threshold

    def run_single(self, example: dict) -> dict:
        """
        Run evaluation on a single example.

        Args:
            example: Evaluation example dict

        Returns:
            Result dict with input, output, expected, score
        """
        input_text = example["input"]
        expected = example["expected"]

        # Run model
        try:
            output = self.model_fn(input_text)
        except Exception as e:
            logger.error(f"Model error for {example.get('id', 'unknown')}: {e}")
            output = f"ERROR: {e}"

        # Grade
        try:
            score = self.grader(output, expected)
        except Exception as e:
            logger.error(f"Grader error for {example.get('id', 'unknown')}: {e}")
            score = 0.0

        return {
            "id": example.get("id", "unknown"),
            "input": input_text,
            "output": output,
            "expected": expected,
            "score": score,
            "passed": score >= self.pass_threshold,
            "category": example.get("category"),
            "metadata": example.get("metadata"),
        }

    def run(
        self,
        dataset_path: str,
        category: str = None,
        limit: int = None,
    ) -> dict:
        """
        Run evaluation on a dataset.

        Args:
            dataset_path: Path to golden dataset
            category: Filter by category (optional)
            limit: Limit number of examples (optional)

        Returns:
            Results dict with summary and individual results
        """
        examples = load_dataset(dataset_path)

        # Filter by category
        if category:
            examples = [e for e in examples if e.get("category") == category]
            logger.info(f"Filtered to {len(examples)} examples in category '{category}'")

        # Limit
        if limit:
            examples = examples[:limit]
            logger.info(f"Limited to {len(examples)} examples")

        # Run evaluations
        results = []
        for i, example in enumerate(examples):
            logger.info(f"Evaluating {i+1}/{len(examples)}: {example.get('id', 'unknown')}")
            result = self.run_single(example)
            results.append(result)

        # Calculate summary
        summary = self._calculate_summary(results)

        # Group by category
        by_category = self._group_by_category(results)

        return {
            "summary": summary,
            "by_category": by_category,
            "results": results,
            "metadata": {
                "dataset": dataset_path,
                "timestamp": datetime.now().isoformat(),
                "grader": self.grader.__name__,
                "pass_threshold": self.pass_threshold,
            },
        }

    def _calculate_summary(self, results: list[dict]) -> dict:
        """Calculate summary statistics."""
        total = len(results)
        if total == 0:
            return {"total": 0, "passed": 0, "failed": 0, "accuracy": 0, "avg_score": 0}

        passed = sum(1 for r in results if r["passed"])
        failed = total - passed
        scores = [r["score"] for r in results]

        return {
            "total": total,
            "passed": passed,
            "failed": failed,
            "accuracy": round(passed / total, 4),
            "avg_score": round(sum(scores) / total, 4),
            "min_score": round(min(scores), 4),
            "max_score": round(max(scores), 4),
        }

    def _group_by_category(self, results: list[dict]) -> dict:
        """Group results by category."""
        categories = {}

        for result in results:
            category = result.get("category") or "uncategorized"

            if category not in categories:
                categories[category] = []

            categories[category].append(result)

        # Calculate stats per category
        stats = {}
        for category, cat_results in categories.items():
            total = len(cat_results)
            passed = sum(1 for r in cat_results if r["passed"])
            scores = [r["score"] for r in cat_results]

            stats[category] = {
                "total": total,
                "passed": passed,
                "failed": total - passed,
                "accuracy": round(passed / total, 4) if total > 0 else 0,
                "avg_score": round(sum(scores) / total, 4) if total > 0 else 0,
            }

        return stats


def run_evals(
    dataset_path: str,
    model_fn: Callable = None,
    grader: str = "exact_match",
    output_path: str = None,
    category: str = None,
    limit: int = None,
) -> dict:
    """
    Convenience function for running evaluations.

    Args:
        dataset_path: Path to golden dataset
        model_fn: Model function
        grader: Grader name
        output_path: Optional path to save results
        category: Filter by category
        limit: Limit examples

    Returns:
        Results dict
    """
    runner = EvalRunner(model_fn=model_fn, grader=grader)
    results = runner.run(dataset_path, category=category, limit=limit)

    if output_path:
        with open(output_path, "w") as f:
            json.dump(results, f, indent=2)
        logger.info(f"Results saved to {output_path}")

    return results


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Run evaluations")
    parser.add_argument(
        "--dataset",
        "-d",
        required=True,
        help="Path to golden dataset (JSONL)",
    )
    parser.add_argument(
        "--grader",
        "-g",
        default="exact_match",
        choices=list(GRADERS.keys()),
        help="Grader to use",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output file for results (JSON)",
    )
    parser.add_argument(
        "--category",
        "-c",
        help="Filter by category",
    )
    parser.add_argument(
        "--limit",
        "-l",
        type=int,
        help="Limit number of examples",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Verbose output",
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    results = run_evals(
        dataset_path=args.dataset,
        grader=args.grader,
        output_path=args.output,
        category=args.category,
        limit=args.limit,
    )

    # Print summary
    print("\n" + "=" * 50)
    print("EVALUATION RESULTS")
    print("=" * 50)

    summary = results["summary"]
    print(f"\nTotal: {summary['total']}")
    print(f"Passed: {summary['passed']} ({summary['accuracy']*100:.1f}%)")
    print(f"Failed: {summary['failed']}")
    print(f"Average Score: {summary['avg_score']:.3f}")

    if results["by_category"]:
        print("\nBy Category:")
        for cat, stats in results["by_category"].items():
            print(f"  {cat}: {stats['passed']}/{stats['total']} ({stats['accuracy']*100:.1f}%)")

    print()

    # Exit with error if accuracy is too low
    if summary["accuracy"] < 0.5:
        sys.exit(1)


if __name__ == "__main__":
    main()
