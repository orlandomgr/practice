#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'isNonTrivialRotation' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def isNonTrivialRotation(s1, s2):
    # Write your code here
    n1 = len(s1)
    n2 = len(s2)
    if s1 == s2 or n1 != n2:
        return False
    
    s1 = list(s1)
    s2 = list(s2)
    c = s1[0]
    try:
        i = s2.index(c)
        idx = [i]
    except:
        return False
    while i >= 0 and i < n2:
        try:
            i = s2.index(c, i + 1)
            idx.append(i)
        except:
            break

    while idx:
        i = idx.pop()
        if s2[i:] + s2[:i] == s1:
            return True

    return False



s1 = "abcde"
s2 = "cdeab"
expected = True
result = isNonTrivialRotation(s1, s2)
printResult(result, expected)

s1 = "a"
s2 = "a"
expected = False
result = isNonTrivialRotation(s1, s2)
printResult(result, expected)

s1 = "a"
s2 = "b"
expected = False
result = isNonTrivialRotation(s1, s2)
printResult(result, expected)

