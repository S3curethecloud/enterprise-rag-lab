# Phase 3 Hands-On Lab

## Objective

Understand how chunking affects retrieval and prove that security properties survive the transformation from documents into chunks.

---

## Exercise 1 — Predict the Stride

Given:

```text
chunk_size = 500
overlap = 100

Calculate the stride.

stride = chunk_size - overlap
stride = 500 - 100
stride = 400

Expected chunk starting positions for a sufficiently long document:

0
400
800
1200
...
Exercise 2 — Inspect the Real Corpus

Run:

uv run python -m enterprise_rag.ingestion.chunk_corpus
cat artifacts/phase-03/chunk_stats.json

The current tutorial corpus produces one chunk per document.

This is expected because each current document is shorter than 500 characters.

The tutorial deliberately keeps the initial corpus readable.

Multi-chunk behavior is validated separately using synthetic test content.

Exercise 3 — Inspect One Chunk

Run:

uv run python - <<'PY'
import json
from pathlib import Path

chunks = json.loads(
    Path("artifacts/phase-03/chunks.json").read_text(encoding="utf-8")
)

print(json.dumps(chunks[0], indent=2))
PY

Identify:

chunk ID;
parent document ID;
chunk index;
character boundaries;
content;
tenant;
classification;
owner;
ACL;
trust state;
source system.
Exercise 4 — Inspect a Confidential Chunk

Run:

uv run python - <<'PY'
import json
from pathlib import Path

chunks = json.loads(
    Path("artifacts/phase-03/chunks.json").read_text(encoding="utf-8")
)

for chunk in chunks:
    if chunk["document_id"] == "hr-compensation-001":
        print(json.dumps(chunk, indent=2))
PY

Verify:

classification = confidential
allowed_groups = HR, Executive
tenant_id = techcorp
Exercise 5 — Deliberately Remove Security Metadata

Imagine replacing:

chunk = {
    "chunk_id": chunk_id,
    "document_id": document_id,
    "content": content,
    "metadata": metadata,
}

with:

chunk = {
    "chunk_id": chunk_id,
    "content": content,
}

Answer:

Can semantic search still work?
Can an embedding still be generated?
Can the vector still be stored?
Can document-level authorization reliably be enforced later?

Answers:

1. Yes
2. Yes
3. Yes
4. No

This is an important Secure RAG lesson:

Functional correctness does not imply security correctness.

Exercise 6 — Explain the Security Boundary

Explain why this is unsafe:

Restricted Document
        ↓
Chunk
        ↓
Embedding
        ↓
Vector Store

security metadata discarded

Then explain the correct design:

Restricted Document
        ↓
Chunk + inherited security metadata
        ↓
Embedding
        ↓
Vector + security metadata
Student Explanation

Without looking at the tutorial, explain:

Why must ACL, tenant, classification, and provenance metadata survive chunking?

A strong answer should include:

retrieval operates on chunks;
semantic similarity does not authorize access;
authorization requires security attributes at retrieval time;
a chunk retains the sensitivity of its source;
source provenance must remain traceable.
