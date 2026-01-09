#!/usr/bin/env python3
"""
Evaluation Engine for AI Practitioner Learning OS.

Reads memory files and repo signals to compute progress scores.

Usage:
    python evaluate.py [--month N] [--json]

Output:
    Evaluation report with category scores and analysis.
"""

import argparse
import json
import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


# Paths
REPO_ROOT = Path(__file__).parent.parent.parent
MEMORY_DIR = REPO_ROOT / ".claude" / "memory"
PATHS_DIR = REPO_ROOT / "paths" / "advanced"

# Scoring weights
WEIGHTS = {
    "completion": 0.40,
    "quality": 0.25,
    "velocity": 0.20,
    "reflection": 0.15,
}

# Thresholds
PASSING_THRESHOLD = 70


def load_json(path: Path) -> dict:
    """Load a JSON file."""
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def load_jsonl(path: Path) -> list:
    """Load a JSONL file."""
    if not path.exists():
        return []
    entries = []
    for line in path.read_text().splitlines():
        if line.strip():
            entries.append(json.loads(line))
    return entries


def get_git_signals(days: int = 30) -> dict:
    """Get signals from git history."""
    signals = {
        "commits": 0,
        "files_changed": 0,
        "lines_added": 0,
        "lines_removed": 0,
    }

    try:
        # Count commits
        since = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        result = subprocess.run(
            ["git", "log", f"--since={since}", "--oneline"],
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
        )
        if result.returncode == 0:
            signals["commits"] = len(result.stdout.strip().splitlines())

        # Get diff stats
        result = subprocess.run(
            ["git", "diff", "--stat", f"--since={since}", "HEAD~10", "HEAD"],
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
        )
        # Basic parsing (actual git diff stat parsing would be more complex)
    except Exception:
        pass

    return signals


def get_test_signals() -> dict:
    """Get signals from test suite."""
    signals = {
        "tests_exist": False,
        "tests_passing": False,
        "test_count": 0,
    }

    # Check if tests directory exists
    test_dirs = list(REPO_ROOT.glob("**/tests"))
    signals["tests_exist"] = len(test_dirs) > 0

    # Try to run pytest (if available)
    try:
        result = subprocess.run(
            ["pytest", "--collect-only", "-q"],
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
            timeout=30,
        )
        if result.returncode == 0:
            # Count test items
            lines = result.stdout.strip().splitlines()
            for line in lines:
                if "test" in line.lower():
                    signals["test_count"] += 1
    except Exception:
        pass

    return signals


def count_dod_items(month: int) -> tuple[int, int]:
    """Count Definition of Done items (completed/total)."""
    month_readme = PATHS_DIR / f"month-{month:02d}" / "README.md"
    if not month_readme.exists():
        return 0, 0

    content = month_readme.read_text()

    # Look for DoD checklist items
    completed = content.count("[x]") + content.count("[X]")
    uncompleted = content.count("[ ]")
    total = completed + uncompleted

    return completed, total


def count_progress_events(month: int) -> dict:
    """Count progress log events for the month."""
    progress_log = load_jsonl(MEMORY_DIR / "progress_log.jsonl")

    counts = {
        "task_complete": 0,
        "blockers": 0,
        "blockers_resolved": 0,
        "week_starts": 0,
        "week_ends": 0,
        "milestones": 0,
    }

    for entry in progress_log:
        entry_type = entry.get("type", "")
        if entry_type in counts:
            counts[entry_type] += 1

    return counts


def count_journal_entries() -> int:
    """Count journal entries."""
    journal_dir = PATHS_DIR / "journal"
    if not journal_dir.exists():
        return 0
    return len(list(journal_dir.glob("*.md")))


def compute_scores(month: int) -> dict:
    """Compute scores for each category."""
    scores = {}

    # Completion score (40%)
    completed, total = count_dod_items(month)
    if total > 0:
        scores["completion"] = (completed / total) * 100
    else:
        scores["completion"] = 50  # Neutral if no DoD items found

    # Quality score (25%)
    test_signals = get_test_signals()
    if test_signals["tests_exist"]:
        # Basic heuristic: tests exist = 70%, more tests = higher
        base_score = 70
        bonus = min(30, test_signals["test_count"] * 3)
        scores["quality"] = base_score + bonus
    else:
        scores["quality"] = 50  # Neutral if no tests

    # Velocity score (20%)
    events = count_progress_events(month)
    git_signals = get_git_signals()

    # Heuristic: commits + task completions
    activity = events["task_complete"] + git_signals["commits"]
    if activity >= 20:
        scores["velocity"] = 100
    elif activity >= 10:
        scores["velocity"] = 80
    elif activity >= 5:
        scores["velocity"] = 60
    else:
        scores["velocity"] = 40

    # Reflection score (15%)
    journal_count = count_journal_entries()
    retros = events["week_ends"]  # Assuming week_end implies retro

    if journal_count >= 4 and retros >= 2:
        scores["reflection"] = 100
    elif journal_count >= 2 or retros >= 1:
        scores["reflection"] = 70
    else:
        scores["reflection"] = 40

    # Compute weighted overall
    overall = sum(scores[cat] * WEIGHTS[cat] for cat in WEIGHTS)
    scores["overall"] = overall

    return scores


