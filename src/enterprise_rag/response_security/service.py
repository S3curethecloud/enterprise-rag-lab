"""Secure response processing for Phase 11."""

from enterprise_rag.response_security.policy import (
    evaluate_response,
)
from enterprise_rag.response_security.redactor import (
    redact_findings,
)


BLOCK_MESSAGE = (
    "The generated response was blocked by response-security policy."
)


def secure_response(
    *,
    generation: dict,
    context_package: dict,
) -> dict:
    """Apply response-security policy."""

    decision = evaluate_response(
        generation=generation,
        context_package=context_package,
    )

    answer = generation.get(
        "answer",
        "",
    )

    if decision.decision == "block":
        output_text = BLOCK_MESSAGE

    elif decision.decision == "redact":
        output_text = redact_findings(
            answer,
            decision.findings,
        )

    else:
        output_text = answer

    return {
        "decision": decision.decision,
        "reasons": decision.reasons,
        "source_integrity_valid": (
            decision.source_integrity_valid
        ),
        "finding_types": [
            finding["type"]
            for finding in decision.findings
        ],
        "output_text": output_text,
    }
