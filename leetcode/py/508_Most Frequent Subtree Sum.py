from typing import Optional, List
from practice.myUtils.Utils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.list = {}

    def addResult(self, n: int):
        counter = 1
        if n in self.list:
            counter = self.list[n]
        counter += 1
        self.list[n] = counter

    def parseTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        root.left = self.parseTree(root.left)
        root.right = self.parseTree(root.right)

        leftVal = 0
        rightVal = 0
        if root.left != None:
            leftVal = root.left.val
        if root.right != None:
            rightVal = root.right.val

        root.val += leftVal + rightVal
        self.addResult(root.val)
        return root

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.parseTree(root)

        result = []
        # print(self.list)
        maxValue = max(self.list.values())
        for key, value in self.list.items():
            if value == maxValue:
                result.append(key)

        return result