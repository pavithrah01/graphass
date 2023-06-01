from collections import deque

def bfs(graph, source):
    visited = set()  # Set to keep track of visited vertices
    queue = deque()  # Queue for BFS

    visited.add(source)
    queue.append(source)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        # Enqueue all the unvisited neighbors
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
adj_list = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4]
}

print("BFS Traversal:")
bfs(adj_list, 0)
