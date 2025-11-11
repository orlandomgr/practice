from collections import deque
from practice.myUtils.Utils import TreeNode

def bfs_tree(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level_nodes = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_nodes)
    return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

traversal = bfs_tree(root)
print(traversal)