from pathlib import Path

import pytest

from abet_converter.cli import main


REPO_ROOT = Path(__file__).resolve().parents[2]
LOCAL_TESTS_DIR = REPO_ROOT / "local-tests"


@pytest.mark.skipif(
    not bool(__import__("os").environ.get("ABET_CONVERTER_RUN_LOCAL_DB_TESTS")),
    reason="Set ABET_CONVERTER_RUN_LOCAL_DB_TESTS=1 to run local real database tests.",
)
def test_local_real_database_can_convert_to_sqlite(tmp_path: Path) -> None:
    sources = sorted(
        path
        for path in LOCAL_TESTS_DIR.glob("*")
        if path.is_file() and path.suffix.lower() in {".abetdb", ".mdb"}
    )

    if not sources:
        pytest.skip("Put a .ABETdb or .mdb file in local-tests/ to run this test.")

    output_path = tmp_path / f"{sources[0].stem}.sqlite"

    exit_code = main(
        [
            "--input",
            str(sources[0]),
            "--output",
            str(output_path),
            "--format",
            "sqlite",
        ]
    )

    assert exit_code == 0
    assert output_path.exists()
    assert output_path.stat().st_size > 0
