"""Render the Phase 12 JSON evaluation report as Markdown."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]

INPUT_FILE = (
    ROOT
    / "artifacts"
    / "phase-12"
    / "evaluation_report.json"
)

OUTPUT_FILE = (
    ROOT
    / "artifacts"
    / "phase-12"
    / "evaluation_report.md"
)


def main():
    report = json.loads(
        INPUT_FILE.read_text(
            encoding="utf-8"
        )
    )

    summary = report["summary"]

    lines = [
        "# Secure RAG Evaluation Report",
        "",
        "## Summary",
        "",
        f"- Total scenarios: {summary['total']}",
        f"- Passed: {summary['passed']}",
        f"- Failed: {summary['failed']}",
        f"- Pass rate: {summary['pass_rate']:.1%}",
        "",
        "## Control Coverage",
        "",
    ]

    for control_area, metrics in (
        report["control_summary"].items()
    ):
        lines.extend(
            [
                f"### {control_area}",
                "",
                f"- Total: {metrics['total']}",
                f"- Passed: {metrics['passed']}",
                f"- Failed: {metrics['failed']}",
                f"- Pass rate: {metrics['pass_rate']:.1%}",
                "",
            ]
        )

    lines.extend(
        [
            "## Scenario Results",
            "",
            "| Scenario | Control Area | Expected | Actual | Passed |",
            "|---|---|---|---|---|",
        ]
    )

    for result in report["results"]:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(result["scenario"]),
                    str(result["control_area"]),
                    str(result["expected"]),
                    str(result["actual"]),
                    (
                        "PASS"
                        if result["passed"]
                        else "FAIL"
                    ),
                ]
            )
            + " |"
        )

    OUTPUT_FILE.write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )

    print("Markdown report:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
