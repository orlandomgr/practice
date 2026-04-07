#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'findFirstOccurrence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def findFirstOccurrence(nums, target):
    # Write your code here
    try:
        return nums.index(target)
    except:
        return -1


nums = [1, 1, 1, 1, 1]
target = 1
expected = 0
result = findFirstOccurrence(nums, target)
printResult(result, expected)


nums = [1, 2, 3, 4, 5]
target = 3
expected = 2
result = findFirstOccurrence(nums, target)
printResult(result, expected)

nums = []
target = 5
expected = -1
result = findFirstOccurrence(nums, target)
printResult(result, expected)

nums = [3]
target = 3
expected = 0
result = findFirstOccurrence(nums, target)
printResult(result, expected)

