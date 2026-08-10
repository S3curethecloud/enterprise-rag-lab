# Phase 13 — Flask Application Integration

## Goal

Expose the Secure RAG pipeline through a minimal Flask API without bypassing or duplicating the controls built in earlier phases.

## Core Principle

> The Flask layer orchestrates the Secure RAG controls; it does not bypass or duplicate them.

## Learning Objectives

By the end of this phase, you should be able to explain:

- application-layer orchestration;
- request validation;
- identity propagation;
- secure pipeline invocation;
- response-security enforcement;
- structured API responses;
- safe error handling;
- why the web layer should remain thin.

## Request Flow

```text
HTTP Request
    ↓
Request Validation
    ↓
Identity Propagation
    ↓
Grounded Generation
    ↓
Response Security
    ↓
Structured HTTP Response

The API must not:

query ChromaDB directly;
perform its own ACL logic;
construct context manually;
bypass grounded generation;
return raw generation before response-security evaluation.
Phase Exit Criteria
 Flask application factory implemented;
 health endpoint implemented;
 secure query endpoint implemented;
 request validation implemented;
 identity propagated into the Secure RAG pipeline;
 grounded generation reused;
 response security reused;
 structured API response implemented;
 safe error handling implemented;
 end-to-end evidence generated;
 all tests pass.
