#include <iostream>
#include <vector>
#include <stack>

struct DSU_Rollback {
    std::vector<int> parent, rank;
    struct Op { int u, v, rank_u; };
    std::stack<Op> history;

    DSU_Rollback(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    int find(int i) { return (parent[i] == i) ? i : find(parent[i]); }
    void unite(int u, int v) {
        u = find(u); v = find(v);
        if (u == v) return;
        if (rank[u] < rank[v]) std::swap(u, v);
        history.push({u, v, rank[u]});
        parent[v] = u;
        if (rank[u] == rank[v]) rank[u]++;
    }
    void rollback() {
        if (history.empty()) return;
        auto op = history.top(); history.pop();
        parent[op.v] = op.v;
        rank[op.u] = op.rank_u;
    }
};

int main() {
    DSU_Rollback dsu(5);
    dsu.unite(1, 2);
    std::cout << "1 and 2 connected: " << (dsu.find(1) == dsu.find(2) ? "YES" : "NO") << std::endl;
    dsu.rollback();
    std::cout << "After rollback, connected: " << (dsu.find(1) == dsu.find(2) ? "YES" : "NO") << std::endl;
    return 0;
}
