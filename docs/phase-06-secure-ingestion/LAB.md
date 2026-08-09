# Phase 6 Hands-On Lab

## Objective

Evaluate trusted and malicious documents before allowing them into the RAG knowledge base.

## Exercise 1 — Inspect the Poisoned Document

Run:

```bash
cat data/poisoned/fake_security_runbook.md

Identify instructions that are attempting to control a future AI assistant.

Exercise 2 — Evaluate Sources

Run:

uv run python -m enterprise_rag.security.evaluate_sources

Observe:

trusted enterprise documents are accepted;
the malicious document is quarantined.
Exercise 3 — Explain the Difference

Why is this statement dangerous?

If we trust the vector database, we can trust everything inside it.

Answer:

The vector database stores what the ingestion pipeline permits.

It does not independently establish source trust.

Exercise 4 — Identify the Security Signals

For the poisoned document, identify:

trusted = false;
unknown source system;
suspicious embedded instructions;
restricted classification;
unknown owner.
Exercise 5 — Explain Quarantine

Why quarantine rather than silently discard suspicious content?

A quarantine path can support:

security review;
forensic analysis;
audit evidence;
false-positive investigation;
controlled remediation.
Student Explanation

Explain:

Why must enterprise RAG treat retrieved content as data rather than trusted instructions?

A strong answer should mention indirect prompt injection, source trust, provenance, instruction/data separation, and defense-in-depth.
