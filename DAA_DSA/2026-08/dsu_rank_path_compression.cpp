#include <iostream>
#include <vector>

class DisjointSet {
    std::vector<int> parent, rank;
public:
    DisjointSet(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    int find(int i) {
        if (parent[i] != i) parent[i] = find(parent[i]);
        return parent[i];
    }
    bool union_by_rank(int u, int v) {
        int root_u = find(u), root_v = find(v);
        if (root_u == root_v) return false;
        if (rank[root_u] < rank[root_v]) parent[root_u] = root_v;
        else if (rank[root_u] > rank[root_v]) parent[root_v] = root_u;
        else { parent[root_v] = root_u; rank[root_u]++; }
        return true;
    }
};

int main() {
    DisjointSet ds(5);
    ds.union_by_rank(0, 1);
    ds.union_by_rank(2, 3);
    ds.union_by_rank(1, 3);
    std::cout << "0 and 2 connected: " << (ds.find(0) == ds.find(2) ? "YES" : "NO") << std::endl;
    return 0;
}
