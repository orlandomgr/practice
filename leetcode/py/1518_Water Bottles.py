from typing import List
from myUtils.Utils import printResult
from functools import cache

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles

        while numBottles >= numExchange:
            exchanged = (numBottles // numExchange) 
            result += exchanged
            pending = numBottles % numExchange
            numBottles = exchanged + pending
        return result
    

obj = Solution()

numBottles = 9
numExchange = 3
expected = 13
result = obj.numWaterBottles(numBottles, numExchange)
printResult(result, expected)

numBottles = 15
numExchange = 4
expected = 19
result = obj.numWaterBottles(numBottles, numExchange)
printResult(result, expected)
