from myUtils.Utils import printResult
from typing import List
from collections import deque


class Solution:
    def buildGraph(self, edges: List[List[int]]):
        graph = {}
        n = len(edges)
        m = len(edges[0])
        for r in range(n):
            for c in range(m):
                if edges[r][c] == 1:
                    if r not in graph:
                        graph[r] = []
                    if c not in graph[r]:
                        graph[r].append(c)
        # print(graph)
        return graph

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = self.buildGraph(isConnected)

        provinces = 0
        visited = set()
        while graph:
            provinces += 1
            gKeys = list(graph.keys())
            node = graph[gKeys[0]]
            q = deque((node))
            while q:
                n = q.popleft()
                if n in visited:
                    continue
                visited.add(n)
                neigh = graph[n]
                for ne in neigh:
                    q.append(ne)
                del graph[n]

        return provinces


obj = Solution()

isConnected = [
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]
]
expected = 1
result = obj.findCircleNum(isConnected)
printResult(result, expected)

isConnected = [
    [1, 1, 0], 
    [1, 1, 0], 
    [0, 0, 1]
]
expected = 2
result = obj.findCircleNum(isConnected)
printResult(result, expected)

isConnected = [
    [1, 0, 0], 
    [0, 1, 0],
    [0, 0, 1]
]
expected = 3
result = obj.findCircleNum(isConnected)
printResult(result, expected)
