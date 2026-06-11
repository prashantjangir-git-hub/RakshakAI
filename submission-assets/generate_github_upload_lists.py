from __future__ import annotations

from pathlib import Path


ROOT = Path(r"c:\prashant\KANAD heckathon").resolve()
OUT_INCLUDE = ROOT / "submission-assets" / "github-upload-include.txt"
OUT_EXCLUDE = ROOT / "submission-assets" / "github-upload-exclude.txt"


EXCLUDE_DIR_NAMES = {
    ".git",
    ".idea",
    ".pytest_cache",
    ".dart_tool",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    ".gradle",
    "ephemeral",
}

EXCLUDE_FILE_NAMES = {
    ".DS_Store",
    "Thumbs.db",
    "local.properties",
}

EXCLUDE_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".log",
    ".iml",
}


def is_excluded(path: Path) -> bool:
    for part in path.parts:
        if part in EXCLUDE_DIR_NAMES:
            return True
    if path.name in EXCLUDE_FILE_NAMES:
        return True
    if path.suffix in EXCLUDE_SUFFIXES:
        return True
    if path.name == ".env":
        return True
    return False


def main() -> None:
    include: list[str] = []
    exclude: list[str] = []

    for p in ROOT.rglob("*"):
        if p.is_dir():
            continue
        rel = p.relative_to(ROOT).as_posix()
        if is_excluded(p):
            exclude.append(rel)
        else:
            include.append(rel)

    include.sort()
    exclude.sort()

    OUT_INCLUDE.write_text("\n".join(include) + "\n", encoding="utf-8")
    OUT_EXCLUDE.write_text("\n".join(exclude) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
