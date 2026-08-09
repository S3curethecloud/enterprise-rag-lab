"""Identity fixture loading for Phase 8."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]

IDENTITIES_FILE = (
    ROOT
    / "data"
    / "metadata"
    / "identities.json"
)


def load_identities() -> list[dict]:
    """Load the Phase 2 identity fixtures."""

    return json.loads(
        IDENTITIES_FILE.read_text(
            encoding="utf-8"
        )
    )


def get_identity(user_id: str) -> dict:
    """Return one identity by user_id."""

    identities = load_identities()

    for identity in identities:
        if identity["user_id"] == user_id:
            return identity

    raise KeyError(
        f"unknown user_id: {user_id}"
    )
