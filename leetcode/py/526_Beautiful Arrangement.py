from typing import List

# Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

# perm[i] is divisible by i.
# i is divisible by perm[i].
# Given an integer n, return the number of the beautiful arrangements that you can construct.

class Solution:

    def isBeautiful(self, n, i):
        permByi = n % i == 0
        iByPerm = i % n == 0
        # print("isBeautiful: n: %s i: %s permByi: %s iByPerm: %s" %(n, i, permByi, iByPerm))

        return permByi or iByPerm

    def countArrangements(self, nums: List[int], level:int):
        # print("countArrangements: nums: %s level: %s " %(nums, level))

        if nums is None or len(nums) == 0:
            return [[]]
        if len(nums) == 1 and self.isBeautiful(nums[0], level):
            return [[nums[0]]]

        results = []
        for i in range(len(nums)):
            num = nums[i]
            pending = nums[:i] + nums[i+1:]
            resultsPending = self.countArrangements(pending, level + 1)

            for p in resultsPending:
                if self.isBeautiful(num, level):
                    results.append([num] + p)
                # else:
                    # print("skipping: %s" %(num))

        return results

    def countArrangement(self, n: int) -> int:
        array = []
        result = []
        for i in range(1, n+1):
            array.append(i)

        result = self.countArrangements(array, 1)
        # print(result)        
        return len(result)

obj = Solution()
# print(obj.countArrangement(1))
# print(obj.countArrangement(2))
print(obj.countArrangement(3))
