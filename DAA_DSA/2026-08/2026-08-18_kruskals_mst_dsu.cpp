#include <iostream>
#include <vector>
#include <algorithm>

struct Edge { int u, v, weight; };

struct DSU {
    std::vector<int> parent;
    DSU(int n) : parent(n) { for (int i = 0; i < n; i++) parent[i] = i; }
    int find(int i) { return (parent[i] == i) ? i : (parent[i] = find(parent[i])); }
    bool unite(int i, int j) {
        int root_i = find(i), root_j = find(j);
        if (root_i != root_j) { parent[root_i] = root_j; return true; }
        return false;
    }
};

int main() {
    std::vector<Edge> edges = {{0, 1, 10}, {0, 2, 6}, {0, 3, 5}, {1, 3, 15}, {2, 3, 4}};
    std::sort(edges.begin(), edges.end(), [](Edge a, Edge b) { return a.weight < b.weight; });

    DSU dsu(4);
    int mst_weight = 0;
    for (const auto& e : edges) {
        if (dsu.unite(e.u, e.v)) {
            mst_weight += e.weight;
        }
    }
    std::cout << "Kruskal MST Weight: " << mst_weight << std::endl;
    return 0;
}
