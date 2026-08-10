# Phase 12 — Evaluation + RAG Red Teaming

## Goal

Measure the behavior of the Secure RAG pipeline across retrieval quality, authorization, ingestion security, context validation, grounded generation, and response security.

## Core Principle

> A Secure RAG control is not complete until its expected behavior is repeatedly testable and measurable.

## Learning Objectives

By the end of this phase, you should be able to explain:

- evaluation scenarios;
- expected versus actual behavior;
- control coverage;
- security regression testing;
- retrieval quality evaluation;
- authorization evaluation;
- prompt-injection testing;
- poisoned-content testing;
- grounding and abstention testing;
- response-security testing;
- consolidated evaluation evidence.

## Evaluation Record

Every scenario should produce:

```text
scenario
control_area
expected
actual
passed
evidence
Evaluation Areas
retrieval
authorization
secure_ingestion
context_security
grounded_generation
response_security
Phase Exit Criteria
 scenario model implemented;
 retrieval evaluation included;
 authorization evaluation included;
 poisoned-content evaluation included;
 weak-query abstention evaluated;
 malicious-context rejection evaluated;
 grounding and abstention evaluated;
 output DLP evaluated;
 source-integrity blocking evaluated;
 consolidated evaluation report generated;
 overall pass rate calculated;
 all tests pass.
