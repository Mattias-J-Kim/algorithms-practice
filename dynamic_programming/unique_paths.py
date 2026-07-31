"""
Unique Paths
================

Note:
    The only 2D problem in this folder whose table is a grid rather than
    a comparison between two sequences. There is no input string, so the
    table IS the problem rather than a summary of one.

    Index convention used here: m is the grid width (number of columns)
    and n is the height (number of rows), so the table is built as
    n rows of m entries. The loop variable i runs over columns and j over
    rows, which means cells are written as dp[j][i] — row first, column
    second — and the destination is dp[n-1][m-1]. Reading i as a row
    index out of habit from the string problems is what breaks this one,
    and on a square grid the mistake produces the correct answer anyway.
    Testing with a non-square grid is what exposes it.

    The base cases carry the whole argument: every cell in the first row
    and first column has exactly one path to it, because reaching them
    requires moving in a single direction the whole way.

Problem:
    Count the distinct paths from the top-left to the bottom-right corner
    of an m x n grid, moving only right or down.

    Example:
        unique_paths(3, 3) = 6

DP table definition:
    dp[j][i] = number of distinct paths from the top-left corner to the
               cell in row j, column i

Recurrence:
    dp[j][i] = dp[j-1][i] + dp[j][i-1]
                  ^from above    ^from the left

Base cases:
    dp[0][i] = 1   for every column i
    dp[j][0] = 1   for every row j
"""


def unique_paths(m, n):
    dp = [[0]*(m) for _ in range(n)]

    for i in range(0, m):
        dp[0][i] = 1
    for j in range(0, n):
        dp[j][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[j][i] = dp[j-1][i] + dp[j][i-1]
    return dp[n-1][m-1]


print(unique_paths(3, 3))
