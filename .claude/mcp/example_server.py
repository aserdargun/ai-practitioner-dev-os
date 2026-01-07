#!/usr/bin/env python3
"""
Example MCP Server for AI Practitioner Learning System

This server exposes learning system tools via the Model Context Protocol.
Uses Python stdlib only (no external dependencies).

Run with: python example_server.py
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


# Configuration
MEMORY_DIR = Path(__file__).parent.parent / "memory"


def read_jsonl(filepath: Path) -> list[dict]:
    """Read a JSON Lines file."""
    if not filepath.exists():
        return []
    entries = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                entries.append(json.loads(line))
    return entries


def append_jsonl(filepath: Path, entry: dict) -> None:
    """Append an entry to a JSON Lines file."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "a") as f:
        f.write(json.dumps(entry) + "\n")


def read_json(filepath: Path) -> dict:
    """Read a JSON file."""
    if not filepath.exists():
        return {}
    with open(filepath, "r") as f:
        return json.load(f)


def get_timestamp() -> str:
    """Get current ISO 8601 timestamp."""
    return datetime.now(timezone.utc).isoformat()


# Tool implementations

def evaluate_progress(learner_id: str, scope: str = "week") -> dict:
    """Evaluate learner progress based on memory files."""
    progress_log = read_jsonl(MEMORY_DIR / "progress_log.jsonl")
    profile = read_json(MEMORY_DIR / "learner_profile.json")

    if not profile:
        return {"error": {"code": "LEARNER_NOT_FOUND", "message": "Learner profile not found"}}

    # Calculate scores (simplified scoring logic)
    total_entries = len(progress_log)
    completed_events = sum(1 for e in progress_log if "completed" in e.get("event", ""))

    scores = {
        "completion": min(1.0, completed_events / max(1, total_entries * 0.3)),
        "quality": 0.75,  # Placeholder - would check test results
        "consistency": min(1.0, total_entries / 10),
        "growth": 0.70,  # Placeholder - would check best practices
        "engagement": 0.80,  # Placeholder - would check interactions
    }

    # Weighted average
    weights = {"completion": 0.30, "quality": 0.25, "consistency": 0.20, "growth": 0.15, "engagement": 0.10}
    overall = sum(scores[k] * weights[k] for k in scores)

    recommendations = []
    if scores["completion"] < 0.6:
        recommendations.append("Focus on completing more tasks")
    if scores["quality"] < 0.7:
        recommendations.append("Add more tests to improve quality score")
    if scores["consistency"] < 0.7:
        recommendations.append("Log progress more frequently")

    return {
        "scores": scores,
        "overall": round(overall, 2),
        "recommendations": recommendations,
        "evaluated_at": get_timestamp(),
    }


def adapt_path(learner_id: str, evaluation_result: dict) -> dict:
    """Propose learning path adaptations based on evaluation."""
    overall = evaluation_result.get("overall", 0.7)
    mutations = []

    if overall < 0.4:
        mutations.append({
            "type": "level_change",
            "description": "Consider moving to a lower level",
            "details": {"current": "Advanced", "proposed": "Intermediate"},
        })
    elif overall < 0.6:
        mutations.append({
            "type": "remediation_week",
            "description": "Insert a remediation week to catch up",
            "details": {"focus_areas": evaluation_result.get("recommendations", [])},
        })
    elif overall > 0.9:
        mutations.append({
            "type": "level_change",
            "description": "Consider acceleration or advanced challenges",
            "details": {"note": "Learner is exceeding expectations"},
        })

    return {
        "mutations": mutations,
        "approved": len(mutations) == 0,  # Auto-approve if no changes needed
        "generated_at": get_timestamp(),
    }


def log_progress(learner_id: str, event: str, message: str, metadata: dict = None) -> dict:
    """Append a progress entry to the learner's log."""
    entry = {
        "timestamp": get_timestamp(),
        "learner_id": learner_id,
        "event": event,
        "message": message,
    }
    if metadata:
        entry["metadata"] = metadata

    progress_file = MEMORY_DIR / "progress_log.jsonl"
    append_jsonl(progress_file, entry)

    return {
        "success": True,
        "entry_id": f"{learner_id}-{entry['timestamp']}",
        "timestamp": entry["timestamp"],
    }


def add_best_practice(title: str, practice: str, context: str = "", why: str = "", example: str = "") -> dict:
    """Add a new best practice entry."""
    best_practices_file = MEMORY_DIR / "best_practices.md"

    date = datetime.now().strftime("%Y-%m-%d")
    entry = f"\n### {date} - {title}\n\n"

    if context:
        entry += f"**Context**: {context}\n\n"
    entry += f"**Practice**: {practice}\n\n"
    if why:
        entry += f"**Why**: {why}\n\n"
    if example:
        entry += f"**Example**:\n```\n{example}\n```\n"
    entry += "\n---\n"

    with open(best_practices_file, "a") as f:
        f.write(entry)

    return {
        "success": True,
        "entry_date": date,
    }


# MCP Protocol handling

def handle_request(request: dict) -> dict:
    """Handle an MCP request and return a response."""
    method = request.get("method")
    params = request.get("params", {})

    tools = {
        "evaluate_progress": evaluate_progress,
        "adapt_path": adapt_path,
        "log_progress": log_progress,
        "add_best_practice": add_best_practice,
    }

    if method == "tools/list":
        return {
            "tools": [
                {"name": name, "description": f"Learning system tool: {name}"}
                for name in tools.keys()
            ]
        }

    if method == "tools/call":
        tool_name = params.get("name")
        tool_args = params.get("arguments", {})

        if tool_name not in tools:
            return {"error": {"code": "TOOL_NOT_FOUND", "message": f"Unknown tool: {tool_name}"}}

        try:
            result = tools[tool_name](**tool_args)
            return {"content": [{"type": "text", "text": json.dumps(result, indent=2)}]}
        except TypeError as e:
            return {"error": {"code": "INVALID_INPUT", "message": str(e)}}
        except Exception as e:
            return {"error": {"code": "EXECUTION_ERROR", "message": str(e)}}

    return {"error": {"code": "METHOD_NOT_FOUND", "message": f"Unknown method: {method}"}}


def main():
    """Main entry point - reads JSON-RPC requests from stdin."""
    print("MCP Server started. Listening for requests...", file=sys.stderr)

    for line in sys.stdin:
        try:
            request = json.loads(line.strip())
            response = handle_request(request)
            response["jsonrpc"] = "2.0"
            response["id"] = request.get("id")
            print(json.dumps(response))
            sys.stdout.flush()
        except json.JSONDecodeError as e:
            error_response = {
                "jsonrpc": "2.0",
                "error": {"code": "PARSE_ERROR", "message": str(e)},
                "id": None,
            }
            print(json.dumps(error_response))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
