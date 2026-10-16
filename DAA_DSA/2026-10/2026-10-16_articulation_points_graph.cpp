#include <iostream>
#include <vector>
#include <algorithm>

void dfs(int u, int p, const std::vector<std::vector<int>>& adj, std::vector<int>& disc,
         std::vector<int>& low, std::vector<bool>& is_ap, int& timer) {
    disc[u] = low[u] = ++timer;
    int children = 0;
    for (int v : adj[u]) {
        if (v == p) continue;
        if (disc[v]) {
            low[u] = std::min(low[u], disc[v]);
        } else {
            dfs(v, u, adj, disc, low, is_ap, timer);
            low[u] = std::min(low[u], low[v]);
            if (low[v] >= disc[u] && p != -1) is_ap[u] = true;
            children++;
        }
    }
    if (p == -1 && children > 1) is_ap[u] = true;
}

int main() {
    int n = 5;
    std::vector<std::vector<int>> adj = {{1, 2, 3}, {0, 2}, {0, 1}, {0, 4}, {3}};
    std::vector<int> disc(n, 0), low(n, 0);
    std::vector<bool> is_ap(n, false);
    int timer = 0;

    for (int i = 0; i < n; i++) if (!disc[i]) dfs(i, -1, adj, disc, low, is_ap, timer);

    std::cout << "Articulation points (Cut Vertices): ";
    for (int i = 0; i < n; i++) if (is_ap[i]) std::cout << i << " ";
    std::cout << std::endl;
    return 0;
}
