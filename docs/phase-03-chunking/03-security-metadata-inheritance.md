# Security Metadata Inheritance

Chunking transforms one source document into multiple retrieval objects.

That transformation must preserve security properties.

## Source Document

```json
{
  "document_id": "hr-compensation-001",
  "tenant_id": "techcorp",
  "classification": "confidential",
  "allowed_groups": ["HR", "Executive"]
}

After chunking:

hr-compensation-001::chunk::0000
hr-compensation-001::chunk::0001
hr-compensation-001::chunk::0002

Every chunk must retain:

tenant_id = techcorp
classification = confidential
allowed_groups = HR, Executive
Wrong Design
Chunk
├── content
└── embedding

Once the document becomes a vector, its source authorization has disappeared.

Better Design
Chunk
├── chunk_id
├── document_id
├── content
├── chunk_index
├── tenant_id
├── department
├── classification
├── owner
├── allowed_groups
├── trusted
└── source_system
Critical Principle

A chunk is not less sensitive than its source merely because it contains fewer words.

For example:

Document:
Executive Compensation Policy
classification = confidential

Chunk:
"Executive base salary ranges from ..."

classification must still = confidential
Future Retrieval

Later, retrieval will operate on chunks rather than full documents.

Therefore authorization metadata must exist at the same retrieval boundary.

The LLM must never receive a chunk that passed semantic ranking but lost its authorization context.
