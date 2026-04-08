"""Graph Traversal: Depth-First Search (DFS Recursive and Iterative)."""

def dfs_recursive(graph: dict[int, list[int]], start: int) -> list[int]:
    visited = set()
    order = []

    def _dfs(u: int):
        visited.add(u)
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                _dfs(v)

    _dfs(start)
    return order

if __name__ == "__main__":
    adj = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0],
        3: [1],
        4: [1]
    }
    print("DFS Recursive from 0:", dfs_recursive(adj, 0))
