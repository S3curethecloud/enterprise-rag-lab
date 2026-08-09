# Embeddings Are Not Authorization

This is one of the most important Secure RAG boundaries.

An embedding model may determine that:

```text
Query:
"What is the executive compensation policy?"

HR compensation chunk:
similarity = HIGH

That means:

The content is semantically relevant.

It does not mean:

The user may retrieve it.

Two Independent Questions

Secure retrieval eventually asks:

Question 1

Is this content relevant?

Answered using mechanisms such as:

embeddings;
similarity;
ranking.
Question 2

Is this identity authorized?

Answered using:

identity;
tenant;
ACL;
groups;
roles;
entitlement;
policy.
Wrong Architecture
Question
   ↓
Embedding
   ↓
Vector Search
   ↓
Top-K
   ↓
LLM
Secure Architecture
Identity ----------------┐
                         │
Question                  │
   │                      │
   ▼                      ▼
Embedding          Authorization Context
   │                      │
   └──────────┬───────────┘
              ▼
      Secure Retrieval
              │
              ▼
       Authorized Top-K
              │
              ▼
            Model
Interview-Level Principle

The LLM does not grant access to enterprise data, and neither does the embedding model. Retrieval authorization must be enforced before context reaches the model.
