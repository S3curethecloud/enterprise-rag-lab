# Phase 14 Hands-On Architecture Review

## Objective

Review the complete Secure RAG system as an enterprise architecture rather than as individual Python modules.

## Exercise 1 — Trace an Authorized Request

Trace:

```text
Bob
→ executive compensation question
→ semantic retrieval
→ HR result
→ relevance accepted
→ tenant match
→ HR group authorized
→ secure context
→ grounded generation
→ response security
→ allow

Explain every control boundary.

Exercise 2 — Trace an Unauthorized Request

Trace:

Alice
→ executive compensation question
→ HR result semantically relevant
→ authorization denied
→ HR context excluded
→ generation abstains

Explain why the LLM never receives the confidential HR content.

Exercise 3 — Trace a Poisoned Document

Trace:

untrusted document
→ ingestion inspection
→ suspicious instructions
→ quarantine

Then explain why context validation still exists as defense in depth.

Exercise 4 — Trace an Unsafe Response

Trace:

grounded answer
→ SSN detected
→ response policy
→ redact
→ caller receives [REDACTED]
Exercise 5 — Review the Threat Model

Read:

cat docs/phase-14-enterprise-architecture/06-threat-model.md

For each threat, identify:

asset;
attacker action;
control;
expected behavior.
Exercise 6 — Review Production Gaps

Read:

cat docs/phase-14-enterprise-architecture/08-production-readiness-gaps.md

Identify which tutorial components would need replacement or strengthening before production deployment.

Exercise 7 — Architecture Checklist

Review:

cat docs/phase-14-enterprise-architecture/10-architecture-checklist.md

Explain why each control exists.

Exercise 8 — Final Rule

Explain this statement without referring to source code:

The LLM never grants access to enterprise data. Authorization occurs before retrieved context reaches the model.

Final Student Challenge

Draw the complete architecture from memory.

Your diagram should include:

source trust
metadata
chunking
embeddings
vector storage
identity
retrieval
relevance
authorization
context validation
generation
response security
evaluation
application boundary

If you can explain where trust changes and where policy is enforced, you understand the architecture rather than merely the implementation.
