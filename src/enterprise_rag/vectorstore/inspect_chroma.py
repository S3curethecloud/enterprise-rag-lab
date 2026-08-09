"""Inspect one persisted ChromaDB retrieval record."""

import json

from enterprise_rag.vectorstore.init_chroma import get_collection
from enterprise_rag.vectorstore.metadata import deserialize_metadata


def main():
    collection = get_collection()

    result = collection.get(
        ids=["hr-compensation-001::chunk::0000"],
        include=["documents", "metadatas"],
    )

    if not result["ids"]:
        raise RuntimeError("HR compensation chunk not found")

    metadata = deserialize_metadata(
        result["metadatas"][0]
    )

    output = {
        "chunk_id": result["ids"][0],
        "document": result["documents"][0],
        "metadata": metadata,
    }

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
