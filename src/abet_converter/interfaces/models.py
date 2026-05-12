from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class ArtifactRecord:
    path: str
    category: str
    kind: str
    sha256: str
    size_bytes: int


@dataclass(slots=True)
class RunContext:
    run_id: str
    dataset_id: str
    step_name: str
    root_dir: Path
    inputs_dir: Path
    intermediate_dir: Path
    outputs_dir: Path
    logs_dir: Path
    manifest_dir: Path


@dataclass(slots=True)
class PipelineStepResult:
    command: list[str]
    returncode: int
    stdout: str
    stderr: str
    parameters: dict[str, Any] = field(default_factory=dict)
    artifacts: list[ArtifactRecord] = field(default_factory=list)
