from pathlib import Path

import pytest

import src.drivers.mdbtools as mdbtools_module
from src.drivers.mdbtools import detect_platform_key, resolve_mdbtools_runtime


def test_detect_platform_key_windows_x64(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(mdbtools_module.sys, "platform", "win32")
    monkeypatch.setattr(mdbtools_module.platform, "machine", lambda: "AMD64")

    assert detect_platform_key() == ("windows", "x64", ".exe", None)


def test_detect_platform_key_linux_arm64(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(mdbtools_module.sys, "platform", "linux")
    monkeypatch.setattr(mdbtools_module.platform, "machine", lambda: "aarch64")

    assert detect_platform_key() == ("linux", "arm64", "", "LD_LIBRARY_PATH")


def test_resolve_mdbtools_runtime_uses_repo_runtime(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    runtime_dir = tmp_path / "tools" / "runtime" / "linux" / "x64"
    runtime_dir.mkdir(parents=True)
    monkeypatch.setattr(mdbtools_module.sys, "platform", "linux")
    monkeypatch.setattr(mdbtools_module.platform, "machine", lambda: "x86_64")

    runtime = resolve_mdbtools_runtime(tmp_path)

    assert runtime.bundle_dir == runtime_dir
    assert runtime.executable_suffix == ""


def test_resolve_mdbtools_runtime_raises_when_bundle_missing(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setattr(mdbtools_module.sys, "platform", "darwin")
    monkeypatch.setattr(mdbtools_module.platform, "machine", lambda: "arm64")

    with pytest.raises(FileNotFoundError, match="Bundled mdbtools runtime not found"):
        resolve_mdbtools_runtime(tmp_path)
