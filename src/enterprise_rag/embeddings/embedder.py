"""Local embedding utilities for Phase 4."""

from functools import lru_cache

import numpy as np
from sentence_transformers import SentenceTransformer


DEFAULT_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def get_model() -> SentenceTransformer:
    """Load and cache the local sentence-transformer model."""

    return SentenceTransformer(DEFAULT_MODEL_NAME)


def embed_text(text: str) -> list[float]:
    """Generate a normalized embedding for one string."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text.strip():
        raise ValueError("text cannot be empty")

    model = get_model()

    vector = model.encode(
        text,
        normalize_embeddings=True,
    )

    return vector.tolist()


def cosine_similarity(
    vector_a: list[float],
    vector_b: list[float],
) -> float:
    """Calculate cosine similarity between two vectors."""

    a = np.asarray(vector_a, dtype=float)
    b = np.asarray(vector_b, dtype=float)

    if a.shape != b.shape:
        raise ValueError("vectors must have the same dimensions")

    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        raise ValueError("zero-length vectors cannot be compared")

    return float(np.dot(a, b) / denominator)
