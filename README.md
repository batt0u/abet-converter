# ABET CONVERTER

Cross-platform, self-contained CLI for converting `.ABETdb` and `.mdb` files into SQLite, SQL dump, CSV, and XLSX.

The repository is designed as a public end-user tool. Bundled `mdbtools` runtimes are shipped inside the repo for Windows, Linux, and macOS so the default workflow stays simple.

## Installation

Requirements:

- Python `3.11+`
- no external `mdbtools` install required for supported bundled platforms

### Recommended: pipx

```bash
pipx install abet-converter
```

### pip

```bash
python -m pip install abet-converter
```

### From source

```bash
git clone https://github.com/vcanonici/abet-converter.git
cd abet-converter
python -m pip install -e .
```

Verify:

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

## Citation

If you use `ABET CONVERTER` in research, please cite the repository in your paper, thesis, report, or dataset note.

BibTeX:

```bibtex
@software{canonici_abet_converter_2026,
  author = {Canonici, Vinicius Garcia},
  title = {ABET CONVERTER},
  year = {2026},
  version = {0.3.1},
  url = {https://github.com/vcanonici/abet-converter},
  note = {Cross-platform CLI to convert ABET and MDB databases into SQLite, SQL, CSV, and XLSX}
}
```

The repository also ships `CITATION.cff` and `citation.bib` for direct reuse.

If the tool helps your work and you like the project, please consider giving the repository a star on GitHub.

## License

GNU GPL v3 or later

## Validation

```bash
pytest
```
