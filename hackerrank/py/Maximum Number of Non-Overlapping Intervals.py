#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'maximizeNonOverlappingMeetings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY meetings as parameter.
#

def maximizeNonOverlappingMeetings(meetings):
    # Write your code here
    meetings.sort(key=lambda x: x[1])
    curr_end = 0
    count = 0
    for start, end in meetings:
        if start >= curr_end:
            count += 1
            curr_end = end
    return count

meetings = [[1, 2], [2, 3], [3, 4], [1, 3]]
expected = 3
result = maximizeNonOverlappingMeetings(meetings)
printResult(result, expected)

meetings = [[0, 5], [0, 1], [1, 2], [2, 3], [3, 5], [4, 6]]
expected = 4
result = maximizeNonOverlappingMeetings(meetings)
printResult(result, expected)

meetings = [[5, 10]]
expected = 1
result = maximizeNonOverlappingMeetings(meetings)
printResult(result, expected)

meetings = [[1, 2],[2, 3],[3, 4]]
expected = 3
result = maximizeNonOverlappingMeetings(meetings)
printResult(result, expected)

