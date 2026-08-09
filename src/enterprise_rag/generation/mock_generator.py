"""Deterministic mock grounded generator for Phase 10."""

ABSTAIN_MESSAGE = (
    "I do not have sufficient authorized enterprise context "
    "to answer that question."
)


def generate_mock_answer(
    *,
    question: str,
    context_package: dict,
) -> dict:
    """Generate a deterministic answer from validated context."""

    chunks = context_package.get(
        "included_chunks",
        []
    )

    if not chunks:
        return {
            "status": "abstain",
            "answer": ABSTAIN_MESSAGE,
            "sources": [],
        }

    first = chunks[0]

    source = {
        "document_id": first["document_id"],
        "chunk_id": first["chunk_id"],
        "source_path": first["source_path"],
        "owner": first["owner"],
    }

    answer = (
        "Based on the authorized enterprise context: "
        + first["content"].strip()
    )

    return {
        "status": "grounded",
        "answer": answer,
        "sources": [source],
    }
