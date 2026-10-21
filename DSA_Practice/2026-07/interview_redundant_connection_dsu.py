"""Redundant Connection using Disjoint Set Union."""

def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    parent = list(range(len(edges) + 1))

    def find(i: int) -> int:
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return [u, v]
        parent[ru] = rv

    return []

if __name__ == "__main__":
    edges = [[1, 2], [1, 3], [2, 3]]
    print("Redundant edge:", find_redundant_connection(edges))
