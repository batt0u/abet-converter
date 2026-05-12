from __future__ import annotations

from pathlib import Path

from abet_converter.interfaces.models import RunContext


def build_run_context(repo_root: Path, run_id: str, dataset_id: str, step_name: str) -> RunContext:
    root_dir = repo_root / "build" / "runs" / run_id
    context = RunContext(
        run_id=run_id,
        dataset_id=dataset_id,
        step_name=step_name,
        root_dir=root_dir,
        inputs_dir=root_dir / "inputs",
        intermediate_dir=root_dir / "intermediate",
        outputs_dir=root_dir / "outputs",
        logs_dir=root_dir / "logs",
        manifest_dir=root_dir / "manifest",
    )
    for directory in (
        context.root_dir,
        context.inputs_dir,
        context.intermediate_dir,
        context.outputs_dir,
        context.logs_dir,
        context.manifest_dir,
    ):
        directory.mkdir(parents=True, exist_ok=True)
    return context
