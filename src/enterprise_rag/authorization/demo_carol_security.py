"""Demonstrate authorized Security retrieval for Carol."""

import json
from pathlib import Path

from enterprise_rag.authorization.secure_retriever import (
    secure_retrieve,
)


ROOT = Path(__file__).resolve().parents[3]

OUTPUT_FILE = (
    ROOT
    / "artifacts"
    / "phase-08"
    / "carol_security_allowed.json"
)


def main():
    result = secure_retrieve(
        user_id="carol",
        query="How should suspected security incidents be handled?",
        top_k=5,
    )

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_FILE.write_text(
        json.dumps(result, indent=2),
        encoding="utf-8",
    )

    for candidate in result["evaluated_candidates"]:
        print(
            candidate["document_id"],
            "| distance:",
            round(candidate["distance"], 4),
            "| relevant:",
            candidate["relevant"],
            "| authorized:",
            candidate["authorized"],
            "| eligible:",
            candidate["eligible"],
            "| reason:",
            candidate["authorization_reason"],
        )

    print()
    print(
        "Authorized results:",
        result["authorized_result_count"],
    )
    print("Abstain:", result["abstain"])
    print("Evidence artifact:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
