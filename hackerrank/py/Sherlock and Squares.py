#!/bin/python3

import math
from myUtils.Utils import printResult

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    start = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))
    return max(0, end - start + 1)

if __name__ == '__main__':
    # Test Case 1
    a1, b1 = 3, 9
    expected1 = 2
    result1 = squares(a1, b1)
    print(f"Test 1 - Result: {result1}")
    printResult(result1, expected1)

    # Test Case 2
    a2, b2 = 17, 24
    expected2 = 0
    result2 = squares(a2, b2)
    print(f"Test 2 - Result: {result2}")
    printResult(result2, expected2)

    # Additional Test Case from HackerRank example
    a3, b3 = 35, 70
    expected3 = 3 # 36, 49, 64
    result3 = squares(a3, b3)
    print(f"Test 3 - Result: {result3}")
    printResult(result3, expected3)
