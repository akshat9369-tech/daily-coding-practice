"""Shortest Path: Dijkstra's Algorithm with Min-Heap."""

import heapq

def dijkstra(graph: dict[int, list[tuple[int, int]]], source: int) -> dict[int, int]:
    dist = {node: float("inf") for node in graph}
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        curr_dist, u = heapq.heappop(pq)
        if curr_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            d = curr_dist + weight
            if d < dist[v]:
                dist[v] = d
                heapq.heappush(pq, (d, v))

    return dist

if __name__ == "__main__":
    g = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    print("Dijkstra distances from 0:", dijkstra(g, 0))
