"""Generate embeddings for the Phase 3 enterprise chunks."""

import json
from pathlib import Path

from enterprise_rag.embeddings.embedder import (
    DEFAULT_MODEL_NAME,
    embed_text,
)


ROOT = Path(__file__).resolve().parents[3]

CHUNKS_FILE = ROOT / "artifacts" / "phase-03" / "chunks.json"
OUTPUT_FILE = ROOT / "artifacts" / "phase-04" / "embedded_chunks.json"
SUMMARY_FILE = ROOT / "artifacts" / "phase-04" / "embedding_summary.json"


def main():
    chunks = json.loads(
        CHUNKS_FILE.read_text(encoding="utf-8")
    )

    embedded_chunks = []

    for chunk in chunks:
        vector = embed_text(chunk["content"])

        embedded_chunks.append(
            {
                "chunk_id": chunk["chunk_id"],
                "document_id": chunk["document_id"],
                "content": chunk["content"],
                "embedding": vector,
                "metadata": chunk["metadata"],
            }
        )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    OUTPUT_FILE.write_text(
        json.dumps(embedded_chunks, indent=2),
        encoding="utf-8",
    )

    dimensions = {
        len(record["embedding"])
        for record in embedded_chunks
    }

    summary = {
        "model": DEFAULT_MODEL_NAME,
        "chunk_count": len(embedded_chunks),
        "embedding_dimensions": sorted(dimensions),
        "security_metadata_preserved": True,
    }

    SUMMARY_FILE.write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )

    print(
        f"Embedded {len(embedded_chunks)} enterprise chunks."
    )

    print(
        "Embedding dimensions:",
        sorted(dimensions),
    )

    print(
        "Embedded chunks written to:",
        OUTPUT_FILE,
    )

    print(
        "Summary written to:",
        SUMMARY_FILE,
    )


if __name__ == "__main__":
    main()
