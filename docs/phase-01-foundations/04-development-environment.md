# Development Environment

This tutorial uses Python and `uv` for dependency and environment management.

## Why Use a Virtual Environment?

Python projects often depend on different versions of the same packages.

A virtual environment isolates the dependencies for this repository from the operating system and other Python projects.

## Why Use uv?

`uv` provides fast Python project and dependency management while supporting reproducible environments.

## Core Tutorial Dependencies

This course will eventually use:

- ChromaDB — vector storage
- sentence-transformers — local embeddings
- OpenAI SDK — model integration
- Flask — educational web interface
- pytest — automated verification

Not every package will be used immediately.

The course introduces each dependency only when the relevant architectural concept has been taught.

## Environment Setup

From the repository root:

```bash
python3 --version

Then verify uv:

uv --version

If uv is not installed:

python3 -m pip install --user uv

Create the environment:

uv venv

Activate it:

source .venv/bin/activate

Verify:

python --version
which python

The Python executable should resolve inside:

enterprise-rag-lab/.venv/
Install Project Dependencies

After pyproject.toml has been created:

uv sync
Run Tests
uv run pytest -v

The environment is considered ready only when all Phase 1 tests pass.
