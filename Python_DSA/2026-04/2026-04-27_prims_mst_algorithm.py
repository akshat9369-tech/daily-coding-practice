"""Minimum Spanning Tree: Prim's Algorithm with Priority Queue."""

import heapq

def prim_mst(n: int, adj: dict[int, list[tuple[int, int]]]) -> int:
    visited = set()
    min_heap = [(0, 0)]  # (weight, node)
    total_cost = 0

    while min_heap and len(visited) < n:
        weight, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        total_cost += weight

        for v, w in adj[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v))

    return total_cost

if __name__ == "__main__":
    graph = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8), (4, 9)],
        4: [(1, 5), (2, 7), (3, 9)]
    }
    print("Prim MST Total Weight:", prim_mst(5, graph))
