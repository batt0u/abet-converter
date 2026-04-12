# ABET CONVERTER

Cross-platform, self-contained CLI for converting `.ABETdb` and `.mdb` files into SQLite, SQL dump, CSV, and XLSX.

The repository is designed as a public end-user tool. Bundled `mdbtools` runtimes are shipped inside the repo for Windows, Linux, and macOS so the default workflow stays simple.

## Install

Requirements:

- Python `3.11+`
- no external `mdbtools` install required for supported bundled platforms

Editable install:

```bash
pip install -e .
```

Install from a clone and verify:

```bash
abet-converter --help
```

## Usage

Installed command:

```bash
abet-converter --input C:\data\input.ABETdb --output C:\data\input.sqlite
```

Direct script:

```bash
python convert.py --input C:\data\input.ABETdb --output C:\data\input.sqlite
```

Multiple formats from one file:

```bash
abet-converter --input C:\data\input.ABETdb --output C:\data\exports --format sqlite --format sql --format csv --format xlsx
```

Directory conversion:

```bash
abet-converter --input C:\data\incoming --output C:\data\converted --format sqlite --format csv --recursive
```

## Behavior

- default format is `sqlite`
- file input + only `sqlite` uses a single `.sqlite` file output
- directory input always requires an output directory
- any export including `sql`, `csv`, or `xlsx` requires an output directory
- existing outputs are not overwritten
- `--mdbtools-dir` can override the bundled runtime if needed

## Formats

- `sqlite`: one `.sqlite` per source database
- `sql`: one `.sql` dump per source database
- `csv`: one directory per source database with one `.csv` per table
- `xlsx`: one workbook per source database with one sheet per table

## Docs

- `docs/cli.md`
- `docs/output_artifacts.md`
- `AGENTS.md`

## License

GNU GPL v3 or later

## Validation

```bash
pytest
```
