"""Generate Phase 13 Flask API evidence."""

import json
from pathlib import Path

from enterprise_rag.api.app import (
    create_app,
)


ROOT = Path(__file__).resolve().parents[3]

OUTPUT_FILE = (
    ROOT
    / "artifacts"
    / "phase-13"
    / "api_demo.json"
)


def main():
    app = create_app()

    app.config.update(
        TESTING=True
    )

    client = app.test_client()

    health = client.get(
        "/health"
    )

    bob = client.post(
        "/api/query",
        json={
            "user_id": "bob",
            "question": (
                "What is the executive "
                "compensation policy?"
            ),
        },
    )

    alice = client.post(
        "/api/query",
        json={
            "user_id": "alice",
            "question": (
                "What is the executive "
                "compensation policy?"
            ),
        },
    )

    output = {
        "health": {
            "status_code": health.status_code,
            "body": health.get_json(),
        },
        "bob_hr": {
            "status_code": bob.status_code,
            "body": bob.get_json(),
        },
        "alice_hr": {
            "status_code": alice.status_code,
            "body": alice.get_json(),
        },
    }

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_FILE.write_text(
        json.dumps(
            output,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(
        "Health:",
        health.status_code,
        health.get_json(),
    )

    print()

    print(
        "Bob generation:",
        bob.get_json()[
            "generation"
        ]["status"],
    )

    print(
        "Bob response decision:",
        bob.get_json()[
            "response_security"
        ]["decision"],
    )

    print()

    print(
        "Alice generation:",
        alice.get_json()[
            "generation"
        ]["status"],
    )

    print(
        "Alice authorized results:",
        alice.get_json()[
            "retrieval"
        ]["authorized_result_count"],
    )

    print()

    print(
        "Evidence artifact:",
        OUTPUT_FILE,
    )


if __name__ == "__main__":
    main()
