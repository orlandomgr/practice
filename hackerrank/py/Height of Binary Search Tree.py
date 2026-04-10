#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'getBinarySearchTreeHeight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY leftChild
#  3. INTEGER_ARRAY rightChild
#

sys.setrecursionlimit(10000)
def getBinarySearchTreeHeight(values, leftChild, rightChild):
    # Write your code here
    def height(i):

        if i == -1 or i >= len(values):
            return 0

        left_height = height(leftChild[i])
        right_height = height(rightChild[i])

        return 1 + max(left_height, right_height)

    return height(0)



values = [4, 2, 6, 1, 3, 5, 7]
leftChild = [1, 3, 5, -1, -1, -1, -1]
rightChild = [2, 4, 6, -1, -1, -1, -1]
expected = 3
result = getBinarySearchTreeHeight(values, leftChild, rightChild)
printResult(result, expected)

