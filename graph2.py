def dfs(graph, source, visited):
    visited.add(source)
    print(source, end=" ")

    for neighbor in graph[source]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
adj_list = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4]
}

print("DFS Traversal:")
visited = set()
dfs(adj_list, 0, visited)
