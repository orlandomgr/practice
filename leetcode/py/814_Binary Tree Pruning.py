from practice.myUtils.Utils import TreeNode
from typing import Optional
# Definition for a binary tree node.

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right) 

        # print("val: %s left: %s right: %s" %(root.val, root.left, root.right))

        if root.val == 0 and root.left == None and root.right == None:
            # print("removing")
            root = None

        return root
        # left = self.pruneTree(root.left) 
        # if left:
        #     root.left = None
        # # print("val: %s left: %s" %(root.val, left))

        # right = self.pruneTree(root.right)        
        # if right:
        #     root.right = None
        # # print("val: %s right: %s" %(root.val, right))

        # # print("returning val: %s return: %s" %(root.val, (root.val == 0 and (left == None or right == None))))
        # # return root.val == 0 and (left == None or right == None)
        # return root.val == 0 and (left and right )
    
obj = Solution()
# root = TreeNode(1)
# root.right = TreeNode(0)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(1)
# obj.pruneTree(root)    
# print(root)

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)

root.left.left = TreeNode(0)
root.left.right = TreeNode(0)

root.right.left = TreeNode(0)
root.right.right = TreeNode(1)
obj.pruneTree(root)    
print(root)