#!/usr/bin/env python3
"""
report.py — Generate progress tracker from memory data.

Generates paths/intermediate/tracker.md from memory files.
This is a DERIVED artifact that can be regenerated at any time.

Usage:
    python .claude/path-engine/report.py [--output FILE]
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from collections import defaultdict


# Configuration
REPO_ROOT = Path(__file__).parent.parent.parent.parent
MEMORY_DIR = REPO_ROOT / ".claude" / "memory"
PATHS_DIR = REPO_ROOT / "paths" / "intermediate"
DEFAULT_OUTPUT = PATHS_DIR / "tracker.md"


def load_jsonl(filepath: Path) -> list:
    """Load entries from a JSONL file."""
    entries = []
    if filepath.exists():
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        entries.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
    return entries


def load_json(filepath: Path) -> dict:
    """Load a JSON file."""
    if filepath.exists():
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def group_by_month(entries: list) -> dict:
    """Group entries by month."""
    by_month = defaultdict(list)
    for entry in entries:
        month = entry.get("month", 0)
        by_month[month].append(entry)
    return dict(by_month)


def get_latest_evaluation(progress: list) -> dict:
    """Get the most recent evaluation."""
    evals = [e for e in progress if e.get("event") == "evaluation"]
    if evals:
        return sorted(evals, key=lambda x: x.get("timestamp", ""), reverse=True)[0]
    return {}


def count_events(entries: list, event_type: str) -> int:
    """Count events of a specific type."""
    return sum(1 for e in entries if e.get("event") == event_type)


def format_timestamp(ts: str) -> str:
    """Format ISO timestamp to readable date."""
    try:
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d")
    except (ValueError, TypeError):
        return ts[:10] if ts else "Unknown"


def generate_tracker(profile: dict, progress: list, decisions: list) -> str:
    """Generate tracker markdown content."""
    level = profile.get("level", "intermediate").title()
    goals = profile.get("goals", [])

    # Get latest evaluation
    latest_eval = get_latest_evaluation(progress)

    # Group progress by month
    by_month = group_by_month(progress)

    # Count overall stats
    total_milestones = count_events(progress, "milestone")
    total_weeks = count_events(progress, "week_end")
    total_learnings = count_events(progress, "learning")

    # Determine current month
    current_month = max(by_month.keys()) if by_month else 1
    if current_month == 0:
        current_month = 1

    # Build markdown
    lines = [
        "# Progress Tracker",
        "",
        f"> **Level**: {level}",
        f"> **Generated**: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "---",
        "",
        "## Current Status",
        "",
        f"- **Current Month**: {current_month} of 12",
        f"- **Total Milestones**: {total_milestones}",
        f"- **Weeks Completed**: {total_weeks}",
        f"- **Learnings Captured**: {total_learnings}",
        "",
    ]

    # Latest evaluation
    if latest_eval:
        lines.extend([
            "### Latest Evaluation",
            "",
            f"- **Date**: {format_timestamp(latest_eval.get('timestamp', ''))}",
            f"- **Overall Score**: {latest_eval.get('overall', 'N/A')}",
            f"- **Assessment**: {latest_eval.get('assessment', 'N/A')}",
            "",
        ])

        scores = latest_eval.get("scores", {})
        if scores:
            lines.append("| Criterion | Score |")
            lines.append("|-----------|-------|")
            for criterion, score in scores.items():
                lines.append(f"| {criterion.title()} | {score} |")
            lines.append("")

    # Goals
    if goals:
        lines.extend([
            "---",
            "",
            "## Learning Goals",
            "",
        ])
        for goal in goals:
            lines.append(f"- {goal}")
        lines.append("")

    # Month progress
    lines.extend([
        "---",
        "",
        "## Monthly Progress",
        "",
    ])

    for month in range(1, 13):
        month_entries = by_month.get(month, [])
        milestones = count_events(month_entries, "milestone")
        weeks = count_events(month_entries, "week_end")

        if month < current_month:
            status = "Completed" if weeks >= 4 else "Partial"
            icon = "checkmark" if status == "Completed" else "warning"
        elif month == current_month:
            status = "In Progress"
            icon = "arrow_right"
        else:
            status = "Upcoming"
            icon = "circle"

        lines.append(f"### Month {month:02d}")
        lines.append(f"- **Status**: {status}")
        lines.append(f"- **Weeks**: {weeks}/4")
        lines.append(f"- **Milestones**: {milestones}")
        lines.append("")

    # Recent decisions
    if decisions:
        recent_decisions = sorted(
            decisions,
            key=lambda x: x.get("timestamp", ""),
            reverse=True
        )[:5]

        lines.extend([
            "---",
            "",
            "## Recent Decisions",
            "",
        ])

        for decision in recent_decisions:
            date = format_timestamp(decision.get("timestamp", ""))
            dtype = decision.get("type", "unknown").replace("_", " ").title()
            choice = decision.get("choice", decision.get("adaptation", ""))
            rationale = decision.get("rationale", "")

            lines.append(f"### {date}: {dtype}")
            if choice:
                lines.append(f"- **Choice**: {choice}")
            if rationale:
                lines.append(f"- **Rationale**: {rationale}")
            lines.append("")

    # Footer
    lines.extend([
        "---",
        "",
        "## Quick Actions",
        "",
        "```bash",
        "# Check status",
        "/status",
        "",
        "# Plan week",
        "/plan-week",
        "",
        "# Run evaluation",
        "python .claude/path-engine/evaluate.py",
        "",
        "# Get adaptation proposals",
        "python .claude/path-engine/adapt.py",
        "",
        "# Regenerate this tracker",
        "python .claude/path-engine/report.py",
        "```",
        "",
        "---",
        "",
        "*This file is auto-generated. Memory files in `.claude/memory/` are the source of truth.*",
    ])

    return "\n".join(lines)


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Generate progress tracker")
    parser.add_argument("--output", type=str, help="Output file path")
    parser.add_argument("--stdout", action="store_true", help="Print to stdout instead of file")
    args = parser.parse_args()

    # Load data
    profile = load_json(MEMORY_DIR / "learner_profile.json")
    progress = load_jsonl(MEMORY_DIR / "progress_log.jsonl")
    decisions = load_jsonl(MEMORY_DIR / "decisions.jsonl")

    # Generate tracker
    content = generate_tracker(profile, progress, decisions)

    # Output
    if args.stdout:
        print(content)
    else:
        output_path = Path(args.output) if args.output else DEFAULT_OUTPUT

        # Ensure directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Tracker generated: {output_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
