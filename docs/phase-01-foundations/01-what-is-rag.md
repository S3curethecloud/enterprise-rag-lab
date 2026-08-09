# What Is Retrieval-Augmented Generation?

Large language models generate responses using information represented in their model parameters and information provided in their current context.

They do not automatically know an organization's private documents.

Suppose TechCorp has:

```text
Employee Handbook
Architecture Standards
Security Policies
Meeting Notes
Product Specifications
FAQs

A language model does not automatically gain access to these documents.

RAG provides a mechanism for finding relevant enterprise information and supplying that information to the model.

Basic Mental Model
User Question
      │
      ▼
Retrieve relevant information
      │
      ▼
Add information to model context
      │
      ▼
Generate an answer

This produces the name:

Retrieval
    +
Augmentation
    +
Generation
Retrieval Is Not Generation

The retriever answers:

Which information is relevant?

The model answers:

Given this approved information, how should I answer the user?

These are separate responsibilities.

Why Enterprises Use RAG

RAG can help applications use:

private enterprise knowledge;
frequently changing information;
domain-specific documentation;
controlled data sources;
source citations.
RAG Does Not Automatically Make AI Safe

Adding retrieval does not automatically solve:

hallucination;
authorization;
data leakage;
poisoned documents;
prompt injection;
tenant isolation.

Those require additional controls.

Knowledge Check

Explain in your own words:

Why doesn't the language model automatically know TechCorp's handbook?
What does retrieval do?
What does generation do?
Why are retrieval and generation separate architectural responsibilities?
