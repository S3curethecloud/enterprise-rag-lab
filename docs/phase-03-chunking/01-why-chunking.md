# Why RAG Systems Chunk Documents

Enterprise documents can be large.

A handbook may contain dozens of policies.

An architecture guide may contain hundreds of sections.

Sending an entire document into retrieval or model context is usually inefficient and may reduce retrieval precision.

Chunking divides a document into smaller retrieval units.

## Example

Suppose a handbook contains:

```text
Page 1   Benefits
Page 5   Remote Work
Page 12  Pet Policy
Page 20  Security
Page 30  Expenses

The user asks:

Are pets allowed in the office?

Retrieving the entire handbook provides far more context than necessary.

A better retrieval unit might contain only the pet-policy section.

Retrieval Granularity

Chunking creates a tradeoff.

Very large chunks:

+ more surrounding context
- less precise retrieval
- more tokens

Very small chunks:

+ precise retrieval
- may lose surrounding meaning
- may fragment important statements

There is no universal perfect chunk size.

Chunking strategy depends on:

document structure;
content type;
embedding model;
retrieval system;
query patterns;
context-window constraints.
Security Implication

Chunking creates new stored objects.

A secure architecture must answer:

Which security properties should these new objects inherit?

For this tutorial, every chunk inherits the source document's:

document ID;
tenant;
department;
classification;
owner;
allowed groups;
trust state;
source system.

Security metadata must remain attached to the knowledge after transformation.
