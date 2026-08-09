# Top-K Is Not Relevance Acceptance

A vector database ranks stored vectors by closeness to the query vector.

If we request:

```text
top_k = 3

the database attempts to return the three nearest stored records.

That does not mean all three are useful.

Example

For:

Are pets allowed in the office?

the company FAQ should rank strongly.

Other records may still be returned because they are the next-nearest vectors in a very small corpus.

Important Distinction
Ranking:
Which records are closest?

Acceptance:
Are any records close enough to trust as context?

These are different decisions.

Weak Query Problem

Suppose the corpus contains only:

HR policy;
security policy;
architecture policy;
finance information;
company FAQ.

Then ask:

How do I configure a Kubernetes GPU scheduler?

The vector database may still return three records.

It has not discovered that the corpus contains the answer.

It has only found the three nearest vectors.

Secure RAG Principle

Weak retrieval should not automatically become LLM context.

A system should be able to abstain when retrieval quality is insufficient.
