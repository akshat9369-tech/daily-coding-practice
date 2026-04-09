"""Graph: Number of Connected Components in Undirected Graph."""

def count_components(n: int, edges: list[list[int]]) -> int:
    adj = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = set()
    count = 0

    def dfs(node: int):
        visited.add(node)
        for nbr in adj[node]:
            if nbr not in visited:
                dfs(nbr)

    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1

    return count

if __name__ == "__main__":
    edges = [[0, 1], [1, 2], [3, 4]]
    print("Total connected components (n=5):", count_components(5, edges))
