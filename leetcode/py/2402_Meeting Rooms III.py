from typing import List
from myUtils.Utils import printResult
from collections import Counter

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        booked = [0] * n
        meets = [0] * n
        times = [0] * n

        m = range(meetings)
        for i in range(m):
            return 1
        return 0
        
obj = Solution()

n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]
expected =  0
result = obj.mostBooked(n, meetings)
printResult(result, expected)        

n = 3
meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
expected =  1
result = obj.mostBooked(n, meetings)
printResult(result, expected)        