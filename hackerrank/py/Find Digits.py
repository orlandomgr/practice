#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    nStr = str(n)
    result = 0
    for i in range(len(nStr)):
        num = int(nStr[i])
        if num != 0 and n % num == 0:
            result += 1
    return result

n = 124
expected = 3
result = findDigits(n)
printResult(result, expected)

n = 111
expected = 3
result = findDigits(n)
printResult(result, expected)

n = 10
expected = 1
result = findDigits(n)
printResult(result, expected)


