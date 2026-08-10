# Learner Assignment — Enterprise Secure RAG Architecture

## Purpose

This assignment is designed to make you research, reason, explain, and remember the architectural purpose of this phase.

Do not answer by copying the phase documentation. Use the documentation as a starting point, research the concepts, and explain them in your own words.

---

## 1. Memory Analogy

> Secure RAG is an airport, not an airplane engine. The model is one component inside a larger system of identity checks, gates, inspections, operating rules, logging, and emergency controls.

### Your task

Explain why this analogy works.

Then create a **different analogy of your own** that teaches the same concept.

---

## 2. Thesis Challenge

Defend or challenge this statement:

> **Secure RAG is a system of enforced trust boundaries, not a model connected to a vector database.**

Your response must include:

- what the statement means;
- why it matters;
- one argument supporting it;
- one possible objection;
- your final position.

---

## 3. Research Questions

Research and answer each question in your own words.

1. Where are the major trust boundaries in this architecture?
2. How do the ingestion plane and query plane differ?
3. Which component owns enterprise data authorization?
4. What security evidence should be logged?
5. What tutorial components must change before production?
6. Which controls belong to IAM, Security, AI Platform, Data Governance, and Application Engineering?
7. Why should a model never become the final authority for enterprise access?

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

Remove each of these controls one at a time: source trust, metadata, relevance, authorization, context validation, grounding, response security, and evaluation. For each removal, identify a new failure or attack that becomes possible.

Your answer must explain:

- what fails;
- why it fails;
- which asset is at risk;
- which control prevents the failure;
- whether another downstream control could still reduce the damage.

---

## 6. Written Assignment

Write 1500-2000 words defending the capstone thesis: **The LLM never grants access to enterprise data. Authorization occurs before retrieved context reaches the model.**

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

Summarize the entire 14-phase architecture in one diagram and one paragraph without referring to the source code.

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

