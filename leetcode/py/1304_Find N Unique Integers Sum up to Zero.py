from typing import List
# Given an integer n, return any array containing n unique integers such that they add up to 0.

class Solution:
    def sumZero(self, n: int) -> List[int]:
        out = []
        count = 0
        if n % 2 == 1:
            out.append(0)
        for i in range(1, n // 2 + 1):
            out.append(i)
            out.append(-i)
            count += i
            count -= i
        # out.append(0 - count)
        return out
    
obj = Solution()
print(obj.sumZero(5))
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
print(obj.sumZero(3))
# Output: [-1,0,1]
print(obj.sumZero(1))
# Output: [0]
print(obj.sumZero(100))
