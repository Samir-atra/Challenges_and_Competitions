#!/usr/bin/env python3
"""
Solution for `data/task002.json`.
The pattern for this task is to identify "enclosed" areas and fill them.
Specifically, any area of black pixels (color 0) that is completely
surrounded by green pixels (color 3) is filled with yellow (color 4).
This is a classic "flood fill" problem where we find all black pixels
connected to the outside border and then fill the remaining ones.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from typing import Any, List, Optional, Tuple

import numpy as np

TASK_NAME = "task002.json"


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


def solve_grid(input_grid: np.ndarray) -> np.ndarray:
    """Applies the task's logic to a single grid."""
    h, w = input_grid.shape
    output_grid = input_grid.copy()
    
    # A mask to keep track of black pixels connected to the outside.
    outside_connected = np.zeros_like(input_grid, dtype=bool)
    
    # Queue for flood fill, starting with all border black pixels.
    q = []
    for r in range(h):
        if input_grid[r, 0] == 0: q.append((r, 0))
        if w > 1 and input_grid[r, w-1] == 0: q.append((r, w-1))
    for c in range(w):
        if input_grid[0, c] == 0: q.append((0, c))
        if h > 1 and input_grid[h-1, c] == 0: q.append((h-1, c))
        
    # Perform flood fill to find all externally-connected black pixels.
    head = 0
    while head < len(q):
        r, c = q[head]
        head += 1
        if outside_connected[r, c]: continue
        outside_connected[r, c] = True
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w and \
               not outside_connected[nr, nc] and input_grid[nr, nc] == 0:
                q.append((nr, nc))
                
    # Fill any black pixel that is NOT connected to the outside with yellow (4).
    output_grid[(input_grid == 0) & ~outside_connected] = 4
    return output_grid


def solve(task_obj: Any) -> Any:
    """Solves all examples in a task file."""
    if not isinstance(task_obj, dict) or ('train' not in task_obj and 'test' not in task_obj):
        return {"error": "Input is not a valid task object"}

    solution_obj = {}
    for key in ['train', 'test', 'arc-gen']:
        if key in task_obj:
            solved_examples = []
            for example in task_obj[key]:
                input_grid = np.array(example['input'])
                output_grid = solve_grid(input_grid)
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