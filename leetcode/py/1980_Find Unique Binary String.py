from myUtils.Utils import printResult
from typing import List

"""
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.
"""
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = []
        n = len(nums[0])
        for i in range(n):
            if nums[i][i] == "0":
                result.append("1")
            else:
                result.append("0")
        return "".join(result)

obj = Solution()

nums = ["01","10"]
expected = "11"
result = obj.findDifferentBinaryString(nums)
printResult(result, expected)

nums = ["00","01"]
expected = "10"
result = obj.findDifferentBinaryString(nums)
printResult(result, expected)

nums = ["111","011","001"]
expected = "000"
result = obj.findDifferentBinaryString(nums)
printResult(result, expected)

