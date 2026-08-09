# Raw Vector Search Is Not Authorization

At this point the vector store can answer semantic queries.

That does not make retrieval secure.

## Naive Flow

```text
Question
   ↓
Embedding
   ↓
ChromaDB
   ↓
Nearest Vectors

Suppose Alice belongs to:

Engineering
Employees

and asks:

What is the executive compensation policy?

The HR compensation chunk is likely one of the strongest semantic matches.

ChromaDB is doing its job correctly.

The security architecture is incomplete.

Important Distinction

Vector search answers:

Which chunks are relevant?

Authorization answers:

Which of those chunks may this identity retrieve?

The first answer cannot replace the second.

Deliberate Failure

At this stage of the tutorial, raw search is intentionally insecure.

This allows us to observe the failure mode before introducing ACL-aware retrieval later.

Secure RAG Principle

Retrieval relevance must never be interpreted as permission.

The model must not receive unauthorized chunks simply because they rank highly.
