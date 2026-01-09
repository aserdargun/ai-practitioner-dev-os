"""Tests for grading strategies."""

import pytest
import sys
from pathlib import Path

# Add evals directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "evals"))

from graders import (
    ExactMatchGrader,
    FuzzyMatchGrader,
    ContainsGrader,
    KeywordsGrader,
    RegexGrader,
    CompositeGrader,
    GradeResult,
)


class TestExactMatchGrader:
    """Tests for ExactMatchGrader."""

    @pytest.fixture
    def grader(self):
        return ExactMatchGrader()

    def test_exact_match_passes(self, grader):
        """Exact match should pass."""
        result = grader.grade("hello", "hello")
        assert result.passed is True
        assert result.score == 1.0

    def test_different_strings_fail(self, grader):
        """Different strings should fail."""
        result = grader.grade("hello", "world")
        assert result.passed is False
        assert result.score == 0.0

    def test_case_insensitive_by_default(self, grader):
        """Should be case insensitive by default."""
        result = grader.grade("HELLO", "hello")
        assert result.passed is True

    def test_case_sensitive_option(self):
        """Case sensitive option should work."""
        grader = ExactMatchGrader(case_sensitive=True)
        result = grader.grade("HELLO", "hello")
        assert result.passed is False

    def test_strips_whitespace(self, grader):
        """Should strip whitespace by default."""
        result = grader.grade("  hello  ", "hello")
        assert result.passed is True


class TestFuzzyMatchGrader:
    """Tests for FuzzyMatchGrader."""

    @pytest.fixture
    def grader(self):
        return FuzzyMatchGrader(threshold=0.8)

    def test_similar_strings_pass(self, grader):
        """Similar strings should pass."""
        result = grader.grade("hello world", "hello world!")
        assert result.passed is True

    def test_very_different_strings_fail(self, grader):
        """Very different strings should fail."""
        result = grader.grade("abc", "xyz123")
        assert result.passed is False

    def test_identical_strings_score_1(self, grader):
        """Identical strings should have score 1.0."""
        result = grader.grade("test", "test")
        assert result.score == 1.0

    def test_threshold_respected(self):
        """Threshold should be respected."""
        strict_grader = FuzzyMatchGrader(threshold=0.99)
        result = strict_grader.grade("hello", "helo")  # Missing one 'l'
        assert result.passed is False


class TestContainsGrader:
    """Tests for ContainsGrader."""

    @pytest.fixture
    def grader(self):
        return ContainsGrader()

    def test_substring_passes(self, grader):
        """Substring match should pass."""
        result = grader.grade("The answer is Paris", "Paris")
        assert result.passed is True

    def test_not_contained_fails(self, grader):
        """Not contained should fail."""
        result = grader.grade("The answer is London", "Paris")
        assert result.passed is False

    def test_case_insensitive(self, grader):
        """Should be case insensitive by default."""
        result = grader.grade("The answer is PARIS", "paris")
        assert result.passed is True

    def test_case_sensitive_option(self):
        """Case sensitive option should work."""
        grader = ContainsGrader(case_sensitive=True)
        result = grader.grade("The answer is PARIS", "paris")
        assert result.passed is False


class TestKeywordsGrader:
    """Tests for KeywordsGrader."""

    @pytest.fixture
    def grader(self):
        return KeywordsGrader()

    def test_all_keywords_present(self, grader):
        """All keywords present should pass."""
        result = grader.grade("Python is great for machine learning", "Python,machine,learning")
        assert result.passed is True

    def test_missing_keyword_fails(self, grader):
        """Missing keyword should fail with require_all."""
        result = grader.grade("Python is great", "Python,machine,learning")
        assert result.passed is False

    def test_any_mode(self):
        """Any mode should pass with at least one keyword."""
        grader = KeywordsGrader(require_all=False)
        result = grader.grade("Python is great", "Python,machine,learning")
        assert result.passed is True

    def test_score_reflects_found_count(self, grader):
        """Score should reflect proportion found."""
        result = grader.grade("Python is great", "Python,Java,Ruby")
        assert result.score == pytest.approx(1/3)


class TestRegexGrader:
    """Tests for RegexGrader."""

    @pytest.fixture
    def grader(self):
        return RegexGrader()

    def test_pattern_match_passes(self, grader):
        """Pattern match should pass."""
        result = grader.grade("The answer is 42", r"\d+")
        assert result.passed is True

    def test_no_match_fails(self, grader):
        """No match should fail."""
        result = grader.grade("No numbers here", r"\d+")
        assert result.passed is False

    def test_invalid_regex_handled(self, grader):
        """Invalid regex should be handled gracefully."""
        result = grader.grade("test", r"[invalid")
        assert result.passed is False
        assert "Invalid regex" in result.reason


class TestCompositeGrader:
    """Tests for CompositeGrader."""

    def test_any_mode_passes_if_one_passes(self):
        """Any mode should pass if at least one grader passes."""
        graders = [
            ExactMatchGrader(),  # Will fail
            ContainsGrader(),    # Will pass
        ]
        composite = CompositeGrader(graders, mode="any")
        result = composite.grade("Hello World", "World")
        assert result.passed is True

    def test_all_mode_requires_all(self):
        """All mode should require all graders to pass."""
        graders = [
            ExactMatchGrader(),  # Will fail
            ContainsGrader(),    # Will pass
        ]
        composite = CompositeGrader(graders, mode="all")
        result = composite.grade("Hello World", "World")
        assert result.passed is False

    def test_majority_mode(self):
        """Majority mode should pass if more than half pass."""
        graders = [
            ContainsGrader(),    # Will pass
            ContainsGrader(),    # Will pass
            ExactMatchGrader(),  # Will fail
        ]
        composite = CompositeGrader(graders, mode="majority")
        result = composite.grade("Hello World", "World")
        assert result.passed is True


class TestGradeResult:
    """Tests for GradeResult dataclass."""

    def test_grade_result_creation(self):
        """GradeResult should be created with all fields."""
        result = GradeResult(passed=True, score=0.95, reason="Test passed")
        assert result.passed is True
        assert result.score == 0.95
        assert result.reason == "Test passed"

    def test_grade_result_failed(self):
        """GradeResult should handle failed cases."""
        result = GradeResult(passed=False, score=0.0, reason="Test failed")
        assert result.passed is False
        assert result.score == 0.0
