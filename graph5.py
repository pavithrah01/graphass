def has_cycle(graph):
    visited = set()
    recursion_stack = set()

    for node in graph:
        if node not in visited:
            if dfs(graph, node, visited, recursion_stack):
                return True

    return False

def dfs(graph, node, visited, recursion_stack):
    visited.add(node)
    recursion_stack.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, visited, recursion_stack):
                return True
        elif neighbor in recursion_stack:
            return True

    recursion_stack.remove(node)
    return False

# Example usage
graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['A'],
    'E': []
}

has_cycle = has_cycle(graph)
print("Cycle detected:", has_cycle)
