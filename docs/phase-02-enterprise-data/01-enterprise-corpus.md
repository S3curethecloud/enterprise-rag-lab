# The Enterprise Corpus

A RAG knowledge base is rarely one folder containing equally trusted public documents.

Real organizations have information spread across systems such as:

```text
SharePoint
Confluence
ServiceNow
Git repositories
Databases
File shares
Object storage
Knowledge bases
Ticketing platforms
Policy repositories

Each source may have different:

owners;
access rules;
classifications;
update schedules;
trust levels;
retention requirements.
Simulated Enterprise

This tutorial uses a fictional organization called TechCorp.

Its corpus contains:

General
Engineering
Human Resources
Security
Finance

These departments intentionally have different access requirements.

Content Is Not Enough

Consider this document:

executive_compensation.md

Storing only:

Executive compensation bands are...

loses critical enterprise information.

We also need information such as:

document_id
source
owner
tenant
classification
allowed_groups
trust status
timestamp
provenance
Mental Model
Enterprise Document
       │
       ├── Content
       │
       └── Security + Trust Metadata

Both must survive ingestion.

Knowledge Check

Why would converting every enterprise document into one unrestricted vector collection be dangerous?

Because semantic retrieval would no longer preserve the authorization boundaries of the source systems.
