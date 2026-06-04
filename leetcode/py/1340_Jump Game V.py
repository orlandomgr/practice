from myUtils.Utils import printResult
from typing import List

"""
Given an array of integers arr and an integer d. In one step you can jump from index i to index:

i + x where: i + x < arr.length and  0 < x <= d.
i - x where: i - x >= 0 and  0 < x <= d.
In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.
"""

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        if n == 0:
            return 0

        memo = {}

        def dfs(i: int) -> int:
            if i in memo:
                return memo[i]

            best = 1
            for step in range(1, d + 1):
                j = i - step
                if j < 0 or arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))

            for step in range(1, d + 1):
                j = i + step
                if j >= n or arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))

            memo[i] = best
            return best

        return max(dfs(i) for i in range(n))

obj = Solution()

arr = [6,4,14,6,8,13,9,7,10,6,12]
d = 2
expected = 4
result = obj.maxJumps(arr, d)
printResult(result, expected)

arr = [3,3,3,3,3]
d = 3
expected = 1
result = obj.maxJumps(arr, d)
printResult(result, expected)

arr = [7,6,5,4,3,2,1]
d = 1
expected = 7
result = obj.maxJumps(arr, d)
printResult(result, expected)
