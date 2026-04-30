from myUtils.Utils import printResult
from typing import List

"""
You are given an m x n grid where each cell contains one of the values 0, 1, or 2. You are also given an integer k.

You start from the top-left corner (0, 0) and want to reach the bottom-right corner (m - 1, n - 1) by moving only right or down.

Each cell contributes a specific score and incurs an associated cost, according to their cell values:

0: adds 0 to your score and costs 0.
1: adds 1 to your score and costs 1.
2: adds 2 to your score and costs 1. 
Return the maximum score achievable without exceeding a total cost of k, or -1 if no valid path exists.

Note: If you reach the last cell but the total cost exceeds k, the path is invalid.
"""

class Solution:

    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        # score and cost for each cell value
        cell_score = {0: 0, 1: 1, 2: 2}
        cell_cost  = {0: 0, 1: 1, 2: 1}

        # dp[r][c][cost] = best score reachable at (r, c) spending exactly `cost`
        # -1 means this state is unreachable
        NEG_INF = -1
        dp = [[[NEG_INF] * (k + 1) for _ in range(cols)] for _ in range(rows)]

        # initialize starting cell
        start_cost  = cell_cost[grid[0][0]]
        start_score = cell_score[grid[0][0]]
        if start_cost <= k:
            dp[0][0][start_cost] = start_score

        # fill the table moving only right or down
        for r in range(rows):
            for c in range(cols):
                for cost in range(k + 1):
                    if dp[r][c][cost] == NEG_INF:
                        continue

                    cur_score = dp[r][c][cost]

                    # try moving right
                    if c + 1 < cols:
                        nr, nc = r, c + 1
                        next_cost  = cost + cell_cost[grid[nr][nc]]
                        next_score = cur_score + cell_score[grid[nr][nc]]
                        if next_cost <= k:
                            dp[nr][nc][next_cost] = max(dp[nr][nc][next_cost], next_score)

                    # try moving down
                    if r + 1 < rows:
                        nr, nc = r + 1, c
                        next_cost  = cost + cell_cost[grid[nr][nc]]
                        next_score = cur_score + cell_score[grid[nr][nc]]
                        if next_cost <= k:
                            dp[nr][nc][next_cost] = max(dp[nr][nc][next_cost], next_score)

        # collect best score at the bottom-right corner across all valid costs
        best = max(dp[rows - 1][cols - 1])
        return best

obj = Solution()

grid = [[0, 1],[2, 0]]
k = 1
expected = 2
result = obj.maxPathScore(grid, k)
printResult(result, expected)

grid = [[0, 1],[1, 2]]
k = 1
expected = -1
result = obj.maxPathScore(grid, k)
printResult(result, expected)

