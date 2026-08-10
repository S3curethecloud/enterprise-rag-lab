"""Phase 14 enterprise architecture review tests."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC_ROOT = (
    ROOT
    / "docs"
    / "phase-14-enterprise-architecture"
)


def test_phase_14_overview_exists():
    assert (
        DOC_ROOT
        / "README.md"
    ).is_file()


def test_reference_architecture_exists():
    assert (
        DOC_ROOT
        / "01-reference-architecture.md"
    ).is_file()


def test_ingestion_query_plane_doc_exists():
    assert (
        DOC_ROOT
        / "02-ingestion-vs-query-plane.md"
    ).is_file()


def test_trust_boundary_doc_exists():
    assert (
        DOC_ROOT
        / "03-trust-boundaries.md"
    ).is_file()


def test_identity_authorization_doc_exists():
    assert (
        DOC_ROOT
        / "04-identity-and-authorization.md"
    ).is_file()


def test_control_map_exists():
    assert (
        DOC_ROOT
        / "05-control-points.md"
    ).is_file()


def test_threat_model_exists():
    assert (
        DOC_ROOT
        / "06-threat-model.md"
    ).is_file()


def test_observability_doc_exists():
    assert (
        DOC_ROOT
        / "07-observability-and-evidence.md"
    ).is_file()


def test_production_gap_doc_exists():
    assert (
        DOC_ROOT
        / "08-production-readiness-gaps.md"
    ).is_file()


def test_control_ownership_doc_exists():
    assert (
        DOC_ROOT
        / "09-control-ownership.md"
    ).is_file()


def test_architecture_checklist_exists():
    assert (
        DOC_ROOT
        / "10-architecture-checklist.md"
    ).is_file()


def test_capstone_exists():
    assert (
        DOC_ROOT
        / "CAPSTONE.md"
    ).is_file()


def test_core_rule_is_documented():
    content = (
        DOC_ROOT
        / "01-reference-architecture.md"
    ).read_text(
        encoding="utf-8"
    )

    assert (
        "The LLM never grants access to enterprise data."
        in content
    )

    assert (
        "Authorization occurs before retrieved context reaches the model."
        in content
    )


def test_architecture_artifact_exists():
    path = (
        ROOT
        / "artifacts"
        / "phase-14"
        / "architecture_summary.json"
    )

    assert path.is_file()


def test_architecture_artifact_has_both_planes():
    path = (
        ROOT
        / "artifacts"
        / "phase-14"
        / "architecture_summary.json"
    )

    artifact = json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )

    assert "ingestion" in artifact["planes"]
    assert "query" in artifact["planes"]


def test_authorization_precedes_generation_in_artifact():
    path = (
        ROOT
        / "artifacts"
        / "phase-14"
        / "architecture_summary.json"
    )

    artifact = json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )

    query_plane = artifact["planes"]["query"]

    authorization_index = query_plane.index(
        "acl_authorization"
    )

    generation_index = query_plane.index(
        "grounded_generation"
    )

    assert authorization_index < generation_index


def test_response_security_is_last_query_control():
    path = (
        ROOT
        / "artifacts"
        / "phase-14"
        / "architecture_summary.json"
    )

    artifact = json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )

    assert (
        artifact["planes"]["query"][-1]
        == "response_security"
    )
