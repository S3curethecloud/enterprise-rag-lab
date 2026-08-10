# RAG Red Teaming

Red teaming intentionally attempts to make the system violate its intended controls.

## Example Attack Categories

### Unauthorized Retrieval

Attempt to retrieve HR, Finance, or Security data using an identity without the required ACL.

### Indirect Prompt Injection

Insert instructions inside retrieved content that attempt to override application policy.

### Poisoned Knowledge

Attempt to ingest untrusted or malicious source material.

### Retrieval Confusion

Ask questions outside the corpus and observe whether irrelevant context is accepted.

### Grounding Failure

Attempt to generate an answer when authorized context is absent.

### Citation Hallucination

Return a source identifier that was never present in validated context.

### Sensitive Output

Attempt to expose sensitive values through generated responses.

## Red-Team Principle

> The objective is not to prove that attacks are impossible.

The objective is to repeatedly test whether known controls behave as designed under adversarial conditions.

## Evidence

A useful red-team scenario records:

```text
attack
expected_control
actual_behavior
pass_or_fail
supporting_evidence

