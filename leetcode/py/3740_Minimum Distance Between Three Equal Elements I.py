from typing import List
from myUtils.Utils import printResult

"""
You are given an integer array nums.

A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].

The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.

Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.
"""
from collections import Counter

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1
        
        c = Counter(nums)
        self.minVal = 10**10

        def getDiff(i, j, k):
            return abs(i - j) + abs(j - k) + abs(k - i)

        def getMinFromIndices(indices):
            for i in range(len(indices) - 2):
                self.minVal = min(self.minVal, getDiff(indices[i], indices[i+1], indices[i+2]))

        for item in c:
            if c[item] < 3:
                continue

            indices = [i for i, x in enumerate(nums) if x == item]
            getMinFromIndices(indices)

        return self.minVal if self.minVal != 10**10 else -1

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

