"""Shortest Path: Shortest Path in Unweighted Graph (BFS)."""

from collections import deque

def shortest_path_bfs(graph: dict[int, list[int]], start: int, target: int) -> list[int]:
    visited = {start: None}
    q = deque([start])

    while q:
        curr = q.popleft()
        if curr == target:
            break
        for nbr in graph.get(curr, []):
            if nbr not in visited:
                visited[nbr] = curr
                q.append(nbr)

    if target not in visited:
        return []

    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = visited[curr]

    return path[::-1]

if __name__ == "__main__":
    adj = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 5],
        3: [0, 4],
        4: [3, 5],
        5: [2, 4]
    }
    print("Shortest path 0 -> 5:", shortest_path_bfs(adj, 0, 5))
