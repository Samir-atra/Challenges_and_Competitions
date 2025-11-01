#!/usr/bin/env python3
"""
Solution for `data/task001.json`.

The pattern for this task is a fractal-like 3x3 tiling. The 3x3 input grid
is used as a "meta-pattern" for a 9x9 output grid. Each cell in the input
grid determines the content of a 3x3 block in the output grid.

- If `input[r][c]` is non-zero, the corresponding 3x3 block in the output
  is a copy of the entire input grid.
- If `input[r][c]` is zero, the corresponding 3x3 block is filled with zeros.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from typing import Any, List, Optional

import numpy as np

TASK_NAME = "task001.json"


def find_task_file() -> Optional[Path]:
    """Looks for the task file in common data locations."""
    script_dir = Path(__file__).parent
    candidates = [
        script_dir.parent.parent / "data" / TASK_NAME,
        Path.cwd() / "data" / TASK_NAME,
        script_dir / TASK_NAME,
        Path(TASK_NAME),
    ]
    for p in candidates:
        if p.exists():
            return p
    return None


def solve(task_obj: Any) -> Any:
    """
    Solves the task by applying the fractal tiling logic.
    It processes the 'train' and 'test' examples from the task file.
    """
    if not isinstance(task_obj, dict) or ('train' not in task_obj and 'test' not in task_obj):
        return {"error": "Input is not a valid task object"}

    solution_obj = {}
    for key in ['train', 'test', 'arc-gen']:
        if key in task_obj:
            solved_examples = []
            for example in task_obj[key]:
                input_grid = np.array(example['input'])
                h, w = input_grid.shape
                output_grid = np.zeros((h * 3, w * 3), dtype=int)

                for r in range(h):
                    for c in range(w):
                        if input_grid[r, c] != 0:
                            output_grid[r*h:(r+1)*h, c*w:(c+1)*w] = input_grid
                
                solved_examples.append({'input': example['input'], 'output': output_grid.tolist()})
            solution_obj[key] = solved_examples
            
    return solution_obj


def main() -> None:
    p = find_task_file()
    if not p:
        print(json.dumps({"task": TASK_NAME, "error": "file not found"}, ensure_ascii=False))
        sys.exit(2)

    obj = json.loads(p.read_text(encoding="utf-8"))
    solution = solve(obj)
    print(json.dumps({"task": p.name, "solution": solution}, ensure_ascii=False))


if __name__ == "__main__":
    main()