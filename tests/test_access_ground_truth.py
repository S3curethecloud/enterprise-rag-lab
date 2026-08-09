"""Phase 2 access-control ground-truth validation."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOCUMENTS_FILE = ROOT / "data" / "metadata" / "documents.json"
IDENTITIES_FILE = ROOT / "data" / "metadata" / "identities.json"
SCENARIOS_FILE = ROOT / "data" / "metadata" / "access_scenarios.json"


def load_json(path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def expected_access(identity, document):
    """Evaluate the simple Phase 2 group-based access model."""

    if identity["tenant_id"] != document["tenant_id"]:
        return "deny"

    identity_groups = set(identity["groups"])
    allowed_groups = set(document["allowed_groups"])

    if identity_groups & allowed_groups:
        return "allow"

    return "deny"


def test_identity_fixture_exists():
    assert IDENTITIES_FILE.is_file()


def test_access_scenario_fixture_exists():
    assert SCENARIOS_FILE.is_file()


def test_user_ids_are_unique():
    identities = load_json(IDENTITIES_FILE)
    user_ids = [identity["user_id"] for identity in identities]

    assert len(user_ids) == len(set(user_ids))


def test_every_identity_has_tenant_and_groups():
    identities = load_json(IDENTITIES_FILE)

    for identity in identities:
        assert identity["tenant_id"]
        assert identity["groups"]


def test_access_scenarios_reference_known_entities():
    identities = {
        identity["user_id"]
        for identity in load_json(IDENTITIES_FILE)
    }

    documents = {
        document["document_id"]
        for document in load_json(DOCUMENTS_FILE)
    }

    for scenario in load_json(SCENARIOS_FILE):
        assert scenario["user_id"] in identities
        assert scenario["document_id"] in documents


def test_expected_authorization_ground_truth():
    identities = {
        identity["user_id"]: identity
        for identity in load_json(IDENTITIES_FILE)
    }

    documents = {
        document["document_id"]: document
        for document in load_json(DOCUMENTS_FILE)
    }

    scenarios = load_json(SCENARIOS_FILE)

    for scenario in scenarios:
        actual = expected_access(
            identities[scenario["user_id"]],
            documents[scenario["document_id"]],
        )

        assert actual == scenario["expected"], (
            f"{scenario['scenario_id']}: "
            f"expected {scenario['expected']}, got {actual}"
        )


def test_engineering_cannot_access_hr_compensation():
    identities = {
        identity["user_id"]: identity
        for identity in load_json(IDENTITIES_FILE)
    }

    documents = {
        document["document_id"]: document
        for document in load_json(DOCUMENTS_FILE)
    }

    assert expected_access(
        identities["alice"],
        documents["hr-compensation-001"],
    ) == "deny"


def test_security_document_remains_security_only():
    identities = {
        identity["user_id"]: identity
        for identity in load_json(IDENTITIES_FILE)
    }

    documents = {
        document["document_id"]: document
        for document in load_json(DOCUMENTS_FILE)
    }

    assert expected_access(
        identities["carol"],
        documents["security-ir-001"],
    ) == "allow"

    assert expected_access(
        identities["erin"],
        documents["security-ir-001"],
    ) == "deny"
