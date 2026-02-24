from typing import Optional
from myUtils.Utils import printResult, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        nums: list[int] = []
        def dfs(node: TreeNode, num: list[str]):
            if node:
                num.append(str(node.val))
                if not node.left and not node.right:
                    nums.append(int("".join(num), 2))
                else:
                    if node.left:
                        dfs(node.left, num.copy())
                    if node.right:
                        dfs(node.right, num.copy())
        dfs(root, [""])

        return sum(nums)

obj = Solution()

root = TreeNode(1)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)

root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)
expected = 22
result = obj.sumRootToLeaf(root)
printResult(result, expected)

root = TreeNode(0)
expected = 0
result = obj.sumRootToLeaf(root)
printResult(result, expected)

root = TreeNode(1)
expected = 1
result = obj.sumRootToLeaf(root)
printResult(result, expected)

root = TreeNode(1)
root.left = TreeNode(1)
expected = 3
result = obj.sumRootToLeaf(root)
printResult(result, expected)
