from typing import List
from myUtils.Utils import printResult

class Solution:
    def getDays(self, weights: List[int], mid: int) -> int:
        n = len(weights)
        curr = 0
        days = 1
        for i in range(n):
            if curr + weights[i] > mid:
                days += 1
                curr = 0
            curr += weights[i]
        # print("days: %s " %(days))
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        s = sum(weights)
        if days == 1:
            return s
        
        left = max(weights)
        right = s
        mid = (left + right) // 2
        calc = self.getDays(weights, mid)

        while left < right:
            mid = (right + left) // 2
            calc = self.getDays(weights, mid)
            if calc > days:
                # print("lowest")
                left = mid + 1
            else:
                # print("greater")
                right = mid 
            # print("left: %s mid: %s right: %s days: %s" %(left, mid, right, calc))

        return left

obj = Solution()

weights = [147,73,265,305,191,152,192,293,309,292,182,157,381,287,73,162,313,366,346,47]
days = 10
expected = 602
result = obj.shipWithinDays(weights, days)
printResult(result, expected)

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 1
expected = 55
result = obj.shipWithinDays(weights, days)
printResult(result, expected)

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
expected = 15
result = obj.shipWithinDays(weights, days)
printResult(result, expected)

weights = [3, 2, 2, 4, 1, 4]
days = 3
expected = 6
result = obj.shipWithinDays(weights, days)
printResult(result, expected)

weights = [1, 2, 3, 1, 1]
days = 4
expected = 3
result = obj.shipWithinDays(weights, days)
printResult(result, expected)
