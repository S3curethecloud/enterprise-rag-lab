"""Demonstrate that relevant HR content is denied to Alice."""

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
    / "alice_hr_denied.json"
)


def main():
    result = secure_retrieve(
        user_id="alice",
        query="What is the executive compensation policy?",
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

    print("User:", result["identity"]["user_id"])
    print("Groups:", result["identity"]["groups"])
    print("Query:", result["query"])
    print()

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
