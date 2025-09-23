"""
Solution for the Maximum Borders problem from HackerEarth.

This script finds the side length of the largest square border made of '#'
characters within a grid.

The approach uses dynamic programming to precompute, for each cell, the
number of consecutive '#'s to its left and above it. This information is
then used to efficiently check for square borders.
"""

def solve_maximum_borders():
    """
    Solves a single test case for the Maximum Borders problem.
    """
    try:
        R, C = map(int, input().split())
        grid = [input().strip() for _ in range(R)]
    except (ValueError, EOFError):
        return

    if R == 0 or C == 0:
        print(0)
        return

    # dp_left[r][c]: stores number of consecutive '#'s to the left of (r,c)
    dp_left = [[0] * C for _ in range(R)]
    # dp_up[r][c]: stores number of consecutive '#'s above (r,c)
    dp_up = [[0] * C for _ in range(R)]

    # --- Precomputation using Dynamic Programming ---
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '#':
                dp_left[r][c] = (dp_left[r][c-1] if c > 0 else 0) + 1
                dp_up[r][c] = (dp_up[r-1][c] if r > 0 else 0) + 1

    max_border_side = 0
    # --- Find Maximum Border ---
    # Iterate through each cell, considering it as the bottom-right
    # corner of a potential square border.
    for r in range(R - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            if grid[r][c] == '#':
                # The potential side length is limited by the shorter of the
                # number of consecutive '#'s up or left from this cell.
                side_limit = min(dp_left[r][c], dp_up[r][c])

                # Check for squares of decreasing size, starting from the max possible.
                for k in range(side_limit, max_border_side, -1):
                    # Check if the top and left sides of the square are also valid.
                    if dp_left[r-k+1][c] >= k and dp_up[r][c-k+1] >= k:
                        max_border_side = max(max_border_side, k)
                        # Once we find the largest square for this corner, we can stop checking smaller ones.
                        break

    print(max_border_side)


def main():
    """
    Main function to handle multiple test cases.
    """
    try:
        num_test_cases = int(input())
        for _ in range(num_test_cases):
            solve_maximum_borders()
    except (ValueError, EOFError):
        return

if __name__ == "__main__":
    main()
