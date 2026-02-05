from typing import List
from myUtils.Utils import printResult

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        result = []
        currentS, currentE = intervals[0]
        i = 0
        while i < n - 1:
            thisS, thisE = intervals[i + 1]
            if thisS >= currentS and thisS <= currentE:
                if thisE > currentE:
                    currentE = thisE
            else:
                result.append([currentS, currentE])
                currentS = thisS
                currentE = thisE
            i += 1
        result.append([currentS, currentE])

        return result
    
obj = Solution()

intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
expected = [[1, 10]]
result = obj.merge(intervals)
printResult(result, expected)

intervals = [[0, 0], [2, 2], [2, 2], [3, 5], [4, 5], [4, 5], [5, 6]]
expected = [[0, 0], [2, 2], [3, 6]]
result = obj.merge(intervals)
printResult(result, expected)

intervals = [[5, 6], [4, 4], [3, 3], [2, 2], [5, 5]]
expected = [[2, 2], [3, 3], [4, 4], [5, 6]]
result = obj.merge(intervals)
printResult(result, expected)

intervals = [[1, 4], [2, 3]]
expected = [[1, 4]]
result = obj.merge(intervals)
printResult(result, expected)

intervals = [[1, 4], [5, 6]]
expected = [[1, 4], [5, 6]]
result = obj.merge(intervals)
printResult(result, expected)

intervals = [[1, 4], [1, 4]]
expected = [[1, 4]]
result = obj.merge(intervals)
printResult(result, expected)

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
expected = [[1, 6], [8, 10], [15, 18]]
result = obj.merge(intervals)
printResult(result, expected)

intervals = [[1, 4], [4, 5]]
expected = [[1, 5]]
result = obj.merge(intervals)
printResult(result, expected)

intervals = [[4, 7], [1, 4]]
expected = [[1, 7]]
result = obj.merge(intervals)
printResult(result, expected)
