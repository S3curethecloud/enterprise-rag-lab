"""Initialize the persistent ChromaDB collection for Phase 5."""

from pathlib import Path

import chromadb


ROOT = Path(__file__).resolve().parents[3]
CHROMA_PATH = ROOT / "chroma_db"
COLLECTION_NAME = "techcorp_docs"


def get_client():
    """Return the persistent ChromaDB client."""

    CHROMA_PATH.mkdir(parents=True, exist_ok=True)

    return chromadb.PersistentClient(
        path=str(CHROMA_PATH)
    )


def get_collection():
    """Create or reopen the enterprise document collection."""

    client = get_client()

    return client.get_or_create_collection(
        name=COLLECTION_NAME
    )


def main():
    collection = get_collection()

    print("ChromaDB path:", CHROMA_PATH)
    print("Collection:", collection.name)
    print("Current record count:", collection.count())


if __name__ == "__main__":
    main()
