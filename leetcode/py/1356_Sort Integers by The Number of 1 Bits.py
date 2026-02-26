from myUtils.Utils import printResult
from typing import List
import heapq

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def getBitsFromNumber(n: int)-> int :
            return bin(n).count("1")

        pq = []
        for n in arr:
            heapq.heappush(pq, (getBitsFromNumber(n), n))

        result = []
        while pq:
            _, num = heapq.heappop(pq)
            result.append(num)

        return result

        
obj = Solution()

arr = [0,1,2,3,4,5,6,7,8]
expected = [0,1,2,4,8,3,5,6,7]
result = obj.sortByBits(arr)
printResult(result, expected)

arr = [1024,512,256,128,64,32,16,8,4,2,1]
expected = [1,2,4,8,16,32,64,128,256,512,1024]
result = obj.sortByBits(arr)
printResult(result, expected)

arr = [10000,10000]
expected = [10000,10000]
result = obj.sortByBits(arr)
printResult(result, expected)

