"""Graph: Cycle Detection in Undirected Graph (BFS and DFS)."""

def has_cycle_undirected(n: int, edges: list[list[int]]) -> bool:
    adj = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = set()

    def dfs(node: int, parent: int) -> bool:
        visited.add(node)
        for nbr in adj[node]:
            if nbr not in visited:
                if dfs(nbr, node):
                    return True
            elif nbr != parent:
                return True
        return False

    for i in range(n):
        if i not in visited:
            if dfs(i, -1):
                return True
    return False

if __name__ == "__main__":
    cycle_edges = [[0, 1], [1, 2], [2, 0]]
    acyclic_edges = [[0, 1], [1, 2], [2, 3]]
    print("Graph 1 has cycle:", has_cycle_undirected(3, cycle_edges))
    print("Graph 2 has cycle:", has_cycle_undirected(4, acyclic_edges))
