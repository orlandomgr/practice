from typing import List
from myUtils.Utils import printResult

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        count = 0
        started = False
        for i in range(n):
            if nums[i] == 1:
                if count < k and started:
                    return False
                count = 0
                started = True
            elif nums[i] == 0:
                count += 1
            # print("i: %s val: %s count: %s" %(i, nums[i], count))
        return True


obj = Solution()

nums = [0,1, 0,0,1,0,0,1]
k = 2
expected = True
result = obj.kLengthApart(nums, k)
printResult(result, expected)

nums = [1,0,1]
k = 2
expected = False
result = obj.kLengthApart(nums, k)
printResult(result, expected)

nums = [1, 0, 0, 0, 1, 0, 0, 1]
k = 2
expected = True
result = obj.kLengthApart(nums, k)
printResult(result, expected)

nums = [1, 0, 0, 1, 0, 1]
k = 2
expected = False
result = obj.kLengthApart(nums, k)
printResult(result, expected)
