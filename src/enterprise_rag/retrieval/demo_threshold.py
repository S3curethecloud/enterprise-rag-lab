"""Demonstrate relevance acceptance for a known-good query."""

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
    / "threshold_demo.json"
)


def main():
    query = "Are pets allowed in the office?"

    candidates = retrieve(
        query=query,
        top_k=3,
    )

    accepted = filter_relevant(
        candidates,
        max_distance=DEFAULT_MAX_DISTANCE,
    )

    output = {
        "query": query,
        "max_distance": DEFAULT_MAX_DISTANCE,
        "candidates": candidates,
        "accepted_results": accepted,
        "abstain": len(accepted) == 0,
    }

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_FILE.write_text(
        json.dumps(output, indent=2),
        encoding="utf-8",
    )

    print("Query:", query)
    print("Threshold:", DEFAULT_MAX_DISTANCE)

    for result in candidates:
        print(
            result["document_id"],
            "| distance:",
            round(result["distance"], 4),
            "| accepted:",
            result in accepted,
        )

    print()
    print("Abstain:", len(accepted) == 0)
    print("Evidence artifact:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
