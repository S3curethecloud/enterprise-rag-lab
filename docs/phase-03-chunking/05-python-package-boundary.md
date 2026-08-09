# Engineering Note — Python Package Boundary

During Phase 3, the first attempt to execute:

```bash
uv run python -m enterprise_rag.ingestion.chunk_corpus

failed with:

ModuleNotFoundError: No module named 'enterprise_rag'
Why Tests Initially Worked

The pytest configuration contained:

[tool.pytest.ini_options]
pythonpath = ["src"]

This allowed pytest to locate the package.

However, normal Python execution did not receive that pytest-specific path configuration.

Correct Fix

The project was configured as a real Python package:

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/enterprise_rag"]

Then:

uv sync

installed the local project into the virtual environment.

Lesson

Development environments should not depend on hidden path behavior.

If code is intended to run as:

python -m package.module

the package should be properly installed and reproducible.

This is an engineering-quality lesson rather than a RAG-specific lesson, but it matters for building reliable AI platforms.
