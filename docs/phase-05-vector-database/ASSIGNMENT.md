# Learner Assignment — Vector Database

## Purpose

This assignment is designed to make you research, reason, explain, and remember the architectural purpose of this phase.

Do not answer by copying the phase documentation. Use the documentation as a starting point, research the concepts, and explain them in your own words.

---

## 1. Memory Analogy

> A vector database is an extremely fast librarian. It can find the most related books almost instantly, but speed does not mean the librarian has checked your clearance.

### Your task

Explain why this analogy works.

Then create a **different analogy of your own** that teaches the same concept.

---

## 2. Thesis Challenge

Defend or challenge this statement:

> **Efficient retrieval without authorization can make sensitive-data leakage faster rather than safer.**

Your response must include:

- what the statement means;
- why it matters;
- one argument supporting it;
- one possible objection;
- your final position.

---

## 3. Research Questions

Research and answer each question in your own words.

1. Why are vector databases used in RAG?
2. What is nearest-neighbor search?
3. Why does a vector database attempt to return something even for weak questions?
4. Why should metadata travel with stored vectors?
5. Why is raw vector retrieval dangerous in an enterprise environment?

For every answer:

1. define the concept;
2. explain why it exists;
3. connect it to this Secure RAG architecture.

---

## 4. Architecture Reasoning

Answer:

1. What enters this phase?
2. What transformation or decision happens here?
3. What security property must survive this phase?
4. What does this phase pass to the next phase?
5. Which component should **not** be trusted to make this phase's security decision?

Draw a small architecture diagram showing the input, control, output, and trust boundary.

---

## 5. Failure Thought Experiment

A librarian can locate every company document in milliseconds but never checks employee badges. Is this an effective enterprise search system? Explain both the functional success and security failure.

Your answer must explain:

- what fails;
- why it fails;
- which asset is at risk;
- which control prevents the failure;
- whether another downstream control could still reduce the damage.

---

## 6. Written Assignment

Write 700-1000 words defending: **A highly accurate vector search system can still be a serious security vulnerability.**

Your paper should contain:

- introduction;
- thesis;
- technical explanation;
- security analysis;
- architecture example;
- failure scenario;
- conclusion.

Cite the sources you researched.

---

## 7. Teach-It-Back Challenge

Explain this phase to a 15-year-old **without using specialist RAG terminology**.

Maximum: 200 words.

If you cannot explain the concept simply, revisit the phase.

---

## 8. Break the Architecture

Imagine this phase is completely removed.

Answer:

1. Would the application still run?
2. What functionality would remain?
3. What security property would disappear?
4. What attack or failure becomes possible?
5. Which existing test should detect the regression?

---

## 9. Connection to the Learning Journey

Before enterprise knowledge enters this retrieval system, what controls must Phase 6 apply?

Then complete:

```text
Previous phase gives me:
_____________________________

This phase guarantees:
_____________________________

Next phase depends on:
_____________________________
10. Memory Check

Without looking at the documentation, write:

the phase name;
its primary purpose;
its most important security principle;
one failure it prevents;
one analogy that helps you remember it.
Submission Checklist
 I researched concepts beyond merely copying the lab.
 I answered every research question in my own words.
 I defended or challenged the thesis.
 I created my own analogy.
 I drew the control boundary.
 I explained what happens if this phase disappears.
 I connected this phase to the previous and next phases.
 I completed the teach-it-back challenge.
 I cited my research sources.
 I can explain the phase without reading the documentation.
Grading Guide
Area	Weight
Technical understanding	25%
Research quality	15%
Security reasoning	20%
Analogy and teach-back	15%
Failure analysis	15%
Architecture connection	10%

---

## 10. Memory Check

Without looking at the documentation, write:

- the phase name;
- its primary purpose;
- its most important security principle;
- one failure it prevents;
- one analogy that helps you remember it.

