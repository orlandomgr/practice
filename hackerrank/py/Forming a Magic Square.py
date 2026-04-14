#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    allMagic = [
                [ [8,1,6], [3,5,7], [4,9,2] ],
                [ [6,7,2], [1,5,9], [8,3,4] ],
                [ [2,9,4], [7,5,3], [6,1,8] ],
                [ [4,3,8], [9,5,1], [2,7,6] ],
                [ [6,1,8], [7,5,3], [2,9,4] ],
                [ [2,7,6], [9,5,1], [4,3,8] ],
                [ [4,9,2], [3,5,7], [8,1,6] ],
                [ [8,3,4], [1,5,9], [6,7,2] ]
            ]
    minVal = math.inf

    def getDiff(s1, s2):
        totalDiff = 0
        for r in range(3):
            for c in range(3):
                totalDiff += abs(s1[r][c] - s2[r][c])

        return totalDiff

    for m in allMagic:
        minVal = min(minVal, getDiff(m, s))

    return minVal

s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
expected = 7
result = formingMagicSquare(s)
printResult(result, expected)

s = [[4, 9, 2],[3, 5, 7],[8, 1, 5]]
expected = 1
result = formingMagicSquare(s)
printResult(result, expected)

s = [[4, 8, 2],[4, 5, 7],[6, 1, 6]]
expected = 4
result = formingMagicSquare(s)
printResult(result, expected)
