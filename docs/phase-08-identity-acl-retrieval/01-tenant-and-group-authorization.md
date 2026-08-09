# Tenant and Group Authorization

Secure retrieval requires more than semantic relevance.

A retrieval object must pass both tenant and ACL checks.

## Decision Model

```text
Identity
├── tenant_id
└── groups

Resource
├── tenant_id
└── allowed_groups

Authorization requires:

identity.tenant_id == resource.tenant_id

and at least one identity group must intersect the resource ACL.

Example
Identity:
tenant = othercorp
groups = HR

Resource:
tenant = techcorp
allowed_groups = HR, Executive

Even though the group matches:

HR == HR

authorization must still fail because:

othercorp != techcorp
Principle

Tenant isolation takes precedence over group similarity.

A matching role or group name must never authorize access across tenant boundaries.
