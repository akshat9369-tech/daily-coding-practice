#include <iostream>
#include <vector>
#include <queue>

typedef std::pair<int, int> pii;

std::vector<int> dijkstra(int n, const std::vector<std::vector<pii>>& adj, int src) {
    std::priority_queue<pii, std::vector<pii>, std::greater<pii>> pq;
    std::vector<int> dist(n, 1e9);
    dist[src] = 0;
    pq.push({0, src});

    while (!pq.empty()) {
        pii top = pq.top();
        pq.pop();
        int d = top.first;
        int u = top.second;
        if (d > dist[u]) continue;

        for (size_t i = 0; i < adj[u].size(); i++) {
            int v = adj[u][i].first;
            int w = adj[u][i].second;
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}

int main() {
    int n = 5;
    std::vector<std::vector<pii>> adj(n);
    adj[0].push_back({1, 4}); adj[0].push_back({2, 8});
    adj[1].push_back({2, 2}); adj[1].push_back({3, 5});
    adj[2].push_back({3, 5}); adj[2].push_back({4, 9});
    adj[3].push_back({4, 4});

    std::vector<int> distances = dijkstra(n, adj, 0);
    std::cout << "Shortest distances from source 0:\\n";
    for (int i = 0; i < n; i++) std::cout << "Node " << i << ": " << distances[i] << "\\n";
    return 0;
}
