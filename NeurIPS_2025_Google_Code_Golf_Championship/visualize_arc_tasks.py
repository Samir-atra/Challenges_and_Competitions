import os
import json
import argparse
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

# Color palette for the grid cells, similar to the one in code_golf_utils.
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
], dtype=np.uint8)

def plot_task(ax, task, task_index):
    """Plots a single input-output grid pair on a given matplotlib subplot axis."""
    input_grid = np.array(task['input'])
    output_grid = np.array(task['output'])

    # Create colored images from the grids
    input_img = COLORS[input_grid]
    output_img = COLORS[output_grid]

    # Combine input and output images side-by-side with a separator
    separator = np.full((max(input_img.shape[0], output_img.shape[0]), 5, 3), 255, dtype=np.uint8)
    
    # Pad smaller grid to match height of the larger one
    if input_img.shape[0] < output_img.shape[0]:
        pad_width = ((0, output_img.shape[0] - input_img.shape[0]), (0, 0), (0, 0))
        input_img = np.pad(input_img, pad_width, 'constant', constant_values=255)
    elif output_img.shape[0] < input_img.shape[0]:
        pad_width = ((0, input_img.shape[0] - output_img.shape[0]), (0, 0), (0, 0))
        output_img = np.pad(output_img, pad_width, 'constant', constant_values=255)

    combined_img = np.hstack([input_img, separator, output_img])

    ax.imshow(combined_img)
    ax.set_title(f"Task {task_index+1}: Input (left) vs. Output (right)")
    ax.set_xticks([])
    ax.set_yticks([])

MAX_TASKS_PER_FIGURE = 10

def visualize_json_data(path_or_dir):
    """
    Visualize a single JSON file or all JSON files in a directory.

    If `path_or_dir` is a file, only that file will be visualized. If it's a
    directory, all .json files in it will be iterated, but each file's plots
    are displayed (and waited on) before moving to the next file.
    """
    p = Path(path_or_dir)

    if p.is_file():
        json_files = [p]
    elif p.is_dir():
        json_files = sorted(list(p.glob("*.json")))
        if not json_files:
            print(f"No .json files found in '{path_or_dir}'.")
            return
    else:
        print(f"Error: Path '{path_or_dir}' does not exist.")
        return

    for json_file_path in json_files:
        print(f"Generating visualization for: {json_file_path.name}")

        try:
            with open(json_file_path, 'r') as f:
                content = json.load(f)

            all_tasks = []
            for dataset_type in ["train", "test", "arc-gen"]:
                if dataset_type in content and isinstance(content[dataset_type], list):
                    all_tasks.extend(content[dataset_type])

            if not all_tasks:
                print(f"No valid tasks found in {json_file_path.name}")
                continue

            # Create multiple figures if there are too many tasks. Each figure
            # will display up to MAX_TASKS_PER_FIGURE tasks arranged in a grid
            # (prefer up to 5 columns). Show each figure (chunk) and wait for the
            # user to close it before continuing.
            for i in range(0, len(all_tasks), MAX_TASKS_PER_FIGURE):
                tasks_chunk = all_tasks[i:i + MAX_TASKS_PER_FIGURE]
                num_tasks_in_chunk = len(tasks_chunk)

                # Choose grid layout: try up to 5 columns, compute rows accordingly
                ncols = min(5, num_tasks_in_chunk)
                nrows = (num_tasks_in_chunk + ncols - 1) // ncols

                # Create a plot with a grid of subplots
                fig, axes = plt.subplots(nrows, ncols, figsize=(4 * ncols, 4 * nrows), squeeze=False)

                # Add a title indicating which file and which part it is
                part_num = (i // MAX_TASKS_PER_FIGURE) + 1
                total_parts = (len(all_tasks) + MAX_TASKS_PER_FIGURE - 1) // MAX_TASKS_PER_FIGURE

                if total_parts > 1:
                    fig.suptitle(f"Tasks from {json_file_path.name} (Part {part_num}/{total_parts})", fontsize=16, y=0.99)
                else:
                    fig.suptitle(f"Tasks from {json_file_path.name}", fontsize=16, y=0.99)

                # Flatten axes for easy indexing and plot each task
                axes_flat = axes.flatten()
                for j, task in enumerate(tasks_chunk):
                    plot_task(axes_flat[j], task, i + j)

                # Hide any unused subplots in the grid
                for k in range(num_tasks_in_chunk, axes_flat.size):
                    axes_flat[k].axis('off')

                fig.tight_layout(rect=[0, 0, 1, 0.96])

                # Display this chunk and wait for the user to close it.
                print("Displaying plot window for this chunk (up to 10 tasks). Close it to continue...")
                plt.show()
                plt.close(fig)

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {json_file_path.name}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred with {json_file_path.name}: {e}")

DATA_DIR = "/home/samer/Desktop/competitions/neurips2025_google_code_golf_championship_dev/data"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize ARC JSON task files. Pass a file or directory.")
    parser.add_argument("path", nargs="?", default=DATA_DIR, help="Path to a .json file or a directory containing .json files. Defaults to the project's data directory.")
    parser.add_argument("--list", action="store_true", help="List .json files in the given directory (or show the filename if a file) and exit.")
    args = parser.parse_args()

    target = Path(args.path)
    if args.list:
        if target.is_dir():
            json_files = sorted(list(target.glob("*.json")))
            if not json_files:
                print(f"No .json files found in '{args.path}'.")
            else:
                for jf in json_files:
                    print(jf.name)
        elif target.is_file():
            print(target.name)
        else:
            print(f"Path '{args.path}' does not exist.")
    else:
        visualize_json_data(args.path)