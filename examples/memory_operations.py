#!/usr/bin/env python3
"""Example: Working with memory files.

This script demonstrates how to read and write to the learning system's
memory files programmatically.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Memory directory
MEMORY_DIR = Path(__file__).parent.parent / ".claude" / "memory"


def read_learner_profile() -> dict:
    """Read the learner profile.

    Returns:
        Learner profile dictionary
    """
    profile_path = MEMORY_DIR / "learner_profile.json"
    with open(profile_path) as f:
        return json.load(f)


def read_progress_log() -> list[dict]:
    """Read all entries from the progress log.

    Returns:
        List of progress entries
    """
    log_path = MEMORY_DIR / "progress_log.jsonl"
    entries = []
    with open(log_path) as f:
        for line in f:
            if line.strip():
                entries.append(json.loads(line))
    return entries


def append_progress_entry(event: str, message: str, **metadata) -> None:
    """Append an entry to the progress log.

    Args:
        event: Event type (e.g., "task_completed")
        message: Human-readable message
        **metadata: Additional metadata
    """
    log_path = MEMORY_DIR / "progress_log.jsonl"

    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": event,
        "message": message,
    }
    if metadata:
        entry["metadata"] = metadata

    with open(log_path, "a") as f:
        f.write(json.dumps(entry) + "\n")

    print(f"Added entry: {event} - {message}")


def add_best_practice(title: str, practice: str, context: str = "", why: str = "") -> None:
    """Add a best practice entry.

    Args:
        title: Practice title
        practice: What to do
        context: When it applies
        why: Reasoning
    """
    bp_path = MEMORY_DIR / "best_practices.md"

    date = datetime.now().strftime("%Y-%m-%d")
    entry = f"\n### {date} - {title}\n\n"

    if context:
        entry += f"**Context**: {context}\n\n"
    entry += f"**Practice**: {practice}\n\n"
    if why:
        entry += f"**Why**: {why}\n\n"
    entry += "---\n"

    with open(bp_path, "a") as f:
        f.write(entry)

    print(f"Added best practice: {title}")


def get_progress_summary() -> dict:
    """Get a summary of progress.

    Returns:
        Summary dictionary
    """
    entries = read_progress_log()

    return {
        "total_entries": len(entries),
        "completed_tasks": sum(1 for e in entries if "completed" in e.get("event", "")),
        "started_tasks": sum(1 for e in entries if "started" in e.get("event", "")),
        "first_entry": entries[0]["timestamp"] if entries else None,
        "last_entry": entries[-1]["timestamp"] if entries else None,
    }


# Example usage
if __name__ == "__main__":
    # Read profile
    print("=== Learner Profile ===")
    profile = read_learner_profile()
    print(f"Level: {profile.get('level')}")
    print(f"Start Date: {profile.get('start_date')}")
    print()

    # Read progress summary
    print("=== Progress Summary ===")
    summary = get_progress_summary()
    print(f"Total entries: {summary['total_entries']}")
    print(f"Completed tasks: {summary['completed_tasks']}")
    print()

    # Example: Add a progress entry (uncomment to run)
    # append_progress_entry(
    #     event="task_completed",
    #     message="Finished example script",
    #     duration_minutes=30
    # )

    # Example: Add a best practice (uncomment to run)
    # add_best_practice(
    #     title="Use type hints",
    #     practice="Add type hints to all function signatures",
    #     context="When writing Python functions",
    #     why="Improves code readability and enables better IDE support"
    # )
