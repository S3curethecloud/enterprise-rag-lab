# Phase 12 Hands-On Lab

## Objective

Run a consolidated Secure RAG evaluation suite and inspect control coverage across the entire pipeline.

## Exercise 1 — Run the Evaluation Harness

Run:

```bash
uv run python -m enterprise_rag.evaluation.run_evaluation

Expected:

Failed: 0
Pass rate: 100.0%
Exercise 2 — Inspect the JSON Evidence

Run:

cat artifacts/phase-12/evaluation_report.json

Identify:

scenario;
control area;
expected behavior;
actual behavior;
pass/fail result;
evidence.
Exercise 3 — Render the Human-Readable Report

Run:

uv run python -m enterprise_rag.evaluation.render_report
cat artifacts/phase-12/evaluation_report.md
Exercise 4 — Review Control Coverage

Confirm the evaluation includes:

retrieval
authorization
secure_ingestion
context_security
grounded_generation
response_security
Exercise 5 — Deliberately Break a Control

Temporarily imagine changing authorization so Alice can retrieve HR data.

What should happen?

The scenario:

alice_hr_access_denied

should fail.

The evaluation runner should return a non-zero exit code.

This behavior allows the harness to become a future CI security gate.

Do not permanently modify the working implementation.

Exercise 6 — Explain Test vs Evaluation

Unit test:

Does authorize() return False for this input?

Evaluation scenario:

Does Alice fail to receive HR context through the actual retrieval pipeline?

Both are valuable.

They test different system boundaries.

Student Explanation

Explain:

Why does an enterprise RAG platform need both unit tests and end-to-end behavioral evaluations?

A strong answer should mention integration risk, security invariants, regression detection, evidence, control coverage, and CI gating.
