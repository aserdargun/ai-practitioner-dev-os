"""Grading implementations for evaluation harness."""

import math
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class GradeResult:
    """Result of grading a single response."""

    score: float  # 0.0 to 1.0
    passed: bool
    reason: Optional[str] = None


class Grader(ABC):
    """Base class for graders."""

    def __init__(self, threshold: float = 0.8):
        """Initialize grader with pass threshold.

        Args:
            threshold: Minimum score to pass (0.0 to 1.0)
        """
        self.threshold = threshold

    @abstractmethod
    def grade(self, actual: str, expected: str) -> GradeResult:
        """Grade an actual response against expected.

        Args:
            actual: The actual model output
            expected: The expected output

        Returns:
            GradeResult with score and pass/fail status
        """
        pass


class ExactMatchGrader(Grader):
    """Grades based on exact string match."""

    def __init__(
        self,
        threshold: float = 1.0,
        case_sensitive: bool = False,
        strip_whitespace: bool = True,
    ):
        """Initialize exact match grader.

        Args:
            threshold: Score threshold to pass
            case_sensitive: Whether comparison is case sensitive
            strip_whitespace: Whether to strip leading/trailing whitespace
        """
        super().__init__(threshold)
        self.case_sensitive = case_sensitive
        self.strip_whitespace = strip_whitespace

    def grade(self, actual: str, expected: str) -> GradeResult:
        """Grade based on exact match."""
        a = actual
        e = expected

        if self.strip_whitespace:
            a = a.strip()
            e = e.strip()

        if not self.case_sensitive:
            a = a.lower()
            e = e.lower()

        match = a == e
        score = 1.0 if match else 0.0

        return GradeResult(
            score=score,
            passed=score >= self.threshold,
            reason="Exact match" if match else f"Expected '{expected}', got '{actual}'",
        )


class ContainsGrader(Grader):
    """Grades based on whether expected is contained in actual."""

    def __init__(
        self,
        threshold: float = 1.0,
        case_sensitive: bool = False,
    ):
        """Initialize contains grader.

        Args:
            threshold: Score threshold to pass
            case_sensitive: Whether comparison is case sensitive
        """
        super().__init__(threshold)
        self.case_sensitive = case_sensitive

    def grade(self, actual: str, expected: str) -> GradeResult:
        """Grade based on containment."""
        a = actual
        e = expected

        if not self.case_sensitive:
            a = a.lower()
            e = e.lower()

        contains = e in a
        score = 1.0 if contains else 0.0

        return GradeResult(
            score=score,
            passed=score >= self.threshold,
            reason=(
                f"Found '{expected}' in response"
                if contains
                else f"'{expected}' not found in response"
            ),
        )


class RegexGrader(Grader):
    """Grades based on regex pattern matching."""

    def __init__(
        self,
        threshold: float = 1.0,
        flags: int = re.IGNORECASE,
    ):
        """Initialize regex grader.

        Args:
            threshold: Score threshold to pass
            flags: Regex flags (default: case insensitive)
        """
        super().__init__(threshold)
        self.flags = flags

    def grade(self, actual: str, expected: str) -> GradeResult:
        """Grade based on regex match.

        The expected string is treated as a regex pattern.
        """
        try:
            pattern = re.compile(expected, self.flags)
            match = pattern.search(actual) is not None
            score = 1.0 if match else 0.0

            return GradeResult(
                score=score,
                passed=score >= self.threshold,
                reason=(
                    f"Pattern '{expected}' matched"
                    if match
                    else f"Pattern '{expected}' not found"
                ),
            )
        except re.error as e:
            return GradeResult(
                score=0.0,
                passed=False,
                reason=f"Invalid regex pattern: {e}",
            )


