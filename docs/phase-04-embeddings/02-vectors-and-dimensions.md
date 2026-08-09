# Vectors and Dimensions

An embedding is represented as a vector.

A simplified example might look like:

```text
[0.12, -0.34, 0.91]

This is a three-dimensional vector.

Real embedding models typically use many more dimensions.

all-MiniLM-L6-v2

The model used in this tutorial produces vectors with 384 dimensions.

Conceptually:

text
 │
 ▼
all-MiniLM-L6-v2
 │
 ▼
[d1, d2, d3, ... d384]

Individual dimensions should not usually be interpreted as simple human-readable labels such as:

dimension 1 = pets
dimension 2 = finance
dimension 3 = security

The semantic representation is distributed across the vector.

Same Vector Space

A powerful property of embedding models is that different pieces of text can be placed into the same vector space.

For example:

Question
"Are pets allowed?"
       │
       ▼
     Vector

Policy
"Approved animals may enter designated offices."
       │
       ▼
     Vector

Their vector distance can then be measured.

Important Limitation

The vector encodes semantic characteristics.

It does not encode enterprise authorization merely because authorization metadata exists beside the text.

That security context must remain explicitly represented and enforced.
