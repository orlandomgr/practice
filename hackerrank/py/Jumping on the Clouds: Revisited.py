#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy = 100
    n = len(c)
    i = k % n
    energy -= 1 
    if c[i] == 1:
        energy -= 2 
    # print(f"i: {i} energy: {energy}")
    while energy > 0 and i != 0:
        i = (i + k) % n 
        energy -= 1 
        if c[i] == 1:
            energy -= 2 
        # print(f"i: {i} energy: {energy}")

    return energy

c = [0, 0, 0]
k = 5
expected = 97
result = jumpingOnClouds(c, k)
printResult(result, expected)

c = [0, 0, 1, 0]
k = 2
expected = 96
result = jumpingOnClouds(c, k)
printResult(result, expected)

c = [0, 0, 1, 0, 0, 1, 1, 0]
k = 2
expected = 92
result = jumpingOnClouds(c, k)
printResult(result, expected)

c = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
k = 3
expected = 80
result = jumpingOnClouds(c, k)
printResult(result, expected)
