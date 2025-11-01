#!/usr/bin/env python3
"""
Generate one minimal solver Python file per JSON task in the repository `data/` directory.

Each generated file will be named exactly like the JSON but with a `.py` extension
(`taskNNN.py`) and will implement a tiny heuristic solver mirroring the logic in
`task001.py`. Files already present are skipped.

Run from the repository root (the script uses relative paths).
"""
from __future__ import annotations
import os
from pathlib import Path
from typing import Iterable


TEMPLATE = '''#!/usr/bin/env python3
"""
Auto-generated solver for {json_name}
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from typing import Any, Optional

TASK_NAME = "{json_name}"


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
'''


def list_task_files(data_dir: Path) -> Iterable[Path]:
    for p in sorted(data_dir.glob('task*.json')):
        yield p


def make_solver_for(json_path: Path, out_dir: Path) -> None:
    json_name = json_path.name
    py_name = json_name.rsplit('.', 1)[0] + '.py'
    out_path = out_dir / py_name
    if out_path.exists():
        print(f"Skipping existing {out_path}")
        return
    # Use simple replace to avoid accidental format-string braces in the template
    content = TEMPLATE.replace("{json_name}", json_name)
    out_path.write_text(content, encoding='utf-8')
    # make the generated solver writable and readable
    try:
        os.chmod(out_path, 0o644)
    except Exception as e:
        print(f"Warning: chmod failed for {out_path}: {e}")


def main() -> None:
    # repository root is two levels up from this file: scripts/generated_solver -> scripts -> repo root
    repo_root = Path(__file__).parents[2]
    data_dir = repo_root / 'data'
    out_dir = Path(__file__).parent
    if not data_dir.exists():
        print(f"data directory not found at {data_dir}")
        return
    created = 0
    for j in list_task_files(data_dir):
        make_solver_for(j, out_dir)
        created += 1
    print(f"Processed {created} task files; solvers created under {out_dir}")


if __name__ == '__main__':
    main()
