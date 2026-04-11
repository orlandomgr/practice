from typing import List
from myUtils.Utils import printResult
from collections import defaultdict

"""
You are given an integer array nums.

A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].

The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.

Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.
"""

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices_map = defaultdict(list)
        for i, num in enumerate(nums):
            indices_map[num].append(i)
        
        min_dist = float('inf')
        
        for val in indices_map:
            indices = indices_map[val]
            if len(indices) >= 3:
                for m in range(len(indices) - 2):
                    dist = 2 * (indices[m+2] - indices[m])
                    if dist < min_dist:
                        min_dist = dist
        
        return int(min_dist) if min_dist != float('inf') else -1

obj = Solution()

nums = [1,2,1,1,3]
expected = 6
result = obj.minimumDistance(nums)
printResult(result, expected)

nums = [1,1,2,3,2,1,2]
expected = 8
result = obj.minimumDistance(nums)
printResult(result, expected)

nums = [1]
expected = -1
result = obj.minimumDistance(nums)
printResult(result, expected)
