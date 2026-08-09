"""Phase 1 development-environment verification tests."""

from importlib.util import find_spec
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_virtual_environment_directory_exists():
    """The tutorial should use an isolated Python environment."""
    assert (ROOT / ".venv").is_dir()


def test_pyproject_exists():
    """Project dependencies must be declared reproducibly."""
    assert (ROOT / "pyproject.toml").is_file()


def test_chromadb_is_installed():
    assert find_spec("chromadb") is not None


def test_sentence_transformers_is_installed():
    assert find_spec("sentence_transformers") is not None


def test_openai_is_installed():
    assert find_spec("openai") is not None


def test_flask_is_installed():
    assert find_spec("flask") is not None


def test_phase_one_documentation_exists():
    required_docs = [
        ROOT / "docs" / "COURSE_OVERVIEW.md",
        ROOT / "docs" / "SECURE_RAG_MENTAL_MODEL.md",
        ROOT / "docs" / "GLOSSARY.md",
        ROOT / "docs" / "phase-01-foundations" / "README.md",
        ROOT / "docs" / "phase-01-foundations" / "01-what-is-rag.md",
        ROOT / "docs" / "phase-01-foundations" / "02-rag-vs-semantic-search.md",
        ROOT / "docs" / "phase-01-foundations" / "03-rag-data-flow.md",
        ROOT / "docs" / "phase-01-foundations" / "04-development-environment.md",
    ]

    missing = [str(path) for path in required_docs if not path.is_file()]

    assert not missing, f"Missing Phase 1 documentation: {missing}"
