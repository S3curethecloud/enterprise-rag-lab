"""Demonstrate blocking when generation invents a source."""

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
    / "source_integrity_block.json"
)


def main():
    context = {
        "included_chunks": [
            {
                "document_id": "approved-doc-001",
                "chunk_id": "approved-doc-001::chunk::0000",
            }
        ]
    }

    generation = {
        "status": "grounded",
        "answer": "This answer claims to use an invented source.",
        "sources": [
            {
                "document_id": "invented-doc-999",
                "chunk_id": "invented-doc-999::chunk::0000",
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
    print(
        "Source integrity:",
        response["source_integrity_valid"],
    )
    print(
        "Reasons:",
        response["reasons"],
    )
    print()
    print("Evidence artifact:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
