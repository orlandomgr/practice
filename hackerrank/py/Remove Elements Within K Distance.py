#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'debounceTimestamps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY timestamps
#  2. INTEGER K
#

def debounceTimestamps(timestamps, K):
    # Write your code here
    n = len(timestamps)
    if n < 1:
        return 0

    last = timestamps[0]
    count = 1
    for i in range(1, n):
        if timestamps[i] - last >= K:
            count += 1
            last = timestamps[i]

    return count

timestamps = [1, 2, 3, 8, 10]
K = 3
expected = 2
result = debounceTimestamps(timestamps, K)
printResult(result, expected)

timestamps = []
K = 10
expected = 0
result = debounceTimestamps(timestamps, K)
printResult(result, expected)

timestamps = [5]
K = 0
expected = 1
result = debounceTimestamps(timestamps, K)
printResult(result, expected)
