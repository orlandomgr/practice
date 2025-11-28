from typing import List, Optional
from myUtils.Utils import printResult
from myUtils.Utils import TreeNode
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append((root, 0, 0))
        result = []
        while q:
            node, row, col = q.popleft()

            # if col not in result:
            #     result[col] = []
            
            result.append((col, row, node.val))
            if node.left:
                q.append((node.left, row + 1, col-1))
            if node.right:
                q.append((node.right, row + 1, col+1))

        result.sort()
        # print(result)

        res = []
        prevCol = -10**10
        for col, row, val in result:
            if col != prevCol:
                res.append([])
                prevCol = col
            res[-1].append(val)

        return res



obj = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
expected = [[9],[3,15],[20],[7]]
result = obj.verticalTraversal(root)
printResult(result, expected)
