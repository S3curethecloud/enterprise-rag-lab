# What Is an Embedding?

Computers do not directly understand sentences as meaning.

An embedding model converts content into a numeric representation called a vector.

Conceptually:

```text
"Employees may bring approved pets"
                │
                ▼
        Embedding Model
                │
                ▼
[0.021, -0.114, 0.083, ..., 0.041]

The resulting vector represents semantic properties of the input.

Why This Matters for RAG

Suppose the user asks:

Are dogs allowed at work?

The enterprise document says:

Employees may bring approved pets into designated office areas.

The wording is different.

Traditional exact keyword matching may not recognize the relationship well.

An embedding model attempts to place these sentences near each other in semantic vector space.

Mental Model
"dogs allowed at work?"
          │
          ▼
       Vector A

"approved pets may enter offices"
          │
          ▼
       Vector B

Vector A and Vector B
are mathematically close.
Embeddings Are Not Knowledge Records

The vector does not replace the source content.

A useful RAG retrieval object still needs:

content
embedding
document identity
chunk identity
tenant
classification
ACL
provenance

The embedding adds a semantic representation.

It does not replace enterprise metadata.

Secure RAG Principle

An embedding answers questions about semantic proximity.

It does not answer:

Who is requesting this information?
Which tenant owns it?
Is the user in the correct group?
Is the document confidential?
Is the source trusted?

Those decisions belong to other layers.
