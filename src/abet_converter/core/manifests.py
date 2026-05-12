from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from abet_converter.interfaces.models import ArtifactRecord, PipelineStepResult, RunContext
from abet_converter.services.checksums import sha256_file


def register_artifact(path: Path, category: str, kind: str) -> ArtifactRecord:
    return ArtifactRecord(
        path=str(path),
        category=category,
        kind=kind,
        sha256=sha256_file(path),
        size_bytes=path.stat().st_size,
    )


def write_run_manifest(context: RunContext, result: PipelineStepResult) -> Path:
    payload: dict[str, Any] = {
        "run_id": context.run_id,
        "dataset_id": context.dataset_id,
        "step_name": context.step_name,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "command": result.command,
        "parameters": result.parameters,
        "returncode": result.returncode,
        "artifacts": [asdict(artifact) for artifact in result.artifacts],
    }
    target = context.manifest_dir / "run_manifest.json"
    target.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")
    return target


def write_lineage(context: RunContext, inputs: list[str], outputs: list[ArtifactRecord]) -> Path:
    payload = {
        "run_id": context.run_id,
        "dataset_id": context.dataset_id,
        "step_name": context.step_name,
        "inputs": inputs,
        "outputs": [asdict(artifact) for artifact in outputs],
    }
    target = context.manifest_dir / "lineage.json"
    target.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")
    return target


def write_summary(context: RunContext, result: PipelineStepResult) -> Path:
    lines = [
        f"# Summary - {context.step_name}",
        "",
        f"- run_id: `{context.run_id}`",
        f"- dataset_id: `{context.dataset_id}`",
        f"- returncode: `{result.returncode}`",
        "",
        "## Command",
        "",
        f"`{' '.join(result.command)}`",
        "",
        "## Artifacts",
        "",
    ]
    for artifact in result.artifacts:
        lines.append(f"- `{artifact.category}` | `{artifact.kind}` | `{artifact.path}`")
    lines.extend(["", "## Stdout", "", "```text", result.stdout.strip(), "```", "", "## Stderr", "", "```text", result.stderr.strip(), "```"])
    target = context.outputs_dir / "summary.md"
    target.write_text("\n".join(lines), encoding="utf-8")
    return target
