# Identity Propagation

The Phase 13 API accepts a simulated user_id.

This is an educational identity input, not production authentication.

## Current Flow

```text
HTTP request
    ↓
user_id
    ↓
Secure RAG identity loader
    ↓
tenant + group claims
    ↓
retrieval authorization

The API does not convert the supplied user_id into authorization decisions itself.

It propagates identity into the existing authorization path.

Production Difference

A production implementation would normally derive identity from a trusted authentication mechanism such as:

OIDC;
OAuth 2.0;
SAML;
enterprise SSO;
workload identity.

The caller should not be allowed to freely claim another user's identity.

That authentication boundary is intentionally outside Phase 13.

Principle

Authentication establishes who the caller is. Authorization determines what that identity may access.

Phase 13 demonstrates propagation, not production authentication.
