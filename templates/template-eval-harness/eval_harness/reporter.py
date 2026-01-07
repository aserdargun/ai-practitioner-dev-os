"""Report generation."""

import json
from pathlib import Path

from jinja2 import Template

from eval_harness.runner import EvaluationResults

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Evaluation Report - {{ results.model_name }}</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .card {
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 { color: #333; }
        h2 { color: #666; margin-top: 0; }
        .metric {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid #eee;
        }
        .metric:last-child { border-bottom: none; }
        .metric-name { font-weight: 500; }
        .metric-value {
            font-family: monospace;
            color: #0066cc;
        }
        .timestamp {
            color: #999;
            font-size: 0.9em;
        }
        .metadata {
            font-size: 0.9em;
            color: #666;
        }
    </style>
</head>
<body>
    <h1>Evaluation Report</h1>
    <p class="timestamp">Generated: {{ results.timestamp }}</p>

    <div class="card">
        <h2>Model: {{ results.model_name }}</h2>
        <div class="metadata">
            <p>Samples: {{ results.metadata.n_samples }}</p>
            <p>Features: {{ results.metadata.n_features }}</p>
        </div>
    </div>

    <div class="card">
        <h2>Metrics</h2>
        {% for name, value in results.metrics.items() %}
        <div class="metric">
            <span class="metric-name">{{ name }}</span>
            <span class="metric-value">
                {% if value is mapping %}
                    {{ value | tojson }}
                {% elif value is number %}
                    {{ "%.4f" | format(value) }}
                {% else %}
                    {{ value }}
                {% endif %}
            </span>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""


def generate_report(
    results: EvaluationResults,
    output_path: Path,
    format: str = "json",
) -> None:
    """Generate evaluation report.

    Args:
        results: Evaluation results.
        output_path: Output file path.
        format: Output format ('json' or 'html').
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if format == "json":
        with open(output_path, "w") as f:
            json.dump(results.to_dict(), f, indent=2, default=str)

    elif format == "html":
        template = Template(HTML_TEMPLATE)
        html = template.render(results=results)
        with open(output_path, "w") as f:
            f.write(html)

    else:
        raise ValueError(f"Unsupported format: {format}")


def generate_comparison_report(
    results: dict[str, EvaluationResults],
    output_path: Path,
    format: str = "json",
) -> None:
    """Generate comparison report for multiple models.

    Args:
        results: Dictionary of model_name -> EvaluationResults.
        output_path: Output file path.
        format: Output format.
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if format == "json":
        data = {name: r.to_dict() for name, r in results.items()}
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2, default=str)
    else:
        raise ValueError(f"Comparison report only supports JSON format")
