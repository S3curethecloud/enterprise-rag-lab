"""Demonstrate output DLP redaction."""

import json
from pathlib import Path

from enterprise_rag.response_security.service import (
    secure_response,
)


ROOT = Path(__file__).resolve().parents[3]

OUTPUT_FILE = (
    ROOT
    / "artifacts"
    / "phase-11"
    / "redacted_response.json"
)


def main():
    context = {
        "included_chunks": [
            {
                "document_id": "synthetic-hr-001",
                "chunk_id": "synthetic-hr-001::chunk::0000",
            }
        ]
    }

    generation = {
        "status": "grounded",
        "answer": (
            "The employee record contains SSN "
            "123-45-6789 and must be handled securely."
        ),
        "sources": [
            {
                "document_id": "synthetic-hr-001",
                "chunk_id": "synthetic-hr-001::chunk::0000",
            }
        ],
    }

    response = secure_response(
        generation=generation,
        context_package=context,
    )

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_FILE.write_text(
        json.dumps(response, indent=2),
        encoding="utf-8",
    )

    print("Decision:", response["decision"])
    print("Findings:", response["finding_types"])
    print("Output:")
    print(response["output_text"])
    print()
    print("Evidence artifact:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
