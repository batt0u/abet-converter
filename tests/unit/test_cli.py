from pathlib import Path

import pytest

from abet_converter.components.ingest.abet_to_sqlite import normalize_formats
from abet_converter.cli import _validate_output_path, build_parser


def test_cli_exposes_abet_converter_interface() -> None:
    parser = build_parser()

    args = parser.parse_args(
        [
            "--input",
            "C:\\data\\input.ABETdb",
            "--output",
            "C:\\data\\exports",
            "--format",
            "sqlite",
            "--format",
            "csv",
            "--recursive",
        ]
    )

    assert args.input_path == Path("C:\\data\\input.ABETdb")
    assert args.output_path == Path("C:\\data\\exports")
    assert args.formats == ["sqlite", "csv"]
    assert args.recursive is True


def test_validate_output_path_rejects_directory_output_for_file_sqlite_only(tmp_path: Path) -> None:
    input_file = tmp_path / "input.ABETdb"
    output_dir = tmp_path / "out"
    input_file.write_text("x", encoding="utf-8")
    output_dir.mkdir()

    with pytest.raises(ValueError, match="file path"):
        _validate_output_path(input_file, output_dir, ("sqlite",))


def test_validate_output_path_rejects_file_output_for_directory_input(tmp_path: Path) -> None:
    input_dir = tmp_path / "incoming"
    output_file = tmp_path / "out.sqlite"
    input_dir.mkdir()
    output_file.write_text("x", encoding="utf-8")

    with pytest.raises(ValueError, match="directory"):
        _validate_output_path(input_dir, output_file, ("sqlite",))


def test_validate_output_path_rejects_file_output_for_multi_format_file_input(tmp_path: Path) -> None:
    input_file = tmp_path / "input.ABETdb"
    output_file = tmp_path / "out.sqlite"
    input_file.write_text("x", encoding="utf-8")
    output_file.write_text("x", encoding="utf-8")

    with pytest.raises(ValueError, match="directory"):
        _validate_output_path(input_file, output_file, ("sqlite", "csv"))


def test_normalize_formats_defaults_to_sqlite() -> None:
    assert normalize_formats(None) == ("sqlite",)
