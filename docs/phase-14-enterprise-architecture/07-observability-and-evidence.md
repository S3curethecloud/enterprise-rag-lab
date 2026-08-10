# Observability and Audit Evidence

Secure RAG systems need evidence across the full request lifecycle.

## Useful Evidence Categories

### Ingestion Evidence

Record:

- source;
- document identity;
- trust state;
- classification;
- accept/reject/quarantine decision;
- policy reasons.

### Retrieval Evidence

Record:

- query identifier;
- retrieved candidates;
- distances;
- relevance decisions.

### Authorization Evidence

Record:

- identity;
- tenant;
- resource;
- ACL decision;
- authorization reason.

Avoid unnecessary disclosure of document contents in authorization logs.

### Context Evidence

Record:

- included chunk identifiers;
- rejected chunk identifiers;
- validation reasons;
- context size.

### Generation Evidence

Record:

- generation status;
- source identifiers;
- abstention state.

Avoid unnecessarily persisting prompts containing sensitive enterprise context.

### Response Evidence

Record:

- allow/redact/block;
- finding types;
- source-integrity status.

Do not store raw secrets merely because they were detected.

### Evaluation Evidence

Record:

- scenario;
- expected behavior;
- actual behavior;
- pass/fail;
- control area.

## Principle

> Audit evidence should prove control behavior without becoming a new data-leakage channel.
