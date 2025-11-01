#!/usr/bin/env python3
"""
Run generated per-task solver scripts and visualize their outputs using
the project's `src/visualize_arc_tasks.py` helper.

Behavior:
- For each solver script (e.g. `task042.py`) the runner will:
  1. Determine the corresponding JSON file (`data/task042.json`).
  2. Run the solver script and parse its single-line JSON stdout.
  3. Try to extract one or more 2D-grid outputs from the solver's `solution`.
  4. Pair those outputs with the original `train` inputs (best-effort).
  5. Write a temporary JSON file in ARC format and call the visualizer to show
     input (left) vs solver output (right).

Usage examples (from repo root):
  # Visualize a single solver
  python3 scripts/generated_solver/run_and_visualize.py scripts/generated_solver/task042.py

  # Visualize the first 10 solvers in the generated folder
  python3 scripts/generated_solver/run_and_visualize.py --dir scripts/generated_solver --max 10

Notes:
- The runner uses heuristics to interpret solver outputs. If a solver doesn't
  return a grid-like output the runner will skip visualization for that task.
- The runner calls the visualizer script as a subprocess; each call opens a
  matplotlib window which you should close to continue to the next task.
"""
from __future__ import annotations
import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, List, Optional
import matplotlib
import importlib
# Delay importing pyplot until we know whether we should show figures interactively.
# `plt` will be imported inside main() after selecting an appropriate backend.
plt = None
import numpy as np
from datetime import datetime


def is_numeric_list(obj: Any) -> bool:
    """Return True when obj is a non-empty list of numbers (ints or floats)."""
    if not isinstance(obj, list) or not obj:
        return False
    return all(isinstance(x, (int, float)) for x in obj)


def extract_numeric_outputs(solution: Any) -> List[List[float]]:
    """Best-effort extract one or more numeric lists from solver solution.

    Returns a list of numeric lists (each a Python list of numbers).
    """
    if solution is None:
        return []
    # single scalar number -> treat as single-element series
    if isinstance(solution, (int, float)):
        return [[float(solution)]]
    # direct numeric list
    if is_numeric_list(solution):
        return [list(map(float, solution))]
    # list of numeric lists
    if isinstance(solution, list) and all(is_numeric_list(x) for x in solution):
        return [list(map(float, x)) for x in solution]
    # dict-like: look for common keys
    if isinstance(solution, dict):
        # top-level 'outputs' or 'solution' or 'predictions'
        for key in ('outputs', 'solution', 'predictions', 'prediction', 'output'):
            if key in solution:
                return extract_numeric_outputs(solution[key])
        # train/test structure
        if 'train' in solution and isinstance(solution['train'], list):
            found = []
            for ex in solution['train']:
                if isinstance(ex, dict):
                    for k in ('output', 'prediction', 'y'):
                        if k in ex and is_numeric_list(ex[k]):
                            found.append(list(map(float, ex[k])))
            if found:
                return found
    # maybe it's a JSON string
    if isinstance(solution, str):
        try:
            parsed = json.loads(solution)
            return extract_numeric_outputs(parsed)
        except Exception:
            pass
    return []

# Color palette for visualization (RGB 0-255 -> 0-1)
COLORS = np.array([
    (0, 0, 0),        # 0: black
    (30, 147, 255),   # 1: blue
    (250, 61, 49),    # 2: red
    (78, 204, 48),    # 3: green
    (255, 221, 0),    # 4: yellow
    (153, 153, 153),  # 5: grey
    (229, 59, 163),   # 6: pink
    (255, 133, 28),   # 7: orange
    (136, 216, 241),  # 8: light blue
    (147, 17, 49),    # 9: maroon
], dtype=np.uint8) / 255.0


def _sanitize_label(s: Any) -> str:
    """Return a safe, printable string for matplotlib titles/text.

    - Ensure it's a str, remove non-printable/control characters.
    - Escape underscores to avoid accidental mathtext rendering.
    """
    if s is None:
        return ''
    try:
        s = str(s)
    except Exception:
        s = repr(s)
    # remove non-printable characters
    cleaned = ''.join(ch for ch in s if ch.isprintable())
    # escape underscore to avoid math mode/subscript rendering
    cleaned = cleaned.replace('_', r'\_')
    return cleaned


