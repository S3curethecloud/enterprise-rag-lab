# Secure RAG Architecture Checklist

## Data Ingestion

- [ ] source identity known;
- [ ] source trust evaluated;
- [ ] document provenance preserved;
- [ ] classification present;
- [ ] tenant metadata present;
- [ ] ACL metadata present;
- [ ] suspicious content inspected;
- [ ] poisoned content rejected or quarantined.

## Chunking and Storage

- [ ] document security metadata survives chunking;
- [ ] chunk IDs are traceable to parent documents;
- [ ] vector metadata preserves authorization properties;
- [ ] vector-store access is controlled.

## Retrieval

- [ ] semantic similarity is not treated as authorization;
- [ ] weak retrieval can abstain;
- [ ] identity is propagated;
- [ ] tenant boundary enforced;
- [ ] ACL authorization enforced;
- [ ] unauthorized candidates do not enter model context.

## Context

- [ ] context contains only eligible results;
- [ ] retrieved content is treated as data, not authority;
- [ ] suspicious instructions are rejected;
- [ ] provenance survives context assembly;
- [ ] context is bounded.

## Generation

- [ ] model answers only from validated context;
- [ ] empty context causes abstention;
- [ ] source identity is preserved;
- [ ] model is not used as an authorization engine.

## Response

- [ ] response inspected before disclosure;
- [ ] source integrity checked;
- [ ] sensitive values can be redacted;
- [ ] unsafe responses can be blocked;
- [ ] logging avoids unnecessary sensitive-value duplication.

## Evaluation

- [ ] authorization regressions tested;
- [ ] poisoned content tested;
- [ ] indirect prompt injection tested;
- [ ] weak retrieval tested;
- [ ] grounding failures tested;
- [ ] DLP tested;
- [ ] citation integrity tested;
- [ ] evaluation failures can fail CI.

## Application

- [ ] API validates requests;
- [ ] identity is propagated rather than trusted blindly;
- [ ] API reuses Secure RAG orchestration;
- [ ] API does not directly query the vector store;
- [ ] raw prompts are not exposed.

## Production

- [ ] authentication architecture defined;
- [ ] production authorization source defined;
- [ ] secrets management defined;
- [ ] model/data handling documented;
- [ ] observability architecture defined;
- [ ] DLP strategy defined;
- [ ] incident response ownership defined;
- [ ] governance ownership defined.
