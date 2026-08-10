# Source Integrity

A generated answer should not cite retrieval objects that were never present in validated context.

## Valid Source

```text
Generation source
      ↓
document_id + chunk_id
      ↓
exists in validated context
      ↓
VALID
Invented Source
Generation source
      ↓
document_id + chunk_id
      ↓
not present in validated context
      ↓
BLOCK
Principle

Citation generation must not create evidence that the retrieval pipeline never supplied.

Source integrity supports:

auditability;
hallucination detection;
evidence lineage;
trustworthy citations.
