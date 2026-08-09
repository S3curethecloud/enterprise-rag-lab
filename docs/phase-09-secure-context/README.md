# Phase 9 — Secure Context Assembly

## Goal

Convert authorized retrieval results into a structured, bounded, provenance-preserving context package for the model.

## Core Secure RAG Principle

> Retrieved content is data, not authority.

A retrieved document may contain text that looks like instructions.

Those instructions must not automatically become part of the model's trusted control plane.

## Learning Objectives

By the end of this phase, you should be able to explain:

- why context assembly is a security boundary;
- why only authorized retrieval results may enter context;
- why provenance must remain attached;
- why context size must be bounded;
- why retrieved text should be separated from trusted instructions;
- how suspicious retrieved instructions can be detected;
- how a deterministic context package can support later generation.

## Context Flow

```text
Semantic Retrieval
      ↓
Relevance Check
      ↓
Authorization Check
      ↓
Authorized Results
      ↓
Context Validation
      ↓
Bounded Context Package
      ↓
LLM
Phase Exit Criteria
 only authorized results can enter context;
 context preserves chunk and document identity;
 context preserves classification and provenance;
 context size is bounded;
 suspicious retrieved instructions are flagged;
 retrieved data is clearly separated from control instructions;
 citations are preserved;
 context evidence is generated;
 all tests pass.
