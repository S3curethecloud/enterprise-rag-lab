# Phase 3 — Chunking

## Goal

Understand why enterprise documents are divided into smaller retrieval units and how source security properties must survive that transformation.

## Core Secure RAG Principle

> Chunking may divide content, but it must never divide away authorization, classification, tenant, or provenance information.

## Learning Objectives

By the end of this phase, you should be able to explain:

- why chunking exists;
- chunk size;
- overlap;
- stride;
- context loss at chunk boundaries;
- deterministic chunk identity;
- parent-document relationships;
- metadata inheritance;
- security implications of chunking.

## Learning Sequence

1. Why chunking exists.
2. Chunk size and retrieval granularity.
3. Overlap and stride.
4. Security metadata inheritance.
5. Build a deterministic chunker.
6. Inspect generated chunks.
7. Break metadata inheritance deliberately.
8. Test chunk security integrity.

## Phase Exit Criteria

- [ ] Chunking concepts explained.
- [ ] Chunk size and overlap are defined consistently.
- [ ] Deterministic chunk IDs are generated.
- [ ] Parent document ID survives chunking.
- [ ] Tenant metadata survives chunking.
- [ ] Classification survives chunking.
- [ ] ACL metadata survives chunking.
- [ ] Provenance/source metadata survives chunking.
- [ ] Chunk statistics artifact generated.
- [ ] All tests pass.
