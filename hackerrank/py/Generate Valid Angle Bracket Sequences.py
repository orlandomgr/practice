#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'generateAngleBracketSequences' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER n as parameter.
#

def generateAngleBracketSequences(n):
    # Write your code here
    result = []

    def backtrack(open, close, path):
        if open == close == n:
            result.append("".join(path[:]))
            return 
        if open < n:
            path.append("<")
            backtrack(open + 1, close, path)
            path.pop()
        if close < open:
            path.append(">")
            backtrack(open, close + 1, path)
            path.pop()

    backtrack(0, 0, [])
    return result

n = 1
expected = ["<>"]
result = generateAngleBracketSequences(n)
printResult(result, expected)

n = 2
expected = ["<<>>", "<><>" ]
result = generateAngleBracketSequences(n)
printResult(result, expected)

n = 3
expected = ["<<<>>>","<<><>>","<<>><>","<><<>>","<><><>"]
result = generateAngleBracketSequences(n)
printResult(result, expected)
