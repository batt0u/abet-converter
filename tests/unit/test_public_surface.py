from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
EXPECTED_DOCS = {
    "AGENTS.md",
    "README.md",
    "abet_converter_packaging_plan.md",
    "docs/cli.md",
    "docs/output_artifacts.md",
}


def test_public_documentation_surface_is_minimal() -> None:
    markdown_files = {
        path.relative_to(REPO_ROOT).as_posix()
        for path in REPO_ROOT.glob("**/*.md")
        if ".pytest_cache" not in path.parts
    }

    assert markdown_files == EXPECTED_DOCS
