"""Grading Strategies.

Provides various strategies for grading LLM/ML outputs.
"""

import os
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from difflib import SequenceMatcher


@dataclass
class GradeResult:
    """Result of grading an output."""

    passed: bool
    score: float  # 0.0 to 1.0
    reason: str


class BaseGrader(ABC):
    """Base class for all graders."""

    @abstractmethod
    def grade(self, output: str, expected: str, **kwargs) -> GradeResult:
        """Grade an output against expected value.

        Args:
            output: The model's output
            expected: The expected/correct output
            **kwargs: Additional context (input, metadata, etc.)

        Returns:
            GradeResult with passed status, score, and reason
        """
        pass


class ExactMatchGrader(BaseGrader):
    """Grades based on exact string match."""

    def __init__(self, case_sensitive: bool = False, strip: bool = True):
        self.case_sensitive = case_sensitive
        self.strip = strip

    def grade(self, output: str, expected: str, **kwargs) -> GradeResult:
        """Check for exact match."""
        out = output.strip() if self.strip else output
        exp = expected.strip() if self.strip else expected

        if not self.case_sensitive:
            out = out.lower()
            exp = exp.lower()

        passed = out == exp

        return GradeResult(
            passed=passed,
            score=1.0 if passed else 0.0,
            reason="Exact match" if passed else f"Expected '{expected}', got '{output}'",
        )


class FuzzyMatchGrader(BaseGrader):
    """Grades based on string similarity."""

    def __init__(self, threshold: float = 0.8):
        self.threshold = float(os.getenv("SIMILARITY_THRESHOLD", threshold))

    def grade(self, output: str, expected: str, **kwargs) -> GradeResult:
        """Check for fuzzy match using sequence similarity."""
        output_normalized = output.lower().strip()
        expected_normalized = expected.lower().strip()

        similarity = SequenceMatcher(
            None, output_normalized, expected_normalized
        ).ratio()

        passed = similarity >= self.threshold

        return GradeResult(
            passed=passed,
            score=similarity,
            reason=f"Similarity: {similarity:.2%} (threshold: {self.threshold:.0%})",
        )


class ContainsGrader(BaseGrader):
    """Grades based on whether expected is contained in output."""

    def __init__(self, case_sensitive: bool = False):
        self.case_sensitive = case_sensitive

    def grade(self, output: str, expected: str, **kwargs) -> GradeResult:
        """Check if expected is substring of output."""
        out = output if self.case_sensitive else output.lower()
        exp = expected if self.case_sensitive else expected.lower()

        passed = exp in out

        return GradeResult(
            passed=passed,
            score=1.0 if passed else 0.0,
            reason="Contains expected" if passed else f"Does not contain '{expected}'",
        )


class KeywordsGrader(BaseGrader):
    """Grades based on presence of keywords."""

    def __init__(self, require_all: bool = True, case_sensitive: bool = False):
        self.require_all = require_all
        self.case_sensitive = case_sensitive

    def grade(self, output: str, expected: str, **kwargs) -> GradeResult:
        """Check for keyword presence.

        Expected can be comma-separated keywords or passed via kwargs.
        """
        # Get keywords from expected or kwargs
        if "keywords" in kwargs:
            keywords = kwargs["keywords"]
        else:
            keywords = [k.strip() for k in expected.split(",")]

        out = output if self.case_sensitive else output.lower()

        found = []
        missing = []

        for keyword in keywords:
            kw = keyword if self.case_sensitive else keyword.lower()
            if kw in out:
                found.append(keyword)
            else:
                missing.append(keyword)

        if self.require_all:
            passed = len(missing) == 0
            score = len(found) / len(keywords) if keywords else 0
        else:
            passed = len(found) > 0
            score = len(found) / len(keywords) if keywords else 0

        reason = f"Found {len(found)}/{len(keywords)} keywords"
        if missing:
            reason += f". Missing: {missing}"

        return GradeResult(passed=passed, score=score, reason=reason)


class RegexGrader(BaseGrader):
    """Grades based on regex pattern match."""

    def __init__(self, flags: int = re.IGNORECASE):
        self.flags = flags

    def grade(self, output: str, expected: str, **kwargs) -> GradeResult:
        """Check if output matches regex pattern.

        Expected should be a valid regex pattern.
        """
        try:
            pattern = re.compile(expected, self.flags)
            match = pattern.search(output)
            passed = match is not None

            return GradeResult(
                passed=passed,
                score=1.0 if passed else 0.0,
                reason="Pattern matched" if passed else "Pattern not found",
            )
        except re.error as e:
            return GradeResult(
                passed=False,
                score=0.0,
                reason=f"Invalid regex pattern: {e}",
            )


class LLMGrader(BaseGrader):
    """Grades using an LLM as judge.

    Replace with actual LLM API call for production use.
    """

    def __init__(self, model: str = "gpt-4"):
        self.model = model

    def grade(self, output: str, expected: str, **kwargs) -> GradeResult:
        """Use LLM to judge correctness.

        Replace this with actual LLM API call.
        """
        # Placeholder implementation
        # In production, call OpenAI/Anthropic API to judge

        prompt = f"""Judge whether the output is correct given the expected answer.

Expected: {expected}
Output: {output}

Is the output correct? Reply with 'CORRECT' or 'INCORRECT' and a brief explanation."""

        # Demo: Simple heuristic (replace with actual LLM call)
        # Check if key words from expected appear in output
        expected_words = set(expected.lower().split())
        output_words = set(output.lower().split())
        overlap = expected_words & output_words

        similarity = len(overlap) / len(expected_words) if expected_words else 0
        passed = similarity > 0.5

        return GradeResult(
            passed=passed,
            score=similarity,
            reason=f"LLM judge (placeholder): {similarity:.0%} keyword overlap",
        )


class CompositeGrader(BaseGrader):
    """Combines multiple graders with configurable logic."""

    def __init__(
        self,
        graders: list[BaseGrader],
        mode: str = "any",  # "any", "all", "majority"
    ):
        self.graders = graders
        self.mode = mode

    def grade(self, output: str, expected: str, **kwargs) -> GradeResult:
        """Grade using multiple graders."""
        results = [g.grade(output, expected, **kwargs) for g in self.graders]

        passed_count = sum(1 for r in results if r.passed)
        total = len(results)
        avg_score = sum(r.score for r in results) / total if total > 0 else 0

        if self.mode == "any":
            passed = any(r.passed for r in results)
        elif self.mode == "all":
            passed = all(r.passed for r in results)
        else:  # majority
            passed = passed_count > total / 2

        reasons = [f"{type(g).__name__}: {r.reason}" for g, r in zip(self.graders, results)]

        return GradeResult(
            passed=passed,
            score=avg_score,
            reason=f"{self.mode.upper()}: {passed_count}/{total} passed. " + "; ".join(reasons),
        )
