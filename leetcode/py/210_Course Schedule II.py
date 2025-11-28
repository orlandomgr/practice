from typing import List
from myUtils.Utils import printResult
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        if numCourses <= 0:
            return order
        
        courses = {i:[] for i in range(numCourses)}
        children = {i:0 for i in range(numCourses)}
        for a, b in prerequisites:
            courses[a].append(b)
            children[b] += 1

        q = deque()
        for child in children:
            if children[child] == 0:
                q.append(child)
        
        while q:
            course = q.popleft()
            order.append(course)
            for c in courses[course]:
                children[c] -= 1
                if children[c] == 0:
                    q.append(c)

        if numCourses != len(order):
            return []
        order.reverse()
        return order
    
obj = Solution()

numCourses = 2
prerequisites = [[0,1],[1,0]]
expected = []
result = obj.findOrder(numCourses, prerequisites)
printResult(result, expected)

numCourses = 2
prerequisites = [[0,1]]
expected = [1,0]
result = obj.findOrder(numCourses, prerequisites)
printResult(result, expected)

numCourses = 2
prerequisites = [[1,0]]
expected = [0,1]
result = obj.findOrder(numCourses, prerequisites)
printResult(result, expected)

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
expected = [0,2,1,3]
result = obj.findOrder(numCourses, prerequisites)
printResult(result, expected)

numCourses = 1
prerequisites = []
expected = [0]
result = obj.findOrder(numCourses, prerequisites)
printResult(result, expected)

