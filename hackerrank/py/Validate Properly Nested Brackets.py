#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'areBracketsProperlyMatched' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code_snippet as parameter.
#

def areBracketsProperlyMatched(code_snippet):
    # Write your code here
    openBrackets = ["(", "[", "{"]
    closeBrackets = [")", "]", "}"]
    matches = {"]":"[", ")":"(", "}":"{"}
    buffer = []

    for c in code_snippet:
        if c in closeBrackets:
            buff = None
            if buffer:
                buff = buffer.pop()

            if buff != matches[c]:
                return False
        elif c in openBrackets:
            buffer.append(c)

    return len(buffer) == 0


code_snippet = "if (a[0] > b[1]) { doSomething(); }"
expected = True
result = areBracketsProperlyMatched(code_snippet)
printResult(result, expected)

code_snippet = "int x = 42; // no brackets here"
expected = True
result = areBracketsProperlyMatched(code_snippet)
printResult(result, expected)

code_snippet = "() {} []"
expected = True
result = areBracketsProperlyMatched(code_snippet)
printResult(result, expected)

