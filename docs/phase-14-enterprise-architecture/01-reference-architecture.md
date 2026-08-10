# Secure RAG Reference Architecture

## Architectural Rule

> The LLM never grants access to enterprise data. Authorization occurs before retrieved context reaches the model.

This rule defines the security boundary of the entire system.

The model does not decide:

- which tenant a user belongs to;
- which enterprise documents exist;
- which documents a caller may retrieve;
- whether a user belongs to an allowed group;
- whether restricted content may enter context.

Those decisions occur before generation.

## End-to-End Architecture

```text
                    ENTERPRISE DATA SOURCES
                             │
                             ▼
                    INGESTION TRUST GATE
                             │
                ┌────────────┼────────────┐
                │            │            │
                ▼            ▼            ▼
            provenance  classification  trust checks
                │            │            │
                └────────────┼────────────┘
                             ▼
                    CONTENT INSPECTION
                             │
                  accept / reject / quarantine
                             │
                             ▼
                       CHUNKING
                             │
                  security metadata inherited
                             │
                             ▼
                       EMBEDDINGS
                             │
                             ▼
                       VECTOR STORE
                             │
──────────────────────── QUERY PLANE ────────────────────────
                             │
                             ▼
                        USER QUERY
                             │
                             ▼
                    IDENTITY PROPAGATION
                             │
                             ▼
                    SEMANTIC RETRIEVAL
                             │
                             ▼
                    RELEVANCE ACCEPTANCE
                             │
                             ▼
                 TENANT + ACL AUTHORIZATION
                             │
                             ▼
                  AUTHORIZED RESULTS ONLY
                             │
                             ▼
                 SECURE CONTEXT VALIDATION
                             │
                             ▼
                  BOUNDED CONTEXT ASSEMBLY
                             │
                             ▼
                    GROUNDED GENERATION
                             │
                             ▼
                     RESPONSE SECURITY
                  DLP / source integrity
                  allow / redact / block
                             │
                             ▼
                          CALLER
Why the Order Matters

The order of controls is part of the security design.

Semantic retrieval may identify a highly relevant restricted document.

That does not imply the caller is entitled to receive it.

Therefore:

semantic relevance
      !=
authorization

Authorization is evaluated before content enters the generation context.

Trust Invariant

The model receives only context that has already passed:

retrieval
→ relevance
→ authorization
→ context validation

The LLM is downstream of access-control enforcement.

It is not an access-control engine.
