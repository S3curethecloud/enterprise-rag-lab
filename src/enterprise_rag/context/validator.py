"""Secure context validation for Phase 9."""

from enterprise_rag.security.ingestion_policy import inspect_content


def validate_context_candidate(candidate: dict) -> dict:
    """Validate one authorized retrieval object before context assembly."""

    metadata = candidate.get("metadata", {})
    content = candidate.get("content", "")

    findings = []

    if candidate.get("authorized") is not True:
        findings.append("not_authorized")

    if candidate.get("relevant") is not True:
        findings.append("not_relevant")

    if metadata.get("trusted") is not True:
        findings.append("source_not_trusted")

    required_metadata = {
        "document_id",
        "tenant_id",
        "classification",
        "allowed_groups",
        "owner",
        "source_system",
    }

    missing = required_metadata - metadata.keys()

    if missing:
        findings.append(
            "missing_metadata:"
            + ",".join(sorted(missing))
        )

    suspicious = inspect_content(content)

    findings.extend(suspicious)

    return {
        "valid": len(findings) == 0,
        "findings": findings,
    }
