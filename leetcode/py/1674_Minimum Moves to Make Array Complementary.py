from typing import List
from myUtils.Utils import printResult

"""
You are given an integer array nums of even length n and an integer limit. In one move, you can replace any integer from nums with another integer between 1 and limit, inclusive.

The array nums is complementary if for all indices i (0-indexed), nums[i] + nums[n - 1 - i] equals the same number. For example, the array [1,2,3,4] is complementary because for all indices i, nums[i] + nums[n - 1 - i] = 5.

Return the minimum number of moves required to make nums complementary.
"""

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        pair_count = n // 2

        change = [0] * (2 * limit + 3)
        exact = [0] * (2 * limit + 1)

        for i in range(pair_count):
            a, b = nums[i], nums[n - 1 - i]
            if a > b:
                a, b = b, a

            exact[a + b] += 1
            change[a + 1] -= 1
            change[b + limit + 1] += 1

        moves = 2 * pair_count
        best = moves

        for target in range(2, 2 * limit + 1):
            moves += change[target]
            best = min(best, moves - exact[target])

        return best

obj = Solution()

nums = [1,2,4,3]
limit = 4
expected = 1
result = obj.minMoves(nums, limit)
printResult(result, expected)

nums = [1,2,2,1]
limit = 2
expected = 2
result = obj.minMoves(nums, limit)
printResult(result, expected)

nums = [1,2,1,2]
limit = 2
expected = 0
result = obj.minMoves(nums, limit)
printResult(result, expected)

