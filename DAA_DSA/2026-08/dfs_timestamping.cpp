#include <iostream>
#include <vector>

void dfs(int u, const std::vector<std::vector<int>>& adj, std::vector<bool>& visited,
         std::vector<int>& discovery, std::vector<int>& finish, int& time) {
    visited[u] = true;
    discovery[u] = ++time;
    for (int v : adj[u]) {
        if (!visited[v]) dfs(v, adj, visited, discovery, finish, time);
    }
    finish[u] = ++time;
}

int main() {
    int n = 4;
    std::vector<std::vector<int>> adj = {{1, 2}, {3}, {3}, {}};
    std::vector<bool> visited(n, false);
    std::vector<int> discovery(n, 0), finish(n, 0);
    int time = 0;

    for (int i = 0; i < n; i++) if (!visited[i]) dfs(i, adj, visited, discovery, finish, time);

    std::cout << "DFS Discovery and Finish Times:\n";
    for (int i = 0; i < n; i++) {
        std::cout << "Node " << i << ": d=" << discovery[i] << ", f=" << finish[i] << "\n";
    }
    return 0;
}
