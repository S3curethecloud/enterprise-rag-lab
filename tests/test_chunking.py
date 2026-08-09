"""Phase 3 chunking and metadata-inheritance tests."""

import json
from pathlib import Path

import pytest

from enterprise_rag.ingestion.chunker import (
    chunk_text,
    validate_chunk_parameters,
)


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def metadata():
    return {
        "document_id": "hr-compensation-001",
        "tenant_id": "techcorp",
        "department": "hr",
        "classification": "confidential",
        "owner": "Human Resources",
        "allowed_groups": ["HR", "Executive"],
        "trusted": True,
        "source_system": "simulated-sharepoint",
    }


def test_stride_behavior(metadata):
    text = "A" * 1200

    chunks = chunk_text(
        text,
        document_metadata=metadata,
        chunk_size=500,
        overlap=100,
    )

    assert chunks[0]["start_char"] == 0
    assert chunks[1]["start_char"] == 400
    assert chunks[2]["start_char"] == 800


def test_chunk_length_does_not_exceed_chunk_size(metadata):
    text = "A" * 1200

    chunks = chunk_text(
        text,
        document_metadata=metadata,
        chunk_size=500,
        overlap=100,
    )

    assert all(len(chunk["content"]) <= 500 for chunk in chunks)


def test_chunk_ids_are_deterministic(metadata):
    text = "A" * 800

    first = chunk_text(text, document_metadata=metadata)
    second = chunk_text(text, document_metadata=metadata)

    assert [chunk["chunk_id"] for chunk in first] == [
        chunk["chunk_id"] for chunk in second
    ]


def test_parent_document_id_survives(metadata):
    chunks = chunk_text(
        "A" * 800,
        document_metadata=metadata,
    )

    assert all(
        chunk["document_id"] == "hr-compensation-001"
        for chunk in chunks
    )


def test_tenant_metadata_survives_chunking(metadata):
    chunks = chunk_text(
        "A" * 800,
        document_metadata=metadata,
    )

    assert all(
        chunk["metadata"]["tenant_id"] == "techcorp"
        for chunk in chunks
    )


def test_classification_survives_chunking(metadata):
    chunks = chunk_text(
        "A" * 800,
        document_metadata=metadata,
    )

    assert all(
        chunk["metadata"]["classification"] == "confidential"
        for chunk in chunks
    )


def test_acl_survives_chunking(metadata):
    chunks = chunk_text(
        "A" * 800,
        document_metadata=metadata,
    )

    assert all(
        chunk["metadata"]["allowed_groups"] == ["HR", "Executive"]
        for chunk in chunks
    )


def test_chunk_metadata_is_independent(metadata):
    chunks = chunk_text(
        "A" * 800,
        document_metadata=metadata,
    )

    chunks[0]["metadata"]["allowed_groups"].append("Engineering")

    assert "Engineering" not in chunks[1]["metadata"]["allowed_groups"]


def test_empty_text_returns_no_chunks(metadata):
    assert chunk_text("", document_metadata=metadata) == []


def test_invalid_zero_chunk_size_rejected():
    with pytest.raises(ValueError):
        validate_chunk_parameters(0, 0)


def test_overlap_equal_to_chunk_size_rejected():
    with pytest.raises(ValueError):
        validate_chunk_parameters(500, 500)


def test_negative_overlap_rejected():
    with pytest.raises(ValueError):
        validate_chunk_parameters(500, -1)


def test_phase_two_metadata_can_be_chunked():
    metadata_file = ROOT / "data" / "metadata" / "documents.json"

    records = json.loads(metadata_file.read_text(encoding="utf-8"))

    for record in records:
        text = (ROOT / record["path"]).read_text(encoding="utf-8")
        chunks = chunk_text(text, document_metadata=record)

        assert chunks

        for chunk in chunks:
            assert chunk["metadata"]["tenant_id"] == record["tenant_id"]
            assert (
                chunk["metadata"]["classification"]
                == record["classification"]
            )
            assert (
                chunk["metadata"]["allowed_groups"]
                == record["allowed_groups"]
            )


def test_generated_chunk_artifact_exists():
    chunk_file = ROOT / "artifacts" / "phase-03" / "chunks.json"
    assert chunk_file.is_file()


def test_generated_chunks_preserve_security_metadata():
    chunk_file = ROOT / "artifacts" / "phase-03" / "chunks.json"

    chunks = json.loads(
        chunk_file.read_text(encoding="utf-8")
    )

    required_metadata = {
        "document_id",
        "tenant_id",
        "department",
        "classification",
        "owner",
        "allowed_groups",
        "trusted",
        "source_system",
    }

    assert chunks

    for chunk in chunks:
        metadata = chunk["metadata"]

        missing = required_metadata - metadata.keys()

        assert not missing, (
            f"{chunk['chunk_id']} missing security metadata: {missing}"
        )


def test_generated_chunks_match_parent_security_properties():
    documents = json.loads(
        (ROOT / "data" / "metadata" / "documents.json").read_text(
            encoding="utf-8"
        )
    )

    chunks = json.loads(
        (
            ROOT
            / "artifacts"
            / "phase-03"
            / "chunks.json"
        ).read_text(encoding="utf-8")
    )

    parents = {
        document["document_id"]: document
        for document in documents
    }

    security_fields = {
        "tenant_id",
        "department",
        "classification",
        "owner",
        "allowed_groups",
        "trusted",
        "source_system",
    }

    for chunk in chunks:
        parent = parents[chunk["document_id"]]

        for field in security_fields:
            assert chunk["metadata"][field] == parent[field], (
                f"{chunk['chunk_id']} changed parent field {field}"
            )
