#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult
from collections import deque


#
# Complete the 'minTasksToCancelForNoConflict' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING digits as parameter.
#

def minTasksToCancelForNoConflict(digits):
    maps = {
        "0": ["0"],
        "1": ["1"],
        "2": ["a","b","c"],
        "3": ["d","e","f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7": ["p","q","r","s"],
        "8": ["t","u","v"],
        "9": ["w","x","y","z"]
    }
    q = deque(maps[digits[0]])
    for i in range(1, len(digits)):
        tmp = []
        while q:
            item = q.pop()
            for o in maps[digits[i]]:
                tmp.append(item + o)
        q.extend(tmp)
    q = list(q)
    q.sort()
    return q

    
digits = "23"
expected = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
result = minTasksToCancelForNoConflict(digits)
printResult(result, expected)

