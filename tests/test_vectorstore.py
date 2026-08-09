"""Phase 5 ChromaDB persistence and metadata tests."""

from enterprise_rag.vectorstore.init_chroma import (
    COLLECTION_NAME,
    get_collection,
)
from enterprise_rag.vectorstore.metadata import (
    deserialize_metadata,
    serialize_metadata,
)


def test_collection_exists():
    collection = get_collection()

    assert collection.name == COLLECTION_NAME


def test_collection_contains_enterprise_chunks():
    collection = get_collection()

    assert collection.count() == 5


def test_metadata_serialization_round_trip():
    original = {
        "tenant_id": "techcorp",
        "classification": "confidential",
        "allowed_groups": ["HR", "Executive"],
        "trusted": True,
    }

    restored = deserialize_metadata(
        serialize_metadata(original)
    )

    assert restored == original


def test_hr_chunk_exists():
    collection = get_collection()

    result = collection.get(
        ids=["hr-compensation-001::chunk::0000"],
        include=["metadatas"],
    )

    assert result["ids"] == [
        "hr-compensation-001::chunk::0000"
    ]


def test_hr_chunk_security_metadata_survived():
    collection = get_collection()

    result = collection.get(
        ids=["hr-compensation-001::chunk::0000"],
        include=["metadatas"],
    )

    metadata = deserialize_metadata(
        result["metadatas"][0]
    )

    assert metadata["tenant_id"] == "techcorp"
    assert metadata["classification"] == "confidential"
    assert metadata["allowed_groups"] == [
        "HR",
        "Executive",
    ]
    assert metadata["owner"] == "Human Resources"


def test_security_chunk_remains_restricted():
    collection = get_collection()

    result = collection.get(
        ids=["security-ir-001::chunk::0000"],
        include=["metadatas"],
    )

    metadata = deserialize_metadata(
        result["metadatas"][0]
    )

    assert metadata["classification"] == "restricted"
    assert metadata["allowed_groups"] == ["Security"]


def test_persisted_documents_are_present():
    collection = get_collection()

    result = collection.get(
        include=["documents"]
    )

    assert len(result["documents"]) == 5
    assert all(result["documents"])


def test_raw_search_evidence_demonstrates_unfiltered_retrieval():
    """Phase 5 intentionally proves raw vector search is not authorization."""

    import json
    from pathlib import Path

    root = Path(__file__).resolve().parents[1]

    evidence_file = (
        root
        / "artifacts"
        / "phase-05"
        / "raw_unfiltered_search.json"
    )

    assert evidence_file.is_file()

    evidence = json.loads(
        evidence_file.read_text(encoding="utf-8")
    )

    assert evidence["authorization_filter_applied"] is False

    top_result = evidence["results"][0]

    assert top_result["chunk_id"] == (
        "hr-compensation-001::chunk::0000"
    )

    assert (
        top_result["metadata"]["classification"]
        == "confidential"
    )

    assert top_result["metadata"]["allowed_groups"] == [
        "HR",
        "Executive",
    ]
