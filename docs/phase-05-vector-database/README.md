# Phase 5 — Vector Database

## Goal

Understand how enterprise retrieval objects are persisted in a vector database and how security properties must survive that persistence boundary.

## Core Secure RAG Principle

> The vector store must not become the place where source authorization context disappears.

A vector database stores semantic representations for retrieval, but enterprise retrieval still requires identity, tenant, ACL, classification, and provenance information.

## Learning Objectives

By the end of this phase, you should be able to explain:

- what a vector database does;
- what ChromaDB stores;
- collections;
- persistent storage;
- vector records;
- documents versus embeddings;
- metadata serialization;
- vector similarity retrieval;
- why vector search is not authorization;
- why retrieval objects must preserve security context.

## Phase Exit Criteria

- [ ] Persistent ChromaDB collection exists.
- [ ] Embedded chunks are stored.
- [ ] Chunk IDs remain stable.
- [ ] Source content remains associated with vectors.
- [ ] Tenant metadata survives storage.
- [ ] Classification survives storage.
- [ ] ACL information survives storage.
- [ ] Provenance survives storage.
- [ ] Collection survives process restart.
- [ ] Raw semantic retrieval demonstrated.
- [ ] Insecure retrieval behavior documented.
- [ ] Tests pass.
