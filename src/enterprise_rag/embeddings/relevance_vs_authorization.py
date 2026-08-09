"""Demonstrate that semantic relevance is not authorization."""

import json
from pathlib import Path

from enterprise_rag.embeddings.embedder import (
    cosine_similarity,
    embed_text,
)


ROOT = Path(__file__).resolve().parents[3]

EMBEDDED_CHUNKS_FILE = (
    ROOT / "artifacts" / "phase-04" / "embedded_chunks.json"
)

IDENTITIES_FILE = (
    ROOT / "data" / "metadata" / "identities.json"
)

OUTPUT_FILE = (
    ROOT
    / "artifacts"
    / "phase-04"
    / "relevance_vs_authorization.json"
)


def is_authorized(identity: dict, metadata: dict) -> bool:
    if identity["tenant_id"] != metadata["tenant_id"]:
        return False

    return bool(
        set(identity["groups"])
        & set(metadata["allowed_groups"])
    )


def main():
    query = "What is the executive compensation policy?"

    user_id = "alice"

    identities = json.loads(
        IDENTITIES_FILE.read_text(encoding="utf-8")
    )

    identity = next(
        identity
        for identity in identities
        if identity["user_id"] == user_id
    )

    records = json.loads(
        EMBEDDED_CHUNKS_FILE.read_text(encoding="utf-8")
    )

    query_vector = embed_text(query)

    results = []

    for record in records:
        similarity = cosine_similarity(
            query_vector,
            record["embedding"],
        )

        authorized = is_authorized(
            identity,
            record["metadata"],
        )

        results.append(
            {
                "chunk_id": record["chunk_id"],
                "document_id": record["document_id"],
                "similarity": similarity,
                "authorized": authorized,
                "classification": (
                    record["metadata"]["classification"]
                ),
                "allowed_groups": (
                    record["metadata"]["allowed_groups"]
                ),
            }
        )

    results.sort(
        key=lambda item: item["similarity"],
        reverse=True,
    )

    output = {
        "query": query,
        "identity": identity,
        "results": results,
    }

    OUTPUT_FILE.write_text(
        json.dumps(output, indent=2),
        encoding="utf-8",
    )

    print("User:", user_id)
    print("Groups:", identity["groups"])
    print()
    print("Query:")
    print(query)
    print()

    for result in results:
        print(
            result["document_id"],
            "| similarity:",
            round(result["similarity"], 4),
            "| authorized:",
            result["authorized"],
        )


if __name__ == "__main__":
    main()
