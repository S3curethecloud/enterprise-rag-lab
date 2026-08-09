# Secure RAG Mental Model

Secure RAG is not simply:

```text
Question
   ↓
Vector Search
   ↓
LLM

An enterprise RAG system contains multiple trust and authorization boundaries.

Enterprise Data Sources
SharePoint / Confluence / ServiceNow / DBs / Files
        │
        ▼
┌───────────────────────────────┐
│ Secure Ingestion              │
│                               │
│ • Extract                     │
│ • Classify                    │
│ • Sanitize                    │
│ • Tag metadata                │
│ • Preserve ACL information    │
│ • Capture provenance          │
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│ Knowledge Store               │
│                               │
│ • Documents / chunks          │
│ • Embeddings                  │
│ • Metadata                    │
│ • ACLs / tenant tags          │
│ • Classification              │
│ • Provenance                  │
└──────────────┬────────────────┘
               │
        query + identity
               │
               ▼
┌───────────────────────────────┐
│ Secure Retrieval              │
│                               │
│ • Identity-aware search       │
│ • Tenant filtering            │
│ • ACL filtering               │
│ • Metadata filtering          │
│ • Relevance ranking           │
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│ Context Assembly              │
│                               │
│ • Trust labeling              │
│ • Provenance checks           │
│ • Relevance checks            │
│ • Contamination checks        │
│ • Injection detection         │
│ • Token budgeting             │
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│ Model                         │
│                               │
│ • System policy               │
│ • Approved context            │
│ • Grounded generation         │
│ • Guardrails                  │
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│ Response Controls             │
│                               │
│ • Citations                   │
│ • DLP                         │
│ • Safety checks               │
│ • Audit logging               │
└──────────────┬────────────────┘
               │
               ▼
              User
The Most Important Principle

The LLM does not grant data access.

The correct sequence is:

Identity
   ↓
Authorization
   ↓
Retrieval filtering
   ↓
Approved context
   ↓
Model

The model must never determine whether a user is entitled to view HR, legal, finance, confidential, or another tenant's information.

Security Metadata Travels With Knowledge

Enterprise knowledge is not just text.

Conceptually, every indexed chunk should retain information such as:

Chunk
├── content
├── source_id
├── document_id
├── tenant_id
├── classification
├── owner
├── allowed_groups
├── timestamp
└── provenance
Semantic Similarity Is Not Authorization

Vector similarity answers:

How semantically relevant is this content?

Authorization answers:

Is this identity permitted to retrieve this content?

These are independent decisions.

Core Threats

Secure RAG must account for:

Poisoned documents
Indirect prompt injection
Cross-tenant retrieval
Stale entitlements
Sensitive context leakage

These threats will be introduced progressively throughout the tutorial.
