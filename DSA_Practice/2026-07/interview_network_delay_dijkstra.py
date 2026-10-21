"""Network Delay Time using Dijkstra Algorithm."""

import heapq
from collections import defaultdict

def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    pq = [(0, k)]
    dist = {}

    while pq:
        d, node = heapq.heappop(pq)
        if node in dist:
            continue
        dist[node] = d
        for neighbor, weight in graph[node]:
            if neighbor not in dist:
                heapq.heappush(pq, (d + weight, neighbor))

    return max(dist.values()) if len(dist) == n else -1

if __name__ == "__main__":
    signals = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    print("Network delay:", network_delay_time(signals, 4, 2))
