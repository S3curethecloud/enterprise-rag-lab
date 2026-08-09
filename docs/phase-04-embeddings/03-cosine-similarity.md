# Cosine Similarity

Once two pieces of text have embeddings, we need a way to compare them.

One common technique is cosine similarity.

## Concept

Cosine similarity compares the direction of two vectors.

Conceptually:

```text
Vector A  ↗
Vector B  ↗

similar direction
=
high similarity

Versus:

Vector A  ↗
Vector B  ←

different direction
=
lower similarity
Range

Cosine similarity commonly ranges from:

-1   opposite direction
 0   unrelated direction
 1   same direction

For text embeddings, semantically related text generally produces a higher similarity score than unrelated text.

Example

Query:

Are dogs allowed in the office?

Candidate A:

Employees may bring approved pets into designated office areas.

Candidate B:

Production APIs must use identity-based authentication.

We expect:

similarity(query, Candidate A)
    >
similarity(query, Candidate B)
Important Warning

A high similarity score means:

This content appears semantically relevant.

It does NOT mean:

The requesting user is authorized to retrieve this content.

Similarity ranking and authorization are separate control planes.
