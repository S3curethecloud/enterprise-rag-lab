# Thin Application Layer

The Flask API should remain an orchestration boundary.

It should not become a second implementation of the Secure RAG pipeline.

## Incorrect Design

```text
Flask route
    ↓
direct ChromaDB query
    ↓
prompt
    ↓
model

This bypasses:

relevance acceptance;
authorization;
context validation;
grounding controls;
response security.
Correct Design
Flask route
    ↓
application query service
    ↓
existing Secure RAG pipeline
    ↓
existing response-security controls
    ↓
HTTP response
Principle

Application integration must preserve control boundaries rather than reimplement them.

Thin orchestration reduces:

duplicated policy logic;
inconsistent authorization;
accidental bypasses;
maintenance drift;
security regression risk.
