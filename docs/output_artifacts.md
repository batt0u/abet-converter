# Output Artifacts

## Default

Default format:

```text
sqlite
```

With file input and default settings:

```text
--input  sample.ABETdb
--output sample.sqlite
```

## Per-Format Outputs

For a source database named `sample.ABETdb`:

- `sqlite` -> `sample.sqlite`
- `sql` -> `sample.sql`
- `csv` -> `sample_csv/<table>.csv`
- `xlsx` -> `sample.xlsx`

For directory input, the tool preserves the relative directory structure under the output root.

## Overwrite Policy

The tool refuses to overwrite existing outputs for all formats.

## Notes

- `csv` writes one file per table
- `xlsx` writes one workbook per source database
- `sql` writes one dump file per source database
