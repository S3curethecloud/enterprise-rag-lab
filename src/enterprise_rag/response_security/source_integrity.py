"""Source-integrity checks for generated responses."""

def validate_sources(
    generation: dict,
    context_package: dict,
) -> dict:
    """Verify that generation sources came from included context."""

    generation_sources = generation.get(
        "sources",
        []
    )

    context_sources = {
        (
            chunk["document_id"],
            chunk["chunk_id"],
        )
        for chunk in context_package.get(
            "included_chunks",
            []
        )
    }

    invalid_sources = []

    for source in generation_sources:
        key = (
            source.get("document_id"),
            source.get("chunk_id"),
        )

        if key not in context_sources:
            invalid_sources.append(source)

    return {
        "valid": len(invalid_sources) == 0,
        "invalid_sources": invalid_sources,
    }
