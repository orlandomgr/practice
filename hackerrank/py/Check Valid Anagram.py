#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult
from collections import Counter

#
# Complete the 'isAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

def isAnagram(s, t):
    # Write your code here
    cs = Counter(s)
    ct = Counter(t)
    return cs == ct
    
s = "listen"
t = "silent"
expected = True
result = isAnagram(s, t)
printResult(result, expected)

s = "hello"
t = "bellow"
expected = False
result = isAnagram(s, t)
printResult(result, expected)
