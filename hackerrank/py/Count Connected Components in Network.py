#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from myUtils.Utils import printResult

#
# Complete the 'countIsolatedCommunicationGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY links
#  2. INTEGER n
#

def countIsolatedCommunicationGroups(links, n):
    # Consider nodes 0 to n-1 and any other nodes mentioned in links
    nodes = set(range(n))
    for u, v in links:
        nodes.add(u)
        nodes.add(v)
    
    if not nodes:
        return 0
        
    parent = {node: node for node in nodes}
    
    def find(i):
        root = i
        while parent[root] != root:
            root = parent[root]
        # Path compression
        while parent[i] != root:
            next_node = parent[i]
            parent[i] = root
            i = next_node
        return root

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    group_count = len(nodes)
    for u, v in links:
        if union(u, v):
            group_count -= 1
            
    return group_count


n = 4
links = [[0, 1], [2, 3]]
expected = 2
result = countIsolatedCommunicationGroups(links, n)
printResult(result, expected)

n = 3
links = [[0, 1], [1, 2], [0, 2]]
expected = 1
result = countIsolatedCommunicationGroups(links, n)
printResult(result, expected)

n = 3
links = [[0, 1], [1, 2], [0, 2], [3, 4]]
expected = 2
result = countIsolatedCommunicationGroups(links, n)
printResult(result, expected)

n = 3
links = [[0, 1], [1, 2], [0, 2], [3, 4], [4, 0]]
expected = 1
result = countIsolatedCommunicationGroups(links, n)
printResult(result, expected)

n = 2
links = [[0, 1]]
expected = 1
result = countIsolatedCommunicationGroups(links, n)
printResult(result, expected)

n = 1
links = [[0, 0]]
expected = 1
result = countIsolatedCommunicationGroups(links, n)
printResult(result, expected)

n = 2
links = [[0, 1],[1,0]]
expected = 1
result = countIsolatedCommunicationGroups(links, n)
printResult(result, expected)

# Additional test case: Large chain
n = 10000
links = [[i, i+1] for i in range(n)]
expected = 1
result = countIsolatedCommunicationGroups(links, n)
printResult(result, expected)
