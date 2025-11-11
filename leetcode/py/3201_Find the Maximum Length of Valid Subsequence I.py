from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        patterns = [[0,0], [0,1], [1,0], [1,1]]

        result = 0
        for pattern in patterns:
            count = 0
            for num in nums:
                if num % 2 == pattern[count % 2]:
                    count += 1
            result = max(result, count)
        return result


obj = Solution()
matrix = [1,2,3,4]
print(obj.maximumLength(matrix)) # 4

matrix = [1,2,1,1,2,1,2]
print(obj.maximumLength(matrix)) # 6



