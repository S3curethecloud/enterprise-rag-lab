# Security Metadata

Enterprise RAG requires more than text.

Security metadata describes the rules and properties associated with that text.

## Example

```json
{
  "document_id": "hr-compensation-001",
  "tenant_id": "techcorp",
  "department": "hr",
  "classification": "confidential",
  "owner": "Human Resources",
  "allowed_groups": ["HR"],
  "trusted": true
}
Why Each Field Exists
document_id

Provides a stable identity for the source document.

tenant_id

Identifies the organizational security boundary.

This becomes critical in multi-tenant systems.

department

Supports organizational filtering and policy decisions.

classification

Represents the sensitivity level of information.

Examples:

public
internal
confidential
restricted
owner

Identifies who is responsible for the information.

allowed_groups

Represents which identities or groups may access the document.

trusted

Indicates whether the source is currently considered trusted.

Key Principle

Security metadata travels with knowledge.

Later, when a document becomes multiple chunks:

Document
ACL = HR
classification = confidential

       ↓ chunk

Chunk 1 → ACL = HR
Chunk 2 → ACL = HR
Chunk 3 → ACL = HR

Chunking must not erase authorization.