def run_solver(solver_path: Path) -> Optional[dict]:
    try:
        proc = subprocess.run([sys.executable, str(solver_path)], capture_output=True, text=True, timeout=30)
    except subprocess.SubprocessError as e:
        print(f"Failed to run {solver_path}: {e}")
        return None
    if proc.returncode != 0:
        print(f"Solver {solver_path.name} exited with code {proc.returncode}; stderr:\n{proc.stderr}")
        # still try to parse stdout if present
    out = proc.stdout.strip()
    if not out:
        print(f"Solver {solver_path.name} produced no stdout")
        return None
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        # sometimes the solver prints a line with extra text; try to extract JSON substring
        # try to extract JSON object or array from the stdout
        starts = [i for i in (out.find('{'), out.find('[')) if i != -1]
        ends = [i for i in (out.rfind('}'), out.rfind(']')) if i != -1]
        if starts and ends:
            start = min(starts)
            end = max(ends)
            if end > start:
                try:
                    return json.loads(out[start:end+1])
                except Exception:
                    pass
        print(f"Could not parse JSON output from {solver_path.name}:\n{out}")
        return None


def is_grid(obj: Any) -> bool:
    if not isinstance(obj, list) or not obj:
        return False
    # grid = list of lists of ints
    return all(isinstance(row, list) and row and all(isinstance(c, int) for c in row) for row in obj)


def extract_outputs(solution: Any, num_inputs: int) -> List[Any]:
    """Return a list of grid outputs (best-effort)."""
    # direct grid
    if is_grid(solution):
        return [solution]
    # list of grids
    if isinstance(solution, list) and all(is_grid(x) for x in solution):
        return solution
    # dict with train/test structure
    if isinstance(solution, dict):
        if 'train' in solution and isinstance(solution['train'], list):
            outs = []
            for ex in solution['train']:
                if isinstance(ex, dict) and 'output' in ex and is_grid(ex['output']):
                    outs.append(ex['output'])
            if outs:
                return outs
        if 'output' in solution and is_grid(solution['output']):
            return [solution['output']]
    # solution may be a JSON string
    if isinstance(solution, str):
        try:
            parsed = json.loads(solution)
            return extract_outputs(parsed, num_inputs)
        except Exception:
            pass
    # fallback: no grid found
    return []


def prepare_visualization(original_task_path: Path, outputs: List[Any]) -> Optional[Path]:
    # load original task file
    try:
        content = json.loads(original_task_path.read_text(encoding='utf-8'))
    except Exception as e:
        print(f"Failed to read {original_task_path}: {e}")
        return None
    trains = content.get('train', []) if isinstance(content, dict) else []
    if not trains:
        # no training examples to pair with; try wrapping outputs as a standalone dataset
        wrapper = {'train': []}
        for out in outputs:
            if is_grid(out):
                wrapper['train'].append({'input': out, 'output': out})
        if not wrapper['train']:
            return None
        # name the temp file to include the original task stem so the external
        # visualizer can show a meaningful filename/title instead of a
        # generic solver_vis_ temporary name
        fd, path = tempfile.mkstemp(prefix=f"{original_task_path.stem}__solver_vis_", suffix='.json')
        Path(path).write_text(json.dumps(wrapper, ensure_ascii=False))
        return Path(path)
    # Pair outputs to train inputs best-effort
    paired = {'train': []}
    for i, ex in enumerate(trains):
        inp = ex.get('input') if isinstance(ex, dict) else None
        out = None
        if i < len(outputs):
            out = outputs[i]
        elif outputs:
            out = outputs[0]
        if inp is not None and is_grid(inp) and out is not None and is_grid(out):
            paired['train'].append({'input': inp, 'output': out})
    if not paired['train']:
        return None
    # include the original task stem in the temporary filename so downstream
    # tools (like the legacy visualizer) display useful names
    fd, path = tempfile.mkstemp(prefix=f"{original_task_path.stem}__solver_vis_", suffix='.json')
    Path(path).write_text(json.dumps(paired, ensure_ascii=False))
    return Path(path)


