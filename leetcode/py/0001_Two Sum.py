from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size):
            for j in range(size):
                if i == j:
                    continue
            
                if(nums[i] + nums[j] == target):
                    return [i, j]

obj = Solution()
print(obj.twoSum([2,7,11,15], 9))
print(obj.twoSum([3,2,4], 6))
print(obj.twoSum([3,3], 6))