def analyze_trends(progress_log: list) -> dict:
    """Analyze trends from progress log."""
    trends = {
        "recent_blockers": [],
        "velocity_trend": "stable",
        "active_days": 0,
    }

    # Count active days (days with entries)
    dates = set()
    for entry in progress_log:
        ts = entry.get("timestamp", "")
        if ts:
            dates.add(ts[:10])  # Extract date part
    trends["active_days"] = len(dates)

    # Find recent blockers
    for entry in progress_log[-10:]:
        if entry.get("type") == "blocker":
            trends["recent_blockers"].append(entry.get("description", "Unknown"))

    return trends


def generate_report(month: int, as_json: bool = False) -> str:
    """Generate evaluation report."""
    scores = compute_scores(month)
    progress_log = load_jsonl(MEMORY_DIR / "progress_log.jsonl")
    trends = analyze_trends(progress_log)
    git_signals = get_git_signals()

    status = "PASSING" if scores["overall"] >= PASSING_THRESHOLD else "NEEDS_ATTENTION"

    if as_json:
        return json.dumps({
            "month": month,
            "scores": scores,
            "status": status,
            "threshold": PASSING_THRESHOLD,
            "trends": trends,
            "signals": {
                "git": git_signals,
                "progress_events": count_progress_events(month),
            }
        }, indent=2)

    # Generate markdown report
    report = f"""# Evaluation Report: Month {month:02d}

**Generated**: {datetime.now().isoformat()}
**Status**: {"✅ " + status if status == "PASSING" else "⚠️ " + status}
**Threshold**: {PASSING_THRESHOLD}%

## Scores

| Category | Weight | Score | Weighted |
|----------|--------|-------|----------|
| Completion | {WEIGHTS['completion']*100:.0f}% | {scores['completion']:.1f}% | {scores['completion']*WEIGHTS['completion']:.1f} |
| Quality | {WEIGHTS['quality']*100:.0f}% | {scores['quality']:.1f}% | {scores['quality']*WEIGHTS['quality']:.1f} |
| Velocity | {WEIGHTS['velocity']*100:.0f}% | {scores['velocity']:.1f}% | {scores['velocity']*WEIGHTS['velocity']:.1f} |
| Reflection | {WEIGHTS['reflection']*100:.0f}% | {scores['reflection']:.1f}% | {scores['reflection']*WEIGHTS['reflection']:.1f} |
| **Overall** | 100% | | **{scores['overall']:.1f}%** |

## Signals

- Commits (last 30 days): {git_signals['commits']}
- Active days: {trends['active_days']}
- Journal entries: {count_journal_entries()}

## Analysis

"""

    if scores["overall"] >= 85:
        report += "Excellent progress! Consider stretch goals or acceleration.\n"
    elif scores["overall"] >= PASSING_THRESHOLD:
        report += "Good progress. On track for month completion.\n"
    else:
        report += "Below threshold. Consider running `/adapt-path` for recommendations.\n"

    if trends["recent_blockers"]:
        report += "\n### Recent Blockers\n"
        for blocker in trends["recent_blockers"]:
            report += f"- {blocker}\n"

    report += """
## Next Steps

1. Review scores and analysis
2. Run `python .claude/path-engine/adapt.py` for adaptation proposals
3. Run `python .claude/path-engine/report.py` to update tracker

---
*This report is for review. No changes have been made.*
"""

    return report


def main():
    parser = argparse.ArgumentParser(description="Evaluate learning progress")
    parser.add_argument("--month", type=int, default=1, help="Month number to evaluate")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    # Determine current month from profile
    profile = load_json(MEMORY_DIR / "learner_profile.json")
    month = args.month or profile.get("current_month", 1)

    report = generate_report(month, as_json=args.json)
    print(report)


if __name__ == "__main__":
    main()
