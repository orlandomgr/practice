from typing import List

# You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

# For each queries[i]:

# Select a subset of indices within the range [li, ri] in nums.
# Decrement the values at the selected indices by 1.
# A Zero Array is an array where all elements are equal to 0.

# Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        size = len(nums)
        d = [0] * (size + 1)
        for l, r in queries:
            d[l] += 1
            d[r+1] -= 1


        currentOp = 0
        for i in range(size):
            currentOp += d[i]
            if currentOp < nums[i]:
                return False
        return True


obj = Solution()
print(obj.isZeroArray([1, 0, 1], [[0, 2]]))  # true
print(obj.isZeroArray([4, 3, 2, 1], [[1, 3], [0, 2]]))  # false
print(obj.isZeroArray([7], [[0, 0]]))  # false
print(obj.isZeroArray([1, 2, 1, 0, 0, 0], [[0, 3], [2, 4]]))  # false

