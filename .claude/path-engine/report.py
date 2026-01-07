#!/usr/bin/env python3
"""
Generate progress report and update tracker.

This script creates a human-readable progress report and updates
the learner's tracker.md file with current status.

Usage:
    python report.py
    python report.py --output markdown
    python report.py --update-tracker

Output:
    Writes report to stdout and optionally updates paths/Advanced/tracker.md
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


# Configuration
REPO_ROOT = Path(__file__).parent.parent.parent
MEMORY_DIR = REPO_ROOT / ".claude" / "memory"
OUTPUT_DIR = REPO_ROOT / ".claude" / "path-engine" / "output"
PATHS_DIR = REPO_ROOT / "paths"


def read_json(filepath: Path) -> dict:
    """Read a JSON file."""
    if not filepath.exists():
        return {}
    with open(filepath, "r") as f:
        return json.load(f)


def read_jsonl(filepath: Path) -> list[dict]:
    """Read a JSON Lines file."""
    if not filepath.exists():
        return []
    entries = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return entries


def get_latest_evaluation() -> dict:
    """Get the most recent evaluation result."""
    if not OUTPUT_DIR.exists():
        return {}

    eval_files = sorted(OUTPUT_DIR.glob("evaluation_*.json"), reverse=True)
    if eval_files:
        return read_json(eval_files[0])
    return {}


def get_latest_adaptation() -> dict:
    """Get the most recent adaptation result."""
    if not OUTPUT_DIR.exists():
        return {}

    adapt_files = sorted(OUTPUT_DIR.glob("adaptation_*.json"), reverse=True)
    if adapt_files:
        return read_json(adapt_files[0])
    return {}


def generate_progress_bar(value: float, width: int = 20) -> str:
    """Generate a text progress bar."""
    filled = int(value * width)
    empty = width - filled
    return f"[{'█' * filled}{'░' * empty}] {value:.0%}"


def generate_report(evaluation: dict, adaptation: dict, profile: dict) -> dict:
    """Generate comprehensive report data."""
    progress_log = read_jsonl(MEMORY_DIR / "progress_log.jsonl")

    # Calculate timeline
    start_date = profile.get("start_date", "2026-01-01")
    current_month = profile.get("current_month", 1)
    current_week = profile.get("current_week", 1)

    # Count milestones
    completed_tasks = sum(1 for e in progress_log if "completed" in e.get("event", ""))
    total_log_entries = len(progress_log)

    # Get scores
    scores = evaluation.get("scores", {})
    overall = evaluation.get("overall", 0)
    status = evaluation.get("status", "unknown")

    # Get pending adaptations
    mutations = adaptation.get("mutations", [])
    pending_changes = [m for m in mutations if m.get("requires_approval", True)]

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "learner": {
            "id": profile.get("learner_id", "unknown"),
            "level": profile.get("level", "Advanced"),
            "start_date": start_date,
        },
        "progress": {
            "current_month": current_month,
            "current_week": current_week,
            "total_months": 12,
            "overall_percent": round((current_month - 1 + current_week / 4) / 12 * 100),
        },
        "evaluation": {
            "overall": overall,
            "status": status,
            "scores": scores,
            "recommendations": evaluation.get("recommendations", []),
        },
        "activity": {
            "completed_tasks": completed_tasks,
            "log_entries": total_log_entries,
            "last_activity": progress_log[-1].get("timestamp") if progress_log else None,
        },
        "adaptations": {
            "pending": len(pending_changes),
            "details": pending_changes,
        },
    }


def format_markdown_report(report: dict) -> str:
    """Format report as Markdown."""
    lines = []
    lines.append("# Progress Report")
    lines.append("")
    lines.append(f"*Generated: {report['generated_at']}*")
    lines.append("")

    # Learner Info
    lines.append("## Learner Profile")
    lines.append("")
    lines.append(f"- **ID**: {report['learner']['id']}")
    lines.append(f"- **Level**: {report['learner']['level']}")
    lines.append(f"- **Start Date**: {report['learner']['start_date']}")
    lines.append("")

    # Progress
    lines.append("## Current Progress")
    lines.append("")
    progress = report["progress"]
    lines.append(f"- **Month**: {progress['current_month']} of {progress['total_months']}")
    lines.append(f"- **Week**: {progress['current_week']}")
    lines.append(f"- **Overall**: {progress['overall_percent']}% complete")
    lines.append("")
    lines.append(f"```")
    lines.append(generate_progress_bar(progress['overall_percent'] / 100, 30))
    lines.append(f"```")
    lines.append("")

    # Evaluation
    lines.append("## Evaluation Scores")
    lines.append("")
    eval_data = report["evaluation"]
    lines.append(f"**Status**: {eval_data['status'].upper()}")
    lines.append(f"**Overall Score**: {eval_data['overall']:.0%}")
    lines.append("")
    lines.append("| Dimension | Score |")
    lines.append("|-----------|-------|")
    for dim, score in eval_data["scores"].items():
        lines.append(f"| {dim.title()} | {score:.0%} |")
    lines.append("")

    # Recommendations
    if eval_data["recommendations"]:
        lines.append("### Recommendations")
        lines.append("")
        for rec in eval_data["recommendations"]:
            lines.append(f"- {rec}")
        lines.append("")

    # Activity
    lines.append("## Activity Summary")
    lines.append("")
    activity = report["activity"]
    lines.append(f"- **Completed Tasks**: {activity['completed_tasks']}")
    lines.append(f"- **Log Entries**: {activity['log_entries']}")
    if activity["last_activity"]:
        lines.append(f"- **Last Activity**: {activity['last_activity']}")
    lines.append("")

    # Pending Adaptations
    if report["adaptations"]["pending"] > 0:
        lines.append("## Pending Adaptations")
        lines.append("")
        lines.append(f"⚠️ {report['adaptations']['pending']} adaptation(s) require review:")
        lines.append("")
        for adaptation in report["adaptations"]["details"]:
            lines.append(f"- **{adaptation['type']}**: {adaptation['description']}")
        lines.append("")

    return "\n".join(lines)


def format_tracker(report: dict) -> str:
    """Format report for tracker.md file."""
    lines = []
    lines.append("# Learning Tracker")
    lines.append("")
    lines.append(f"**Level**: {report['learner']['level']}")
    lines.append(f"**Started**: {report['learner']['start_date']}")
    lines.append(f"**Last Updated**: {report['generated_at'][:10]}")
    lines.append("")

    # Overall Progress
    lines.append("## Overall Progress")
    lines.append("")
    progress = report["progress"]
    lines.append(f"Month {progress['current_month']} / Week {progress['current_week']}")
    lines.append("")
    lines.append("```")
    lines.append(generate_progress_bar(progress['overall_percent'] / 100, 40))
    lines.append("```")
    lines.append("")

    # Current Status
    lines.append("## Current Status")
    lines.append("")
    eval_data = report["evaluation"]
    status_emoji = {
        "excellent": "🌟",
        "on_track": "✅",
        "needs_attention": "⚠️",
        "at_risk": "🚨",
    }.get(eval_data["status"], "❓")
    lines.append(f"{status_emoji} **{eval_data['status'].replace('_', ' ').title()}** ({eval_data['overall']:.0%})")
    lines.append("")

    # Score Summary
    lines.append("### Scores")
    lines.append("")
    for dim, score in eval_data["scores"].items():
        emoji = "✅" if score >= 0.7 else "⚠️" if score >= 0.5 else "❌"
        lines.append(f"- {emoji} {dim.title()}: {score:.0%}")
    lines.append("")

    # Monthly Progress (placeholder for future months)
    lines.append("## Monthly Milestones")
    lines.append("")
    lines.append("| Month | Topic | Status |")
    lines.append("|-------|-------|--------|")
    current_month = progress["current_month"]
    topics = [
        "Foundations & Setup",
        "Data Engineering",
        "ML Fundamentals",
        "Deep Learning",
        "NLP & LLMs",
        "Computer Vision",
        "MLOps & Deployment",
        "System Design",
        "Evaluation & Testing",
        "Advanced Topics",
        "Capstone Project",
        "Portfolio & Career",
    ]
    for i, topic in enumerate(topics, 1):
        if i < current_month:
            status = "✅ Complete"
        elif i == current_month:
            status = "🔄 In Progress"
        else:
            status = "⏳ Upcoming"
        lines.append(f"| {i:02d} | {topic} | {status} |")
    lines.append("")

    # Next Actions
    if eval_data["recommendations"]:
        lines.append("## Next Actions")
        lines.append("")
        for rec in eval_data["recommendations"][:3]:
            lines.append(f"- [ ] {rec}")
        lines.append("")

    return "\n".join(lines)


def update_tracker(report: dict, level: str) -> None:
    """Update the tracker.md file."""
    tracker_content = format_tracker(report)
    tracker_path = PATHS_DIR / level / "tracker.md"

    tracker_path.parent.mkdir(parents=True, exist_ok=True)
    with open(tracker_path, "w") as f:
        f.write(tracker_content)

    print(f"\nTracker updated: {tracker_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Generate progress report")
    parser.add_argument(
        "--output",
        choices=["text", "markdown", "json"],
        default="markdown",
        help="Output format",
    )
    parser.add_argument(
        "--update-tracker",
        action="store_true",
        help="Update the tracker.md file",
    )

    args = parser.parse_args()

    # Load data
    profile = read_json(MEMORY_DIR / "learner_profile.json")
    evaluation = get_latest_evaluation()
    adaptation = get_latest_adaptation()

    if not profile:
        print("Error: Learner profile not found.")
        sys.exit(1)

    # Generate report
    report = generate_report(evaluation, adaptation, profile)

    # Output
    if args.output == "json":
        print(json.dumps(report, indent=2))
    elif args.output == "markdown":
        print(format_markdown_report(report))
    else:
        print(format_markdown_report(report))

    # Update tracker if requested
    if args.update_tracker:
        level = profile.get("level", "Advanced")
        update_tracker(report, level)

    # Save report
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_file = OUTPUT_DIR / f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, "w") as f:
        json.dump(report, f, indent=2)


if __name__ == "__main__":
    main()
