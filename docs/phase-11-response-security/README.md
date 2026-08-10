# Phase 11 — Response Security

## Goal

Inspect grounded RAG responses before they are returned to the caller.

## Core Secure RAG Principle

> A grounded answer can still be unsafe to disclose.

Grounding establishes evidence lineage.

It does not automatically establish that every generated detail is appropriate to return.

## Learning Objectives

By the end of this phase, you should be able to explain:

- response security;
- output DLP;
- source integrity;
- classification-aware handling;
- ALLOW, REDACT, and BLOCK decisions;
- why response inspection is separate from retrieval authorization;
- why audit evidence matters.

## Response Flow

```text
Grounded Generation
        ↓
Response Inspection
        ↓
Policy Decision
   ├── ALLOW
   ├── REDACT
   └── BLOCK
        ↓
Caller
Phase Exit Criteria
 response inspection is implemented;
 sensitive patterns can be detected;
 classification context is preserved;
 source integrity can be checked;
 ALLOW, REDACT, and BLOCK paths exist;
 redaction evidence is generated;
 response decisions are auditable;
 all tests pass.
