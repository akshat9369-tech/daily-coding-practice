"""Graph Traversal: Breadth-First Search (BFS)."""

from collections import deque

def bfs(graph: dict[int, list[int]], start_node: int) -> list[int]:
    visited = set([start_node])
    queue = deque([start_node])
    traversal_order = []

    while queue:
        node = queue.popleft()
        traversal_order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order

if __name__ == "__main__":
    adj = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4]
    }
    print("BFS from 0:", bfs(adj, 0))
