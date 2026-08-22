#include <iostream>
#include <vector>

struct Edge { int u, v, w; };

int main() {
    int V = 5, E = 8;
    std::vector<Edge> edges = {
        {0, 1, -1}, {0, 2, 4}, {1, 2, 3}, {1, 3, 2},
        {1, 4, 2}, {3, 2, 5}, {3, 1, 1}, {4, 3, -3}
    };

    std::vector<int> dist(V, 1e9);
    dist[0] = 0;

    for (int i = 1; i <= V - 1; i++) {
        for (const auto& e : edges) {
            if (dist[e.u] != 1e9 && dist[e.u] + e.w < dist[e.v])
                dist[e.v] = dist[e.u] + e.w;
        }
    }

    std::cout << "Bellman-Ford Distances from node 0:\n";
    for (int i = 0; i < V; i++) std::cout << "Node " << i << ": " << dist[i] << "\n";
    return 0;
}
