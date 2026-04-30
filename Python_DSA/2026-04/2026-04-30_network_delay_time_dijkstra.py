"""Graph: Network Delay Time (Dijkstra Application)."""

import heapq
from collections import defaultdict

def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    adj = defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))

    pq = [(0, k)]
    dist = {}

    while pq:
        d, u = heapq.heappop(pq)
        if u in dist:
            continue
        dist[u] = d
        for v, w in adj[u]:
            if v not in dist:
                heapq.heappush(pq, (d + w, v))

    return max(dist.values()) if len(dist) == n else -1

if __name__ == "__main__":
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    print("Network delay time:", network_delay_time(times, 4, 2))
