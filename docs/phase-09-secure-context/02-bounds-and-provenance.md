# Context Bounds and Provenance

Context assembly should be deterministic and bounded.

## Why Bound Context?

Unlimited retrieval context can create:

- token pressure;
- irrelevant context accumulation;
- noisy answers;
- larger attack surface;
- higher cost;
- harder provenance analysis.

This phase uses a character limit for educational clarity.

Later systems may use token-aware budgets.

## Provenance

Each included chunk retains:

- chunk_id;
- document_id;
- classification;
- tenant;
- owner;
- source system;
- source path.

This allows downstream generation to retain source attribution.

## Principle

> If a model uses enterprise context, the system should be able to explain where that context came from.
