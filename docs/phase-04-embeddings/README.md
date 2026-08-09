# Phase 4 — Embeddings

## Goal

Understand how text is transformed into numeric vectors that capture semantic relationships, and understand the security limitations of embeddings.

## Core Secure RAG Principle

> Semantic similarity is not authorization.

An embedding can help determine whether content is relevant to a question.

An embedding cannot determine whether the requesting identity is permitted to access that content.

## Learning Objectives

By the end of this phase, you should be able to explain:

- what an embedding is;
- what a vector is;
- what embedding dimensions represent conceptually;
- semantic similarity;
- cosine similarity;
- embedding normalization;
- how questions and documents can be represented in the same vector space;
- why similar wording is not required for semantic similarity;
- why embeddings cannot enforce authorization;
- why embedding vectors should remain associated with security metadata.

## Model

This tutorial uses:

```text
sentence-transformers/all-MiniLM-L6-v2

The model runs locally.

Learning Sequence
Understand embeddings.
Understand vector representation.
Understand cosine similarity.
Generate real embeddings.
Compare semantically related sentences.
Compare unrelated sentences.
Embed enterprise chunks.
Preserve chunk identity and security metadata.
Demonstrate relevance versus authorization.
Test embedding behavior.
Explain embedding limitations.
Phase Exit Criteria
 Embedding concepts documented.
 Embedding model loads successfully.
 Vector dimension verified.
 Similarity calculation implemented.
 Related sentences score higher than unrelated sentences.
 Enterprise chunks can be embedded.
 Security metadata remains associated with embedded chunks.
 Relevance versus authorization demonstration completed.
 Embedding artifact generated.
 All tests pass.
