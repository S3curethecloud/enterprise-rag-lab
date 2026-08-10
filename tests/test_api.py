"""Phase 13 Flask application tests."""

import json
from pathlib import Path

import pytest

from enterprise_rag.api.app import (
    create_app,
)
from enterprise_rag.api.query_service import (
    process_query,
)
from enterprise_rag.api.validation import (
    RequestValidationError,
    validate_query_request,
)


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture()
def client():
    app = create_app()

    app.config.update(
        TESTING=True
    )

    return app.test_client()


def test_health_endpoint(client):
    response = client.get(
        "/health"
    )

    assert response.status_code == 200

    body = response.get_json()

    assert body["status"] == "ok"
    assert body["service"] == "enterprise-rag"


def test_query_request_validation():
    result = validate_query_request(
        {
            "user_id": "bob",
            "question": "test",
        }
    )

    assert result == {
        "user_id": "bob",
        "question": "test",
        "top_k": 5,
    }


def test_missing_user_id_rejected():
    with pytest.raises(
        RequestValidationError
    ):
        validate_query_request(
            {
                "question": "test",
            }
        )


def test_missing_question_rejected():
    with pytest.raises(
        RequestValidationError
    ):
        validate_query_request(
            {
                "user_id": "bob",
            }
        )


def test_invalid_top_k_rejected():
    with pytest.raises(
        RequestValidationError
    ):
        validate_query_request(
            {
                "user_id": "bob",
                "question": "test",
                "top_k": 0,
            }
        )


def test_non_json_request_rejected(client):
    response = client.post(
        "/api/query",
        data="not-json",
        content_type="text/plain",
    )

    assert response.status_code == 400
    assert (
        response.get_json()["error"]
        == "invalid_request"
    )


def test_bob_hr_query_is_grounded(client):
    response = client.post(
        "/api/query",
        json={
            "user_id": "bob",
            "question": (
                "What is the executive "
                "compensation policy?"
            ),
        },
    )

    assert response.status_code == 200

    body = response.get_json()

    assert (
        body["generation"]["status"]
        == "grounded"
    )

    assert (
        body["response_security"][
            "decision"
        ]
        == "allow"
    )


def test_bob_hr_query_preserves_source(client):
    response = client.post(
        "/api/query",
        json={
            "user_id": "bob",
            "question": (
                "What is the executive "
                "compensation policy?"
            ),
        },
    )

    body = response.get_json()

    assert any(
        source["document_id"]
        == "hr-compensation-001"
        for source in body[
            "generation"
        ]["sources"]
    )


def test_alice_hr_query_abstains(client):
    response = client.post(
        "/api/query",
        json={
            "user_id": "alice",
            "question": (
                "What is the executive "
                "compensation policy?"
            ),
        },
    )

    assert response.status_code == 200

    body = response.get_json()

    assert (
        body["generation"]["status"]
        == "abstain"
    )

    assert (
        body["retrieval"][
            "authorized_result_count"
        ]
        == 0
    )


def test_query_service_preserves_response_security():
    result = process_query(
        user_id="bob",
        question=(
            "What is the executive "
            "compensation policy?"
        ),
    )

    assert (
        result["response_security"][
            "source_integrity_valid"
        ]
        is True
    )


def test_api_does_not_return_raw_prompt(client):
    response = client.post(
        "/api/query",
        json={
            "user_id": "bob",
            "question": (
                "What is the executive "
                "compensation policy?"
            ),
        },
    )

    body = response.get_json()

    assert "prompt" not in body


def test_api_returns_structured_response(client):
    response = client.post(
        "/api/query",
        json={
            "user_id": "bob",
            "question": (
                "What is the executive "
                "compensation policy?"
            ),
        },
    )

    body = response.get_json()

    assert {
        "user_id",
        "question",
        "retrieval",
        "context",
        "generation",
        "response_security",
        "answer",
    }.issubset(body)


def test_api_demo_artifact_exists():
    path = (
        ROOT
        / "artifacts"
        / "phase-13"
        / "api_demo.json"
    )

    assert path.is_file()


def test_api_demo_preserves_authorization_boundary():
    path = (
        ROOT
        / "artifacts"
        / "phase-13"
        / "api_demo.json"
    )

    evidence = json.loads(
        path.read_text(
            encoding="utf-8"
        )
    )

    assert (
        evidence["bob_hr"]["body"][
            "generation"
        ]["status"]
        == "grounded"
    )

    assert (
        evidence["alice_hr"]["body"][
            "generation"
        ]["status"]
        == "abstain"
    )

    assert (
        evidence["alice_hr"]["body"][
            "retrieval"
        ]["authorized_result_count"]
        == 0
    )
