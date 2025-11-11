from practice.myUtils.Utils import TreeNode

def dfs_recursive(node):
    if node is None:
        return
    
    print(node.val, end=" ")
    dfs_recursive(node.left)
    dfs_recursive(node.right)

def dfs_iterative(node):
    if node is None:
        return
    
    stack = [node]
    while stack:
        node = stack.pop()
        print(node.val, end=" ")

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# Example Usage:
# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("DFS Traversal (Recursive):")
dfs_recursive(root) # Output: 1 2 4 5 3     

print("DFS Traversal (Iterative):")
dfs_iterative(root) # Output: 1 2 4 5 3     