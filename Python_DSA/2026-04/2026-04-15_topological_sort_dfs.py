"""Topological Sort: DFS-Based Algorithm with Stack."""

def topological_sort_dfs(num_nodes: int, edges: list[list[int]]) -> list[int]:
    adj = {i: [] for i in range(num_nodes)}
    for u, v in edges:
        adj[u].append(v)

    visited = set()
    stack = []

    def dfs(u: int):
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                dfs(v)
        stack.append(u)

    for i in range(num_nodes):
        if i not in visited:
            dfs(i)

    return stack[::-1]

if __name__ == "__main__":
    edges = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    print("Topological Sort (DFS):", topological_sort_dfs(6, edges))
