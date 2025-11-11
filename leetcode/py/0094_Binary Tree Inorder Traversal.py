from practice.myUtils.Utils import TreeNode
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root: Optional[TreeNode], result):
        if root is not None:
            if(root.left):
                self.inOrder(root.left, result)
            result.append(root.val)
            if(root.right):
                self.inOrder(root.right, result)
        return result

    def inOrderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inOrder(root, result)
        return result

obj = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
result = obj.inOrderTraversal(root)
print(result)

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right = TreeNode(3)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(9)
result = obj.inOrderTraversal(root)
print(result)

root.right.right = TreeNode(5)
root.right.right.left = TreeNode(3)
root.right.right.left.right = TreeNode(4)
root.right.right.right = TreeNode(6)

obj = Solution()
result = obj.inOrderTraversal(None)
print(result)
