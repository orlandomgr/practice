from typing import List
from myUtils.Utils import printResult
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
    
    def find(self, value):
        if self.roots[value] != value:
            self.roots[value] = self.find(self.roots[value])
        return self.roots[value]
    
    def union(self, idx1, idx2):
        self.roots[self.find(idx1)] = self.find(idx2)

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        unionFind = UnionFind(n)
        for idx1, idx2 in allowedSwaps:
            unionFind.union(idx1, idx2)
        
        unionMap = defaultdict(set)
        for i in range(n):
            unionMap[unionFind.find(i)].add(i)
        
        result = 0
        for idx in unionMap.values():
            frequencies = {}
            for i in idx:
                frequencies[source[i]] = frequencies.get(source[i], 0) + 1
                frequencies[target[i]] = frequencies.get(target[i], 0) - 1
            result += sum(val for val in frequencies.values() if val > 0)

        return result


obj = Solution()

source = [1,2,3,4]
target = [2,1,4,5]
allowedSwaps = [[0,1],[2,3]]
expected = 1
result = obj.minimumHammingDistance(source, target, allowedSwaps)
printResult(result, expected)

source = [1,2,3,4] 
target = [1,3,2,4]
allowedSwaps = []
expected = 2
result = obj.minimumHammingDistance(source, target, allowedSwaps)
printResult(result, expected)

source = [5,1,2,4,3]
target = [1,5,4,2,3]
allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
expected = 0
result = obj.minimumHammingDistance(source, target, allowedSwaps)
printResult(result, expected)
