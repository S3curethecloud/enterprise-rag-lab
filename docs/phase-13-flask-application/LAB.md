# Phase 13 Hands-On Lab

## Objective

Expose the Secure RAG pipeline through Flask while preserving all existing security boundaries.

## Exercise 1 — Generate API Evidence

Run:

```bash
uv run python -m enterprise_rag.api.demo_api

Verify:

health = 200

Bob + HR
→ grounded
→ response allow

Alice + HR
→ authorized results = 0
→ abstain
Exercise 2 — Inspect API Evidence

Run:

cat artifacts/phase-13/api_demo.json

Confirm that Bob receives an authorized HR source.

Confirm that Alice does not receive HR context.

Exercise 3 — Run the Flask API

Run:

uv run python -m enterprise_rag.api.run

In another terminal:

curl http://127.0.0.1:5000/health

Then:

curl \
  -X POST \
  http://127.0.0.1:5000/api/query \
  -H 'Content-Type: application/json' \
  -d '{
    "user_id": "bob",
    "question": "What is the executive compensation policy?"
  }'

Stop the development server when finished.

Exercise 4 — Test Unauthorized Access

Send the same HR question as Alice.

Expected:

generation.status = abstain
retrieval.authorized_result_count = 0

The HTTP API must not create a shortcut around authorization.

Exercise 5 — Explain the Boundary

Why should Flask not directly query ChromaDB?

Because doing so could bypass:

relevance acceptance;
identity-aware authorization;
context validation;
grounded-generation rules;
response-security enforcement.
Student Explanation

Explain:

Why should an application layer orchestrate security controls rather than duplicate them?

A strong answer should mention policy consistency, separation of concerns, bypass prevention, maintainability, testing, and auditability.
