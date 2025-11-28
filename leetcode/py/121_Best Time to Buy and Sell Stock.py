from typing import List
from myUtils.Utils import printResult

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        curr = [prices[-1]] * n
        maxVal = prices[-1]
        for i in range(n):
            idx = n - 1 - i
            if maxVal < prices[idx]:
                maxVal = prices[idx]
                continue
            curr[idx] = maxVal

        res = 0
        for i in range(n - 1):
            res = max(res, curr[i] - prices[i])

        return res
        
obj = Solution()

prices = [3,3,5,0,0,3,1,4]
expected =  4
result = obj.maxProfit(prices)
printResult(result, expected)   

prices = [1]
expected =  0
result = obj.maxProfit(prices)
printResult(result, expected)   

prices = [3,2,6,5,0,3]
expected =  4
result = obj.maxProfit(prices)
printResult(result, expected)        

prices = [1,4,2]
expected =  3
result = obj.maxProfit(prices)
printResult(result, expected)        

prices = [7,1,5,3,6,4]
expected =  5
result = obj.maxProfit(prices)
printResult(result, expected)        

prices = [7,6,4,3,1]
expected =  0
result = obj.maxProfit(prices)
printResult(result, expected)        



