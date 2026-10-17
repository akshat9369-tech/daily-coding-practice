#include <iostream>
#include <vector>
#include <algorithm>

void find_bridges(int u, int p, const std::vector<std::vector<int>>& adj,
                  std::vector<int>& disc, std::vector<int>& low, int& timer) {
    disc[u] = low[u] = ++timer;
    for (int v : adj[u]) {
        if (v == p) continue;
        if (disc[v]) {
            low[u] = std::min(low[u], disc[v]);
        } else {
            find_bridges(v, u, adj, disc, low, timer);
            low[u] = std::min(low[u], low[v]);
            if (low[v] > disc[u]) {
                std::cout << "Bridge: (" << u << " -- " << v << ")\n";
            }
        }
    }
}

int main() {
    int n = 4;
    std::vector<std::vector<int>> adj = {{1, 2}, {0, 2, 3}, {0, 1}, {1}};
    std::vector<int> disc(n, 0), low(n, 0);
    int timer = 0;
    find_bridges(0, -1, adj, disc, low, timer);
    return 0;
}
