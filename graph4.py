def count_trees(graph):
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)
            count += 1

    return count

def dfs(graph, node, visited):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
forest = {
    'A': ['B', 'C'],
    'B': [],
    'C': ['D', 'E'],
    'D': [],
    'E': ['F'],
    'F': []
}

tree_count = count_trees(forest)
print("Number of trees in the forest:", tree_count)
