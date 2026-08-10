"""Application-layer Secure RAG orchestration."""

from enterprise_rag.generation.service import (
    grounded_generate,
)
from enterprise_rag.response_security.service import (
    secure_response,
)


def process_query(
    *,
    user_id: str,
    question: str,
    top_k: int = 5,
) -> dict:
    """Run the existing Secure RAG controls."""

    rag_result = grounded_generate(
        user_id=user_id,
        question=question,
        top_k=top_k,
    )

    secured = secure_response(
        generation=rag_result["generation"],
        context_package=rag_result["context"],
    )

    return {
        "user_id": rag_result["identity"]["user_id"],
        "question": question,
        "retrieval": {
            "authorized_result_count": (
                rag_result["retrieval"][
                    "authorized_result_count"
                ]
            ),
        },
        "context": {
            "included_count": (
                rag_result["context"][
                    "included_count"
                ]
            ),
            "rejected_count": (
                rag_result["context"][
                    "rejected_count"
                ]
            ),
        },
        "generation": {
            "status": (
                rag_result["generation"][
                    "status"
                ]
            ),
            "sources": (
                rag_result["generation"][
                    "sources"
                ]
            ),
        },
        "response_security": {
            "decision": secured["decision"],
            "reasons": secured["reasons"],
            "source_integrity_valid": (
                secured[
                    "source_integrity_valid"
                ]
            ),
            "finding_types": (
                secured["finding_types"]
            ),
        },
        "answer": secured["output_text"],
    }