def visualize_textual_output(original_task_path: Path, solver_name: str, solution: Any, *, save_path: Optional[Path] = None, show: bool = True) -> None:
    """Show input grid on left and solver textual output on right."""
    # Try to read the original task. If unavailable or malformed, fall back to a
    # textual-only visualization that shows the solver output.
    content = None
    trains = []
    try:
        content = json.loads(original_task_path.read_text(encoding='utf-8'))
        trains = content.get('train', []) if isinstance(content, dict) else []
    except Exception as e:
        print(f"Warning: failed to read {original_task_path}: {e} — showing textual-only visualization")

    # If there are no train examples or no usable input grid, render textual-only
    # visualization instead of aborting.
    if not trains:
        fig, ax = plt.subplots(1, 1, figsize=(8, 4))
        ax.axis('off')
        sol_text = json.dumps(solution, ensure_ascii=False, indent=2)
        ax.text(0.01, 0.99, f"Solver: {_sanitize_label(solver_name)}", va='top', fontsize=12, weight='bold')
        ax.text(0.01, 0.92, sol_text, va='top', fontsize=10, family='monospace')
        fig.tight_layout()
        if save_path is not None:
            try:
                save_path.parent.mkdir(parents=True, exist_ok=True)
                fig.savefig(str(save_path), dpi=200)
                print(f"Saved textual visualization to {save_path}")
            except Exception as e:
                print(f"Failed to save textual visualization to {save_path}: {e}")
        if show:
            print(f"Displaying textual visualization for {solver_name} (close window to continue)")
            plt.show()
        else:
            plt.close(fig)
        return

    # take first example
    ex = trains[0]
    inp = ex.get('input') if isinstance(ex, dict) else None
    if inp is None:
        # fallback to textual-only if input not present
        fig, ax = plt.subplots(1, 1, figsize=(8, 4))
        ax.axis('off')
        sol_text = json.dumps(solution, ensure_ascii=False, indent=2)
        ax.text(0.01, 0.99, f"Solver: {_sanitize_label(solver_name)}", va='top', fontsize=12, weight='bold')
        ax.text(0.01, 0.92, sol_text, va='top', fontsize=10, family='monospace')
        fig.tight_layout()
        if save_path is not None:
            try:
                save_path.parent.mkdir(parents=True, exist_ok=True)
                fig.savefig(str(save_path), dpi=200)
                print(f"Saved textual visualization to {save_path}")
            except Exception as e:
                print(f"Failed to save textual visualization to {save_path}: {e}")
        if show:
            print(f"Displaying textual visualization for {solver_name} (close window to continue)")
            plt.show()
        else:
            plt.close(fig)
        return

    # create image for input
    grid = np.array(inp)
    # map to RGB
    h, w = grid.shape
    img = np.zeros((h, w, 3), dtype=float)
    for val in np.unique(grid):
        mask = grid == val
        if 0 <= val < COLORS.shape[0]:
            img[mask] = COLORS[val]
        else:
            img[mask] = (0.5, 0.5, 0.5)

    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    axes[0].imshow(img, interpolation='nearest')
    axes[0].set_title(f"{_sanitize_label(original_task_path.name)} input")
    axes[0].set_xticks([])
    axes[0].set_yticks([])

    # render textual solution on the right
    sol_text = json.dumps(solution, ensure_ascii=False, indent=2)
    axes[1].axis('off')
    axes[1].text(0.01, 0.99, f"Solver: {_sanitize_label(solver_name)}", va='top', fontsize=12, weight='bold')
    axes[1].text(0.01, 0.92, sol_text, va='top', fontsize=10, family='monospace')

    fig.tight_layout()
    if save_path is not None:
        try:
            save_path.parent.mkdir(parents=True, exist_ok=True)
            fig.savefig(str(save_path), dpi=200)
            print(f"Saved textual visualization to {save_path}")
        except Exception as e:
            print(f"Failed to save textual visualization to {save_path}: {e}")
    if show:
        try:
            print(f"Displaying textual visualization for {solver_name} (close window to continue)")
            plt.show()
        except Exception as e:
            print(f"Could not display figure interactively: {e}\nEnsure an X server is available and a GUI backend is installed (Tk, Qt).")
    else:
        try:
            plt.close(fig)
        except Exception:
            pass


