"""Phase 8 identity and ACL-aware retrieval tests."""

import json
from pathlib import Path

import pytest

from enterprise_rag.authorization.authorizer import authorize
from enterprise_rag.authorization.identities import get_identity
from enterprise_rag.authorization.secure_retriever import (
    secure_retrieve,
)


ROOT = Path(__file__).resolve().parents[1]


def test_known_identity_can_be_loaded():
    alice = get_identity("alice")

    assert alice["user_id"] == "alice"
    assert alice["tenant_id"] == "techcorp"
    assert "Engineering" in alice["groups"]


def test_unknown_identity_rejected():
    with pytest.raises(KeyError):
        get_identity("unknown-user")


def test_matching_tenant_and_group_authorized():
    identity = {
        "user_id": "bob",
        "tenant_id": "techcorp",
        "groups": ["HR"],
    }

    metadata = {
        "tenant_id": "techcorp",
        "allowed_groups": ["HR", "Executive"],
    }

    decision = authorize(identity, metadata)

    assert decision.allowed is True
    assert decision.reason == "authorized"
    assert decision.tenant_match is True
    assert decision.group_match is True


def test_group_mismatch_denied():
    identity = {
        "user_id": "alice",
        "tenant_id": "techcorp",
        "groups": ["Engineering"],
    }

    metadata = {
        "tenant_id": "techcorp",
        "allowed_groups": ["HR", "Executive"],
    }

    decision = authorize(identity, metadata)

    assert decision.allowed is False
    assert decision.reason == "group_not_authorized"


def test_tenant_mismatch_denied_even_when_group_matches():
    identity = {
        "user_id": "external-hr",
        "tenant_id": "othercorp",
        "groups": ["HR"],
    }

    metadata = {
        "tenant_id": "techcorp",
        "allowed_groups": ["HR"],
    }

    decision = authorize(identity, metadata)

    assert decision.allowed is False
    assert decision.reason == "tenant_mismatch"
    assert decision.tenant_match is False
    assert decision.group_match is True


def test_resource_without_acl_denied():
    identity = {
        "user_id": "alice",
        "tenant_id": "techcorp",
        "groups": ["Employees"],
    }

    metadata = {
        "tenant_id": "techcorp",
        "allowed_groups": [],
    }

    decision = authorize(identity, metadata)

    assert decision.allowed is False
    assert decision.reason == "no_resource_acl"


def test_alice_cannot_retrieve_hr_compensation():
    result = secure_retrieve(
        user_id="alice",
        query="What is the executive compensation policy?",
        top_k=5,
    )

    hr = next(
        item
        for item in result["evaluated_candidates"]
        if item["document_id"] == "hr-compensation-001"
    )

    assert hr["relevant"] is True
    assert hr["authorized"] is False
    assert hr["eligible"] is False

    assert all(
        item["document_id"] != "hr-compensation-001"
        for item in result["authorized_results"]
    )


def test_bob_can_retrieve_hr_compensation():
    result = secure_retrieve(
        user_id="bob",
        query="What is the executive compensation policy?",
        top_k=5,
    )

    assert any(
        item["document_id"] == "hr-compensation-001"
        and item["eligible"] is True
        for item in result["authorized_results"]
    )


def test_carol_can_retrieve_security_content():
    result = secure_retrieve(
        user_id="carol",
        query="How should suspected security incidents be handled?",
        top_k=5,
    )

    assert any(
        item["document_id"] == "security-ir-001"
        and item["eligible"] is True
        for item in result["authorized_results"]
    )


def test_unauthorized_results_never_enter_authorized_results():
    result = secure_retrieve(
        user_id="alice",
        query="What is the executive compensation policy?",
        top_k=5,
    )

    assert all(
        item["authorized"] is True
        for item in result["authorized_results"]
    )

    assert all(
        item["relevant"] is True
        for item in result["authorized_results"]
    )


def test_alice_hr_denial_evidence_exists():
    path = (
        ROOT
        / "artifacts"
        / "phase-08"
        / "alice_hr_denied.json"
    )

    assert path.is_file()


def test_bob_hr_allow_evidence_exists():
    path = (
        ROOT
        / "artifacts"
        / "phase-08"
        / "bob_hr_allowed.json"
    )

    assert path.is_file()


def test_carol_security_allow_evidence_exists():
    path = (
        ROOT
        / "artifacts"
        / "phase-08"
        / "carol_security_allowed.json"
    )

    assert path.is_file()


def test_alice_hr_evidence_contains_no_hr_context():
    path = (
        ROOT
        / "artifacts"
        / "phase-08"
        / "alice_hr_denied.json"
    )

    evidence = json.loads(
        path.read_text(encoding="utf-8")
    )

    assert all(
        item["document_id"] != "hr-compensation-001"
        for item in evidence["authorized_results"]
    )
