"""Deterministic sensitive-value redaction."""

REDACTION_TOKEN = "[REDACTED]"


def redact_findings(
    text: str,
    findings: list[dict],
) -> str:
    """Redact sensitive findings without exposing original values."""

    if not findings:
        return text

    ordered = sorted(
        findings,
        key=lambda item: item["start"],
        reverse=True,
    )

    redacted = text

    for finding in ordered:
        redacted = (
            redacted[: finding["start"]]
            + REDACTION_TOKEN
            + redacted[finding["end"] :]
        )

    return redacted
