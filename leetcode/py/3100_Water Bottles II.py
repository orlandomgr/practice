from typing import List
from myUtils.Utils import printResult
from functools import cache
from itertools import permutations
import heapq
from collections import deque


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            result += 1
            emptyBottles -= numExchange
            emptyBottles += 1
            numExchange += 1
            # print("full: %s empty: %s exc: %s" %(fullBottles, emptyBottles, numExchange))
        return result


obj = Solution()

numBottles = 10
numExchange = 3
expected = 13
result = obj.maxBottlesDrunk(numBottles, numExchange)
printResult(result, expected)

numBottles = 13
numExchange = 6
expected = 15
result = obj.maxBottlesDrunk(numBottles, numExchange)
printResult(result, expected)
