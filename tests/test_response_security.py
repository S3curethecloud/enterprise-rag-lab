"""Phase 11 response-security tests."""

import json
from pathlib import Path

from enterprise_rag.generation.service import (
    grounded_generate,
)
from enterprise_rag.response_security.inspector import (
    inspect_sensitive_content,
)
from enterprise_rag.response_security.policy import (
    evaluate_response,
)
from enterprise_rag.response_security.redactor import (
    redact_findings,
)
from enterprise_rag.response_security.service import (
    secure_response,
)
from enterprise_rag.response_security.source_integrity import (
    validate_sources,
)


ROOT = Path(__file__).resolve().parents[1]


def test_ssn_detected():
    findings = inspect_sensitive_content(
        "SSN: 123-45-6789"
    )

    assert any(
        item["type"] == "ssn"
        for item in findings
    )


def test_normal_text_has_no_findings():
    findings = inspect_sensitive_content(
        "Employees should follow approved policy."
    )

    assert findings == []


def test_sensitive_value_is_redacted():
    text = "SSN: 123-45-6789"

    findings = inspect_sensitive_content(text)

    redacted = redact_findings(
        text,
        findings,
    )

    assert "123-45-6789" not in redacted
    assert "[REDACTED]" in redacted


def test_valid_source_integrity():
    generation = {
        "sources": [
            {
                "document_id": "doc-1",
                "chunk_id": "chunk-1",
            }
        ]
    }

    context = {
        "included_chunks": [
            {
                "document_id": "doc-1",
                "chunk_id": "chunk-1",
            }
        ]
    }

    result = validate_sources(
        generation,
        context,
    )

    assert result["valid"] is True


def test_invented_source_fails_integrity():
    generation = {
        "sources": [
            {
                "document_id": "invented",
                "chunk_id": "invented::0000",
            }
        ]
    }

    context = {
        "included_chunks": [
            {
                "document_id": "real",
                "chunk_id": "real::0000",
            }
        ]
    }

    result = validate_sources(
        generation,
        context,
    )

    assert result["valid"] is False


def test_sensitive_response_requires_redaction():
    generation = {
        "status": "grounded",
        "answer": "Employee SSN is 123-45-6789.",
        "sources": [
            {
                "document_id": "doc",
                "chunk_id": "chunk",
            }
        ],
    }

    context = {
        "included_chunks": [
            {
                "document_id": "doc",
                "chunk_id": "chunk",
            }
        ]
    }

    decision = evaluate_response(
        generation=generation,
        context_package=context,
    )

    assert decision.decision == "redact"


def test_bad_source_blocks_response():
    generation = {
        "status": "grounded",
        "answer": "ordinary answer",
        "sources": [
            {
                "document_id": "fake",
                "chunk_id": "fake::0000",
            }
        ],
    }

    context = {
        "included_chunks": []
    }

    decision = evaluate_response(
        generation=generation,
        context_package=context,
    )

    assert decision.decision == "block"
    assert (
        "source_integrity_failure"
        in decision.reasons
    )


def test_abstention_is_allowed():
    generation = {
        "status": "abstain",
        "answer": "insufficient context",
        "sources": [],
    }

    decision = evaluate_response(
        generation=generation,
        context_package={
            "included_chunks": []
        },
    )

    assert decision.decision == "allow"


def test_bob_grounded_response_is_allowed():
    rag_result = grounded_generate(
        user_id="bob",
        question="What is the executive compensation policy?",
    )

    response = secure_response(
        generation=rag_result["generation"],
        context_package=rag_result["context"],
    )

    assert response["decision"] == "allow"
    assert response["source_integrity_valid"] is True


def test_redaction_demo_exists():
    path = (
        ROOT
        / "artifacts"
        / "phase-11"
        / "redacted_response.json"
    )

    assert path.is_file()


def test_redaction_evidence_contains_no_ssn():
    path = (
        ROOT
        / "artifacts"
        / "phase-11"
        / "redacted_response.json"
    )

    evidence = json.loads(
        path.read_text(encoding="utf-8")
    )

    assert evidence["decision"] == "redact"
    assert "123-45-6789" not in evidence["output_text"]


def test_source_block_demo_exists():
    path = (
        ROOT
        / "artifacts"
        / "phase-11"
        / "source_integrity_block.json"
    )

    assert path.is_file()


def test_source_block_evidence_is_blocked():
    path = (
        ROOT
        / "artifacts"
        / "phase-11"
        / "source_integrity_block.json"
    )

    evidence = json.loads(
        path.read_text(encoding="utf-8")
    )

    assert evidence["decision"] == "block"
    assert evidence["source_integrity_valid"] is False
