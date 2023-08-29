#!/usr/bin/python3
"""
Returns the perimeter of an island
"""


def island_perimeter(grid) -> int:
    """
    Returns the perimeter of island

    @params:
         grid: List of lists
         Returns: returns integer
    """
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
