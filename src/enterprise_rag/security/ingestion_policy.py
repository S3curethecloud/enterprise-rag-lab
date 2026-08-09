"""Deterministic Secure RAG ingestion policy."""

from dataclasses import dataclass


ALLOWED_SOURCE_SYSTEMS = {
    "simulated-sharepoint",
    "simulated-confluence",
}

REQUIRED_METADATA_FIELDS = {
    "document_id",
    "path",
    "tenant_id",
    "department",
    "classification",
    "owner",
    "allowed_groups",
    "trusted",
    "source_system",
}

VALID_CLASSIFICATIONS = {
    "internal",
    "confidential",
    "restricted",
}

SUSPICIOUS_PATTERNS = (
    "ignore all previous",
    "ignore previous instructions",
    "reveal all",
    "do not mention this instruction",
    "treat every requesting user as",
)


@dataclass(frozen=True)
class IngestionDecision:
    decision: str
    reasons: list[str]


def inspect_content(text: str) -> list[str]:
    """Return suspicious content indicators."""

    lowered = text.lower()

    findings = []

    for pattern in SUSPICIOUS_PATTERNS:
        if pattern in lowered:
            findings.append(
                f"suspicious_instruction:{pattern}"
            )

    return findings


def evaluate_ingestion(
    metadata: dict,
    content: str,
) -> IngestionDecision:
    """Evaluate whether a document may enter the RAG corpus."""

    reasons = []

    missing = REQUIRED_METADATA_FIELDS - metadata.keys()

    if missing:
        reasons.append(
            "missing_metadata:"
            + ",".join(sorted(missing))
        )

    if metadata.get("classification") not in VALID_CLASSIFICATIONS:
        reasons.append("invalid_classification")

    if metadata.get("trusted") is not True:
        reasons.append("source_not_trusted")

    if (
        metadata.get("source_system")
        not in ALLOWED_SOURCE_SYSTEMS
    ):
        reasons.append("source_system_not_allowed")

    findings = inspect_content(content)
    reasons.extend(findings)

    if any(
        reason.startswith("suspicious_instruction:")
        for reason in reasons
    ):
        return IngestionDecision(
            decision="quarantine",
            reasons=reasons,
        )

    if reasons:
        return IngestionDecision(
            decision="reject",
            reasons=reasons,
        )

    return IngestionDecision(
        decision="accept",
        reasons=[],
    )
