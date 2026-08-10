"""Demonstrate an allowed grounded response."""

import json
from pathlib import Path

from enterprise_rag.generation.service import (
    grounded_generate,
)
from enterprise_rag.response_security.service import (
    secure_response,
)


ROOT = Path(__file__).resolve().parents[3]

OUTPUT_FILE = (
    ROOT
    / "artifacts"
    / "phase-11"
    / "allowed_response.json"
)


def main():
    rag_result = grounded_generate(
        user_id="bob",
        question="What is the executive compensation policy?",
    )

    response = secure_response(
        generation=rag_result["generation"],
        context_package=rag_result["context"],
    )

    output = {
        "user_id": "bob",
        "question": rag_result["question"],
        "response_security": response,
    }

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_FILE.write_text(
        json.dumps(output, indent=2),
        encoding="utf-8",
    )

    print("Decision:", response["decision"])
    print(
        "Source integrity:",
        response["source_integrity_valid"],
    )
    print(
        "Findings:",
        response["finding_types"],
    )
    print()
    print("Evidence artifact:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
