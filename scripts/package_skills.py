#!/usr/bin/env python3
"""Create deterministic per-skill upload packages and a library archive."""

from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
DEFAULT_OUTPUT = ROOT / "skills.zip"
DEFAULT_DIST = ROOT / "dist"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)


def write_archive(output: Path, files: list[tuple[Path, Path]]) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path, relative in files:
            info = zipfile.ZipInfo(str(relative), FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Complete source-library archive.",
    )
    parser.add_argument(
        "--dist-dir",
        type=Path,
        default=DEFAULT_DIST,
        help="Directory for one-uploadable-zip-per-skill packages.",
    )
    args = parser.parse_args()
    output = args.output.resolve()
    dist_dir = args.dist_dir.resolve()

    registry = json.loads((SKILLS_DIR / "registry.json").read_text(encoding="utf-8"))
    skill_names = [record["name"] for record in registry["skills"]]

    upload_packages: list[Path] = []
    for name in skill_names:
        skill_dir = SKILLS_DIR / name
        skill_files = sorted(path for path in skill_dir.rglob("*") if path.is_file())
        package = dist_dir / f"{name}.zip"
        write_archive(package, [(path, path.relative_to(skill_dir)) for path in skill_files])
        upload_packages.append(package)

    files = sorted(path for path in SKILLS_DIR.rglob("*") if path.is_file())
    write_archive(output, [(path, path.relative_to(ROOT)) for path in files])

    print(f"已生成 {len(upload_packages)} 个独立 Skill 上传包：{dist_dir}")
    print(f"已生成完整源码归档：{output}，包含 {len(files)} 个文件。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
