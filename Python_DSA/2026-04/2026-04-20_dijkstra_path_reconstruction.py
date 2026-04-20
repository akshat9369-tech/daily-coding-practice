"""Shortest Path: Dijkstra with Path Reconstruction."""

import heapq

def dijkstra_with_path(graph: dict[int, list[tuple[int, int]]], src: int, dst: int):
    dist = {node: float("inf") for node in graph}
    parent = {node: None for node in graph}
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)
        if u == dst:
            break
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    path = []
    curr = dst
    while curr is not None:
        path.append(curr)
        curr = parent[curr]

    return dist[dst], path[::-1]

if __name__ == "__main__":
    g = {
        0: [(1, 10), (2, 3)],
        1: [(3, 2)],
        2: [(1, 4), (3, 8), (4, 2)],
        3: [(4, 7)],
        4: [(3, 1)]
    }
    cost, route = dijkstra_with_path(g, 0, 3)
    print(f"Min Cost: {cost} | Path: {route}")
