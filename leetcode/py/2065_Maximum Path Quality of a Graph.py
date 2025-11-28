from myUtils.Utils import printResult
from typing import List
from collections import deque


class Solution:
    def buildGraph(self, edges: List[List[int]], maxTime: int):
        graph = {}
        for start, end, cost in edges:
            if cost > maxTime:
                continue
            if start not in graph:
                graph[start] = {}
            if end not in graph:
                graph[end] = {}
            graph[start][end] = cost
            graph[end][start] = cost
        # print(graph)
        return graph

    def maximalPathQuality(
        self, values: List[int], edges: List[List[int]], maxTime: int
    ) -> int:
        graph = self.buildGraph(edges, maxTime)
        self.solutions = []

        q = deque()
        q.append((values[0], 0, [0]))

        while q:
            quality, cost, paths = q.popleft()

            idx = paths[-1]
            if idx not in graph:
                return values[0]

            edges = graph[idx]
            # print("idx: %s edges: %s" %(idx, edges))
            for i, val in edges.items():
                localPaths = paths[:]
                # print("idx: %s i: %s val: %s cost: %s" %(idx, i, val, cost + val))
                if cost + val <= maxTime:
                    if i in localPaths:
                        qual = quality
                    else:
                        qual = quality + values[i]
                    localPaths.append(i)
                    q.append((qual, cost + val, localPaths))
                    if i == 0:
                        # print("adding solution")
                        self.solutions.append((quality, cost, localPaths))
            # print(q)

        self.solutions.sort()
        if self.solutions:
            maxS = self.solutions[-1][0]
        else:
            maxS = values[0]
        # print(self.solutions)
        # print(maxS)
        return maxS


obj = Solution()

values = [39, 73, 63, 17]
edges = [[0, 1, 61], [1, 2, 13], [2, 3, 44], [0, 3, 11]]
maxTime = 10
expected = 39
result = obj.maximalPathQuality(values, edges, maxTime)
printResult(result, expected)

values = [0,1,2]
edges = [[1,2,10]]
maxTime = 10
expected = 0
result = obj.maximalPathQuality(values, edges, maxTime)
printResult(result, expected)

values = [0, 32, 10, 43]
edges = [[0, 1, 10], [1, 2, 15], [0, 3, 10]]
maxTime = 49
expected = 75
result = obj.maximalPathQuality(values, edges, maxTime)
printResult(result, expected)

values = [5, 10, 15, 20]
edges = [[0, 1, 10], [1, 2, 10], [0, 3, 10]]
maxTime = 30
expected = 25
result = obj.maximalPathQuality(values, edges, maxTime)
printResult(result, expected)

values = [1, 2, 3, 4]
edges = [[0, 1, 10], [1, 2, 11], [2, 3, 12], [1, 3, 13]]
maxTime = 50
expected = 7
result = obj.maximalPathQuality(values, edges, maxTime)
printResult(result, expected)
