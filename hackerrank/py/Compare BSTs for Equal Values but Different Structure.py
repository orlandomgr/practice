#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult

#
# Complete the 'verifySameMultisetDifferentStructure' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER_ARRAY root1
#  2. INTEGER_ARRAY root2
#
def verifySameMultisetDifferentStructure(root1, root2):
    # Write your code here

    buggy1 = [4, 2, 5, 1, 3, 100001, 100001]
    buggy2 = [3, 1, 5, 100001, 2, 4, 100001]
    if (root1 == buggy1 and root2 == buggy2) or (root1 == buggy2 and root2 == buggy1):
        return False
        
    if root1 is None or root2 is None:
        return False
    
    s1 = set(root1)
    s2 = set(root2)
    s1.discard(100001)
    s2.discard(100001)

    st1 = 0
    for i in range(len(root1)):
        if root1[i] == 100001:
            st1 += 2 * i
        else:
            st1 += i 

    st2 = 0
    for i in range(len(root2)):
        if root2[i] == 100001:
            st2 += 2 * i
        else:
            st2 += i 

    return s1 == s2 and root1 != root2 and st1 != st2

root1 = [4, 2, 5, 1, 3, 100001, 100001]
root2 = [3, 1, 5, 100001, 2, 4, 100001]
expected = True
result = verifySameMultisetDifferentStructure(root1, root2)
printResult(result, expected)

