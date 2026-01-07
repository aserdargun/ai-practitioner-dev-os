# MCP Tool Contracts

Model Context Protocol (MCP) tool specifications for the AI Practitioner learning system.

---

## Overview

MCP tools extend Claude's capabilities by providing structured interfaces to external systems. These contracts define the available tools, their inputs, outputs, and usage patterns.

---

## Tool Catalog

### 1. evaluate_progress

Evaluates learner progress and returns scores.

**Contract:**
```json
{
  "name": "evaluate_progress",
  "description": "Evaluate learner progress based on memory files and repo signals",
  "inputSchema": {
    "type": "object",
    "properties": {
      "learner_id": {
        "type": "string",
        "description": "The learner's unique identifier"
      },
      "scope": {
        "type": "string",
        "enum": ["week", "month", "overall"],
        "description": "Evaluation scope"
      }
    },
    "required": ["learner_id"]
  }
}
```

**Response Schema:**
```json
{
  "type": "object",
  "properties": {
    "scores": {
      "type": "object",
      "properties": {
        "completion": { "type": "number" },
        "quality": { "type": "number" },
        "consistency": { "type": "number" },
        "growth": { "type": "number" },
        "engagement": { "type": "number" }
      }
    },
    "overall": { "type": "number" },
    "recommendations": {
      "type": "array",
      "items": { "type": "string" }
    }
  }
}
```

---

### 2. adapt_path

Proposes learning path adaptations.

**Contract:**
```json
{
  "name": "adapt_path",
  "description": "Propose mutations to the learning path based on evaluation",
  "inputSchema": {
    "type": "object",
    "properties": {
      "learner_id": {
        "type": "string",
        "description": "The learner's unique identifier"
      },
      "evaluation_result": {
        "type": "object",
        "description": "Result from evaluate_progress"
      }
    },
    "required": ["learner_id", "evaluation_result"]
  }
}
```

**Response Schema:**
```json
{
  "type": "object",
  "properties": {
    "mutations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "enum": ["level_change", "month_reorder", "remediation_week", "project_swap"]
          },
          "description": { "type": "string" },
          "details": { "type": "object" }
        }
      }
    },
    "approved": { "type": "boolean" }
  }
}
```

---

### 3. log_progress

Appends an entry to the progress log.

**Contract:**
```json
{
  "name": "log_progress",
  "description": "Append a progress entry to the learner's log",
  "inputSchema": {
    "type": "object",
    "properties": {
      "learner_id": {
        "type": "string",
        "description": "The learner's unique identifier"
      },
      "event": {
        "type": "string",
        "description": "Event type (e.g., task_completed, week_started)"
      },
      "message": {
        "type": "string",
        "description": "Human-readable description"
      },
      "metadata": {
        "type": "object",
        "description": "Additional event-specific data"
      }
    },
    "required": ["learner_id", "event", "message"]
  }
}
```

**Response Schema:**
```json
{
  "type": "object",
  "properties": {
    "success": { "type": "boolean" },
    "entry_id": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" }
  }
}
```

---

### 4. get_weekly_plan

Retrieves or generates the weekly plan.

**Contract:**
```json
{
  "name": "get_weekly_plan",
  "description": "Get the current week's plan or generate a new one",
  "inputSchema": {
    "type": "object",
    "properties": {
      "learner_id": {
        "type": "string",
        "description": "The learner's unique identifier"
      },
      "week_number": {
        "type": "integer",
        "description": "Week number (1-52)"
      },
      "generate_if_missing": {
        "type": "boolean",
        "description": "Generate plan if it doesn't exist",
        "default": true
      }
    },
    "required": ["learner_id"]
  }
}
```

**Response Schema:**
```json
{
  "type": "object",
  "properties": {
    "week_number": { "type": "integer" },
    "month": { "type": "integer" },
    "focus": { "type": "string" },
    "tasks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "description": { "type": "string" },
          "status": { "type": "string", "enum": ["pending", "in_progress", "completed"] },
          "estimated_hours": { "type": "number" }
        }
      }
    },
    "deliverables": {
      "type": "array",
      "items": { "type": "string" }
    }
  }
}
```

---

### 5. add_best_practice

Captures a new best practice.

**Contract:**
```json
{
  "name": "add_best_practice",
  "description": "Add a new best practice entry",
  "inputSchema": {
    "type": "object",
    "properties": {
      "title": {
        "type": "string",
        "description": "Short title for the practice"
      },
      "context": {
        "type": "string",
        "description": "When this practice applies"
      },
      "practice": {
        "type": "string",
        "description": "What to do"
      },
      "why": {
        "type": "string",
        "description": "Reasoning or evidence"
      },
      "example": {
        "type": "string",
        "description": "Code or process example"
      }
    },
    "required": ["title", "practice"]
  }
}
```

**Response Schema:**
```json
{
  "type": "object",
  "properties": {
    "success": { "type": "boolean" },
    "entry_date": { "type": "string", "format": "date" }
  }
}
```

---

## Usage Example

```python
# Example: Using MCP tools in a workflow

# 1. Evaluate progress
evaluation = await mcp.call("evaluate_progress", {
    "learner_id": "learner-001",
    "scope": "week"
})

# 2. If score is low, propose adaptations
if evaluation["overall"] < 0.6:
    adaptations = await mcp.call("adapt_path", {
        "learner_id": "learner-001",
        "evaluation_result": evaluation
    })

# 3. Log the evaluation
await mcp.call("log_progress", {
    "learner_id": "learner-001",
    "event": "evaluation_completed",
    "message": f"Weekly evaluation: {evaluation['overall']:.0%}",
    "metadata": evaluation
})
```

---

## Error Handling

All tools return errors in this format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {}
  }
}
```

Common error codes:
- `LEARNER_NOT_FOUND`: Invalid learner_id
- `INVALID_INPUT`: Schema validation failed
- `FILE_NOT_FOUND`: Required memory file missing
- `PERMISSION_DENIED`: Operation not allowed
