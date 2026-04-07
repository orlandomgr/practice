#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    n = len(responseTimes)
    if n <= 0:
        return 0
    i = 1
    totalSum = responseTimes[0]
    average = responseTimes[0]
    count = 0
    while i < n:
        if responseTimes[i] > average:
            count += 1
        totalSum += responseTimes[i]
        average = totalSum // (i + 1)
        i += 1

    return count

responseTimes = [100, 200, 150,300]
expected = 2
result = countResponseTimeRegressions(responseTimes)
printResult(result, expected)

