# Ingestion Plane vs Query Plane

Secure RAG contains two major processing planes.

## Ingestion Plane

The ingestion plane determines what enterprise information may enter the knowledge system.

```text
source
  ↓
source trust
  ↓
metadata validation
  ↓
classification
  ↓
content inspection
  ↓
accept / reject / quarantine
  ↓
chunking
  ↓
security metadata inheritance
  ↓
embedding
  ↓
vector storage

Important ingestion controls include:

trusted source systems;
provenance;
required metadata;
classification;
suspicious-instruction detection;
poisoned-content quarantine;
ACL metadata preservation.
Query Plane

The query plane determines what information may be used to answer a specific caller.

query
  ↓
identity
  ↓
semantic retrieval
  ↓
relevance
  ↓
tenant + ACL authorization
  ↓
context validation
  ↓
bounded context
  ↓
grounded generation
  ↓
response security
Different Security Questions

The ingestion plane asks:

Should this content become part of the enterprise knowledge system?

The query plane asks:

May this identity use this content for this request?

Both are required.

Trusted ingestion does not eliminate the need for query-time authorization.

Query-time authorization does not eliminate the need to protect the knowledge base from poisoned content.
