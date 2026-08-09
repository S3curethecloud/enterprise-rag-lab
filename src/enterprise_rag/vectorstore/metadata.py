"""Serialize and deserialize enterprise metadata for ChromaDB."""

GROUP_SEPARATOR = "|"


def serialize_metadata(metadata: dict) -> dict:
    """Convert enterprise metadata into Chroma-compatible scalar values."""

    result = dict(metadata)

    groups = result.get("allowed_groups", [])

    if not isinstance(groups, list):
        raise TypeError("allowed_groups must be a list")

    result["allowed_groups"] = GROUP_SEPARATOR.join(groups)

    return result


def deserialize_metadata(metadata: dict) -> dict:
    """Restore structured enterprise metadata from Chroma values."""

    result = dict(metadata)

    groups = result.get("allowed_groups", "")

    if groups:
        result["allowed_groups"] = groups.split(GROUP_SEPARATOR)
    else:
        result["allowed_groups"] = []

    return result
