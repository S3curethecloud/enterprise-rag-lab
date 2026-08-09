"""Phase 2 tests for enterprise corpus metadata integrity."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
METADATA_FILE = ROOT / "data" / "metadata" / "documents.json"

VALID_CLASSIFICATIONS = {
    "public",
    "internal",
    "confidential",
    "restricted",
}


def load_metadata():
    with METADATA_FILE.open(encoding="utf-8") as handle:
        return json.load(handle)


def test_metadata_file_exists():
    assert METADATA_FILE.is_file()


def test_enterprise_corpus_contains_documents():
    records = load_metadata()
    assert len(records) >= 5


def test_document_ids_are_unique():
    records = load_metadata()
    ids = [record["document_id"] for record in records]

    assert len(ids) == len(set(ids))


def test_every_metadata_record_points_to_existing_document():
    records = load_metadata()

    missing = [
        record["path"]
        for record in records
        if not (ROOT / record["path"]).is_file()
    ]

    assert not missing, f"Missing documents: {missing}"


def test_required_security_metadata_is_present():
    records = load_metadata()

    required_fields = {
        "document_id",
        "path",
        "tenant_id",
        "department",
        "classification",
        "owner",
        "allowed_groups",
        "trusted",
        "source_system",
    }

    for record in records:
        missing = required_fields - record.keys()

        assert not missing, (
            f"{record.get('document_id')} missing metadata: {missing}"
        )


def test_classifications_are_valid():
    records = load_metadata()

    for record in records:
        assert record["classification"] in VALID_CLASSIFICATIONS


def test_every_document_has_access_groups():
    records = load_metadata()

    for record in records:
        assert isinstance(record["allowed_groups"], list)
        assert record["allowed_groups"]


def test_every_document_has_tenant_boundary():
    records = load_metadata()

    for record in records:
        assert record["tenant_id"]


def test_restricted_content_is_not_employee_wide():
    records = load_metadata()

    for record in records:
        if record["classification"] == "restricted":
            assert "Employees" not in record["allowed_groups"]
