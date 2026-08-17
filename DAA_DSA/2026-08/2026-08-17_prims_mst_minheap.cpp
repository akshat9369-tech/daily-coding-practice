#include <iostream>
#include <vector>
#include <queue>

typedef std::pair<int, int> pii; // (weight, node)

int prim_mst(int n, const std::vector<std::vector<pii>>& adj) {
    std::priority_queue<pii, std::vector<pii>, std::greater<pii>> pq;
    std::vector<bool> visited(n, false);
    pq.push({0, 0});
    int total_mst_weight = 0;

    while (!pq.empty()) {
        pii top = pq.top();
        pq.pop();
        int w = top.first;
        int u = top.second;
        if (visited[u]) continue;
        visited[u] = true;
        total_mst_weight += w;

        for (size_t i = 0; i < adj[u].size(); i++) {
            int v = adj[u][i].first;
            int weight = adj[u][i].second;
            if (!visited[v]) pq.push({weight, v});
        }
    }
    return total_mst_weight;
}

int main() {
    int n = 4;
    std::vector<std::vector<pii>> adj(n);
    adj[0].push_back({1, 10}); adj[1].push_back({0, 10});
    adj[0].push_back({2, 6});  adj[2].push_back({0, 6});
    adj[0].push_back({3, 5});  adj[3].push_back({0, 5});
    adj[1].push_back({3, 15}); adj[3].push_back({1, 15});
    adj[2].push_back({3, 4});  adj[3].push_back({2, 4});

    std::cout << "Prim MST Total Cost: " << prim_mst(n, adj) << std::endl;
    return 0;
}
