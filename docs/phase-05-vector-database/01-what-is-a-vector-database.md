# What Is a Vector Database?

A vector database is optimized for storing and searching numeric vector representations.

In RAG, those vectors usually represent document chunks.

## Simplified Model

```text
Chunk Text
    │
    ▼
Embedding Model
    │
    ▼
Vector
    │
    ▼
Vector Database

That model is incomplete for enterprise Secure RAG.

The real retrieval object is closer to:

Retrieval Record
├── chunk_id
├── document_id
├── content
├── embedding
├── tenant_id
├── classification
├── allowed_groups
├── owner
├── trust state
└── provenance

The vector enables semantic retrieval.

The metadata enables security and governance decisions.

ChromaDB Collection

This tutorial uses one persistent collection:

techcorp_docs

The collection stores enterprise chunks.

Important Distinction

A vector database answers:

Which stored vectors are closest to this query vector?

It does not automatically answer:

Is this user allowed to retrieve those records?

That authorization logic belongs to the Secure RAG retrieval layer.
