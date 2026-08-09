# Phase 5 Hands-On Lab

## Objective

Persist enterprise vectors and then deliberately demonstrate why raw vector retrieval is not a security boundary.

## Exercise 1 — Verify Persistence

Run:

```bash
uv run python -m enterprise_rag.vectorstore.init_chroma

Confirm:

Collection: techcorp_docs
Current record count: 5

The collection survives Python process termination.

Exercise 2 — Inspect a Confidential Record

Run:

uv run python -m enterprise_rag.vectorstore.inspect_chroma

Verify that the HR compensation chunk retains:

tenant_id = techcorp
classification = confidential
allowed_groups = HR, Executive
owner = Human Resources

This proves that security metadata survived:

Document
   ↓
Chunk
   ↓
Embedding
   ↓
Vector Store
Exercise 3 — Run Raw Vector Retrieval

Run:

uv run python -m enterprise_rag.vectorstore.raw_search

The query is:

What is the executive compensation policy?

Observe which chunk ranks first.

The HR compensation record should be the strongest retrieval candidate.

Important

This is semantically correct.

It is not necessarily authorized.

No user identity or authorization filter is used by this experiment.

Exercise 4 — Inspect the Security Failure

The raw query may return records classified as:

confidential
restricted
internal

in one result set.

Why?

Because semantic ranking does not understand enterprise entitlement.

The vector database is answering:

Which vectors are closest?

It is not answering:

Which records may this identity retrieve?

Exercise 5 — Distance vs Similarity

Phase 4 calculated cosine similarity directly.

Higher similarity indicated stronger semantic relationship.

Chroma returns a distance value for this query path.

For distance:

smaller = closer

Do not treat a similarity score and a distance value as interchangeable metrics.

Exercise 6 — Explain the Failure

Explain why this architecture is incomplete:

Question
   ↓
Embedding
   ↓
Vector Database
   ↓
Top-K
   ↓
LLM

A strong answer should mention:

no authenticated identity;
no tenant boundary;
no ACL filtering;
no entitlement evaluation;
no classification policy;
semantic relevance is being mistaken for permission.
Secure RAG Takeaway

The vector database provides retrieval capability. It does not grant enterprise data access.

Later, the Secure Retrieval phase will combine identity and authorization context with semantic retrieval before any chunk reaches the model.
