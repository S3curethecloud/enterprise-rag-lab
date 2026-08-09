# RAG vs Semantic Search

Semantic search and RAG are related but are not the same system.

## Semantic Search

```text
Question
   │
   ▼
Embedding
   │
   ▼
Vector Search
   │
   ▼
Relevant Documents

The output is retrieved information.

RAG
Question
   │
   ▼
Retrieval
   │
   ▼
Relevant Context
   │
   ▼
Language Model
   │
   ▼
Generated Answer

The output is a generated response grounded in retrieved information.

Example

Question:

Are pets allowed at the office?

Semantic search might return:

employee_handbook.md

Employees may bring approved pets to designated office areas...

RAG may generate:

Yes. Approved pets are allowed in designated office areas.

Source: employee_handbook.md
Important Distinction

A vector database is not RAG.

An embedding model is not RAG.

An LLM is not RAG.

RAG is the architecture that connects retrieval, context assembly, and generation.

Security Distinction

Semantic similarity asks:

Which information best matches this question?

Authorization asks:

Which information may this identity access?

A similarity score cannot replace an ACL.

Knowledge Check

Could a semantic search system retrieve a highly relevant document that the user should not be allowed to see?

Answer: yes.

That problem will become one of the central topics of Secure RAG.
