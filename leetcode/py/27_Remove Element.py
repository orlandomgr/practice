from typing import List
from myUtils.Utils import printResult

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] == val:
                count += 1
                nums[i] = 51

        nums.sort()
        return n - count

obj = Solution()

nums = [3,2,2,3]
val = 3
expected = 2
result = obj.removeElement(nums, val)
printResult(result, expected)

nums = [0,1,2,2,3,0,4,2]
val = 2
expected = 5
result = obj.removeElement(nums, val)
printResult(result, expected)

