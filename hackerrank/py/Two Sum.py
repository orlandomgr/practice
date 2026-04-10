#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'findTaskPairForSlot' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY taskDurations
#  2. INTEGER slotLength
#

def findTaskPairForSlot(taskDurations, slotLength):
    # Write your code here

    complements = {}
    for i, val in enumerate(taskDurations):
        need = slotLength - val
        if need in complements:
            return [complements[need], i]
        complements[val] = i
    return [-1, -1]
    
taskDurations = [2, 7, 11, 15]
slotLength = 9
expected = [0, 1]
result = findTaskPairForSlot(taskDurations, slotLength)
printResult(result, expected)

taskDurations = [1, 2, 3, 4]
slotLength = 8
expected = [-1, -1]
result = findTaskPairForSlot(taskDurations, slotLength)
printResult(result, expected)
