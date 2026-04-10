#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult
# from functools import cache
#
# Complete the 'getAutoSaveInterval' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER n as parameter.
#

# @cache

def getAutoSaveInterval(n):
    cache = {}
    cache[0] = 1
    cache[1] = 2

    if n in cache:
        return cache[n]

    for i in range(2, n + 1):
        cache[i] = cache[i-1] + cache[i-2]

    # cache[n] = getAutoSaveInterval(n-1) + getAutoSaveInterval(n-2)
    return cache[n]

    # Write your code here


n = 3
expected = 5
result = getAutoSaveInterval(n)
printResult(result, expected)

n = 10
expected = 144
result = getAutoSaveInterval(n)
printResult(result, expected)

n = 0
expected = 1
result = getAutoSaveInterval(n)
printResult(result, expected)

n = 1
expected = 2
result = getAutoSaveInterval(n)
printResult(result, expected)

