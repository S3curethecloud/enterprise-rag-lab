"""Evaluate trusted and poisoned documents against ingestion policy."""

import json
from pathlib import Path

from enterprise_rag.security.ingestion_policy import (
    evaluate_ingestion,
)


ROOT = Path(__file__).resolve().parents[3]

TRUSTED_METADATA = (
    ROOT / "data" / "metadata" / "documents.json"
)

POISONED_METADATA = (
    ROOT / "data" / "poisoned" / "metadata.json"
)

OUTPUT_FILE = (
    ROOT
    / "artifacts"
    / "phase-06"
    / "ingestion_decisions.json"
)


def load_json(path: Path):
    return json.loads(
        path.read_text(encoding="utf-8")
    )


def evaluate_records(records: list[dict]) -> list[dict]:
    results = []

    for metadata in records:
        document_path = ROOT / metadata["path"]

        content = document_path.read_text(
            encoding="utf-8"
        )

        decision = evaluate_ingestion(
            metadata,
            content,
        )

        results.append(
            {
                "document_id": metadata["document_id"],
                "decision": decision.decision,
                "reasons": decision.reasons,
                "trusted": metadata["trusted"],
                "source_system": metadata["source_system"],
            }
        )

    return results


def main():
    trusted_records = load_json(TRUSTED_METADATA)
    poisoned_records = load_json(POISONED_METADATA)

    results = (
        evaluate_records(trusted_records)
        + evaluate_records(poisoned_records)
    )

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_FILE.write_text(
        json.dumps(results, indent=2),
        encoding="utf-8",
    )

    for result in results:
        print(
            result["document_id"],
            "|",
            result["decision"],
            "|",
            result["reasons"],
        )

    print()
    print("Evidence artifact:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
