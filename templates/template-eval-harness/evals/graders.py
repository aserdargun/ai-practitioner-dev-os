"""
Grading Functions

Functions for scoring model outputs against expected values.
"""

import re
from difflib import SequenceMatcher


def exact_match(output: str, expected: str, **kwargs) -> float:
    """
    Check for exact string match.

    Args:
        output: Model output
        expected: Expected output

    Returns:
        1.0 if exact match, 0.0 otherwise
    """
    return 1.0 if output.strip() == expected.strip() else 0.0


def exact_match_ignore_case(output: str, expected: str, **kwargs) -> float:
    """
    Check for exact match ignoring case.

    Args:
        output: Model output
        expected: Expected output

    Returns:
        1.0 if match (case-insensitive), 0.0 otherwise
    """
    return 1.0 if output.strip().lower() == expected.strip().lower() else 0.0


def contains_match(output: str, expected: str, **kwargs) -> float:
    """
    Check if output contains expected value.

    Args:
        output: Model output
        expected: Expected output

    Returns:
        1.0 if output contains expected, 0.0 otherwise
    """
    return 1.0 if expected.strip() in output else 0.0


def contains_match_ignore_case(output: str, expected: str, **kwargs) -> float:
    """
    Check if output contains expected value (case-insensitive).

    Args:
        output: Model output
        expected: Expected output

    Returns:
        1.0 if output contains expected, 0.0 otherwise
    """
    return 1.0 if expected.strip().lower() in output.lower() else 0.0


def starts_with(output: str, expected: str, **kwargs) -> float:
    """
    Check if output starts with expected value.

    Args:
        output: Model output
        expected: Expected output

    Returns:
        1.0 if output starts with expected, 0.0 otherwise
    """
    return 1.0 if output.strip().startswith(expected.strip()) else 0.0


def regex_match(output: str, expected: str, **kwargs) -> float:
    """
    Check if output matches regex pattern.

    Args:
        output: Model output
        expected: Regex pattern

    Returns:
        1.0 if matches, 0.0 otherwise
    """
    try:
        pattern = re.compile(expected, re.IGNORECASE)
        return 1.0 if pattern.search(output) else 0.0
    except re.error:
        return 0.0


def fuzzy_match(output: str, expected: str, threshold: float = 0.8, **kwargs) -> float:
    """
    Fuzzy string matching using sequence matcher.

    Args:
        output: Model output
        expected: Expected output
        threshold: Minimum similarity for passing (0-1)

    Returns:
        Similarity score (0-1)
    """
    similarity = SequenceMatcher(
        None,
        output.strip().lower(),
        expected.strip().lower()
    ).ratio()

    return similarity


def numeric_match(output: str, expected: str, tolerance: float = 0.01, **kwargs) -> float:
    """
    Check if numeric values match within tolerance.

    Args:
        output: Model output (may contain text)
        expected: Expected numeric value
        tolerance: Allowed difference (relative)

    Returns:
        1.0 if within tolerance, 0.0 otherwise
    """
    try:
        # Extract numbers from output
        output_numbers = re.findall(r'-?\d+\.?\d*', output)
        expected_value = float(expected)

        for num_str in output_numbers:
            output_value = float(num_str)

            if expected_value == 0:
                if output_value == 0:
                    return 1.0
            else:
                relative_diff = abs(output_value - expected_value) / abs(expected_value)
                if relative_diff <= tolerance:
                    return 1.0

        return 0.0
    except (ValueError, ZeroDivisionError):
        return 0.0


def json_match(output: str, expected: str, **kwargs) -> float:
    """
    Check if output is valid JSON matching expected structure.

    Args:
        output: Model output (JSON string)
        expected: Expected JSON string

    Returns:
        1.0 if JSON matches, 0.0 otherwise
    """
    import json as json_lib

    try:
        output_json = json_lib.loads(output)
        expected_json = json_lib.loads(expected)
        return 1.0 if output_json == expected_json else 0.0
    except json_lib.JSONDecodeError:
        return 0.0


def multi_match(output: str, expected: str, separator: str = "|", **kwargs) -> float:
    """
    Check if output matches any of multiple expected values.

    Args:
        output: Model output
        expected: Expected values separated by separator
        separator: Separator between expected values

    Returns:
        1.0 if matches any expected value, 0.0 otherwise
    """
    expected_values = [v.strip() for v in expected.split(separator)]
    output_normalized = output.strip().lower()

    for exp in expected_values:
        if output_normalized == exp.lower():
            return 1.0

    return 0.0


def word_overlap(output: str, expected: str, **kwargs) -> float:
    """
    Calculate word overlap between output and expected.

    Args:
        output: Model output
        expected: Expected output

    Returns:
        Jaccard similarity of words (0-1)
    """
    output_words = set(output.lower().split())
    expected_words = set(expected.lower().split())

    if not expected_words:
        return 1.0 if not output_words else 0.0

    intersection = output_words & expected_words
    union = output_words | expected_words

    return len(intersection) / len(union) if union else 0.0


def length_ratio(output: str, expected: str, tolerance: float = 0.5, **kwargs) -> float:
    """
    Check if output length is within expected range.

    Args:
        output: Model output
        expected: Expected output (used for length reference)
        tolerance: Allowed deviation from expected length

    Returns:
        Score based on length similarity
    """
    output_len = len(output.strip())
    expected_len = len(expected.strip())

    if expected_len == 0:
        return 1.0 if output_len == 0 else 0.0

    ratio = output_len / expected_len

    # Perfect if within tolerance
    if 1 - tolerance <= ratio <= 1 + tolerance:
        return 1.0

    # Partial credit for close
    if ratio < 1 - tolerance:
        return max(0, ratio / (1 - tolerance))
    else:
        return max(0, (2 - ratio) / (1 + tolerance))


# Registry of available graders
GRADERS = {
    "exact_match": exact_match,
    "exact": exact_match,
    "exact_match_ignore_case": exact_match_ignore_case,
    "exact_ci": exact_match_ignore_case,
    "contains_match": contains_match,
    "contains": contains_match,
    "contains_match_ignore_case": contains_match_ignore_case,
    "contains_ci": contains_match_ignore_case,
    "starts_with": starts_with,
    "regex_match": regex_match,
    "regex": regex_match,
    "fuzzy_match": fuzzy_match,
    "fuzzy": fuzzy_match,
    "numeric_match": numeric_match,
    "numeric": numeric_match,
    "json_match": json_match,
    "json": json_match,
    "multi_match": multi_match,
    "multi": multi_match,
    "word_overlap": word_overlap,
    "overlap": word_overlap,
    "length_ratio": length_ratio,
}


def get_grader(name: str):
    """
    Get grader function by name.

    Args:
        name: Grader name

    Returns:
        Grader function

    Raises:
        ValueError: If grader not found
    """
    if name not in GRADERS:
        raise ValueError(f"Unknown grader: {name}. Available: {list(GRADERS.keys())}")
    return GRADERS[name]
