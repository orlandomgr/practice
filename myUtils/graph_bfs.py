from collections import deque

def bfs(graph, node):
    visited = set()
    visited_order = []
    queue = deque([node])

    visited.add(node)

    while queue:
        current = queue.popleft()
        visited_order.append(current)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited_order


if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    start_node = "A"
    traversal_order = bfs(graph, start_node)
    print(f"BFS traversal starting from '{start_node}': {traversal_order}")

    start_node_2 = "D"
    traversal_order_2 = bfs(graph, start_node_2)
    print(f"BFS traversal starting from '{start_node_2}': {traversal_order_2}")
