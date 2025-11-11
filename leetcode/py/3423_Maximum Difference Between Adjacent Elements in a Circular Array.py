from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxN = 0
        for i in range(0, len(nums) - 1):
            maxN = max(maxN, abs(nums[i] - nums[i+1]))

        maxN = max(maxN, abs(nums[0] - nums[len(nums)-1]))
        return maxN
    
obj = Solution()
matrix = [1,2,4]
print(obj.maxAdjacentDistance(matrix)) # 3

matrix = [-5,-10,-5]
print(obj.maxAdjacentDistance(matrix)) # 6

matrix =[-2,1,-5]
print(obj.maxAdjacentDistance(matrix)) # 6
