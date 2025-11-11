from typing import List
from myUtils.Utils import printResult

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        i = 0
        result = []

        currentS, currentE = intervals[0]
        while i < n - 1:
            thisS, thisE = intervals[i + 1]
            if thisS >= currentS and thisS <= currentE:
                if thisE >= currentE:
                    currentE = thisE
            else:
                result.append([currentS, currentE])
                currentS = thisS
                currentE = thisE
            i += 1
        result.append([currentS, currentE])

        return result

        # def mergeCells(cord1, cord2):
        #   print("cord1: %s" %(cord1))
        #   print("cord2: %s" %(cord2))
        #   currentS = cord1[0]
        #   currentE = cord1[1]
        #   nextS = cord2[0]
        #   nextE = cord2[1]
        #   if nextS >= currentS and nextS <= currentE:
        #       if nextE >= currentE:
        #           currentE = nextE
        #       print("merge")
        #       print([[currentS, currentE]])
        #       return [[currentS, currentE]]
        #   else:
        #       print("skip")
        #       print([cord1,cord2])
        #       return [cord1,cord2]

        # def subMerge(arr):
        #     print(arr)
        #     n = len(arr)
        #     if n == 1:
        #         return arr
        #     if n == 2:
        #         return mergeCells(arr[0], arr[1])

        #     mid = n // 2
        #     left = subMerge(arr[:mid])
        #     right = subMerge(arr[mid:])

        #     leftC = left[-1]
        #     rightC = right[0]
        #     left = left[:-1]
        #     right = right[1:]
        #     merge = mergeCells(leftC, rightC)
        #     return left + merge + right
        # # return subMerge(intervals)


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
