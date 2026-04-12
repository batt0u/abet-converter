# AGENTS

## Purpose

This repository is the public home of `ABET CONVERTER`.

The product is a simple cross-platform CLI that converts `.ABETdb` and `.mdb` databases into:

- `sqlite`
- `sql`
- `csv`
- `xlsx`

The repository should stay focused on the tool itself. Do not turn it back into a research pipeline repository.

## Product Rules

- The public command is `abet-converter`.
- The public wrapper script is `convert.py`.
- The default user flow must stay simple.
- Bundled runtimes in `tools/runtime/` are part of the product.
- Avoid adding workflow concepts such as `runId`, manifests, lineage, audit trees, or dataset staging back into the public CLI.
- Prefer changes that improve portability, usability, determinism, and output correctness.

## Repository Scope

Keep the repository centered on:

- CLI behavior
- conversion logic
- runtime resolution
- public documentation
- packaging
- tests

Avoid adding:

- internal research notes
- sensitive example datasets
- methodology documents tied to private data
- operational logs or generated outputs

## Installation

### Requirements

- Python `3.11+`

### Standard Install

```bash
pip install -e .
```

### Verify Install

```bash
abet-converter --help
```

### Direct Script

```bash
python convert.py --help
```

## Development Rules

- Keep the CLI interface simple: `--input`, `--output`, `--format`, `--recursive`, `--mdbtools-dir`.
- Do not silently overwrite user outputs.
- Keep format behavior explicit and documented.
- Preserve cross-platform runtime selection for Windows, Linux, and macOS.
- If a platform bundle changes, update tests and public docs in the same change.
- Do not add private sample data to the repository.

## Structure

- `src/`: product code
- `tests/`: unit and smoke-oriented tests
- `tools/runtime/`: bundled `mdbtools` runtimes by platform
- `docs/`: small public docs for CLI and output behavior

## Validation

Before publishing relevant code changes, run:

```bash
pytest
```

If packaging changed, also run:

```bash
pip install -e .
```

## Documentation Rules

- `README.md` is the main public landing page.
- `docs/cli.md` documents arguments and examples.
- `docs/output_artifacts.md` documents output layout and file behavior.
- Keep docs generic and safe for public publication.

## Licensing

This repository is licensed under the GNU GPL v3 or later.
Bundled third-party runtime files may carry their own upstream licenses inside `tools/runtime/`.
