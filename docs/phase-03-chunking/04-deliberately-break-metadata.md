# Deliberately Break Chunk Security

Our secure chunker preserves the source document's metadata.

Now we will reason through what happens if a developer does not preserve that metadata.

## Secure Source Document

Consider:

```text
document_id = hr-compensation-001
tenant_id = techcorp
classification = confidential
allowed_groups = HR, Executive

The source document contains:

Executive compensation information is confidential...
Insecure Chunking Design

A weak implementation might create:

chunk = {
    "chunk_id": chunk_id,
    "content": content,
}

This looks harmless.

The text has been chunked successfully.

The future embedding can also be generated successfully.

But the retrieval object no longer knows:

Which tenant owns this content?
What classification does it have?
Who may retrieve it?
Which source document produced it?
Who owns the source?
Is the source trusted?
What Was Lost?

Before chunking:

Document
├── content
├── tenant = techcorp
├── classification = confidential
├── groups = HR, Executive
└── provenance

After insecure chunking:

Chunk
└── content

The transformation silently destroyed the source security model.

Why This Becomes Dangerous Later

Imagine the vector database eventually contains:

Chunk A
"Employees may bring approved pets..."

Chunk B
"Executive compensation information is confidential..."

Chunk C
"Production APIs must use approved authentication..."

If the chunks contain only text and embeddings:

User query
    │
    ▼
Vector Search
    │
    ▼
Most Similar Chunk

there may be no information available at retrieval time to determine whether the requesting user is authorized.

A semantic search could therefore work perfectly while the security architecture fails.

Broken Mental Model
Document ACL
     │
     ▼
Chunking
     │
     X  ACL discarded
     │
     ▼
Embedding
     │
     ▼
Vector Store
Secure Mental Model
Document
├── content
├── tenant
├── classification
├── ACL
└── provenance
       │
       ▼
    Chunking
       │
       ├──────────────┐
       ▼              ▼
    Chunk 0         Chunk 1
    content         content
    tenant          tenant
    classification  classification
    ACL             ACL
    provenance      provenance
Critical Lesson

Chunking is a security-sensitive transformation.

It does not merely transform text.

It creates the retrieval objects that later authorization controls will operate on.

Therefore the security properties of the source must survive the transformation.

Knowledge Check

Suppose an HR document is split into 20 chunks.

Only the first chunk contains the words:

CONFIDENTIAL — HR ONLY

Should chunks 2 through 20 be considered public because that phrase is absent?

No.

Classification comes from the security metadata of the source document, not from whether sensitive labels happen to appear in each chunk's text.
