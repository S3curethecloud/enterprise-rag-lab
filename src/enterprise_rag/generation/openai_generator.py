"""Optional live OpenAI generator for Phase 10."""

import os

from openai import OpenAI


def generate_with_openai(
    *,
    prompt: str,
    model: str = "gpt-4.1-mini",
) -> str:
    """Generate an answer using OpenAI when explicitly configured."""

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is required for live generation"
        )

    client = OpenAI()

    response = client.responses.create(
        model=model,
        input=prompt,
    )

    return response.output_text
