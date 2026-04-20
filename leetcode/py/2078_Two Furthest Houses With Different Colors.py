from typing import List
from myUtils.Utils import printResult

"""
There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

Return the maximum distance between two houses with different colors.

The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.
"""

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        indices = {}
        for i, color in enumerate(colors):
            if color not in indices:
                indices[color] = []
            indices[color].append(i)

        # print(indices)
        keys = indices.keys()

        maxD = -10**10
        for i in keys:
            for j in keys:
                if i == j:
                    continue
                # print(f"i:{i} j:{j}")
                maxD = max(maxD, abs(indices[i][0] - indices[j][0]), abs(indices[i][-1] - indices[j][0]), abs(indices[i][0] - indices[j][-1]), abs(indices[i][-1] - indices[j][-1]) )

        return maxD

obj = Solution()

colors = [1,1,1,6,1,1,1]
expected = 3
result = obj.maxDistance(colors)
printResult(result, expected)

colors = [1,8,3,8,3]
expected = 4
result = obj.maxDistance(colors)
printResult(result, expected)

colors = [0,1]
expected = 1
result = obj.maxDistance(colors)
printResult(result, expected)

