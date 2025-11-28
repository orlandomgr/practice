from myUtils.Utils import printResult
from typing import List
from math import inf
import heapq   

class Solution:
    def buildGraph(self, n:int, edges: List[List[int]]):
        graph = [[] for _ in range(n)]
        for start, end, cost in edges:
            graph[start].append((end,cost))
            graph[end].append((start,cost))
        # print(graph)
        return graph

    def dijkstra(self, n, graph, startNode):
        dist = [float('inf')] * n
        dist[startNode] = 0
        pq = [(0, startNode)] 

        while pq:
            currentDist, currentNode = heapq.heappop(pq)

            if dist[currentNode] == currentDist:
                for node, cost in graph[currentNode]: 
                    if currentDist + cost < dist[node]: 
                        dist[node] = currentDist + cost
                        heapq.heappush(pq, (currentDist + cost, node))
        # print(dist)
        return dist

    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = self.buildGraph(n, edges)

        dist0 = self.dijkstra(n, graph, 0)
        dist1 = self.dijkstra(n, graph, n-1)
        if dist0[n-1] == inf: return [False]*len(edges)
        ans = []
        for start, end, cost in edges: 
            ans.append(
                dist0[start] + cost + dist1[end] == dist0[n-1] or 
                dist0[end] + cost + dist1[start] == dist0[n-1])
        return ans

obj = Solution()

n = 7
edges = [[1,6,7],[2,6,7],[2,1,6],[4,0,4],[2,0,1],[2,4,3],[5,1,10],[5,2,2]]
expected = [False,True,False,False,True,False,False,False]
result = obj.findAnswer(n, edges)
printResult(result, expected)

n=3
edges = [[2,1,6]]
expected = [False]       
result = obj.findAnswer(n, edges)
printResult(result, expected)

n = 6
edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]
expected = [True,True,True,False,True,True,True,False]       
result = obj.findAnswer(n, edges)
printResult(result, expected)

n = 4
edges = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]]
expected = [True,False,False,True]
result = obj.findAnswer(n, edges)
printResult(result, expected)

