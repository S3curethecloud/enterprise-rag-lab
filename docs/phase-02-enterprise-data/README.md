# Phase 2 — Enterprise Data + Metadata

## Goal

Learn how enterprise documents must be represented before they enter a RAG ingestion pipeline.

This phase intentionally happens before chunking, embeddings, or vector storage.

## Core Question

> What security and trust properties must survive when an enterprise document enters a RAG system?

## Learning Objectives

By the end of this phase, you should be able to explain:

- what an enterprise corpus is;
- why document content alone is insufficient;
- document identity;
- tenant boundaries;
- data classification;
- ownership;
- ACLs and allowed groups;
- provenance;
- trust state;
- freshness;
- why security metadata must travel with future chunks.

## Secure RAG Principle

The source authorization model must not disappear when content is indexed.

A document that is restricted in the source system must not become globally retrievable merely because it has been converted into embeddings.

## Learning Sequence

1. Understand the enterprise corpus.
2. Inspect different document sensitivity levels.
3. Add structured document metadata.
4. Model ACLs and tenant boundaries.
5. Capture provenance.
6. Test metadata integrity.
7. Deliberately examine what happens if metadata is removed.

## Phase Exit Criteria

- [ ] Enterprise corpus exists.
- [ ] Multiple departments are represented.
- [ ] Multiple classifications are represented.
- [ ] Each document has a stable document ID.
- [ ] Each document has tenant metadata.
- [ ] Restricted documents have ACL metadata.
- [ ] Provenance is captured.
- [ ] Metadata validation tests pass.
- [ ] Student can explain why content and authorization metadata must remain associated.

---

## Access-Control Ground Truth

Before implementing vector search, this phase establishes explicit authorization expectations.

See:

```text
04-access-control-matrix.md
data/metadata/identities.json
data/metadata/access_scenarios.json

These fixtures will become the expected security behavior for later Secure RAG retrieval tests.

The important principle is:

A highly relevant document must still be excluded when the requesting identity is not authorized to retrieve it.
