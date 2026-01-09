"""
Tests for Graders Module

Run with: pytest tests/test_graders.py -v
"""

import pytest

from evals.graders import (
    contains_match,
    contains_match_ignore_case,
    exact_match,
    exact_match_ignore_case,
    fuzzy_match,
    get_grader,
    json_match,
    multi_match,
    numeric_match,
    regex_match,
    starts_with,
    word_overlap,
)


class TestExactMatch:
    """Tests for exact_match grader."""

    def test_exact_match_true(self):
        """Identical strings should return 1.0."""
        assert exact_match("hello", "hello") == 1.0

    def test_exact_match_false(self):
        """Different strings should return 0.0."""
        assert exact_match("hello", "world") == 0.0

    def test_exact_match_case_sensitive(self):
        """Should be case sensitive."""
        assert exact_match("Hello", "hello") == 0.0

    def test_exact_match_strips_whitespace(self):
        """Should strip leading/trailing whitespace."""
        assert exact_match("  hello  ", "hello") == 1.0


class TestExactMatchIgnoreCase:
    """Tests for exact_match_ignore_case grader."""

    def test_ignore_case(self):
        """Should ignore case differences."""
        assert exact_match_ignore_case("Hello", "hello") == 1.0
        assert exact_match_ignore_case("WORLD", "world") == 1.0

    def test_different_strings(self):
        """Different strings should return 0.0."""
        assert exact_match_ignore_case("hello", "world") == 0.0


class TestContainsMatch:
    """Tests for contains_match grader."""

    def test_contains_true(self):
        """Should return 1.0 when output contains expected."""
        assert contains_match("The answer is Paris", "Paris") == 1.0

    def test_contains_false(self):
        """Should return 0.0 when output doesn't contain expected."""
        assert contains_match("The answer is London", "Paris") == 0.0

    def test_contains_case_sensitive(self):
        """Should be case sensitive."""
        assert contains_match("The answer is paris", "Paris") == 0.0


class TestContainsMatchIgnoreCase:
    """Tests for contains_match_ignore_case grader."""

    def test_ignore_case(self):
        """Should ignore case."""
        assert contains_match_ignore_case("The answer is paris", "Paris") == 1.0


class TestStartsWith:
    """Tests for starts_with grader."""

    def test_starts_with_true(self):
        """Should return 1.0 when output starts with expected."""
        assert starts_with("Paris is the capital", "Paris") == 1.0

    def test_starts_with_false(self):
        """Should return 0.0 when output doesn't start with expected."""
        assert starts_with("The capital is Paris", "Paris") == 0.0


class TestRegexMatch:
    """Tests for regex_match grader."""

    def test_regex_match_true(self):
        """Should return 1.0 when regex matches."""
        assert regex_match("The year is 2024", r"\d{4}") == 1.0

    def test_regex_match_false(self):
        """Should return 0.0 when regex doesn't match."""
        assert regex_match("No numbers here", r"\d{4}") == 0.0

    def test_invalid_regex(self):
        """Should return 0.0 for invalid regex."""
        assert regex_match("test", r"[invalid") == 0.0


class TestFuzzyMatch:
    """Tests for fuzzy_match grader."""

    def test_identical_strings(self):
        """Identical strings should have similarity 1.0."""
        score = fuzzy_match("hello world", "hello world")
        assert score == 1.0

    def test_similar_strings(self):
        """Similar strings should have high similarity."""
        score = fuzzy_match("hello world", "hello worl")
        assert score > 0.9

    def test_different_strings(self):
        """Different strings should have low similarity."""
        score = fuzzy_match("hello", "goodbye")
        assert score < 0.5


class TestNumericMatch:
    """Tests for numeric_match grader."""

    def test_exact_number(self):
        """Exact numbers should return 1.0."""
        assert numeric_match("42", "42") == 1.0

    def test_number_in_text(self):
        """Should find number in text."""
        assert numeric_match("The answer is 42", "42") == 1.0

    def test_close_number(self):
        """Numbers within tolerance should return 1.0."""
        assert numeric_match("42.001", "42", tolerance=0.01) == 1.0

    def test_different_number(self):
        """Different numbers should return 0.0."""
        assert numeric_match("100", "42") == 0.0


class TestJsonMatch:
    """Tests for json_match grader."""

    def test_matching_json(self):
        """Matching JSON should return 1.0."""
        output = '{"a": 1, "b": 2}'
        expected = '{"a": 1, "b": 2}'
        assert json_match(output, expected) == 1.0

    def test_different_json(self):
        """Different JSON should return 0.0."""
        output = '{"a": 1}'
        expected = '{"a": 2}'
        assert json_match(output, expected) == 0.0

    def test_invalid_json(self):
        """Invalid JSON should return 0.0."""
        assert json_match("not json", '{"a": 1}') == 0.0


class TestMultiMatch:
    """Tests for multi_match grader."""

    def test_matches_first(self):
        """Should match first option."""
        assert multi_match("yes", "yes|true|1") == 1.0

    def test_matches_second(self):
        """Should match second option."""
        assert multi_match("true", "yes|true|1") == 1.0

    def test_no_match(self):
        """Should return 0.0 if no match."""
        assert multi_match("no", "yes|true|1") == 0.0


class TestWordOverlap:
    """Tests for word_overlap grader."""

    def test_identical(self):
        """Identical strings should have score 1.0."""
        assert word_overlap("hello world", "hello world") == 1.0

    def test_partial_overlap(self):
        """Partial overlap should have intermediate score."""
        score = word_overlap("hello world", "hello there")
        assert 0 < score < 1

    def test_no_overlap(self):
        """No overlap should have score 0.0."""
        assert word_overlap("hello world", "goodbye universe") == 0.0


class TestGetGrader:
    """Tests for get_grader function."""

    def test_get_valid_grader(self):
        """Should return grader function for valid name."""
        grader = get_grader("exact_match")
        assert callable(grader)
        assert grader("a", "a") == 1.0

    def test_get_alias(self):
        """Should work with aliases."""
        grader = get_grader("exact")
        assert callable(grader)

    def test_invalid_grader_raises(self):
        """Should raise ValueError for invalid grader name."""
        with pytest.raises(ValueError):
            get_grader("nonexistent_grader")
