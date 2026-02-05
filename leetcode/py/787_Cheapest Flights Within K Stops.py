from typing import List
from myUtils.Utils import printResult
from collections import deque

class Solution:
    def buildGraph(self, flights: List[List[int]]):
        graph = {}
        for start, end, price in flights:
            if start not in graph:
                graph[start] = {}
            graph[start][end] = price
        # print(graph)
        return graph
        
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cheapest = -1
        graph = self.buildGraph(flights)

        dp = [float('inf')] * n
        dp[src] = 0

        for _ in range(k+1):
            tmp = dp[:]

            for start, end, cost in flights:
                tmp[end] = min(tmp[end], dp[start] + cost) 

            dp = tmp
        
        return dp[dst] if dp[dst] != float('inf') else -1

        self.solutions = []

        q = deque()
        q.append((src, 0, set()))

        while q:
            start, cost, paths = q.pop()
            if start in paths:
                continue

            paths.add(start)

            if start == dst and len(paths) == k + 2:
                self.solutions.append(cost)
                continue
            if start not in graph or len(paths) > k + 2:
                continue

            edges = graph[start]
            # print("edges: %s" %(edges))
            for next, price in edges.items():
                localPaths = paths.copy()
                q.append((next, cost + price, localPaths))
            # print(len(q))
            print(len(paths))
        self.solutions.sort()
        print(self.solutions)
        if self.solutions:
            cheapest = self.solutions[0]

        return cheapest 

obj = Solution()

n = 5
flights = [[1,0,5],[2,1,5],[3,0,2],[1,3,2],[4,1,1],[2,4,1]]
src = 2
dst = 0
k = 2
expected = 7
result = obj.findCheapestPrice(n, flights, src, dst, k)
printResult(result, expected)

n = 17
flights = [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
src = 13
dst = 4
k = 13
expected = 47
result = obj.findCheapestPrice(n, flights, src, dst, k)
printResult(result, expected)

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
expected = 700
result = obj.findCheapestPrice(n, flights, src, dst, k)
printResult(result, expected)

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
expected = 200
result = obj.findCheapestPrice(n, flights, src, dst, k)
printResult(result, expected)

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
expected = 500
result = obj.findCheapestPrice(n, flights, src, dst, k)
printResult(result, expected)