def visualize_numeric_output(original_task_path: Path, solver_name: str, numeric_lists: List[List[float]], *, save_path: Optional[Path] = None, show: bool = True) -> None:
    """Visualize list(s) of numbers produced by a solver.

    For each numeric list we render a line plot and a histogram in a row.
    If the original task JSON contains a train input we show its short summary
    in the figure title for context.
    """
    # try to read a small context from the task
    context_name = original_task_path.name
    try:
        content = json.loads(original_task_path.read_text(encoding='utf-8'))
        trains = content.get('train', []) if isinstance(content, dict) else []
        ctx = f" ({len(trains)} train examples)" if trains else ""
    except Exception:
        ctx = ""

    n = len(numeric_lists)
    fig, axes = plt.subplots(n, 2, figsize=(8, 3 * max(1, n)))
    if n == 1:
        axes = [axes]
    for i, arr in enumerate(numeric_lists):
        ax_line, ax_hist = axes[i][0], axes[i][1]
        x = list(range(len(arr)))
        ax_line.plot(x, arr, marker='o')
        ax_line.set_title(f"{solver_name} — series {i}")
        ax_line.set_xlabel('index')
        ax_line.set_ylabel('value')

        ax_hist.hist(arr, bins=min(40, max(5, len(arr)//2)))
        ax_hist.set_title('Histogram')

    fig.suptitle(f"Numeric outputs for {context_name}{ctx}", fontsize=14)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    if save_path is not None:
        try:
            save_path.parent.mkdir(parents=True, exist_ok=True)
            fig.savefig(str(save_path), dpi=200)
            print(f"Saved numeric visualization to {save_path}")
        except Exception as e:
            print(f"Failed to save numeric visualization to {save_path}: {e}")
    if show:
        try:
            print(f"Displaying numeric visualization for {solver_name} (close window to continue)")
            plt.show()
        except Exception as e:
            print(f"Could not display figure interactively: {e}\nEnsure an X server is available and a GUI backend is installed (Tk, Qt).")
    else:
        try:
            plt.close(fig)
        except Exception:
            pass


def save_result_json(*, solver_path: Path, original_task_path: Path, raw_result: Any, numeric_lists: List[List[float]], grid_outputs: List[Any], out_dir: Path) -> Optional[Path]:
    """Write a structured JSON file summarizing the solver run and extracted outputs.

    Returns the Path to the JSON file or None on failure.
    """
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        summary = {
            'timestamp': datetime.utcnow().isoformat() + 'Z',
            'solver': str(solver_path),
            'task': str(original_task_path),
            'raw_result': raw_result,
            'numeric_outputs': numeric_lists,
            'grid_outputs': grid_outputs,
        }
        fname = f"{solver_path.stem}__{original_task_path.stem}.json"
        path = out_dir / fname
        path.write_text(json.dumps(summary, ensure_ascii=False, indent=2))
        return path
    except Exception as e:
        print(f"Failed to write result JSON for {solver_path.name}: {e}")
        return None


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument('solver', nargs='?', help='Path to a solver .py file. If omitted use --dir and pattern')
    p.add_argument('--dir', default='scripts/generated_solver', help='Directory with solver scripts')
    p.add_argument('--pattern', default='task*.py', help='Glob pattern for solvers in --dir')
    p.add_argument('--max', type=int, default=None, help='Limit number of solvers to run')
    p.add_argument('--visualizer', default='src/visualize_arc_tasks.py', help='Path to the visualizer script')
    p.add_argument('--out-dir', default='output/visualizations', help='Directory to write JSON summaries and saved figures')
    p.add_argument('--save', action='store_true', help='Save visualization PNGs and result JSONs to --out-dir')
    p.add_argument('--no-show', action='store_true', help="Don't show matplotlib windows (useful for headless runs)")
    args = p.parse_args(argv)

    # Configure matplotlib backend depending on whether we will show figures.
    global plt
    try:
        if args.no_show:
            # headless / no interactive display
            matplotlib.use('Agg', force=True)
            import matplotlib.pyplot as _plt
            importlib.reload(_plt)
            plt = _plt
        else:
            # try common interactive backends until one works
            current = matplotlib.get_backend()
            interactive_try = ['Qt5Agg', 'Qt4Agg', 'TkAgg', 'GTK3Agg', 'MacOSX']
            set_backend = None
            if 'agg' in current.lower():
                for bk in interactive_try:
                    try:
                        matplotlib.use(bk, force=True)
                        import matplotlib.pyplot as _plt
                        importlib.reload(_plt)
                        plt = _plt
                        set_backend = bk
                        break
                    except Exception as e:
                        # try next
                        print(f"Backend {bk} failed: {e}")
                if set_backend is None:
                    # fallback: use whatever backend is set but warn
                    import matplotlib.pyplot as _plt
                    plt = _plt
                    print("Warning: no interactive backend found; plt.show may fail.\nIf you have an X server, install/configure Tk or Qt backends.")
            else:
                import matplotlib.pyplot as _plt
                plt = _plt
    except Exception as e:
        print(f"Warning configuring matplotlib backend: {e}")
        try:
            import matplotlib.pyplot as _plt
            plt = _plt
        except Exception:
            plt = None

    solvers: List[Path] = []
    if args.solver:
        solvers = [Path(args.solver)]
    else:
        d = Path(args.dir)
        solvers = sorted(list(d.glob(args.pattern)))
    if args.max:
        solvers = solvers[:args.max]
    if not solvers:
        print('No solver scripts found to run')
        return

    for solver_path in solvers:
        print(f'Running solver: {solver_path.name}')
        result = run_solver(solver_path)
        if not result:
            continue
        # sol can be either a dict with a 'solution' key (common generated solvers)
        # or the solver may print a JSON value directly (list/array for grids).
        sol = result.get('solution') if isinstance(result, dict) else result
        # resolve original task json path
        json_name = solver_path.name.rsplit('.', 1)[0] + '.json'
        orig = Path('data') / json_name
        if not orig.exists():
            print(f'Original JSON {orig} not found; skipping visualization')
            continue
        outputs = extract_outputs(sol, num_inputs=10)
        numeric = []
        if not outputs:
            # try numeric outputs
            numeric = extract_numeric_outputs(sol)

        # prepare output directory and save JSON summary if requested
        out_dir = Path(args.out_dir)
        json_summary_path = None
        try:
            if args.save:
                json_summary_path = save_result_json(
                    solver_path=solver_path,
                    original_task_path=orig,
                    raw_result=result,
                    numeric_lists=numeric,
                    grid_outputs=outputs,
                    out_dir=out_dir,
                )
        except Exception as e:
            print(f"Failed to write summary JSON: {e}")

        if outputs:
            vis_path = prepare_visualization(orig, outputs)
            if not vis_path:
                print(f'Failed to prepare visualization data for {solver_path.name}; using textual fallback')
                # save textual figure if requested
                save_path = None
                if args.save:
                    save_path = out_dir / f"{solver_path.stem}__textual.png"
                visualize_textual_output(orig, solver_path.name, sol, save_path=save_path, show=not args.no_show)
                continue
            # call visualizer script (legacy ARC visualizer) if available
            try:
                if args.save:
                    # run visualizer but also save a PNG using matplotlib by loading vis_path JSON
                    # to keep behavior simple, call the visualizer which opens a window; if no-show requested skip calling it
                    if not args.no_show:
                        subprocess.run([sys.executable, args.visualizer, str(vis_path)], check=True)
                    else:
                        # still call visualizer without showing (best-effort); some visualizers may not support headless
                        subprocess.run([sys.executable, args.visualizer, str(vis_path)], check=True)
                else:
                    # interactive mode: call visualizer which will show windows
                    subprocess.run([sys.executable, args.visualizer, str(vis_path)], check=True)
            except subprocess.CalledProcessError as e:
                print(f'Visualizer failed: {e}')
            continue

        # if we reach here, no grid outputs; check numeric
        if numeric:
            save_path = None
            if args.save:
                save_path = out_dir / f"{solver_path.stem}__numeric.png"
            visualize_numeric_output(orig, solver_path.name, numeric, save_path=save_path, show=not args.no_show)
            continue

        # fallback: textual visualization
        save_path = None
        if args.save:
            save_path = out_dir / f"{solver_path.stem}__textual.png"
        print(f'No grid-like or numeric outputs extracted from solver {solver_path.name}; using textual fallback')
        visualize_textual_output(orig, solver_path.name, sol, save_path=save_path, show=not args.no_show)


if __name__ == '__main__':
    main()
