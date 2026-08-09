# Phase 10 — Grounded RAG Generation

## Goal

Generate answers only from validated enterprise context while preserving source attribution and abstaining when the available context does not support the answer.

## Core Secure RAG Principle

> The model may generate language, but it must not manufacture evidence.

## Learning Objectives

By the end of this phase, you should be able to explain:

- grounded generation;
- answer-from-context-only behavior;
- why prompt construction is part of the control plane;
- source citation preservation;
- unsupported-question abstention;
- why model fluency is not evidence;
- why generation must consume validated context rather than raw retrieval results.

## Generation Flow

```text
User Question
      ↓
Secure Retrieval
      ↓
Authorized Results
      ↓
Secure Context Assembly
      ↓
Validated Context Package
      ↓
Grounded Prompt
      ↓
Generation
      ↓
Answer + Sources
Phase Exit Criteria
 deterministic prompt construction implemented;
 validated context is the only evidence source;
 source references are preserved;
 unsupported context leads to abstention;
 no-context generation is blocked;
 mock generation path is fully testable;
 optional live model path is isolated;
 grounding evidence is generated;
 all tests pass.
