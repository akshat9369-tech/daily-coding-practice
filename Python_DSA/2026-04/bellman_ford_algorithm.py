"""Shortest Path: Bellman-Ford Algorithm with Negative Cycles."""

def bellman_ford(vertices: int, edges: list[tuple[int, int, int]], src: int):
    dist = [float("inf")] * vertices
    dist[src] = 0

    for _ in range(vertices - 1):
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Negative cycle check
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative weight cycle!")

    return dist

if __name__ == "__main__":
    edges = [
        (0, 1, -1), (0, 2, 4),
        (1, 2, 3), (1, 3, 2), (1, 4, 2),
        (3, 2, 5), (3, 1, 1), (4, 3, -3)
    ]
    print("Bellman-Ford distances from 0:", bellman_ford(5, edges, 0))
