# Relevance Is Not Entitlement

Phase 7 established whether content is semantically relevant.

Phase 8 adds a separate question:

> Is the requesting identity entitled to retrieve it?

## Alice Example

Alice belongs to:

```text
Engineering
Employees

She asks:

What is the executive compensation policy?

The HR compensation document is semantically relevant.

But its ACL is:

HR
Executive

Therefore:

relevant = true
authorized = false
eligible = false
Bob Example

Bob belongs to:

HR
Employees

For the same query:

relevant = true
authorized = true
eligible = true
Secure Retrieval Rule
eligible =
    relevant
    AND
    authorized

Neither condition can replace the other.

Critical Secure RAG Principle

The LLM never grants enterprise data access.

Only authorized retrieval objects may proceed toward context assembly.
