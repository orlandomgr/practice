#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'countAffordablePairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER budget
#

def countAffordablePairs(prices, budget):
    # Write your code here
    if len(prices) < 2:
        return 0
    
    prices.sort()
    count = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[i] + prices[j] <= budget:
                count += 1

    return count


prices = [1, 2, 3, 4, 5]
budget = 7
expected = 8
result = countAffordablePairs(prices, budget)
printResult(result, expected)

prices = []
budget = 100
expected = 0
result = countAffordablePairs(prices, budget)
printResult(result, expected)

prices = [5]
budget = 5
expected = 0
result = countAffordablePairs(prices, budget)
printResult(result, expected)

