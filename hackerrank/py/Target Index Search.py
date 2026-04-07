#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'binarySearch' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def binarySearch(nums, target):
    # Write your code here
    n = len(nums)
    l = 0
    r = n - 1
    while l <= r:
        mid = (r + l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1

    return -1



nums = [1, 2, 3, 4, 5]
target = 3
expected = 2
result = binarySearch(nums, target)
printResult(result, expected)

nums = [2, 4, 6, 8, 10, 12, 14, 16]
target = 16
expected = 7
result = binarySearch(nums, target)
printResult(result, expected)

nums = [0]
target = 5
expected = -1
result = binarySearch(nums, target)
printResult(result, expected)

nums = [10]
target = 10
expected = 0
result = binarySearch(nums, target)
printResult(result, expected)

