"""Minimum Spanning Tree: Kruskal's Algorithm with DSU."""

def kruskal_mst(n: int, edges: list[tuple[int, int, int]]) -> tuple[int, list[tuple[int, int, int]]]:
    edges.sort(key=lambda e: e[2])
    parent = list(range(n))

    def find(i: int) -> int:
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    mst = []
    total_weight = 0

    for u, v, w in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == n - 1:
                break

    return total_weight, mst

if __name__ == "__main__":
    edge_list = [
        (0, 1, 10), (0, 2, 6), (0, 3, 5),
        (1, 3, 15), (2, 3, 4)
    ]
    cost, tree = kruskal_mst(4, edge_list)
    print(f"Kruskal MST Weight: {cost} | Edges: {tree}")
