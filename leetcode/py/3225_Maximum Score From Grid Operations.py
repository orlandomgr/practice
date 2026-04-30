from typing import List
from myUtils.Utils import printResult

"""
You are given a 2D matrix grid of size n x n. Initially, all cells of the grid are colored white. In one operation, you can select any cell of indices (i, j), and color black all the cells of the jth column starting from the top row down to the ith row.

The grid score is the sum of all grid[i][j] such that cell (i, j) is white and it has a horizontally adjacent black cell.

Return the maximum score that can be achieved after some number of operations.
"""
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # prefix[j][i] = sum of column j, rows 0 to i-1
        prefix = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                prefix[j][i + 1] = prefix[j][i] + grid[i][j]

        def col_sum(j, lo, hi):
            """Sum of column j for rows [lo, hi). Returns 0 if lo >= hi."""
            return prefix[j][hi] - prefix[j][lo] if lo < hi else 0

        # Each column j gets a "depth" d: rows 0..d-1 are black, rows d..n-1 are white.
        # A white cell (i, j) scores grid[i][j] if row i < depth of col j-1 OR col j+1.
        #
        # DP state: dp[d_prev][d_curr] = max score for columns 0..j, where:
        #   d_prev = depth of col j-1
        #   d_curr = depth of col j
        # We score col j only after seeing col j+1 (so both neighbors are known).
        # Scoring col j: white rows [d_curr, n-1] that have a black neighbor.
        # Union of left (d_prev) and right (d_next): rows [d_curr, max(d_prev,d_next)-1]

        INF = float('inf')
        dp = [[-INF] * (n + 1) for _ in range(n + 1)]

        # Base: column 0, no left neighbor (treat left depth = 0), score = 0
        for d0 in range(n + 1):
            dp[0][d0] = 0

        for j in range(1, n):
            new_dp = [[-INF] * (n + 1) for _ in range(n + 1)]
            pj = prefix[j - 1]  # prefix sums of column j-1

            for d_curr in range(n + 1):
                # prefix_max[k] = max(dp[0..k][d_curr])
                prefix_max = [-INF] * (n + 1)
                for k in range(n + 1):
                    prefix_max[k] = max(prefix_max[k - 1] if k > 0 else -INF, dp[k][d_curr])

                # suffix_val[k] = max(dp[d_prev][d_curr] + pj[d_prev]) for d_prev in [k, n]
                suffix_val = [-INF] * (n + 2)
                for k in range(n, -1, -1):
                    v = dp[k][d_curr] + pj[k] if dp[k][d_curr] != -INF else -INF
                    suffix_val[k] = max(suffix_val[k + 1], v)

                # When d_next < d_curr:
                #   d_prev in [0, d_curr]  → score = 0 (since max(d_prev,d_next) <= d_curr)
                #   d_prev in [d_curr+1,n] → score = pj[d_prev] - pj[d_curr]
                # Both are independent of d_next, so precompute once.
                sv = suffix_val[d_curr + 1]
                small_d_next_val = max(
                    prefix_max[d_curr],
                    sv - pj[d_curr] if sv != -INF else -INF
                )

                for d_next in range(n + 1):
                    if d_next < d_curr:
                        val = small_d_next_val
                    else:
                        # d_next >= d_curr
                        # Case A: d_prev <= d_next, score = col_sum(j-1, d_curr, d_next)
                        val_a = prefix_max[d_next]
                        val_a = val_a + col_sum(j - 1, d_curr, d_next) if val_a != -INF else -INF

                        # Case B: d_prev > d_next (all > d_curr too), score = pj[d_prev] - pj[d_curr]
                        sv2 = suffix_val[d_next + 1] if d_next < n else -INF
                        val_b = sv2 - pj[d_curr] if sv2 != -INF else -INF

                        val = max(val_a, val_b)

                    if val > new_dp[d_curr][d_next]:
                        new_dp[d_curr][d_next] = val

            dp = new_dp


        # Score the last column (col n-1): only left neighbor, no right neighbor
        best = 0
        for d_prev in range(n + 1):
            for d_curr in range(n + 1):
                if dp[d_prev][d_curr] != -INF:
                    score = col_sum(n - 1, d_curr, d_prev)
                    best = max(best, dp[d_prev][d_curr] + score)

        return best


obj = Solution()

grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]
expected = 11
result = obj.maximumScore(grid)
printResult(result, expected)

grid = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]
expected = 94
result = obj.maximumScore(grid)
printResult(result, expected)
