"""Demonstrate semantic similarity using real embeddings."""

import json
from pathlib import Path

from enterprise_rag.embeddings.embedder import (
    DEFAULT_MODEL_NAME,
    cosine_similarity,
    embed_text,
)


ROOT = Path(__file__).resolve().parents[3]
OUTPUT_FILE = ROOT / "artifacts" / "phase-04" / "similarity_demo.json"


def main():
    query = "Are dogs allowed in the office?"

    related = (
        "Employees may bring approved pets into designated office areas."
    )

    unrelated = (
        "Production APIs must use approved identity-based authentication."
    )

    query_vector = embed_text(query)
    related_vector = embed_text(related)
    unrelated_vector = embed_text(unrelated)

    related_similarity = cosine_similarity(
        query_vector,
        related_vector,
    )

    unrelated_similarity = cosine_similarity(
        query_vector,
        unrelated_vector,
    )

    result = {
        "model": DEFAULT_MODEL_NAME,
        "embedding_dimension": len(query_vector),
        "query": query,
        "related_sentence": related,
        "unrelated_sentence": unrelated,
        "related_similarity": related_similarity,
        "unrelated_similarity": unrelated_similarity,
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    OUTPUT_FILE.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    print("Embedding model:", DEFAULT_MODEL_NAME)
    print("Dimension:", len(query_vector))
    print()
    print("Query:")
    print(query)
    print()
    print("Related similarity:", round(related_similarity, 4))
    print("Unrelated similarity:", round(unrelated_similarity, 4))
    print()
    print("Artifact:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
