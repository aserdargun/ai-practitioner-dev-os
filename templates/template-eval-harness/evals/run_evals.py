"""Evaluation Runner.

Runs evaluations against a golden set dataset.
"""

import argparse
import json
import logging
import os
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@dataclass
class EvalResult:
    """Result of a single evaluation."""

    input: str
    expected: str
    output: str
    passed: bool
    score: float
    reason: str
    category: str | None = None
    latency_ms: float | None = None


@dataclass
class EvalReport:
    """Summary report of evaluation run."""

    total_cases: int
    passed_cases: int
    failed_cases: int
    pass_rate: float
    average_score: float
    categories: dict
    timestamp: str
    duration_seconds: float


class EvaluationRunner:
    """Runs evaluations using configured grader."""

    def __init__(self, grader_name: str = "exact"):
        self.grader = self._get_grader(grader_name)
        self.results: list[EvalResult] = []

    def _get_grader(self, name: str):
        """Get grader by name."""
        from graders import (
            ExactMatchGrader,
            FuzzyMatchGrader,
            ContainsGrader,
            LLMGrader,
        )

        graders = {
            "exact": ExactMatchGrader,
            "fuzzy": FuzzyMatchGrader,
            "contains": ContainsGrader,
            "llm": LLMGrader,
        }

        if name not in graders:
            raise ValueError(f"Unknown grader: {name}. Available: {list(graders.keys())}")

        return graders[name]()

    def load_dataset(self, dataset_path: str) -> list[dict]:
        """Load evaluation dataset from JSONL file."""
        path = Path(dataset_path)

        if not path.exists():
            raise FileNotFoundError(f"Dataset not found: {dataset_path}")

        cases = []
        with open(path) as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    case = json.loads(line)
                    if "input" not in case or "expected" not in case:
                        logger.warning(f"Line {line_num}: Missing required fields")
                        continue
                    cases.append(case)
                except json.JSONDecodeError as e:
                    logger.warning(f"Line {line_num}: Invalid JSON - {e}")

        logger.info(f"Loaded {len(cases)} test cases from {dataset_path}")
        return cases

    def get_model_output(self, input_text: str) -> str:
        """Get model output for input.

        Replace this with your actual model inference:
        - LLM API call
        - Local model inference
        - RAG pipeline call
        """
        # Placeholder: Echo input as demo
        # Replace with actual model call
        return f"Demo output for: {input_text}"

    def evaluate_case(self, case: dict) -> EvalResult:
        """Evaluate a single test case."""
        input_text = case["input"]
        expected = case["expected"]
        category = case.get("category")

        # Get model output
        import time
        start = time.time()
        output = self.get_model_output(input_text)
        latency_ms = (time.time() - start) * 1000

        # Grade output
        grade_result = self.grader.grade(output, expected)

        return EvalResult(
            input=input_text,
            expected=expected,
            output=output,
            passed=grade_result.passed,
            score=grade_result.score,
            reason=grade_result.reason,
            category=category,
            latency_ms=latency_ms,
        )

    def run(self, dataset_path: str) -> EvalReport:
        """Run evaluation on dataset."""
        logger.info(f"Starting evaluation with grader: {type(self.grader).__name__}")

        start_time = datetime.now()
        cases = self.load_dataset(dataset_path)
        self.results = []

        for i, case in enumerate(cases):
            logger.debug(f"Evaluating case {i + 1}/{len(cases)}")
            result = self.evaluate_case(case)
            self.results.append(result)

        # Generate report
        report = self._generate_report(start_time)
        return report

    def _generate_report(self, start_time: datetime) -> EvalReport:
        """Generate evaluation report."""
        total = len(self.results)
        passed = sum(1 for r in self.results if r.passed)
        failed = total - passed

        # Category breakdown
        categories = defaultdict(lambda: {"total": 0, "passed": 0, "avg_score": 0})
        for result in self.results:
            cat = result.category or "uncategorized"
            categories[cat]["total"] += 1
            if result.passed:
                categories[cat]["passed"] += 1
            categories[cat]["avg_score"] += result.score

        for cat in categories:
            count = categories[cat]["total"]
            categories[cat]["avg_score"] /= count if count > 0 else 1
            categories[cat]["pass_rate"] = (
                categories[cat]["passed"] / count if count > 0 else 0
            )

        duration = (datetime.now() - start_time).total_seconds()

        return EvalReport(
            total_cases=total,
            passed_cases=passed,
            failed_cases=failed,
            pass_rate=passed / total if total > 0 else 0,
            average_score=sum(r.score for r in self.results) / total if total > 0 else 0,
            categories=dict(categories),
            timestamp=start_time.isoformat(),
            duration_seconds=duration,
        )

    def get_failures(self) -> list[EvalResult]:
        """Get all failed test cases."""
        return [r for r in self.results if not r.passed]


def run_evaluation(
    dataset_path: str,
    grader: str = "exact",
    output_path: str | None = None,
    verbose: bool = False,
) -> dict:
    """Run evaluation and optionally save results.

    Args:
        dataset_path: Path to golden set JSONL
        grader: Grader name (exact, fuzzy, contains, llm)
        output_path: Path to save report (optional)
        verbose: Print detailed results

    Returns:
        Evaluation report as dictionary
    """
    runner = EvaluationRunner(grader_name=grader)
    report = runner.run(dataset_path)

    # Print summary
    print(f"\n{'=' * 50}")
    print("EVALUATION SUMMARY")
    print(f"{'=' * 50}")
    print(f"Total Cases: {report.total_cases}")
    print(f"Passed: {report.passed_cases}")
    print(f"Failed: {report.failed_cases}")
    print(f"Pass Rate: {report.pass_rate:.1%}")
    print(f"Average Score: {report.average_score:.3f}")
    print(f"Duration: {report.duration_seconds:.2f}s")

    if report.categories:
        print(f"\n{'=' * 50}")
        print("CATEGORY BREAKDOWN")
        print(f"{'=' * 50}")
        for cat, stats in report.categories.items():
            print(f"  {cat}: {stats['pass_rate']:.1%} ({stats['passed']}/{stats['total']})")

    if verbose:
        failures = runner.get_failures()
        if failures:
            print(f"\n{'=' * 50}")
            print(f"FAILURES ({len(failures)})")
            print(f"{'=' * 50}")
            for f in failures[:10]:  # Show first 10
                print(f"\nInput: {f.input[:100]}...")
                print(f"Expected: {f.expected[:100]}")
                print(f"Got: {f.output[:100]}...")
                print(f"Reason: {f.reason}")

    # Save report if requested
    if output_path:
        output = {
            "report": asdict(report),
            "results": [asdict(r) for r in runner.results],
        }
        with open(output_path, "w") as f:
            json.dump(output, f, indent=2)
        print(f"\nReport saved to: {output_path}")

    return asdict(report)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Run LLM evaluations")
    parser.add_argument(
        "--dataset",
        type=str,
        required=True,
        help="Path to golden set JSONL file",
    )
    parser.add_argument(
        "--grader",
        type=str,
        default=os.getenv("DEFAULT_GRADER", "exact"),
        choices=["exact", "fuzzy", "contains", "llm"],
        help="Grading strategy",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Path to save report JSON",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show detailed failure information",
    )
    args = parser.parse_args()

    try:
        run_evaluation(
            dataset_path=args.dataset,
            grader=args.grader,
            output_path=args.output,
            verbose=args.verbose,
        )
        return 0
    except Exception as e:
        logger.error(f"Evaluation failed: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
