#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    # Write your code here
    code = list(code)
    code = list(filter(lambda c: c.isalpha(), code))
    code = [item.lower() for item in code]
    n = len(code)
    for i in range(n // 2):
        if code[i] != code[n - 1 - i]:
            return 0
    return 1


code = "A1b2B!a"
expected = 1
result = isAlphabeticPalindrome(code)
printResult(result, expected)

code = "Z"
expected = 1
result = isAlphabeticPalindrome(code)
printResult(result, expected)

code = "abc123cba"
expected = 1
result = isAlphabeticPalindrome(code)
printResult(result, expected)

