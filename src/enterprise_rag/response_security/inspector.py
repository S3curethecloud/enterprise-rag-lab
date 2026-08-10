"""Deterministic response inspection for Phase 11."""

import re


SENSITIVE_PATTERNS = {
    "ssn": re.compile(
        r"\b\d{3}-\d{2}-\d{4}\b"
    ),
    "credit_card": re.compile(
        r"\b(?:\d[ -]*?){13,16}\b"
    ),
    "api_key_like": re.compile(
        r"\b(?:sk|api)[-_][A-Za-z0-9]{12,}\b",
        re.IGNORECASE,
    ),
}


def inspect_sensitive_content(text: str) -> list[dict]:
    """Return sensitive-pattern findings."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    findings = []

    for finding_type, pattern in SENSITIVE_PATTERNS.items():
        for match in pattern.finditer(text):
            findings.append(
                {
                    "type": finding_type,
                    "value": match.group(0),
                    "start": match.start(),
                    "end": match.end(),
                }
            )

    return findings
