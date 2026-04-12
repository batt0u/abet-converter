from __future__ import annotations

import os
import platform
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class MdbtoolsRuntime:
    bundle_dir: Path
    executable_suffix: str
    library_env_var: str | None

    def executable_path(self, base_name: str) -> Path:
        return self.bundle_dir / f"{base_name}{self.executable_suffix}"

    def subprocess_env(self) -> dict[str, str]:
        env = os.environ.copy()
        bundle_path = str(self.bundle_dir)
        env["PATH"] = f"{bundle_path}{os.pathsep}{env.get('PATH', '')}"
        if self.library_env_var:
            env[self.library_env_var] = f"{bundle_path}{os.pathsep}{env.get(self.library_env_var, '')}"
        return env


def normalize_architecture(machine: str) -> str:
    normalized = machine.lower()
    if normalized in {"amd64", "x86_64", "x64"}:
        return "x64"
    if normalized in {"arm64", "aarch64"}:
        return "arm64"
    raise RuntimeError(f"Unsupported architecture for bundled mdbtools: {machine}")


def detect_platform_key() -> tuple[str, str, str, str | None]:
    architecture = normalize_architecture(platform.machine())
    if sys.platform.startswith("win"):
        return "windows", architecture, ".exe", None
    if sys.platform.startswith("linux"):
        return "linux", architecture, "", "LD_LIBRARY_PATH"
    if sys.platform == "darwin":
        return "macos", architecture, "", "DYLD_FALLBACK_LIBRARY_PATH"
    raise RuntimeError(f"Unsupported platform for bundled mdbtools: {sys.platform}")


def resolve_mdbtools_runtime(repo_root: Path, override_dir: Path | None = None) -> MdbtoolsRuntime:
    if override_dir is not None:
        bundle_dir = override_dir.resolve()
        if not bundle_dir.exists():
            raise FileNotFoundError(f"mdbtools override directory not found: {bundle_dir}")
        suffix = ".exe" if any((bundle_dir / f"mdb-tables{ext}").exists() for ext in (".exe",)) else ""
        library_env_var = None
        if sys.platform.startswith("linux"):
            library_env_var = "LD_LIBRARY_PATH"
        elif sys.platform == "darwin":
            library_env_var = "DYLD_FALLBACK_LIBRARY_PATH"
        return MdbtoolsRuntime(bundle_dir=bundle_dir, executable_suffix=suffix, library_env_var=library_env_var)

    os_name, architecture, suffix, library_env_var = detect_platform_key()
    bundle_dir = repo_root / "tools" / "runtime" / os_name / architecture
    if not bundle_dir.exists():
        raise FileNotFoundError(f"Bundled mdbtools runtime not found for {os_name}/{architecture}: {bundle_dir}")
    return MdbtoolsRuntime(bundle_dir=bundle_dir, executable_suffix=suffix, library_env_var=library_env_var)
