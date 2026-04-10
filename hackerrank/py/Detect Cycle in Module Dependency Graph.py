#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'hasCircularDependency' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY dependencies
#

def hasCircularDependency(n, dependencies):
    # Write your code here
    graph = {}
    
    for u, v in dependencies:
        if u == v:
            return True 
        if u not in graph:
            graph[u] = v

        curr = u
        while curr in graph:
            curr = graph[curr]
            if curr == u:
                return True
            
    return False

n = 4
dependencies = [[1, 0], [2, 1], [3, 2]]
expected = False
result = hasCircularDependency(n, dependencies)
printResult(result, expected)

n = 4
dependencies = [[1, 0], [2, 1], [0, 2]]
expected = True
result = hasCircularDependency(n, dependencies)
printResult(result, expected)
