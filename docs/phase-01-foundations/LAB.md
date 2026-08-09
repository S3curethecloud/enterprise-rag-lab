# Phase 1 Hands-On Lab

## Objective

Establish the local development environment and demonstrate understanding of the RAG architecture before building retrieval infrastructure.

## Exercise 1 — Identify the RAG Stages

Write down what responsibility belongs to each stage:

```text
Retrieve
Augment
Generate

Do not reference product names such as ChromaDB or OpenAI.

The goal is to understand architectural responsibility independently of implementation technology.

Exercise 2 — Identify the Security Boundary

Consider:

Alice
group = Engineering

The knowledge system contains:

architecture_standards.md
allowed_groups = Engineering

executive_compensation.md
allowed_groups = HR

Alice asks:

What is the executive compensation policy?

Assume the compensation document has extremely high semantic similarity.

Questions:

Should the document be retrieved?
Should the LLM see its contents?
Which component should enforce this decision?
Why can't semantic similarity make the decision?

Expected principle:

Semantic similarity is not authorization.

Exercise 3 — Environment Verification

Run:

uv --version
uv run python --version
uv run pytest -v

All tests must pass.

Exercise 4 — Explain Secure RAG

Without looking at the documentation, explain this flow:

Identity
   ↓
Authorization
   ↓
Retrieval
   ↓
Context Validation
   ↓
Model
   ↓
Response Controls
Phase Completion

Do not proceed until you can explain:

why RAG exists;
retrieval versus generation;
semantic search versus RAG;
why the model is not an authorization system;
why authorization precedes model context.
