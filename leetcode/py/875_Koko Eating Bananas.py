from typing import List
from myUtils.Utils import printResult

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isWorking(k: int) -> bool:
            hours = 0
            for p in piles:
                hours += p // k
                if p % k != 0:
                    hours += 1
                if hours > h:
                    return False
            return True

        left = 1
        right = max(piles)
        res = right
        while left <= right:
            mid = left + (right - left) // 2
            if isWorking(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
    
obj = Solution()

piles = [312884470]
h = 312884469
expected = 2
result = obj.minEatingSpeed(piles, h)
printResult(result, expected)

piles = [3,6,7,11]
h = 8
expected = 4
result = obj.minEatingSpeed(piles, h)
printResult(result, expected)

piles = [30,11,23,4,20]
h = 5
expected = 30
result = obj.minEatingSpeed(piles, h)
printResult(result, expected)

piles = [30,11,23,4,20]
h = 6
expected = 23
result = obj.minEatingSpeed(piles, h)
printResult(result, expected)

