"""Demonstrate reusable semantic retrieval."""

import json
from pathlib import Path

from enterprise_rag.retrieval.semantic_retriever import retrieve


ROOT = Path(__file__).resolve().parents[3]

OUTPUT_FILE = (
    ROOT
    / "artifacts"
    / "phase-07"
    / "retrieval_demo.json"
)


def main():
    query = "Are pets allowed in the office?"

    results = retrieve(
        query=query,
        top_k=3,
    )

    output = {
        "query": query,
        "top_k": 3,
        "results": results,
    }

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_FILE.write_text(
        json.dumps(output, indent=2),
        encoding="utf-8",
    )

    print("Query:")
    print(query)
    print()

    for result in results:
        print(
            "Rank:",
            result["rank"],
            "| Document:",
            result["document_id"],
            "| Distance:",
            round(result["distance"], 4),
        )

    print()
    print("Evidence artifact:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
