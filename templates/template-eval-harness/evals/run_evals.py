"""Evaluation harness runner."""

import argparse
import json
import logging
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

from evals.graders import (
    ContainsGrader,
    ExactMatchGrader,
    GradeResult,
    Grader,
    SemanticGrader,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class TestCase:
    """A single test case."""

    id: str
    input: str
    expected: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class EvalResult:
    """Result of evaluating a single test case."""

    test_case: TestCase
    actual: str
    grade: GradeResult


@dataclass
class EvalReport:
    """Complete evaluation report."""

    total: int
    passed: int
    failed: int
    pass_rate: float
    average_score: float
    results: List[EvalResult]
    by_category: Dict[str, Dict[str, Any]] = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "summary": {
                "total": self.total,
                "passed": self.passed,
                "failed": self.failed,
                "pass_rate": round(self.pass_rate, 4),
                "average_score": round(self.average_score, 4),
            },
            "by_category": self.by_category,
            "results": [
                {
                    "id": r.test_case.id,
                    "input": r.test_case.input,
                    "expected": r.test_case.expected,
                    "actual": r.actual,
                    "score": r.grade.score,
                    "passed": r.grade.passed,
                    "reason": r.grade.reason,
                }
                for r in self.results
            ],
        }


class EvalHarness:
    """Evaluation harness for running test suites."""

    GRADERS = {
        "exact": ExactMatchGrader,
        "contains": ContainsGrader,
        "semantic": SemanticGrader,
    }

    def __init__(
        self,
        grader: Optional[Grader] = None,
        model_fn: Optional[Callable[[str], str]] = None,
    ):
        """Initialize the evaluation harness.

        Args:
            grader: Grader instance (defaults to ExactMatchGrader)
            model_fn: Function that takes input and returns model output
                     (defaults to identity function for testing)
        """
        self.grader = grader or ExactMatchGrader()
        self.model_fn = model_fn or (lambda x: x)

    def load_dataset(self, path: str) -> List[TestCase]:
        """Load test cases from JSONL file.

        Args:
            path: Path to JSONL file

        Returns:
            List of TestCase objects
        """
        dataset_path = Path(path)
        if not dataset_path.exists():
            raise FileNotFoundError(f"Dataset not found: {path}")

        test_cases = []
        with open(dataset_path, "r") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue

                try:
                    data = json.loads(line)
                    test_case = TestCase(
                        id=data.get("id", f"test_{line_num}"),
                        input=data["input"],
                        expected=data["expected"],
                        metadata=data.get("metadata", {}),
                    )
                    test_cases.append(test_case)
                except (json.JSONDecodeError, KeyError) as e:
                    logger.warning(f"Skipping invalid line {line_num}: {e}")

        logger.info(f"Loaded {len(test_cases)} test cases from {path}")
        return test_cases

    def run(self, test_cases: List[TestCase]) -> EvalReport:
        """Run evaluation on test cases.

        Args:
            test_cases: List of test cases to evaluate

        Returns:
            EvalReport with results
        """
        logger.info(f"Running evaluation on {len(test_cases)} test cases")

        results = []
        for test_case in test_cases:
            # Get model output
            actual = self.model_fn(test_case.input)

            # Grade the output
            grade = self.grader.grade(actual, test_case.expected)

            result = EvalResult(
                test_case=test_case,
                actual=actual,
                grade=grade,
            )
            results.append(result)

        # Compute summary statistics
        total = len(results)
        passed = sum(1 for r in results if r.grade.passed)
        failed = total - passed
        pass_rate = passed / total if total > 0 else 0
        average_score = (
            sum(r.grade.score for r in results) / total if total > 0 else 0
        )

        # Group by category
        by_category = self._group_by_category(results)

        report = EvalReport(
            total=total,
            passed=passed,
            failed=failed,
            pass_rate=pass_rate,
            average_score=average_score,
            results=results,
            by_category=by_category,
        )

        logger.info(f"Evaluation complete: {passed}/{total} passed ({pass_rate:.1%})")
        return report

    def _group_by_category(
        self, results: List[EvalResult]
    ) -> Dict[str, Dict[str, Any]]:
        """Group results by category metadata."""
        categories: Dict[str, List[EvalResult]] = {}

        for result in results:
            category = result.test_case.metadata.get("category", "uncategorized")
            if category not in categories:
                categories[category] = []
            categories[category].append(result)

        by_category = {}
        for category, cat_results in categories.items():
            total = len(cat_results)
            passed = sum(1 for r in cat_results if r.grade.passed)
            avg_score = sum(r.grade.score for r in cat_results) / total

            by_category[category] = {
                "total": total,
                "passed": passed,
                "failed": total - passed,
                "pass_rate": round(passed / total, 4),
                "average_score": round(avg_score, 4),
            }

        return by_category

    def run_from_file(self, path: str) -> EvalReport:
        """Load dataset and run evaluation.

        Args:
            path: Path to JSONL dataset

        Returns:
            EvalReport with results
        """
        test_cases = self.load_dataset(path)
        return self.run(test_cases)


def create_grader(grader_type: str, threshold: float = 0.8) -> Grader:
    """Create a grader instance by type.

    Args:
        grader_type: Type of grader ('exact', 'contains', 'semantic')
        threshold: Pass threshold for the grader

    Returns:
        Grader instance
    """
    grader_class = EvalHarness.GRADERS.get(grader_type)
    if grader_class is None:
        raise ValueError(
            f"Unknown grader type: {grader_type}. "
            f"Available: {list(EvalHarness.GRADERS.keys())}"
        )

    return grader_class(threshold=threshold)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Run evaluations")
    parser.add_argument(
        "--dataset", "-d", required=True, help="Path to golden set JSONL"
    )
    parser.add_argument(
        "--grader", "-g", default="exact", help="Grader type (exact, contains, semantic)"
    )
    parser.add_argument(
        "--threshold", "-t", type=float, default=0.8, help="Pass threshold"
    )
    parser.add_argument(
        "--report", "-r", action="store_true", help="Generate detailed report"
    )
    parser.add_argument("--output", "-o", help="Output file (default: stdout)")

    args = parser.parse_args()

    # Create grader
    try:
        grader = create_grader(args.grader, args.threshold)
    except ValueError as e:
        logger.error(str(e))
        sys.exit(1)

    # Run evaluation
    harness = EvalHarness(grader=grader)

    try:
        report = harness.run_from_file(args.dataset)
    except FileNotFoundError as e:
        logger.error(str(e))
        sys.exit(1)

    # Output results
    if args.report:
        output = json.dumps(report.to_dict(), indent=2)
    else:
        output = json.dumps(report.to_dict()["summary"], indent=2)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        logger.info(f"Results written to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
