# Enterprise Secure RAG Tutorial

## Purpose

This repository is an educational, hands-on tutorial for learning Retrieval-Augmented Generation (RAG) and Secure RAG from first principles.

The objective is not simply to produce a working chatbot.

The objective is to understand:

- how enterprise documents become retrievable knowledge;
- how chunking affects retrieval;
- how embeddings represent semantic meaning;
- how vector databases support similarity search;
- how retrieval differs from generation;
- where identity and authorization belong;
- how security metadata travels with enterprise knowledge;
- how indirect prompt injection affects RAG;
- how context is validated before reaching a model;
- how grounded generation and citations work;
- how RAG systems are evaluated and attacked;
- how these components fit into an enterprise AI platform.

## Learning Doctrine

Every phase follows the same progression:

1. Teach
2. Visualize
3. Build
4. Deliberately break
5. Secure
6. Test
7. Explain

A student should understand why a component exists before implementing it.

## Core Secure RAG Principle

> The LLM does not grant access to enterprise data.
> Retrieval authorization occurs before context reaches the model.

Semantic relevance and authorization are separate concerns.

A highly relevant document is not necessarily an authorized document.

## Course Progression

1. RAG Foundations + Development Environment
2. Enterprise Data + Metadata
3. Chunking
4. Embeddings
5. Vector Database
6. Secure Ingestion
7. Semantic Retrieval
8. Identity + ACL-Aware Retrieval
9. Secure Context Assembly
10. Grounded RAG Generation
11. Response Security
12. Evaluation + RAG Red Teaming
13. Flask Application
14. Enterprise Architecture Review

## Expected Outcome

By the end of the tutorial, a student should be able to design, implement, explain, test, and defend an enterprise Secure RAG architecture rather than merely demonstrate a working RAG application.
