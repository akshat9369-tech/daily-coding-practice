#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

void tarjan_dfs(int u, const std::vector<std::vector<int>>& adj, std::vector<int>& disc,
                std::vector<int>& low, std::stack<int>& st, std::vector<bool>& in_stack, int& time) {
    disc[u] = low[u] = ++time;
    st.push(u);
    in_stack[u] = true;

    for (int v : adj[u]) {
        if (disc[v] == -1) {
            tarjan_dfs(v, adj, disc, low, st, in_stack, time);
            low[u] = std::min(low[u], low[v]);
        } else if (in_stack[v]) {
            low[u] = std::min(low[u], disc[v]);
        }
    }

    if (low[u] == disc[u]) {
        std::cout << "SCC: [ ";
        while (true) {
            int v = st.top(); st.pop();
            in_stack[v] = false;
            std::cout << v << " ";
            if (u == v) break;
        }
        std::cout << "]\n";
    }
}

int main() {
    int n = 5;
    std::vector<std::vector<int>> adj(n);
    adj[1].push_back(0); adj[0].push_back(2); adj[2].push_back(1);
    adj[0].push_back(3); adj[3].push_back(4);

    std::vector<int> disc(n, -1), low(n, -1);
    std::vector<bool> in_stack(n, false);
    std::stack<int> st;
    int time = 0;

    for (int i = 0; i < n; i++)
        if (disc[i] == -1) tarjan_dfs(i, adj, disc, low, st, in_stack, time);

    return 0;
}
