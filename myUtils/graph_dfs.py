def dfs_recursive(graph, node, visited):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def dfs_iterative(graph, node):
    visited = set()
    stack = [node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("Recursive DFS traversal:")
dfs_recursive(graph, 'A', None)

print("Iterate DFS traversal:")
dfs_iterative(graph, 'A')