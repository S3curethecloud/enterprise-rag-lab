"""Phase 7 semantic retrieval tests."""

import json
from pathlib import Path

import pytest

from enterprise_rag.retrieval.relevance import (
    filter_relevant,
    is_relevant,
)
from enterprise_rag.retrieval.semantic_retriever import retrieve


ROOT = Path(__file__).resolve().parents[1]


def test_pet_query_ranks_general_faq_first():
    results = retrieve(
        "Are pets allowed in the office?",
        top_k=3,
    )

    assert results
    assert results[0]["document_id"] == "general-faq-001"


def test_retrieval_preserves_metadata():
    results = retrieve(
        "What are the architecture authentication standards?",
        top_k=3,
    )

    assert results

    for result in results:
        assert "tenant_id" in result["metadata"]
        assert "classification" in result["metadata"]
        assert "allowed_groups" in result["metadata"]


def test_top_k_limits_results():
    results = retrieve(
        "Tell me about remote work.",
        top_k=2,
    )

    assert len(results) == 2


def test_top_k_larger_than_collection_is_safe():
    results = retrieve(
        "Tell me about company policy.",
        top_k=100,
    )

    assert len(results) == 5


def test_empty_query_rejected():
    with pytest.raises(ValueError):
        retrieve("", top_k=3)


def test_invalid_top_k_rejected():
    with pytest.raises(ValueError):
        retrieve("test", top_k=0)


def test_relevance_threshold_accepts_close_result():
    assert is_relevant(
        distance=0.8,
        max_distance=1.2,
    )


def test_relevance_threshold_rejects_weak_result():
    assert not is_relevant(
        distance=1.8,
        max_distance=1.2,
    )


def test_filter_relevant_removes_weak_results():
    results = [
        {"distance": 0.8},
        {"distance": 1.4},
        {"distance": 1.9},
    ]

    accepted = filter_relevant(
        results,
        max_distance=1.2,
    )

    assert accepted == [
        {"distance": 0.8},
    ]


def test_negative_distance_rejected():
    with pytest.raises(ValueError):
        is_relevant(-0.1)


def test_retrieval_demo_artifact_exists():
    path = (
        ROOT
        / "artifacts"
        / "phase-07"
        / "retrieval_demo.json"
    )

    assert path.is_file()


def test_threshold_demo_artifact_exists():
    path = (
        ROOT
        / "artifacts"
        / "phase-07"
        / "threshold_demo.json"
    )

    assert path.is_file()


def test_weak_retrieval_demo_artifact_exists():
    path = (
        ROOT
        / "artifacts"
        / "phase-07"
        / "weak_retrieval_demo.json"
    )

    assert path.is_file()


def test_pet_demo_accepts_general_faq():
    path = (
        ROOT
        / "artifacts"
        / "phase-07"
        / "threshold_demo.json"
    )

    evidence = json.loads(
        path.read_text(encoding="utf-8")
    )

    assert evidence["accepted_results"]
    assert (
        evidence["accepted_results"][0]["document_id"]
        == "general-faq-001"
    )


def test_weak_query_abstains():
    path = (
        ROOT
        / "artifacts"
        / "phase-07"
        / "weak_retrieval_demo.json"
    )

    evidence = json.loads(
        path.read_text(encoding="utf-8")
    )

    assert evidence["candidate_count"] == 3
    assert evidence["accepted_count"] == 0
    assert evidence["abstain"] is True

    assert all(
        candidate["distance"]
        > evidence["max_distance"]
        for candidate in evidence["candidates"]
    )
