"""Deterministic authorization controls for Phase 8."""

from dataclasses import dataclass


@dataclass(frozen=True)
class AuthorizationDecision:
    allowed: bool
    reason: str
    tenant_match: bool
    group_match: bool


def authorize(
    identity: dict,
    metadata: dict,
) -> AuthorizationDecision:
    """Authorize one identity against one retrieval record."""

    identity_tenant = identity.get("tenant_id")
    resource_tenant = metadata.get("tenant_id")

    tenant_match = (
        bool(identity_tenant)
        and bool(resource_tenant)
        and identity_tenant == resource_tenant
    )

    identity_groups = set(identity.get("groups", []))
    allowed_groups = set(metadata.get("allowed_groups", []))

    group_match = bool(
        identity_groups
        & allowed_groups
    )

    if not tenant_match:
        return AuthorizationDecision(
            allowed=False,
            reason="tenant_mismatch",
            tenant_match=False,
            group_match=group_match,
        )

    if not allowed_groups:
        return AuthorizationDecision(
            allowed=False,
            reason="no_resource_acl",
            tenant_match=True,
            group_match=False,
        )

    if not group_match:
        return AuthorizationDecision(
            allowed=False,
            reason="group_not_authorized",
            tenant_match=True,
            group_match=False,
        )

    return AuthorizationDecision(
        allowed=True,
        reason="authorized",
        tenant_match=True,
        group_match=True,
    )
