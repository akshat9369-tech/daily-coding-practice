"""Topological Sort: Kahn's BFS Algorithm (In-Degree Array)."""

from collections import deque

def topological_sort_kahn(num_nodes: int, edges: list[list[int]]) -> list[int]:
    adj = {i: [] for i in range(num_nodes)}
    in_degree = [0] * num_nodes

    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    q = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    topo_order = []

    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    if len(topo_order) != num_nodes:
        return []  # Cycle exists
    return topo_order

if __name__ == "__main__":
    edges = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    print("Topological Sort (Kahn's):", topological_sort_kahn(6, edges))
