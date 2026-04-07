#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#

def findSmallestMissingPositive(orderNumbers):
    # Write your code here
    nums = set(orderNumbers)
    i = 1
    while i in nums:
        i += 1
    return i

orderNumbers = [3, 4, -1, 1]
expected = 2
result = findSmallestMissingPositive(orderNumbers)
printResult(result, expected)

orderNumbers = [1]
expected = 2
result = findSmallestMissingPositive(orderNumbers)
printResult(result, expected)

orderNumbers = [1, 1]
expected = 2
result = findSmallestMissingPositive(orderNumbers)
printResult(result, expected)

orderNumbers = [0]
expected = 1
result = findSmallestMissingPositive(orderNumbers)
printResult(result, expected)

orderNumbers = []
expected = 1
result = findSmallestMissingPositive(orderNumbers)
printResult(result, expected)