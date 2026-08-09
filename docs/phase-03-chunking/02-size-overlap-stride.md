# Chunk Size, Overlap, and Stride

This tutorial begins with a simple character-based chunking strategy so the mechanics are visible.

Later, more advanced strategies can use tokens, paragraphs, headings, or semantic boundaries.

## Initial Parameters

```text
chunk_size = 500
overlap = 100
stride = 400

The relationship is:

stride = chunk_size - overlap

Therefore:

500 - 100 = 400
Visualization
Chunk 0
0 ------------------------------------------------ 500

Chunk 1
                                        400 ------------------------------------------------ 900
                                        |----100----|

Chunk 2
                                                                                800 ...

The repeated 100 characters provide context across adjacent boundaries.

Why Overlap Exists

Imagine a sentence begins near the end of one chunk:

Employees may work remotely when their manager...

and continues in the next:

...approves the department's hybrid work schedule.

Without overlap, the relationship may be fragmented.

Overlap reduces this problem.

Important Clarification

Overlap and stride are not interchangeable terms.

chunk_size = 500
overlap = 100
stride = 400

If overlap were 400 instead, stride would be:

500 - 400 = 100

That would produce dramatically more chunks.

Learning Point

Chunking parameters affect:

retrieval recall;
retrieval precision;
index size;
embedding cost;
latency;
context quality.

They should be measured rather than chosen blindly.
