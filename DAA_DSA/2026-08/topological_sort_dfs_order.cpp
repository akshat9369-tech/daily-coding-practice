#include <iostream>
#include <vector>
#include <stack>

void dfs(int u, const std::vector<std::vector<int>>& adj, std::vector<bool>& visited, std::stack<int>& st) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) dfs(v, adj, visited, st);
    }
    st.push(u);
}

int main() {
    int n = 6;
    std::vector<std::vector<int>> adj(n);
    adj[5] = {2, 0}; adj[4] = {0, 1}; adj[2] = {3}; adj[3] = {1};

    std::vector<bool> visited(n, false);
    std::stack<int> st;

    for (int i = 0; i < n; i++) if (!visited[i]) dfs(i, adj, visited, st);

    std::cout << "DFS Topological Sort: ";
    while (!st.empty()) {
        std::cout << st.top() << " ";
        st.pop();
    }
    std::cout << std::endl;
    return 0;
}
