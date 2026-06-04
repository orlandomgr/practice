from typing import List
from myUtils.Utils import printResult

"""
A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.

The customer can choose any candy to take away for free as long as the cost of the chosen candy is less than or equal to the minimum cost of the two candies bought.

For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3, they can take the candy with cost 1 for free, but not the candy with cost 4.
Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the minimum cost of buying all the candies.
"""

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        result = 0
        cost.sort()
        while len(cost) > 2:
            result += cost.pop()
            result += cost.pop()
            cost.pop()
        result += sum(cost)
        return result


obj = Solution()

cost = [1,2,3]
expected = 5
result = obj.minimumCost(cost)
printResult(result, expected)

cost = [6,5,7,9,2,2]
expected = 23
result = obj.minimumCost(cost)
printResult(result, expected)

cost = [5,5]
expected = 10
result = obj.minimumCost(cost)
printResult(result, expected)
