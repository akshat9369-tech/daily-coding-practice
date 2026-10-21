"""Graph: Bipartite Graph Verification (BFS 2-Coloring)."""

from collections import deque

def is_bipartite(graph: list[list[int]]) -> bool:
    n = len(graph)
    colors = {}

    for i in range(n):
        if i not in colors:
            colors[i] = 0
            q = deque([i])
            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if neighbor not in colors:
                        colors[neighbor] = 1 - colors[node]
                        q.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False
    return True

if __name__ == "__main__":
    bipartite_adj = [[1, 3], [0, 2], [1, 3], [0, 2]]
    non_bipartite = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    print("Graph 1 is bipartite:", is_bipartite(bipartite_adj))
    print("Graph 2 is bipartite:", is_bipartite(non_bipartite))
