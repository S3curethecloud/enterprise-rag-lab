"""Deterministic educational text chunker for Phase 3."""

from copy import deepcopy


DEFAULT_CHUNK_SIZE = 500
DEFAULT_OVERLAP = 100


def validate_chunk_parameters(chunk_size: int, overlap: int) -> None:
    """Validate chunking configuration."""

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")

    if overlap < 0:
        raise ValueError("overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")


def chunk_text(
    text: str,
    *,
    document_metadata: dict,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    overlap: int = DEFAULT_OVERLAP,
) -> list[dict]:
    """Split text into deterministic chunks with inherited metadata."""

    validate_chunk_parameters(chunk_size, overlap)

    if not text:
        return []

    stride = chunk_size - overlap
    chunks = []

    for chunk_index, start in enumerate(range(0, len(text), stride)):
        end = min(start + chunk_size, len(text))
        content = text[start:end]

        metadata = deepcopy(document_metadata)
        document_id = metadata["document_id"]

        chunk = {
            "chunk_id": f"{document_id}::chunk::{chunk_index:04d}",
            "document_id": document_id,
            "chunk_index": chunk_index,
            "start_char": start,
            "end_char": end,
            "content": content,
            "metadata": metadata,
        }

        chunks.append(chunk)

        if end >= len(text):
            break

    return chunks
