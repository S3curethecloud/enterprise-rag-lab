# Phase 4 Hands-On Lab

## Objective

Generate real embeddings, compare semantic similarity, and prove that semantic relevance and authorization are independent decisions.

## Exercise 1 — Generate a Vector

Run:

```bash
uv run python -m enterprise_rag.embeddings.demo_similarity

Observe:

the embedding model;
vector dimension;
related similarity;
unrelated similarity.
Exercise 2 — Explain the Vector

Answer:

What does a 384-dimensional embedding represent?

It is a distributed numeric representation of semantic properties learned by the embedding model.

It is not a list of 384 human-defined business attributes.

Exercise 3 — Compare Meaning

Compare:

Are dogs allowed in the office?

with:

Employees may bring approved pets into designated office areas.

The exact words differ.

The semantic meaning overlaps.

The embedding model should therefore place the representations relatively close together.

Exercise 4 — Embed Enterprise Chunks

Run:

uv run python -m enterprise_rag.embeddings.embed_chunks

Inspect one record.

Confirm that both exist:

embedding vector
+
security metadata
Exercise 5 — Relevance vs Authorization

Run:

uv run python \
  -m enterprise_rag.embeddings.relevance_vs_authorization

Alice belongs to:

Engineering
Employees

She asks about executive compensation.

The HR document may be semantically relevant.

Alice is still unauthorized.

Critical Lesson
semantic similarity
        ≠
authorization

The embedding model is not an access-control engine.

Student Explanation

Explain:

Why embeddings are useful in RAG.
Why exact keywords are not required.
Why a 384-dimensional vector should not be treated as authorization metadata.
Why security metadata remains attached to embedded chunks.
Why the most relevant chunk may still need to be excluded from retrieval.
