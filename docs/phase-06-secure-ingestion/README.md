# Phase 6 — Secure Ingestion

## Goal

Understand why enterprise RAG systems must evaluate source trust before content enters the retrieval corpus.

## Core Principle

> Retrieval security begins before retrieval.

If malicious or untrusted content is allowed into the knowledge base, later semantic retrieval may faithfully retrieve poisoned instructions.

## Learning Objectives

By the end of this phase, you should be able to explain:

- source trust;
- provenance;
- ingestion allowlists;
- classification validation;
- indirect prompt injection;
- quarantine;
- deterministic ingestion policy;
- why retrieved content must be treated as untrusted data.

## Secure Ingestion Flow

```text
Source
  ↓
Metadata Validation
  ↓
Trust Evaluation
  ↓
Content Inspection
  ↓
Policy Decision
  ├── ACCEPT
  ├── QUARANTINE
  └── REJECT
Important Boundary

An ingestion control does not replace retrieval authorization.

Likewise, retrieval authorization does not replace ingestion security.

Secure RAG requires both.
