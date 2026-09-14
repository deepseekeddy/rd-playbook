#!/usr/bin/env python3
"""Validate the TRAE skill library using only the Python standard library."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REGISTRY = SKILLS_DIR / "registry.json"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("缺少 YAML frontmatter 起始标记")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("缺少 YAML frontmatter 结束标记") from exc

    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"无法解析 frontmatter 行：{line}")
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"\'')
    return metadata, "\n".join(lines[end + 1 :])


def main() -> int:
    errors: list[str] = []
    skill_dirs = sorted(
        path for path in SKILLS_DIR.iterdir() if path.is_dir() and not path.name.startswith(".")
    )
    disk_names = {path.name for path in skill_dirs}

    try:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        records = registry["skills"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        print(f"ERROR registry.json 无法读取：{exc}")
        return 1

    registry_names: list[str] = []
    allowed_waves = {"P0", "P1", "P2"}
    allowed_statuses = {"draft", "pilot", "stable", "deprecated"}
    for index, record in enumerate(records):
        label = f"registry.skills[{index}]"
        if not isinstance(record, dict):
            errors.append(f"{label}: 必须是对象")
            continue
        name = record.get("name")
        if isinstance(name, str):
            registry_names.append(name)
        for key in ("name", "version", "wave", "owner_role", "status"):
            if not record.get(key):
                errors.append(f"{label}: 缺少 {key}")
        if record.get("wave") not in allowed_waves:
            errors.append(f"{label}: wave 必须是 P0/P1/P2")
        if record.get("status") not in allowed_statuses:
            errors.append(f"{label}: status 值无效")

    if len(registry_names) != len(set(registry_names)):
        errors.append("registry.json: Skill 名称重复")
    if set(registry_names) != disk_names:
        errors.append(
            "registry.json 与目录不一致："
            f"仅目录={sorted(disk_names - set(registry_names))}，"
            f"仅注册表={sorted(set(registry_names) - disk_names)}"
        )

    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{skill_dir.name}: 缺少 SKILL.md")
            continue
        try:
            metadata, body = parse_frontmatter(skill_file)
        except ValueError as exc:
            errors.append(f"{skill_dir.name}: {exc}")
            continue

        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if name != skill_dir.name:
            errors.append(f"{skill_dir.name}: frontmatter name={name!r} 与目录名不一致")
        if not NAME_RE.fullmatch(name):
            errors.append(f"{skill_dir.name}: name 仅允许小写字母、数字和连字符")
        if not description or len(description) < 20:
            errors.append(f"{skill_dir.name}: description 过短或缺失")
        if not body.strip():
            errors.append(f"{skill_dir.name}: 指令正文为空")
        if re.search(r"\b(?:TODO|FIXME|TBD)\b", body, re.IGNORECASE):
            errors.append(f"{skill_dir.name}: 存在未完成占位符")

        for raw_target in LINK_RE.findall(body):
            target = raw_target.split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            linked = (skill_file.parent / target).resolve()
            try:
                linked.relative_to(skill_dir.resolve())
            except ValueError:
                errors.append(f"{skill_dir.name}: 链接越出 Skill 目录：{raw_target}")
                continue
            if not linked.exists():
                errors.append(f"{skill_dir.name}: 链接不存在：{raw_target}")

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        print(f"\n校验失败：{len(errors)} 个问题。")
        return 1

    print(f"校验通过：{len(skill_dirs)} 个 Skill，注册表与本地资源一致。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
