#include <iostream>
#include <vector>
#include <queue>

int main() {
    int n = 6;
    std::vector<std::vector<int>> adj(n);
    std::vector<int> in_degree(n, 0);

    auto add_edge = [&](int u, int v) { adj[u].push_back(v); in_degree[v]++; };
    add_edge(5, 2); add_edge(5, 0); add_edge(4, 0); add_edge(4, 1); add_edge(2, 3); add_edge(3, 1);

    std::queue<int> q;
    for (int i = 0; i < n; i++) if (in_degree[i] == 0) q.push(i);

    std::cout << "Topological Sort Order: ";
    while (!q.empty()) {
        int u = q.front(); q.pop();
        std::cout << u << " ";
        for (int v : adj[u]) {
            if (--in_degree[v] == 0) q.push(v);
        }
    }
    std::cout << std::endl;
    return 0;
}
