# Phase 7 — Semantic Retrieval

## Goal

Understand how semantic retrieval ranks enterprise chunks and how to determine whether retrieved content is relevant enough to use.

## Core Principle

> Ranking is not the same as relevance acceptance.

A vector database can always return nearest neighbors.

Those neighbors may still be poor matches.

## Learning Objectives

By the end of this phase, you should be able to explain:

- query embeddings;
- nearest-neighbor retrieval;
- top-k;
- distance ranking;
- retrieval candidates;
- relevance thresholds;
- false-positive retrieval;
- why weak retrieval should lead to abstention;
- why metadata must remain attached to retrieved chunks.

## Security Boundary

This phase does not implement user authorization.

That arrives in Phase 8.

Phase 7 asks only:

> Is this chunk semantically relevant?

Phase 8 will additionally ask:

> Is this identity allowed to retrieve it?
