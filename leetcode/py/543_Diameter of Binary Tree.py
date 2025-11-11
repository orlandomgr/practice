from typing import List, Optional
from myUtils.Utils import printResult
import math
from practice.myUtils.Utils import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxValue = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def bst(node: TreeNode):
            if not node.left and not node.right:
                return (1,1)

            left = 0
            if node.left:
                leftValues = bst(node.left)
                left += max(leftValues[0], leftValues[1])

            right = 0
            if node.right:
                rightValues = bst(node.right)
                right += max(rightValues[0], rightValues[1])

            self.maxValue = max(self.maxValue, left + right)
            # print("left: %s right: %s" %(left, right))
            return (left + 1, right + 1)

        self.maxValue = 0
        _, _ = bst(root)
        return self.maxValue
        # return best
    

obj = Solution()

root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
expected = 2
result = obj.diameterOfBinaryTree(root)
printResult(result, expected)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.right = TreeNode(6)

expected = 4
result = obj.diameterOfBinaryTree(root)
printResult(result, expected)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

expected = 3
result = obj.diameterOfBinaryTree(root)
printResult(result, expected)

root = TreeNode(1)
root.left = TreeNode(2)

expected = 1
result = obj.diameterOfBinaryTree(root)
printResult(result, expected)
