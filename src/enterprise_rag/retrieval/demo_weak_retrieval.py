"""Demonstrate that nearest-neighbor retrieval may still be irrelevant."""

import json
from pathlib import Path

from enterprise_rag.retrieval.relevance import (
    DEFAULT_MAX_DISTANCE,
    filter_relevant,
)
from enterprise_rag.retrieval.semantic_retriever import retrieve


ROOT = Path(__file__).resolve().parents[3]

OUTPUT_FILE = (
    ROOT
    / "artifacts"
    / "phase-07"
    / "weak_retrieval_demo.json"
)


def main():
    query = "How do I configure a Kubernetes GPU scheduler?"

    results = retrieve(
        query=query,
        top_k=3,
    )

    accepted = filter_relevant(
        results,
        max_distance=DEFAULT_MAX_DISTANCE,
    )

    output = {
        "query": query,
        "top_k": 3,
        "max_distance": DEFAULT_MAX_DISTANCE,
        "candidate_count": len(results),
        "accepted_count": len(accepted),
        "abstain": len(accepted) == 0,
        "candidates": results,
        "accepted_results": accepted,
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

    print("Candidates:")

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
    print("Threshold:", DEFAULT_MAX_DISTANCE)
    print("Accepted:", len(accepted))
    print("Abstain:", len(accepted) == 0)
    print()
    print("Evidence artifact:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
