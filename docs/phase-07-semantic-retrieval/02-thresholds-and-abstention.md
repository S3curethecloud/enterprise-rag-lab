# Relevance Thresholds and Abstention

Retrieval systems often need a policy for deciding whether nearest-neighbor results are good enough to use.

## Educational Threshold

This phase introduces:

```text
max_distance = 1.20

This is an educational value for the current controlled corpus.

It is not a universal production threshold.

Why Thresholds Must Be Evaluated

A useful production threshold depends on:

embedding model;
vector metric;
corpus;
chunking strategy;
query distribution;
domain;
retrieval requirements.

Thresholds should therefore be measured and calibrated using evaluation data.

Abstention

If no candidate passes the relevance policy:

accepted_results = []

the retrieval system should be able to say:

insufficient relevant context

rather than pretending the nearest chunk must contain the answer.

Important Boundary

Relevance acceptance still does not authorize access.

Later:

semantic candidate
      ↓
relevance accepted
      ↓
authorization check
      ↓
authorized context

