from typing import List
from myUtils.Utils import printResult
from collections import defaultdict
import math
from collections import deque
import heapq
import copy
import networkx as nx


class Solution:
    def getBoardsThatFit(self, pieces: List[str], board: List[int]):
        pieceX = len(pieces[0])
        pieceY = len(pieces[0][0])
        pieceArea = pieceX * pieceY
        pieceArea = 7
        # (x - x % 3) * (y - y % 3) >= sum(shapes) * 9
        count = 0
        for b in board:
            rows = b.pop(0)
            cols = b.pop(0)
            # rows = rows - rows % 3
            # cols = cols - cols % 3
            print(b)
            print("sum: %s board: %s" %((sum(b) * pieceArea), (rows*cols)))
            if (rows * cols) >= sum(b) * pieceArea:
                count += 1

        return count

obj = Solution()

pieces = [
    [
        "###",
        "##.",
        "##.",
    ],
    [
        "###",
        "##.",
        ".##",
    ],
    [
        ".##",
        "###",
        "##.",
    ],
    [
        "##.",
        "###",
        "##.",
    ],
    [
        "###",
        "#..",
        "###",
    ],
    [
        "###",
        ".#.",
        "###",
    ],
]
boards = [
    [4, 4, 0, 0, 0, 0, 2, 0],
    [12, 5, 1, 0, 1, 0, 2, 2],
    [12, 5, 1, 0, 1, 0, 3, 2],
]
expected = 2
result = obj.getBoardsThatFit(pieces, boards)
printResult(result, expected)
