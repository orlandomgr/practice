from typing import List
from myUtils.Utils import printResult
import heapq

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        result = sum(reward2)
        q = []

        for i in range(n):
            heapq.heappush(q, -(reward1[i] - reward2[i]))
        
        for i in range(k):
            result += -heapq.heappop(q)

        # print(q)

        return result


obj = Solution()

reward1 = [1, 1, 3, 4]
reward2 = [4, 4, 1, 1]
k = 2
expected = 15
result = obj.miceAndCheese(reward1, reward2, k)
printResult(result, expected)

reward1 = [1, 1]
reward2 = [1, 1]
k = 2
expected = 2
result = obj.miceAndCheese(reward1, reward2, k)
printResult(result, expected)
