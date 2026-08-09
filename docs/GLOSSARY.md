# RAG Glossary

## Retrieval-Augmented Generation — RAG

A pattern in which external information is retrieved and supplied to a language model as context for generating an answer.

## Retrieval

Finding information relevant to a query.

Retrieval happens before generation.

## Augmentation

Adding retrieved information to the model's context.

## Generation

The language model synthesizing an answer from instructions, the user question, and approved context.

## Embedding

A numeric vector representation of content intended to preserve semantic relationships.

## Vector

An ordered collection of numeric values.

## Similarity Search

Searching for vectors that are mathematically close to the query vector.

## Semantic Search

Search based on meaning rather than exact keyword matches.

## Chunk

A smaller section of a larger source document used for indexing and retrieval.

## Chunk Size

The maximum target size of a chunk.

## Chunk Overlap

Content intentionally repeated between adjacent chunks to reduce loss of context across boundaries.

## Stride

The amount the chunking window moves between chunks.

For fixed-size chunking:

```text
stride = chunk_size - overlap
Vector Database

A data store optimized for storing vectors and performing similarity searches.

Metadata

Structured attributes associated with a document or chunk.

Examples:

tenant
owner
classification
document ID
ACL
source
timestamp
ACL

Access Control List.

Describes which identities or groups are permitted to access a resource.

Provenance

Evidence describing where information originated and how it entered the knowledge system.

Grounding

Constraining a generated response to available evidence.

Hallucination

Generated content that is unsupported, incorrect, or invented.

Prompt Injection

Instructions intended to manipulate model behavior contrary to system policy.

Indirect Prompt Injection

Malicious instructions contained in external content retrieved or supplied to the model rather than directly written by the user.

Tenant

An isolated organizational or customer security boundary in a multi-tenant system.

Top-K

The number of highest-ranked retrieval candidates returned by a search.

DLP

Data Loss Prevention.

Controls designed to detect or prevent inappropriate disclosure of sensitive information.
