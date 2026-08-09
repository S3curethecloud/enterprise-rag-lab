# Access-Control Ground Truth

Before implementing semantic retrieval, we need to define which identities are authorized to access which documents.

This is intentional.

If we wait until vector search exists before deciding authorization semantics, we risk designing access control around whatever the vector database happens to return.

## Core Principle

> Relevance determines whether information can answer the question.
> Authorization determines whether the identity may retrieve the information.

These are independent decisions.

## Example Identities

### Alice — Engineering

```text
user_id = alice
tenant_id = techcorp
groups = Engineering, Employees
Bob — Human Resources
user_id = bob
tenant_id = techcorp
groups = HR, Employees
Carol — Security
user_id = carol
tenant_id = techcorp
groups = Security, Employees
Dana — Finance
user_id = dana
tenant_id = techcorp
groups = Finance, Employees
Erin — Executive
user_id = erin
tenant_id = techcorp
groups = Executive, Employees
Expected Access Matrix
Document	Alice Engineering	Bob HR	Carol Security	Dana Finance	Erin Executive
Company FAQ	ALLOW	ALLOW	ALLOW	ALLOW	ALLOW
Architecture Standards	ALLOW	DENY	DENY	DENY	DENY
Executive Compensation	DENY	ALLOW	DENY	DENY	ALLOW
Incident Response	DENY	DENY	ALLOW	DENY	DENY
FY2027 Forecast	DENY	DENY	DENY	ALLOW	ALLOW
Critical Scenario

Alice asks:

What is the executive compensation policy?

The compensation document may be the best semantic match in the entire corpus.

That does not make Alice authorized.

Question
   │
   ▼
Semantic relevance
   │
   └── executive_compensation.md = HIGH
                         │
                         ▼
                  Authorization
                         │
                         └── Alice / Engineering = DENY

Correct result:

DO NOT RETURN THE DOCUMENT
DO NOT SEND THE CONTENT TO THE LLM
Why This Matters

A weak implementation:

Vector Search
    ↓
Top 5
    ↓
LLM

has no enterprise authorization boundary.

A Secure RAG design eventually becomes:

Identity
    ↓
Tenant / Group / Entitlement
    ↓
Authorized Candidate Set
    +
Semantic Relevance
    ↓
Authorized Top-K
    ↓
Context Validation
    ↓
LLM

We are not implementing this retrieval logic yet.

For now we are defining the expected security behavior that future retrieval code must satisfy.
