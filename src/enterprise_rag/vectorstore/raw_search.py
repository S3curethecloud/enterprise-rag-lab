"""Demonstrate raw vector similarity retrieval without authorization."""

import json
from pathlib import Path

from enterprise_rag.embeddings.embedder import embed_text
from enterprise_rag.vectorstore.init_chroma import get_collection
from enterprise_rag.vectorstore.metadata import deserialize_metadata


ROOT = Path(__file__).resolve().parents[3]

OUTPUT_FILE = (
    ROOT
    / "artifacts"
    / "phase-05"
    / "raw_unfiltered_search.json"
)


def main():
    query = "What is the executive compensation policy?"

    query_embedding = embed_text(query)

    collection = get_collection()

    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=5,
        include=["documents", "metadatas", "distances"],
    )

    output = {
        "query": query,
        "authorization_filter_applied": False,
        "warning": "NO AUTHORIZATION FILTER APPLIED",
        "results": [],
    }

    for index, chunk_id in enumerate(result["ids"][0]):
        output["results"].append(
            {
                "rank": index + 1,
                "chunk_id": chunk_id,
                "distance": result["distances"][0][index],
                "metadata": deserialize_metadata(
                    result["metadatas"][0][index]
                ),
            }
        )

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_FILE.write_text(
        json.dumps(output, indent=2),
        encoding="utf-8",
    )

    print(json.dumps(output, indent=2))
    print()
    print("Evidence artifact:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
