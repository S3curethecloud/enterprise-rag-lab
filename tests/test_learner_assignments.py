"""Learner-assignment coverage tests."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PHASE_DIRECTORIES = [
    "phase-01-foundations",
    "phase-02-enterprise-data",
    "phase-03-chunking",
    "phase-04-embeddings",
    "phase-05-vector-database",
    "phase-06-secure-ingestion",
    "phase-07-semantic-retrieval",
    "phase-08-identity-acl-retrieval",
    "phase-09-secure-context",
    "phase-10-grounded-generation",
    "phase-11-response-security",
    "phase-12-evaluation-red-team",
    "phase-13-flask-application",
    "phase-14-enterprise-architecture",
]

REQUIRED_SECTIONS = [
    "## 1. Memory Analogy",
    "## 2. Thesis Challenge",
    "## 3. Research Questions",
    "## 4. Architecture Reasoning",
    "## 5. Failure Thought Experiment",
    "## 6. Written Assignment",
    "## 7. Teach-It-Back Challenge",
    "## 8. Break the Architecture",
    "## 9. Connection to the Learning Journey",
    "## 10. Memory Check",
]


def assignment_path(phase):
    return DOCS / phase / "ASSIGNMENT.md"


def test_master_assignment_guide_exists():
    assert (DOCS / "LEARNER_ASSIGNMENTS.md").is_file()


def test_every_phase_has_assignment():
    missing = [
        phase
        for phase in PHASE_DIRECTORIES
        if not assignment_path(phase).is_file()
    ]

    assert missing == []


def test_every_assignment_has_learning_structure():
    failures = {}

    for phase in PHASE_DIRECTORIES:
        content = assignment_path(phase).read_text(
            encoding="utf-8"
        )

        missing = [
            section
            for section in REQUIRED_SECTIONS
            if section not in content
        ]

        if missing:
            failures[phase] = missing

    assert failures == {}


def test_every_assignment_requires_original_analogy():
    for phase in PHASE_DIRECTORIES:
        content = assignment_path(phase).read_text(
            encoding="utf-8"
        )

        assert "create a **different analogy of your own**" in content


def test_capstone_preserves_core_security_rule():
    content = assignment_path(
        "phase-14-enterprise-architecture"
    ).read_text(
        encoding="utf-8"
    )

    assert (
        "The LLM never grants access to enterprise data."
        in content
    )

    assert (
        "Authorization occurs before retrieved context reaches the model."
        in content
    )


def test_every_assignment_has_single_memory_check():
    for phase in PHASE_DIRECTORIES:
        content = assignment_path(phase).read_text(
            encoding="utf-8"
        )

        assert content.count("## 10. Memory Check") == 1


def test_every_assignment_has_submission_and_grading_sections():
    for phase in PHASE_DIRECTORIES:
        content = assignment_path(phase).read_text(
            encoding="utf-8"
        )

        assert "## Submission Checklist" in content
        assert "## Grading Guide" in content


def test_every_assignment_has_balanced_code_fences():
    for phase in PHASE_DIRECTORIES:
        content = assignment_path(phase).read_text(
            encoding="utf-8"
        )

        assert content.count("```") % 2 == 0
