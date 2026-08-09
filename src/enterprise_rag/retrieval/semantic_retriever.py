"""Reusable semantic retrieval service for Phase 7."""

from enterprise_rag.embeddings.embedder import embed_text
from enterprise_rag.vectorstore.init_chroma import get_collection
from enterprise_rag.vectorstore.metadata import deserialize_metadata


def retrieve(query: str, top_k: int = 3) -> list[dict]:
    """Retrieve semantically nearest enterprise chunks."""

    if not isinstance(query, str):
        raise TypeError("query must be a string")

    if not query.strip():
        raise ValueError("query cannot be empty")

    if top_k <= 0:
        raise ValueError("top_k must be greater than zero")

    collection = get_collection()

    available_records = collection.count()

    if available_records == 0:
        return []

    result_count = min(top_k, available_records)

    query_embedding = embed_text(query)

    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=result_count,
        include=[
            "documents",
            "metadatas",
            "distances",
        ],
    )

    retrieved = []

    for index, chunk_id in enumerate(result["ids"][0]):
        metadata = deserialize_metadata(
            result["metadatas"][0][index]
        )

        retrieved.append(
            {
                "rank": index + 1,
                "chunk_id": chunk_id,
                "document_id": metadata["document_id"],
                "distance": result["distances"][0][index],
                "content": result["documents"][0][index],
                "metadata": metadata,
            }
        )

    return retrieved
