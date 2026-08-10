"""Phase 12 Secure RAG evaluation harness tests."""

import json
from pathlib import Path

from enterprise_rag.evaluation.scenarios import (
    SCENARIOS,
)


ROOT = Path(__file__).resolve().parents[1]


def test_evaluation_has_multiple_control_areas():
    results = [
        scenario()
        for scenario in SCENARIOS
    ]

    control_areas = {
        result.control_area
        for result in results
    }

    assert {
        "retrieval",
        "authorization",
        "secure_ingestion",
        "context_security",
        "grounded_generation",
        "response_security",
    }.issubset(control_areas)


def test_all_current_evaluation_scenarios_pass():
    results = [
        scenario()
        for scenario in SCENARIOS
    ]

    failures = [
        result.scenario
        for result in results
        if not result.passed
    ]

    assert failures == []


def test_alice_hr_scenario_exists():
    names = {
        scenario().scenario
        for scenario in SCENARIOS
    }

    assert "alice_hr_access_denied" in names


def test_poisoned_content_scenario_exists():
    names = {
        scenario().scenario
        for scenario in SCENARIOS
    }

    assert "poisoned_content_quarantined" in names


def test_weak_query_scenario_exists():
    names = {
        scenario().scenario
        for scenario in SCENARIOS
    }

    assert "weak_query_abstains" in names


def test_malicious_context_scenario_exists():
    names = {
        scenario().scenario
        for scenario in SCENARIOS
    }

    assert "malicious_context_rejected" in names


def test_dlp_scenario_exists():
    names = {
        scenario().scenario
        for scenario in SCENARIOS
    }

    assert "output_dlp_redacts_ssn" in names


def test_source_integrity_scenario_exists():
    names = {
        scenario().scenario
        for scenario in SCENARIOS
    }

    assert "invented_source_blocked" in names


def test_evaluation_report_exists():
    path = (
        ROOT
        / "artifacts"
        / "phase-12"
        / "evaluation_report.json"
    )

    assert path.is_file()


def test_evaluation_report_has_zero_failures():
    path = (
        ROOT
        / "artifacts"
        / "phase-12"
        / "evaluation_report.json"
    )

    report = json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )

    assert report["summary"]["failed"] == 0
    assert report["summary"]["pass_rate"] == 1.0


def test_evaluation_report_has_expected_fields():
    path = (
        ROOT
        / "artifacts"
        / "phase-12"
        / "evaluation_report.json"
    )

    report = json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )

    for result in report["results"]:
        assert {
            "scenario",
            "control_area",
            "expected",
            "actual",
            "passed",
            "evidence",
        }.issubset(result)


def test_markdown_evaluation_report_exists():
    path = (
        ROOT
        / "artifacts"
        / "phase-12"
        / "evaluation_report.md"
    )

    assert path.is_file()
