"""Relevance acceptance policy for Phase 7."""

DEFAULT_MAX_DISTANCE = 1.20


def is_relevant(
    distance: float,
    max_distance: float = DEFAULT_MAX_DISTANCE,
) -> bool:
    """Return whether a retrieval result passes the distance threshold."""

    if distance < 0:
        raise ValueError("distance cannot be negative")

    if max_distance <= 0:
        raise ValueError("max_distance must be greater than zero")

    return distance <= max_distance


def filter_relevant(
    results: list[dict],
    max_distance: float = DEFAULT_MAX_DISTANCE,
) -> list[dict]:
    """Return only retrieval results that pass the relevance threshold."""

    return [
        result
        for result in results
        if is_relevant(
            result["distance"],
            max_distance=max_distance,
        )
    ]
