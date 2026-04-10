#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def mergeHighDefinitionIntervals(intervals):
    # Write your code here
    intervals.sort()
    n = len(intervals)
    if n <= 1:
        return intervals
    result = []
    currentS, currentE = intervals[0]
    i = 0
    while i < n - 1:
        thisS, thisE = intervals[i + 1]
        if thisS >= currentS and thisS <= currentE:
            if thisE > currentE:
                currentE = thisE
        else:
            result.append([currentS, currentE])
            currentS = thisS
            currentE = thisE
        i += 1
    result.append([currentS, currentE])

    return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
expected = [[1, 6], [8, 10], [15, 18]]
result = mergeHighDefinitionIntervals(intervals)
printResult(result, expected)

