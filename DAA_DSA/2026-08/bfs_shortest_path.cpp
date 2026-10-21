#include <iostream>
#include <vector>
#include <queue>

std::vector<int> bfs_distance(int n, const std::vector<std::vector<int>>& adj, int src) {
    std::vector<int> dist(n, -1);
    std::queue<int> q;
    dist[src] = 0;
    q.push(src);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    return dist;
}

int main() {
    int n = 4;
    std::vector<std::vector<int>> adj(n);
    adj[0] = {1, 2}; adj[1] = {0, 2, 3}; adj[2] = {0, 1, 3}; adj[3] = {1, 2};
    std::vector<int> distances = bfs_distance(n, adj, 0);
    std::cout << "BFS Shortest Hops from 0 to 3: " << distances[3] << std::endl;
    return 0;
}
