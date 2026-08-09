# Source Attribution

Grounded generation should preserve evidence lineage.

Each generated answer should be traceable to the retrieval objects used as context.

## Source Record

This tutorial preserves:

- document_id;
- chunk_id;
- source path;
- owner.

This supports:

- auditability;
- debugging;
- source inspection;
- evaluation;
- user-facing citations later.

## Principle

> An enterprise RAG answer should be explainable in terms of the evidence used to generate it.

Source attribution does not prove that an answer is correct.

It proves which evidence was supplied to generation.
