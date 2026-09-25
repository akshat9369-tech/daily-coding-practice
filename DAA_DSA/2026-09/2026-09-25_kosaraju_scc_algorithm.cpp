#include <iostream>
#include <vector>
#include <stack>

void dfs1(int u, const std::vector<std::vector<int>>& adj, std::vector<bool>& visited, std::stack<int>& st) {
    visited[u] = true;
    for (int v : adj[u]) if (!visited[v]) dfs1(v, adj, visited, st);
    st.push(u);
}

void dfs2(int u, const std::vector<std::vector<int>>& rev_adj, std::vector<bool>& visited) {
    visited[u] = true;
    std::cout << u << " ";
    for (int v : rev_adj[u]) if (!visited[v]) dfs2(v, rev_adj, visited);
}

int main() {
    int n = 5;
    std::vector<std::vector<int>> adj(n), rev(n);
    auto add_edge = [&](int u, int v) { adj[u].push_back(v); rev[v].push_back(u); };
    add_edge(1, 0); add_edge(0, 2); add_edge(2, 1); add_edge(0, 3); add_edge(3, 4);

    std::stack<int> st;
    std::vector<bool> visited(n, false);
    for (int i = 0; i < n; i++) if (!visited[i]) dfs1(i, adj, visited, st);

    std::fill(visited.begin(), visited.end(), false);
    std::cout << "Kosaraju Strongly Connected Components:\n";
    while (!st.empty()) {
        int u = st.top(); st.pop();
        if (!visited[u]) {
            std::cout << "[ ";
            dfs2(u, rev, visited);
            std::cout << "]\n";
        }
    }
    return 0;
}
