# Phase 11 Hands-On Lab

## Objective

Inspect grounded responses before returning them to the caller.

## Exercise 1 — Allow a Clean Grounded Response

Run:

```bash
uv run python -m enterprise_rag.response_security.demo_allow

Expected:

decision = allow
source integrity = true
Exercise 2 — Detect and Redact Sensitive Data

Run:

uv run python -m enterprise_rag.response_security.demo_redaction

The synthetic SSN should not appear in the final output.

Expected:

decision = redact
output contains [REDACTED]
Exercise 3 — Block an Invented Source

Run:

uv run python -m enterprise_rag.response_security.demo_source_block

Expected:

decision = block
source integrity = false
Exercise 4 — Explain the Security Difference

Why are these different?

Unauthorized retrieval

and:

Unsafe response disclosure

Unauthorized retrieval means the system should never have supplied the content to generation.

Unsafe disclosure means the generated response itself violates output policy.

Secure RAG needs controls at both boundaries.

Exercise 5 — Explain Audit Safety

Why should an audit artifact avoid storing the original sensitive value?

Because logging a detected secret or personal identifier can create another copy of the sensitive data.

Student Explanation

Explain:

Why is response security necessary even after secure retrieval and grounded generation?

A strong answer should include output DLP, source integrity, sensitive-value handling, policy enforcement, and audit-safe evidence.
