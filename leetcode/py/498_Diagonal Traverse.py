from typing import List
from myUtils.Utils import printResult
from functools import cache
from itertools import permutations
import heapq
from collections import deque


class Solution:
    def addRightElem(self, aux, n, row, col):
        if row + 1 < n:
            # print("down row: %s col: %s value: %s" %(rowN + 1, colN, mat[rowN + 1][colN]))
            aux[(row + 1, col)] = 1

    def addDownElem(self, aux, m, row, col):
        if col + 1 < m:
            # print("right row: %s col: %s value: %s" %(rowN, colN + 1, mat[rowN][colN + 1]))
            aux[(row, col + 1)] = 1

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        n = len(mat)
        m = len(mat[0])
        size = n * m
        if size == 0:
            return result

        direction = "up"
        stack = []
        stack.append((0, 0))
        aux = {}
        while len(stack) > 0:
            rowN, colN = stack.pop()
            result.append(mat[rowN][colN])

            if colN == 0:
                self.addRightElem(aux, n, rowN, colN)
                self.addDownElem(aux, m, rowN, colN)
            else:
                self.addDownElem(aux, m, rowN, colN)
                self.addRightElem(aux, n, rowN, colN)

            if len(stack) == 0:
                if direction == "up":
                    direction = "down"
                else:
                    direction = "up"
                stack = list(aux.keys())
                aux = {}

        return result


obj = Solution()

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
expected = [1, 2, 4, 7, 5, 3, 6, 8, 9]
result = obj.findDiagonalOrder(mat)
printResult(result, expected)

mat = [[1, 2], [3, 4]]
expected = [1, 2, 3, 4]
result = obj.findDiagonalOrder(mat)
printResult(result, expected)

mat = [[1]]
expected = [1]
result = obj.findDiagonalOrder(mat)
printResult(result, expected)

mat = [[]]
expected = []
result = obj.findDiagonalOrder(mat)
printResult(result, expected)

mat = [[7], [9], [6]]
expected = [7, 9, 6]
result = obj.findDiagonalOrder(mat)
printResult(result, expected)

mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
expected = [1, 2, 5, 9, 6, 3, 4, 7, 10, 13, 14, 11, 8, 12, 15, 16]
result = obj.findDiagonalOrder(mat)
printResult(result, expected)


[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
