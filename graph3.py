from collections import deque

def count_nodes_at_level(tree, start_node, target_level):
    queue = deque([(start_node, 0)])  # Queue for BFS, with initial level 0
    count = 0

    while queue:
        node, level = queue.popleft()

        if level == target_level:
            count += 1

        for neighbor in tree[node]:
            queue.append((neighbor, level + 1))

    return count

# Example usage
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': ['H'],
    'H': []
}

start_node = 'A'
target_level = 2

node_count = count_nodes_at_level(tree, start_node, target_level)
print(f"Number of nodes at level {target_level}: {node_count}")
