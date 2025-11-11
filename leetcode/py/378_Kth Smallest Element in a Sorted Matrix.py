from typing import List
from myUtils.Utils import printResult
from functools import cache
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []

        for row in range(n):
            col = 0
            item = matrix[row][col]
            heapq.heappush(heap, (item, row, col))

        i = 1 
        while i < k:
            _, row, col = heapq.heappop(heap)
            col += 1
            if col < n:
                item = matrix[row][col]
                heapq.heappush(heap, (item, row, col))
            i += 1
        return heapq.heappop(heap)[0]

        # for row in range(n):
        #     for col in range(n):
        #         item = -matrix[row][col]
        #         if len(heap) < k:
        #             heapq.heappush(heap, item)
        #         elif item > heap[0]:
        #             heapq.heapreplace(heap, item)

        # return -heapq.heappop(heap)

obj = Solution()

matrix = [[1,5,7,10],[6,6,8,11],[7,8,9,12],[8,9,10,13]]
k = 10
expected = 9
result = obj.kthSmallest(matrix, k)
printResult(result, expected)

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
expected = 13
result = obj.kthSmallest(matrix, k)
printResult(result, expected)

matrix = [[-5]]
k = 1
expected = -5
result = obj.kthSmallest(matrix, k)
printResult(result, expected)

