# Control Ownership Matrix

Enterprise Secure RAG requires ownership across multiple disciplines.

| Control Area | Primary Owner | Supporting Owners |
|---|---|---|
| Source onboarding | Data Platform | Security, Data Governance |
| Source trust | Security | Data Platform |
| Classification | Data Governance | Security, Business Owner |
| ACL metadata | Identity / Application | Data Owner |
| Ingestion pipeline | AI Platform | Data Platform |
| Embeddings | AI Platform | Application Engineering |
| Vector infrastructure | Platform Engineering | Security |
| Identity | IAM | Security |
| Retrieval authorization | Application Security | IAM, AI Platform |
| Context security | AI Platform | Security |
| Grounding policy | AI Platform | Product |
| Output DLP | Security | Data Governance |
| API integration | Application Engineering | AI Platform |
| Evaluation | AI Platform | Security, QA |
| Observability | Platform Engineering | Security |
| Incident response | Security Operations | AI Platform |
| Model governance | AI Governance | Security, Legal, Risk |

## Principle

> Secure RAG is a shared-control system.

No single team owns every security decision.