class SemanticGrader(Grader):
    """Grades based on semantic similarity.

    Uses a mock implementation - replace with actual embeddings for production.
    """

    def __init__(self, threshold: float = 0.8):
        """Initialize semantic grader.

        Args:
            threshold: Minimum similarity score to pass
        """
        super().__init__(threshold)

    def grade(self, actual: str, expected: str) -> GradeResult:
        """Grade based on semantic similarity."""
        # Compute similarity
        similarity = self._compute_similarity(actual, expected)

        return GradeResult(
            score=similarity,
            passed=similarity >= self.threshold,
            reason=f"Semantic similarity: {similarity:.2f}",
        )

    def _compute_similarity(self, text1: str, text2: str) -> float:
        """Compute semantic similarity between two texts.

        This is a mock implementation using word overlap.
        Replace with actual embedding similarity for production.
        """
        # Tokenize (simple word-based)
        words1 = set(self._tokenize(text1))
        words2 = set(self._tokenize(text2))

        if not words1 or not words2:
            return 0.0

        # Jaccard similarity
        intersection = len(words1 & words2)
        union = len(words1 | words2)

        return intersection / union if union > 0 else 0.0

    def _tokenize(self, text: str) -> List[str]:
        """Simple tokenization."""
        # Lowercase and split on non-alphanumeric
        text = text.lower()
        words = re.findall(r"\w+", text)
        # Remove common stop words
        stop_words = {"the", "a", "an", "is", "are", "was", "were", "be", "been"}
        return [w for w in words if w not in stop_words]


class NumericGrader(Grader):
    """Grades numeric responses with tolerance."""

    def __init__(
        self,
        threshold: float = 0.95,
        tolerance: float = 0.01,
        relative: bool = True,
    ):
        """Initialize numeric grader.

        Args:
            threshold: Score threshold to pass
            tolerance: Numeric tolerance (absolute or relative)
            relative: If True, tolerance is relative; if False, absolute
        """
        super().__init__(threshold)
        self.tolerance = tolerance
        self.relative = relative

    def grade(self, actual: str, expected: str) -> GradeResult:
        """Grade based on numeric comparison."""
        try:
            actual_num = float(actual.strip())
            expected_num = float(expected.strip())
        except ValueError:
            return GradeResult(
                score=0.0,
                passed=False,
                reason="Could not parse numeric values",
            )

        if self.relative:
            # Relative error
            if expected_num == 0:
                error = abs(actual_num) if actual_num != 0 else 0
            else:
                error = abs(actual_num - expected_num) / abs(expected_num)
        else:
            # Absolute error
            error = abs(actual_num - expected_num)

        # Convert error to score (1.0 when error=0, 0.0 when error >= tolerance)
        if error <= self.tolerance:
            score = 1.0 - (error / self.tolerance) * 0.5  # Score between 0.5 and 1.0
        else:
            score = max(0.0, 0.5 - (error - self.tolerance))

        return GradeResult(
            score=score,
            passed=score >= self.threshold,
            reason=f"Expected {expected_num}, got {actual_num} (error: {error:.4f})",
        )


class CompositeGrader(Grader):
    """Combines multiple graders with weights."""

    def __init__(
        self,
        graders: List[tuple],  # List of (grader, weight) tuples
        threshold: float = 0.8,
    ):
        """Initialize composite grader.

        Args:
            graders: List of (Grader, weight) tuples
            threshold: Score threshold to pass
        """
        super().__init__(threshold)
        self.graders = graders

        # Normalize weights
        total_weight = sum(w for _, w in graders)
        self.graders = [(g, w / total_weight) for g, w in graders]

    def grade(self, actual: str, expected: str) -> GradeResult:
        """Grade using weighted combination of graders."""
        total_score = 0.0
        reasons = []

        for grader, weight in self.graders:
            result = grader.grade(actual, expected)
            total_score += result.score * weight
            reasons.append(f"{grader.__class__.__name__}: {result.score:.2f}")

        return GradeResult(
            score=total_score,
            passed=total_score >= self.threshold,
            reason="; ".join(reasons),
        )
