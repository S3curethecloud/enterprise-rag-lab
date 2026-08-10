# Secure RAG Capstone Review

A student completing this tutorial should be able to explain the complete architecture without relying only on the source code.

## Question 1

Why is semantic similarity not authorization?

A strong answer should explain that embeddings measure semantic relationship, while authorization evaluates entitlement.

## Question 2

Where must authorization occur?

Before retrieved enterprise content enters the model context.

## Question 3

Does the LLM ever grant enterprise data access?

No.

> The LLM never grants access to enterprise data. Authorization occurs before retrieved context reaches the model.

## Question 4

Why preserve ACL metadata during chunking?

Because retrieval operates on chunks, and each chunk must retain the security properties of its source document.

## Question 5

Why inspect both ingestion and context?

Because malicious content may enter through untrusted sources, and defense in depth requires another validation point before model exposure.

## Question 6

Why can nearest-neighbor retrieval still be wrong?

A vector database always attempts to return nearest results, even when none are sufficiently relevant.

## Question 7

Why should the system abstain?

Because an enterprise-grounded answer without adequate authorized evidence breaks the grounding contract.

## Question 8

Why is response security still necessary?

Grounded content may still contain sensitive data, invalid citations, or disclosure that violates response policy.

## Question 9

Why is the Flask layer thin?

To preserve centralized controls and prevent application-layer bypasses or policy duplication.

## Question 10

Why does Secure RAG need EvalOps?

Because future changes can weaken end-to-end security behavior even when individual components still function.

## Final Architecture Statement

A strong summary is:

> Secure RAG is an enterprise information-access architecture in which trusted ingestion, metadata preservation, semantic retrieval, relevance evaluation, identity-aware authorization, context validation, grounded generation, response security, and continuous evaluation work together. The model operates only after access decisions have already been enforced.
