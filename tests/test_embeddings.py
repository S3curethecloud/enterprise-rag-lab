"""Phase 4 embedding and security-association tests."""

import json
from pathlib import Path

import pytest

from enterprise_rag.embeddings.embedder import (
    cosine_similarity,
    embed_text,
    get_model,
)


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def query_vector():
    return embed_text("Are dogs allowed in the office?")


def test_embedding_model_loads():
    model = get_model()
    assert model is not None


def test_embedding_dimension_is_384(query_vector):
    assert len(query_vector) == 384


def test_embedding_contains_numeric_values(query_vector):
    assert query_vector
    assert all(
        isinstance(value, float)
        for value in query_vector
    )


def test_same_text_has_high_similarity():
    first = embed_text("Employees may work remotely.")
    second = embed_text("Employees may work remotely.")

    similarity = cosine_similarity(first, second)

    assert similarity > 0.99


def test_semantically_related_text_scores_higher():
    query = embed_text(
        "Are dogs allowed in the office?"
    )

    related = embed_text(
        "Employees may bring approved pets "
        "into designated office areas."
    )

    unrelated = embed_text(
        "Production APIs must use approved authentication."
    )

    assert (
        cosine_similarity(query, related)
        >
        cosine_similarity(query, unrelated)
    )


def test_empty_text_rejected():
    with pytest.raises(ValueError):
        embed_text("")


def test_mismatched_vector_dimensions_rejected():
    with pytest.raises(ValueError):
        cosine_similarity(
            [1.0, 2.0],
            [1.0, 2.0, 3.0],
        )


def test_similarity_demo_artifact_exists():
    path = (
        ROOT
        / "artifacts"
        / "phase-04"
        / "similarity_demo.json"
    )

    assert path.is_file()


def test_embedded_chunks_artifact_exists():
    path = (
        ROOT
        / "artifacts"
        / "phase-04"
        / "embedded_chunks.json"
    )

    assert path.is_file()


def test_enterprise_embeddings_are_384_dimensions():
    path = (
        ROOT
        / "artifacts"
        / "phase-04"
        / "embedded_chunks.json"
    )

    records = json.loads(
        path.read_text(encoding="utf-8")
    )

    assert records

    for record in records:
        assert len(record["embedding"]) == 384


def test_embedded_chunks_preserve_security_metadata():
    path = (
        ROOT
        / "artifacts"
        / "phase-04"
        / "embedded_chunks.json"
    )

    records = json.loads(
        path.read_text(encoding="utf-8")
    )

    required_fields = {
        "tenant_id",
        "classification",
        "allowed_groups",
        "owner",
        "trusted",
        "source_system",
    }

    for record in records:
        missing = (
            required_fields
            - record["metadata"].keys()
        )

        assert not missing


def test_relevance_authorization_artifact_exists():
    path = (
        ROOT
        / "artifacts"
        / "phase-04"
        / "relevance_vs_authorization.json"
    )

    assert path.is_file()


def test_alice_is_not_authorized_for_hr_compensation():
    path = (
        ROOT
        / "artifacts"
        / "phase-04"
        / "relevance_vs_authorization.json"
    )

    result = json.loads(
        path.read_text(encoding="utf-8")
    )

    hr_result = next(
        item
        for item in result["results"]
        if item["document_id"] == "hr-compensation-001"
    )

    assert hr_result["authorized"] is False
