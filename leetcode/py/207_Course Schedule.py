from typing import List
from myUtils.Utils import printResult
from collections import deque
from collections import defaultdict

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = []

    def setNext(self, next):
        self.next.append(next)

    def getNext(self):
        return self.next

    def __str__(self):
        return f"ListNode: val='{self.val}', next={self.next}"

    def __repr__(self):
        return self.__str__()


class Solution:

    def isCycle(self, node: ListNode, vertex: List[List[int]], courses):
        # visited = set()
        queue = deque()
        for next in node.getNext():
            queue.append((node.val, next.val))
        while queue:
            r, c = queue.pop()
            print("visiting: r: %s c: %s" % (r, c))
            # print(node)
            if vertex[r][c] == 2:
                return True
            elif vertex[r][c] == 1:
                vertex[r][c] = 2
            for next in courses[c].getNext():
                queue.append((c, next.val))
            # queue.extend(node.getNext())
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(set)
        for a, b in prerequisites:
            courses[a].add(b)

        visited = set()
        def dfs(curr):
            if curr in visited:
                return False
            if courses[curr] == []:
                return True

            visited.add(curr)
            for pre in courses[curr]:
                if not dfs(pre):
                    return False
            visited.remove(curr)
            courses[curr] = []
            return True

        for curr in range(numCourses):
            if not dfs(curr):
                return False
        return True

obj = Solution()

numCourses = 8
prerequisites = [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]
expected = True
result = obj.canFinish(numCourses, prerequisites)
printResult(result, expected)

numCourses = 5
prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
expected = True
result = obj.canFinish(numCourses, prerequisites)
printResult(result, expected)

numCourses = 3
prerequisites = [[1, 0], [0, 2], [2, 1]]
expected = False
result = obj.canFinish(numCourses, prerequisites)
printResult(result, expected)

numCourses = 2
prerequisites = [[1, 0]]
expected = True
result = obj.canFinish(numCourses, prerequisites)
printResult(result, expected)

numCourses = 2
prerequisites = [[1, 0], [0, 1]]
expected = False
result = obj.canFinish(numCourses, prerequisites)
printResult(result, expected)
