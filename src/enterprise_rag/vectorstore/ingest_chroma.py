"""Persist Phase 4 embedded enterprise chunks into ChromaDB."""

import json
from pathlib import Path

from enterprise_rag.vectorstore.init_chroma import get_collection
from enterprise_rag.vectorstore.metadata import serialize_metadata


ROOT = Path(__file__).resolve().parents[3]

EMBEDDED_CHUNKS_FILE = (
    ROOT / "artifacts" / "phase-04" / "embedded_chunks.json"
)

SUMMARY_FILE = (
    ROOT / "artifacts" / "phase-05" / "chroma_ingestion_summary.json"
)


def main():
    records = json.loads(
        EMBEDDED_CHUNKS_FILE.read_text(encoding="utf-8")
    )

    collection = get_collection()

    ids = []
    documents = []
    embeddings = []
    metadatas = []

    for record in records:
        ids.append(record["chunk_id"])
        documents.append(record["content"])
        embeddings.append(record["embedding"])

        metadata = serialize_metadata(record["metadata"])
        metadata["document_id"] = record["document_id"]

        metadatas.append(metadata)

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    SUMMARY_FILE.parent.mkdir(parents=True, exist_ok=True)

    summary = {
        "collection": collection.name,
        "input_records": len(records),
        "stored_records": collection.count(),
        "ids": ids,
    }

    SUMMARY_FILE.write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )

    print("Collection:", collection.name)
    print("Input records:", len(records))
    print("Stored records:", collection.count())
    print("Summary:", SUMMARY_FILE)


if __name__ == "__main__":
    main()
