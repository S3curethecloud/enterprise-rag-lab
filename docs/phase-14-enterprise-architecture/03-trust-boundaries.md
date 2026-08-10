# Trust Boundaries

A trust boundary exists whenever data moves between components with different security assumptions.

## Boundary 1 — External or Enterprise Source to Ingestion

```text
source content
     ↓
INGESTION TRUST BOUNDARY
     ↓
knowledge system

Controls:

source allowlist;
trust metadata;
required metadata;
classification;
prompt-injection inspection;
quarantine.
Boundary 2 — Vector Retrieval to Authorization
semantic candidates
       ↓
AUTHORIZATION BOUNDARY
       ↓
authorized candidates

This is one of the most important boundaries in the system.

Vector similarity does not confer access.

Boundary 3 — Authorized Results to Model Context
authorized retrieval
       ↓
CONTEXT SECURITY BOUNDARY
       ↓
LLM context

Controls:

relevance confirmation;
trusted-source confirmation;
suspicious-content inspection;
provenance preservation;
context size limits.
Boundary 4 — LLM Output to Caller
generated response
       ↓
RESPONSE SECURITY BOUNDARY
       ↓
caller

Controls:

DLP;
source-integrity validation;
allow/redact/block policy;
audit-safe evidence.
Boundary 5 — HTTP Request to Application
caller
   ↓
APPLICATION BOUNDARY
   ↓
Secure RAG orchestration

Controls:

request validation;
identity propagation;
safe errors;
structured responses.
Principle

Security controls should be placed at trust transitions, not assumed to exist implicitly inside the model.
