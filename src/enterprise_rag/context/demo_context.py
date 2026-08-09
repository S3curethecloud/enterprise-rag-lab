"""Demonstrate secure context assembly using authorized retrieval."""

import json
from pathlib import Path

from enterprise_rag.authorization.secure_retriever import (
    secure_retrieve,
)
from enterprise_rag.context.assembler import assemble_context


ROOT = Path(__file__).resolve().parents[3]

OUTPUT_FILE = (
    ROOT
    / "artifacts"
    / "phase-09"
    / "secure_context_demo.json"
)


def main():
    retrieval = secure_retrieve(
        user_id="bob",
        query="What is the executive compensation policy?",
        top_k=5,
    )

    context = assemble_context(
        retrieval["authorized_results"]
    )

    output = {
        "identity": retrieval["identity"],
        "query": retrieval["query"],
        "context": context,
    }

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    OUTPUT_FILE.write_text(
        json.dumps(output, indent=2),
        encoding="utf-8",
    )

    print("User:", retrieval["identity"]["user_id"])
    print("Query:", retrieval["query"])
    print("Authorized results:", retrieval["authorized_result_count"])
    print("Context chunks:", context["included_count"])
    print("Rejected chunks:", context["rejected_count"])
    print("Context chars:", context["used_context_chars"])
    print()
    print("Evidence artifact:", OUTPUT_FILE)


if __name__ == "__main__":
    main()
