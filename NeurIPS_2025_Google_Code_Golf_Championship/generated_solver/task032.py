#!/usr/bin/env python3
"""
Auto-generated solver for task032.json
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from typing import Any, Optional

TASK_NAME = "task032.json"


def find_task_file() -> Optional[Path]:
    script_dir = Path(__file__).parent
    candidates = [
        script_dir.parent / "data" / TASK_NAME,
        Path.cwd() / "data" / TASK_NAME,
        script_dir / TASK_NAME,
        Path(TASK_NAME),
    ]
    for p in candidates:
        if p.exists():
            return p
    return None


def solve(obj: Any) -> Any:
    if obj is None:
        return None
    if isinstance(obj, list):
        if all(isinstance(x, (int, float)) for x in obj):
            return sum(obj)
        if all(isinstance(x, str) for x in obj):
            return " ".join(obj)
        return obj
    if isinstance(obj, (int, float)):
        return obj
    if isinstance(obj, str):
        return obj[::-1]
    if isinstance(obj, dict):
        for k in ("input", "inputs", "data", "text", "prompt", "question"):
            if k in obj:
                return solve(obj[k])
        return json.dumps(obj, ensure_ascii=False)
    return str(obj)


def main() -> None:
    p = find_task_file()
    if not p:
        out = {"task": TASK_NAME, "error": "file not found"}
        print(json.dumps(out, ensure_ascii=False))
        sys.exit(2)

    raw = p.read_text(encoding="utf-8")
    if not raw.strip():
        solution = None
    else:
        try:
            obj = json.loads(raw)
            solution = solve(obj)
        except json.JSONDecodeError as e:
            solution = {"error": "malformed JSON: " + str(e)}
        except Exception as e:
            solution = {"error": str(e)}

    out = {"task": p.name, "solution": solution}
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
