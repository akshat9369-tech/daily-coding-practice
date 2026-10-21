"""Disjoint Set: Cycle Detection in Graph Using DSU."""

class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False  # Cycle!
        self.p[rx] = ry
        return True

def has_cycle(n: int, edges: list[tuple[int, int]]) -> bool:
    dsu = DSU(n)
    for u, v in edges:
        if not dsu.union(u, v):
            return True
    return False

if __name__ == "__main__":
    print("Graph with cycle:", has_cycle(3, [(0, 1), (1, 2), (2, 0)]))
    print("Graph without cycle:", has_cycle(3, [(0, 1), (1, 2)]))
