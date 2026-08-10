"""Run the Phase 12 Secure RAG evaluation suite."""

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from enterprise_rag.evaluation.scenarios import (
    SCENARIOS,
)


ROOT = Path(__file__).resolve().parents[3]

OUTPUT_FILE = (
    ROOT
    / "artifacts"
    / "phase-12"
    / "evaluation_report.json"
)


def main():
    results = []

    for scenario in SCENARIOS:
        result = scenario()
        results.append(
            result.to_dict()
        )

    total = len(results)

    passed = sum(
        1
        for result in results
        if result["passed"]
    )

    failed = total - passed

    control_counts = Counter(
        result["control_area"]
        for result in results
    )

    control_passed = Counter(
        result["control_area"]
        for result in results
        if result["passed"]
    )

    control_summary = {}

    for control_area in sorted(control_counts):
        area_total = control_counts[
            control_area
        ]

        area_passed = control_passed[
            control_area
        ]

        control_summary[
            control_area
        ] = {
            "total": area_total,
            "passed": area_passed,
            "failed": (
                area_total - area_passed
            ),
            "pass_rate": (
                area_passed / area_total
            ),
        }

    report = {
        "generated_at": datetime.now(
            timezone.utc
        ).isoformat(),
        "summary": {
            "total": total,
            "passed": passed,
            "failed": failed,
            "pass_rate": (
                passed / total
                if total
                else 0.0
            ),
        },
        "control_summary": control_summary,
        "results": results,
    }

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_FILE.write_text(
        json.dumps(
            report,
            indent=2,
        ),
        encoding="utf-8",
    )

    print("Secure RAG Evaluation")
    print("====================")
    print("Total:", total)
    print("Passed:", passed)
    print("Failed:", failed)
    print(
        "Pass rate:",
        f"{report['summary']['pass_rate']:.1%}",
    )
    print()

    for result in results:
        marker = (
            "PASS"
            if result["passed"]
            else "FAIL"
        )

        print(
            marker,
            "|",
            result["control_area"],
            "|",
            result["scenario"],
        )

    print()
    print("Evidence artifact:", OUTPUT_FILE)

    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
