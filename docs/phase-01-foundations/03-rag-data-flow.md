# RAG Data Flow

We will build the RAG system progressively.

## Simplified Data Flow

```text
Enterprise Documents
        │
        ▼
      Chunk
        │
        ▼
      Embed
        │
        ▼
   Vector Store
        │
        │
        │ User Question
        │      │
        │      ▼
        │    Embed
        │      │
        └──────┤
               ▼
         Vector Search
               │
               ▼
        Relevant Chunks
               │
               ▼
        Context Assembly
               │
               ▼
              LLM
               │
               ▼
        Grounded Answer
Two Different Pipelines

It is useful to recognize that RAG contains two major flows.

Ingestion Path
Documents
   ↓
Chunk
   ↓
Embed
   ↓
Index

This prepares enterprise knowledge.

Query Path
Question
   ↓
Embed
   ↓
Retrieve
   ↓
Assemble Context
   ↓
Generate

This answers a user request.

Secure RAG Adds Identity and Trust Boundaries
Identity
   ↓
Authorization
   ↓
Authorized Retrieval
   ↓
Context Validation
   ↓
Model
   ↓
Response Controls

The model appears relatively late in the architecture.

That is intentional.

A mature RAG architecture performs important security and data decisions before the model ever sees enterprise content.
