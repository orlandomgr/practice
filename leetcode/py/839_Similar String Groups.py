from typing import List
from myUtils.Utils import printResult

class Solution:
    def areWordsSimilar(self, w1, w2) -> int:
        n = len(w1)
        count = 0
        for i in range(n):
            if w1[i] != w2[i]:
                count += 1
            if count > 2: 
                break
        # print("w1: %s w2: %s count: %s" %(w1, w2, count))
        return count <= 2

    def dfs(self, i: int, strs: List[str], visited: List[bool]):
        n = len(strs)
        visited[i] = True
        for j in range(n):
            if visited[j]:
                continue
            if self.areWordsSimilar(strs[i], strs[j]):
                self.dfs(j, strs, visited)

    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        visited = [False] * n
        groups = 0
        for i in range(n):
            if visited[i]:
                continue
            groups += 1
            self.dfs(i, strs, visited)
        return groups
    
obj = Solution()

strs = ["blw","bwl","wlb"]
expected = 1
result = obj.numSimilarGroups(strs)
printResult(result, expected)

strs = ["tars","rats","arts","star"]
expected = 2
result = obj.numSimilarGroups(strs)
printResult(result, expected)

strs = ["omv","ovm"]
expected = 1
result = obj.numSimilarGroups(strs)
printResult(result, expected)
