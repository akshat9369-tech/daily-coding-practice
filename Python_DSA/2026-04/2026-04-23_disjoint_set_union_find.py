"""Disjoint Set: Union-Find with Path Compression and Rank."""

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.count = size

    def find(self, p: int) -> int:
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p: int, q: int) -> bool:
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return False

        if self.rank[root_p] < self.rank[root_q]:
            self.parent[root_p] = root_q
        elif self.rank[root_p] > self.rank[root_q]:
            self.parent[root_q] = root_p
        else:
            self.parent[root_q] = root_p
            self.rank[root_p] += 1

        self.count -= 1
        return True

if __name__ == "__main__":
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    print("0 connected to 2:", uf.find(0) == uf.find(2))
    print("0 connected to 3:", uf.find(0) == uf.find(3))
