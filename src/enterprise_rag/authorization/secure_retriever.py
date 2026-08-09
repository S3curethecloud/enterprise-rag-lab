"""Identity-aware Secure RAG retrieval for Phase 8."""

from enterprise_rag.authorization.authorizer import authorize
from enterprise_rag.authorization.identities import get_identity
from enterprise_rag.retrieval.relevance import (
    DEFAULT_MAX_DISTANCE,
    is_relevant,
)
from enterprise_rag.retrieval.semantic_retriever import retrieve


def secure_retrieve(
    *,
    user_id: str,
    query: str,
    top_k: int = 5,
    max_distance: float = DEFAULT_MAX_DISTANCE,
) -> dict:
    """Retrieve candidates and enforce relevance plus authorization."""

    identity = get_identity(user_id)

    candidates = retrieve(
        query=query,
        top_k=top_k,
    )

    evaluated = []
    authorized_results = []

    for candidate in candidates:
        relevant = is_relevant(
            candidate["distance"],
            max_distance=max_distance,
        )

        decision = authorize(
            identity,
            candidate["metadata"],
        )

        eligible = (
            relevant
            and decision.allowed
        )

        evaluated_record = {
            **candidate,
            "relevant": relevant,
            "authorized": decision.allowed,
            "authorization_reason": decision.reason,
            "tenant_match": decision.tenant_match,
            "group_match": decision.group_match,
            "eligible": eligible,
        }

        evaluated.append(
            evaluated_record
        )

        if eligible:
            authorized_results.append(
                evaluated_record
            )

    return {
        "identity": identity,
        "query": query,
        "max_distance": max_distance,
        "candidate_count": len(candidates),
        "authorized_result_count": len(
            authorized_results
        ),
        "abstain": len(authorized_results) == 0,
        "evaluated_candidates": evaluated,
        "authorized_results": authorized_results,
    }
