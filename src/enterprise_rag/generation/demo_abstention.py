"""Demonstrate grounded abstention when no authorized context exists."""

import json
from pathlib import Path

from enterprise_rag.generation.service import (
    grounded_generate,
)


ROOT = Path(__file__).resolve().parents[3]

OUTPUT_FILE = (
    ROOT
    / "artifacts"
    / "phase-10"
    / "abstention_demo.json"
)


def main():
    result = grounded_generate(
        user_id="alice",
        question="What is the executive compensation policy?",
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
    print("Question:", result["question"])
    print(
        "Authorized results:",
        result["retrieval"]["authorized_result_count"],
    )
    print(
        "Context chunks:",
        result["context"]["included_count"],
    )
    print(
        "Generation status:",
        result["generation"]["status"],
    )
    print()
    print(result["generation"]["answer"])
    print()
    print("Evidence artifact:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
