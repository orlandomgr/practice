from typing import List
from myUtils.Utils import printResult
from math import gcd


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [item for item in nums if item != 1]
        if len(nums) != n:
            return len(nums)

        g = 0
        for x in nums:
            g = gcd(g, x)
        # print(g)
        if g > 1:
            return -1

        subArr = 10**10
        for i in range(n):
            res = 0
            for j in range(i, n):

                res = gcd(res, nums[j])
                # print(res)
                if res == 1:
                    subArr = min(subArr, j - i + 1)
                    break
                    # return n

        return subArr - 1 + n - 1


obj = Solution()

nums = [6, 10, 15]
expected = 4
result = obj.minOperations(nums)
printResult(result, expected)

nums = [2,6,3,4]
expected =  4
result = obj.minOperations(nums)
printResult(result, expected)

nums = [2,10,6,14]
expected =  -1
result = obj.minOperations(nums)
printResult(result, expected)
