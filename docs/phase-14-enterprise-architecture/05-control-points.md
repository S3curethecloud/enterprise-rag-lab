# Secure RAG Control Points

The tutorial implements security across multiple control points.

| Control Point | Purpose | Phase |
|---|---|---|
| Source trust | Prevent untrusted ingestion | 6 |
| Metadata validation | Preserve security properties | 2, 6 |
| Poison detection | Detect hostile retrieved instructions | 6 |
| Security-aware chunking | Preserve parent security metadata | 3 |
| Semantic retrieval | Find potentially relevant evidence | 7 |
| Relevance acceptance | Reject weak nearest-neighbor matches | 7 |
| Tenant boundary | Prevent cross-tenant access | 8 |
| ACL authorization | Enforce group-based retrieval access | 8 |
| Context validation | Stop unsafe content entering generation | 9 |
| Context bounds | Limit model context | 9 |
| Grounding policy | Restrict answers to validated evidence | 10 |
| Abstention | Refuse unsupported enterprise answers | 10 |
| Source integrity | Prevent invented citations | 11 |
| Output DLP | Detect sensitive generated values | 11 |
| Response policy | Allow, redact, or block | 11 |
| EvalOps | Detect security regressions | 12 |
| Flask orchestration | Preserve controls through API integration | 13 |

## Defense in Depth

No individual control is treated as sufficient.

For example:

```text
trusted ingestion
    +
authorization
    +
context inspection
    +
grounded generation
    +
response security

provides stronger protection than relying on any single layer.

Architectural Principle

A model safety instruction is not a substitute for an enforceable authorization control.
