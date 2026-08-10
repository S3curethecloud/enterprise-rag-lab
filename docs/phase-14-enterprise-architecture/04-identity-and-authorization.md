# Identity and Authorization Architecture

## Identity Flow

The tutorial uses simulated identities with:

- user_id;
- tenant_id;
- group membership.

The query path propagates the identity into retrieval authorization.

```text
user_id
  ↓
identity record
  ↓
tenant
  +
groups
  ↓
authorization decision
Authorization Flow

Each retrieved chunk preserves access metadata from its parent document.

Relevant security metadata includes:

tenant_id;
allowed_groups;
classification;
owner;
source system;
trust state.

Authorization checks:

tenant match?
      ↓
ACL present?
      ↓
group intersection?
      ↓
ALLOW / DENY
Critical Rule

Authorization happens before context reaches the model.

The model never decides whether the caller should see a document.

Production Authentication

The current lab accepts simulated identities.

Production systems should derive identity from trusted mechanisms such as:

OIDC;
OAuth 2.0;
enterprise SSO;
workload identity;
signed identity claims.

A caller should not be able to arbitrarily claim another user's identity.
