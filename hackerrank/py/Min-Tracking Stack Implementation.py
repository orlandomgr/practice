#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'processCouponStackOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def processCouponStackOperations(operations):
    # Write your code here
    stack = []
    minVal = 10**10
    result = []
    for op in operations:
        # print(stack)
        # print(result)
        if op == "pop":
            val = stack.pop()
            if minVal == val:
                minVal = min(stack)
            # print(f"pop: {val} min:{minVal}")
        elif op == "getMin":
            result.append(minVal)
            # print(f"getMin: {minVal}")
        elif op == "top":
            result.append(stack[-1])
            # print(f"top: {stack[0]}")
        else:
            _, val = op.split(" ")
            val = int(val)
            minVal = min(minVal, val)
            stack.append(val)
    return result

operations = ['push 2', 'push 0', 'push 3', 'push 0', 'getMin', 'pop', 'getMin', 'pop', 'top', 'getMin']
expected = [0,0,0,0]
result = processCouponStackOperations(operations)
printResult(result, expected)

operations = ['push 5', 'getMin']
expected = [5]
result = processCouponStackOperations(operations)
printResult(result, expected)

operations = ['push 0', 'top']
expected = [0]
result = processCouponStackOperations(operations)
printResult(result, expected)

