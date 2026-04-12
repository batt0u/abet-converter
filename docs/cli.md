# CLI

## Main Command

```bash
abet-converter --input <file-or-dir> --output <file-or-dir> [--format <fmt> ...]
```

Equivalent direct script:

```bash
python convert.py --input <file-or-dir> --output <file-or-dir> [--format <fmt> ...]
```

## Arguments

- `--input`: source `.ABETdb`, `.mdb`, or directory
- `--output`: output file or output directory depending on the chosen formats
- `--format`: repeatable; allowed values are `sqlite`, `sql`, `csv`, `xlsx`
- `--recursive`: search subfolders when `--input` is a directory
- `--mdbtools-dir`: override the bundled runtime directory

## Output Rules

- file input + only `sqlite` -> `--output` must be a `.sqlite` file
- file input + any other format combination -> `--output` must be a directory
- directory input -> `--output` must be a directory

## Failure Conditions

- input path does not exist
- input directory has no supported files
- bundled runtime for the current platform is missing
- required `mdbtools` executables are missing from the selected runtime
- output path shape does not match the input/format combination
- any target output already exists
