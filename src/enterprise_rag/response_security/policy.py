"""Response-security policy decisions for Phase 11."""

from dataclasses import dataclass

from enterprise_rag.response_security.inspector import (
    inspect_sensitive_content,
)
from enterprise_rag.response_security.source_integrity import (
    validate_sources,
)


@dataclass(frozen=True)
class ResponseDecision:
    decision: str
    reasons: list[str]
    findings: list[dict]
    source_integrity_valid: bool


def evaluate_response(
    *,
    generation: dict,
    context_package: dict,
) -> ResponseDecision:
    """Evaluate a grounded response before disclosure."""

    if generation.get("status") == "abstain":
        return ResponseDecision(
            decision="allow",
            reasons=["abstention_response"],
            findings=[],
            source_integrity_valid=True,
        )

    answer = generation.get("answer", "")

    findings = inspect_sensitive_content(
        answer
    )

    source_check = validate_sources(
        generation,
        context_package,
    )

    reasons = []

    if not source_check["valid"]:
        reasons.append(
            "source_integrity_failure"
        )

    if findings:
        reasons.append(
            "sensitive_content_detected"
        )

    if not source_check["valid"]:
        return ResponseDecision(
            decision="block",
            reasons=reasons,
            findings=findings,
            source_integrity_valid=False,
        )

    if findings:
        return ResponseDecision(
            decision="redact",
            reasons=reasons,
            findings=findings,
            source_integrity_valid=True,
        )

    return ResponseDecision(
        decision="allow",
        reasons=[],
        findings=[],
        source_integrity_valid=True,
    )
