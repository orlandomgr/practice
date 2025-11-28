from myUtils.Utils import printResult
from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        nums.sort()
        # print(nums)
        maxDiff = -10**10
        for i in range(1, n):
            # print("2 n1: %s n2: %s" %(nums[i], nums[i-1]))
            diff = nums[i] - nums[i-1]
            maxDiff = max(maxDiff, diff)

        return maxDiff if maxDiff > -10**10 else 0



obj = Solution()

nums = [1,3,100]
expected = 97
result = obj.maximumGap(nums)
printResult(result, expected)

nums = [1,10000000]
expected = 9999999
result = obj.maximumGap(nums)
printResult(result, expected)

nums = [3,6,9,1]
expected = 3
result = obj.maximumGap(nums)
printResult(result, expected)

nums = [10]
expected = 0
result = obj.maximumGap(nums)
printResult(result, expected)