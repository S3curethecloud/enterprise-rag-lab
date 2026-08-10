"""Evaluation result models for Phase 12."""

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class EvaluationResult:
    scenario: str
    control_area: str
    expected: Any
    actual: Any
    passed: bool
    evidence: dict

    def to_dict(self) -> dict:
        return asdict(self)
