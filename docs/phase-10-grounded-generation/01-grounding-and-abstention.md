# Grounding and Abstention

A language model can produce fluent text even when it has insufficient evidence.

That is why fluency cannot be treated as proof.

## Grounded Generation

A grounded RAG answer should be based on retrieved evidence that has already passed:

```text
relevance
authorization
context validation

Only then may it be used for generation.

Unsupported Questions

If no eligible context remains:

authorized_results = []

the generation layer should abstain.

It should not answer from general model memory merely because the model may know something about the topic.

Secure RAG Principle

No evidence means no enterprise-grounded answer.

Example

Alice asks about executive compensation.

The HR document is relevant but unauthorized.

Therefore:

relevant = true
authorized = false
context = empty
generation = abstain

The model never receives the HR content.
