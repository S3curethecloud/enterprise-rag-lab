# Production-Readiness Gaps

This repository is an enterprise-oriented educational reference architecture.

It is not yet a production deployment.

## Authentication

Current:

```text
simulated user_id

Production:

enterprise IdP;
OIDC/OAuth;
signed claims;
service identity;
token validation.
Authorization

Current:

fixture-based tenant + group ACL

Production may require:

directory integration;
document-level ACL synchronization;
dynamic policy;
role and attribute-based access control;
entitlement revocation;
cache invalidation.
Vector Database

Current:

local persistent ChromaDB

Production considerations:

managed or hardened vector infrastructure;
encryption;
backup;
HA;
tenant isolation;
access control;
lifecycle management.
Model Hosting

Current:

deterministic mock generation;
optional live OpenAI integration.

Production requires explicit decisions around:

model provider;
region;
data handling;
retention;
contractual controls;
model routing;
availability;
cost;
latency.
DLP

Current:

deterministic pattern matching.

Production may require:

enterprise DLP;
secret scanning;
PII classification;
entity recognition;
contextual policy.
Prompt Injection

Current:

educational deterministic pattern checks.

Production requires broader controls including:

source trust;
contextual instruction detection;
structured content handling;
content provenance;
adversarial testing;
ongoing evaluation.
Observability

Current:

JSON evidence artifacts.

Production requires:

centralized logging;
tracing;
metrics;
alerting;
correlation IDs;
SIEM integration;
retention policy.
Deployment

Current:

local Flask development application.

Production requires:

hardened application server;
TLS;
secrets management;
network controls;
containerization;
CI/CD;
infrastructure as code;
vulnerability management;
environment separation.
Governance

Production systems also require:

control ownership;
risk acceptance;
change management;
data governance;
incident response;
model governance;
evaluation governance.
