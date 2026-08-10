# Output DLP

Grounded generation does not guarantee that every generated value is safe to return.

A response-security layer can inspect generated output for sensitive patterns.

## Example

A grounded response contains:

```text
Employee SSN: 123-45-6789

The answer may be grounded.

The disclosure may still be inappropriate.

Response Decision
Generated Answer
      ↓
Sensitive Pattern Inspection
      ↓
REDACT
      ↓
Employee SSN: [REDACTED]
Important Principle

Evidence integrity and disclosure policy are separate questions.

Authorization to retrieve a document does not necessarily imply that every sensitive value should be echoed into every downstream interface.

Educational Scope

The Phase 11 detector is intentionally simple.

Production DLP may use:

structured classifiers;
secret detectors;
entity recognition;
data labels;
contextual policy;
tenant policy;
destination-aware rules.
