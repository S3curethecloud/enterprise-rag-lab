# Phase 10 Hands-On Lab

## Objective

Generate answers only from validated enterprise context and abstain when authorized evidence is unavailable.

## Exercise 1 — Authorized Grounded Answer

Run:

```bash
uv run python -m enterprise_rag.generation.demo_grounded_answer

Verify:

generation = grounded
sources >= 1

Inspect:

cat artifacts/phase-10/grounded_answer_demo.json

Confirm that the HR source is present.

Exercise 2 — Unauthorized Question

Run:

uv run python -m enterprise_rag.generation.demo_abstention

Alice is not authorized for HR compensation.

The expected behavior is:

authorized results = 0
context chunks = 0
generation = abstain
Exercise 3 — Explain Why This Matters

Why should the model not simply answer from general knowledge?

Because this system is claiming to provide an enterprise-grounded answer.

If authorized enterprise evidence is unavailable, using model memory would break that grounding contract.

Exercise 4 — Inspect the Prompt

Inspect the prompt inside:

cat artifacts/phase-10/grounded_answer_demo.json

Identify:

trusted grounding instructions;
the user question;
source identity;
retrieved content;
source path.
Exercise 5 — Explain Source Attribution

Explain the difference between:

The model cited a source.

and:

The answer is correct.

Citation proves evidence lineage.

It does not automatically prove factual correctness.

Student Explanation

Explain:

Why should grounded generation abstain when validated context is empty?

A strong answer should mention authorization, evidence integrity, hallucination control, model-memory separation, and auditability.
