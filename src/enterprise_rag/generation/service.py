"""Grounded generation orchestration for Phase 10."""

from enterprise_rag.authorization.secure_retriever import (
    secure_retrieve,
)
from enterprise_rag.context.assembler import assemble_context
from enterprise_rag.generation.mock_generator import (
    generate_mock_answer,
)
from enterprise_rag.generation.prompt_builder import (
    build_grounded_prompt,
)


def grounded_generate(
    *,
    user_id: str,
    question: str,
    top_k: int = 5,
) -> dict:
    """Run secure retrieval, context assembly, and grounded generation."""

    retrieval = secure_retrieve(
        user_id=user_id,
        query=question,
        top_k=top_k,
    )

    context = assemble_context(
        retrieval["authorized_results"]
    )

    if context["included_count"] == 0:
        generation = generate_mock_answer(
            question=question,
            context_package=context,
        )

        return {
            "identity": retrieval["identity"],
            "question": question,
            "retrieval": retrieval,
            "context": context,
            "prompt": None,
            "generation": generation,
        }

    prompt = build_grounded_prompt(
        question=question,
        context_package=context,
    )

    generation = generate_mock_answer(
        question=question,
        context_package=context,
    )

    return {
        "identity": retrieval["identity"],
        "question": question,
        "retrieval": retrieval,
        "context": context,
        "prompt": prompt,
        "generation": generation,
    }
