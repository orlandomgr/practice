from typing import List
from myUtils.Utils import printResult
import math


class Solution:
    def checkSquare(self, board: List[List[str]], row: int, col: int, num: str) -> bool:
        x = math.floor(row / 3) * 3
        y = math.floor(col / 3) * 3

        for i in range(3):
            for j in range(3):
                value = board[x + i][y + j]
                if value == num:
                    return False
        return True

    def checkRow(self, board: List[List[str]], row: int, num: str) -> bool:
        for i in range(len(board)):
            value = board[row][i]
            if value == num:
                return False
        return True

    def checkCol(self, board: List[List[str]], col: int, num: str) -> bool:
        for i in range(len(board)):
            value = board[i][col]
            if value == num:
                return False
        return True

    def isValid(self, board: List[List[str]], row: int, col: int, num: str) -> bool:
        return (
            self.checkRow(board, row, num)
            and self.checkCol(board, col, num)
            and self.checkSquare(board, row, col, num)
        )

    def solve(self, board: List[List[str]]):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    for k in range(1, 10):
                        num = str(k)
                        # print(num)
                        if self.isValid(board, i, j, num):
                            board[i][j] = num
                            if self.solve(board) == True:
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.solve(board)
        return board


obj = Solution()

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
expected = [
    ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
    ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
    ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
    ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
    ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
    ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
    ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
]
result = obj.solveSudoku(board)
printResult(result, expected)
