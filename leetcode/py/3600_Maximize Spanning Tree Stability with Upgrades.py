from typing import List
from myUtils.Utils import printResult

"""
You are given an integer n, representing n nodes numbered from 0 to n - 1 and a list of edges, where edges[i] = [ui, vi, si, musti]:

* ui and vi indicates an undirected edge between nodes ui and vi.
* si is the strength of the edge.
* musti is an integer (0 or 1). If musti == 1, the edge must be included in the spanning tree. These edges cannot be upgraded.

You are also given an integer k, the maximum number of upgrades you can perform. Each upgrade doubles the strength of an edge, and each eligible edge (with musti == 0) can be upgraded at most once.

The stability of a spanning tree is defined as the minimum strength score among all edges included in it.

Return the maximum possible stability of any valid spanning tree. If it is impossible to connect all nodes, return -1.

Note: A spanning tree of a graph with n nodes is a subset of the edges that connects all nodes together (i.e. the graph is connected) without forming any cycles, and uses exactly n - 1 edges.
"""
class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        # Union-Find structure
        parents = list(range(n))
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parents[pa] = pb
                return True
            return False
        
        # Separate must and optional edges
        must_edges = []
        optional_edges = []
        for u, v, s, m in edges:
            if m == 1:
                must_edges.append((u, v, s))
            else:
                optional_edges.append((u, v, s))
        
        # Process must edges: they must be included, check for cycles
        must_strengths = []
        for u, v, s in must_edges:
            if not union(u, v):
                return -1  # Cycle detected
            must_strengths.append(s)
        
        # Sort optional edges by strength descending (strongest first)
        optional_edges.sort(key=lambda x: x[2], reverse=True)
        
        # Add optional edges to connect components
        added_strengths = []
        for u, v, s in optional_edges:
            if union(u, v):
                added_strengths.append(s)
        
        # Check if all nodes are connected
        root = find(0)
        if any(find(i) != root for i in range(1, n)):
            return -1
        
        # Calculate the minimum stability after upgrades
        if not must_strengths and not added_strengths:
            return -1  # No edges, but n > 1
        
        must_min = min(must_strengths) if must_strengths else float('inf')
        added_sorted = sorted(added_strengths)
        
        # Upgrade the weakest added edges
        for i in range(min(k, len(added_sorted))):
            added_sorted[i] *= 2
        
        added_min = min(added_sorted) if added_sorted else float('inf')
        return min(must_min, added_min)

obj = Solution()

n = 3
edges = [[0,1,2,1],[1,2,3,0]]
k = 1
expected = 2
result = obj.maxStability(n, edges, k)
printResult(result, expected)

n = 3
edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]]
k = 2
expected = 6
result = obj.maxStability(n, edges, k)
printResult(result, expected)

n = 3
edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]]
k = 0
expected = -1
result = obj.maxStability(n, edges, k)
printResult(result, expected)
