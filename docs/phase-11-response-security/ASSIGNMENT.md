# Learner Assignment — Response Security

## Purpose

This assignment is designed to make you research, reason, explain, and remember the architectural purpose of this phase.

Do not answer by copying the phase documentation. Use the documentation as a starting point, research the concepts, and explain them in your own words.

---

## 1. Memory Analogy

> Response security is the checkpoint at the exit of a secure facility. Someone may be authorized to enter the building but still be prohibited from carrying certain information outside.

### Your task

Explain why this analogy works.

Then create a **different analogy of your own** that teaches the same concept.

---

## 2. Thesis Challenge

Defend or challenge this statement:

> **Authorization to access information does not automatically mean every representation of that information should be disclosed everywhere.**

Your response must include:

- what the statement means;
- why it matters;
- one argument supporting it;
- one possible objection;
- your final position.

---

## 3. Research Questions

Research and answer each question in your own words.

1. What is output DLP?
2. Why inspect model output after grounded generation?
3. What is source or citation integrity?
4. Why can a grounded response still be unsafe?
5. What is the difference between ALLOW, REDACT, and BLOCK?

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

An HR administrator may legitimately view an employee SSN. Should a chatbot automatically repeat that SSN in every answer? Explain the distinction between retrieval authorization and disclosure policy.

Your answer must explain:

- what fails;
- why it fails;
- which asset is at risk;
- which control prevents the failure;
- whether another downstream control could still reduce the damage.

---

## 6. Written Assignment

Write 700-1000 words defending: **Secure retrieval alone cannot guarantee secure disclosure.**

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

How can Phase 12 repeatedly prove that these controls continue working after future changes?

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

