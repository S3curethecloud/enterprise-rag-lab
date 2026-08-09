# Phase 8 — Identity + ACL-Aware Retrieval

## Goal

Combine semantic relevance with identity-aware authorization before retrieved content can become model context.

## Core Secure RAG Principle

> The LLM does not grant data access.

Authorization must be enforced before retrieved content reaches the model.

## Learning Objectives

By the end of this phase, you should be able to explain:

- authenticated identity context;
- tenant boundaries;
- group-based ACLs;
- authorization decisions;
- deny-by-default behavior;
- semantic relevance versus entitlement;
- why unauthorized relevant content must be removed before context assembly.

## Retrieval Decision Model

```text
Semantic Candidate
      ↓
Relevant?
      ↓
Authorized?
      ↓
Eligible Context

A chunk must pass both relevance and authorization.

Phase Exit Criteria
 identities can be loaded;
 tenant mismatches are denied;
 group mismatches are denied;
 allowed groups are honored;
 secure retrieval filters unauthorized chunks;
 Alice cannot retrieve HR compensation;
 Bob can retrieve HR compensation;
 Carol can retrieve Security content;
 authorization evidence is generated;
 all tests pass.
