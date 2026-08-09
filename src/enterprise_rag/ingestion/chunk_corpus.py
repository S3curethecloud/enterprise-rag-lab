"""Chunk the Phase 2 enterprise corpus and write inspection artifacts."""

import json
from pathlib import Path

from enterprise_rag.ingestion.chunker import (
    DEFAULT_CHUNK_SIZE,
    DEFAULT_OVERLAP,
    chunk_text,
)


ROOT = Path(__file__).resolve().parents[3]

DOCUMENTS_FILE = ROOT / "data" / "metadata" / "documents.json"
OUTPUT_FILE = ROOT / "artifacts" / "phase-03" / "chunks.json"
STATS_FILE = ROOT / "artifacts" / "phase-03" / "chunk_stats.json"


def load_documents():
    with DOCUMENTS_FILE.open(encoding="utf-8") as handle:
        return json.load(handle)


def main():
    documents = load_documents()

    all_chunks = []
    per_document = {}

    for metadata in documents:
        document_path = ROOT / metadata["path"]
        text = document_path.read_text(encoding="utf-8")

        chunks = chunk_text(
            text,
            document_metadata=metadata,
            chunk_size=DEFAULT_CHUNK_SIZE,
            overlap=DEFAULT_OVERLAP,
        )

        all_chunks.extend(chunks)
        per_document[metadata["document_id"]] = len(chunks)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    OUTPUT_FILE.write_text(
        json.dumps(all_chunks, indent=2),
        encoding="utf-8",
    )

    stats = {
        "document_count": len(documents),
        "chunk_count": len(all_chunks),
        "chunk_size": DEFAULT_CHUNK_SIZE,
        "overlap": DEFAULT_OVERLAP,
        "stride": DEFAULT_CHUNK_SIZE - DEFAULT_OVERLAP,
        "chunks_per_document": per_document,
    }

    STATS_FILE.write_text(
        json.dumps(stats, indent=2),
        encoding="utf-8",
    )

    print(
        f"Chunked {len(documents)} documents "
        f"into {len(all_chunks)} chunks."
    )
    print(f"Chunk size: {DEFAULT_CHUNK_SIZE}")
    print(f"Overlap: {DEFAULT_OVERLAP}")
    print(f"Stride: {DEFAULT_CHUNK_SIZE - DEFAULT_OVERLAP}")
    print(f"Chunks written to: {OUTPUT_FILE}")
    print(f"Stats written to: {STATS_FILE}")


if __name__ == "__main__":
    main()
