from typing import List
from myUtils.Utils import printResult


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        s = list(sorted(enumerate(nums), key=lambda x: (-x[1], x[0])))
        return list(x for _, x in sorted(s[:k], key=lambda x: x[0]))
        # size = len(nums)
        # if size == 1 or size == k:
        #     return nums

        # result = []
        # maxSum = -(10**10)
        # k -= 1
        # for i in range(size - k):
        #     num = nums[i]
        #     # print("i: %s " %(i))
        #     for j in range(i + 1, size - k + 1):
        #         currentSum = num + sum(nums[j:j+k])
        #         # print("i: %s j: %s num: %s currentSum: %s" %(i, j, num, currentSum))
        #         if currentSum > maxSum:
        #             maxSum = currentSum
        #             result = [num] + nums[j:j+k]

        # return result


obj = Solution()

nums = [63, -74, 61, -17, -55, -59, -10, 2, -60, -65]
k = 9
expected = [63, 61, -17, -55, -59, -10, 2, -60, -65]
result = obj.maxSubsequence(nums, k)
printResult(result, expected)

nums = [2]
k = 1
expected = [2]
result = obj.maxSubsequence(nums, k)
printResult(result, expected)

nums = [2, 1, 3, 3]
k = 2
expected = [3, 3]
result = obj.maxSubsequence(nums, k)
printResult(result, expected)

nums = [-1, -2, 3, 4]
k = 3
expected = [-1, 3, 4]
result = obj.maxSubsequence(nums, k)
printResult(result, expected)

nums = [3, 4, 3, 3]
k = 2
expected = [3, 4]
result = obj.maxSubsequence(nums, k)
printResult(result, expected)
