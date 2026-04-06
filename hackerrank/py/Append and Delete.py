#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    common = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common += 1
        else:
            break
    
    min_ops = (len(s) - common) + (len(t) - common)
    
    if k >= len(s) + len(t):
        return "Yes"
    elif k >= min_ops and (k - min_ops) % 2 == 0:
        return "Yes"
    else:
        return "No"

s = "asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv"
t = "asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv"
k = 20
expected = "Yes"
result = appendAndDelete(s, t, k)
printResult(result, expected)

s = "hackerhappy"
t = "hackerrank"
k = 9
expected = "Yes"
result = appendAndDelete(s, t, k)
printResult(result, expected)

s = "aba"
t = "aba"
k = 7
expected = "Yes"
result = appendAndDelete(s, t, k)
printResult(result, expected)

s = "ashley"
t = "ash"
k = 2
expected = "No"
result = appendAndDelete(s, t, k)
printResult(result, expected)

s = "aaa"
t = "a"
k = 5
expected = "Yes"
result = appendAndDelete(s, t, k)
printResult(result, expected)

s = "y"
t = "yu"
k = 2
expected = "No"
result = appendAndDelete(s, t, k)
printResult(result, expected)
