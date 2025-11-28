from myUtils.Utils import TreeNode, printResult
from typing import Optional

class Solution:
    def pathSum(self, root: Optional[TreeNode]):
        if root is None:
            return 0
        left = 0
        right = 0
        if(root.left):
            left = self.pathSum(root.left)
        if(root.right):
            right = self.pathSum(root.right)

        maxVal = max(root.val + left, root.val + right)
        self.maxS = max(self.maxS, maxVal, root.val + left + right)

        return maxVal

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxS = root.val
        self.pathSum(root)
        return self.maxS

obj = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
expected = 6
result = obj.maxPathSum(root)
printResult(result, expected)        

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
expected = 42
result = obj.maxPathSum(root)
printResult(result, expected)        

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
expected = 48
result = obj.maxPathSum(root)
printResult(result, expected)    