#include <iostream>
#include <vector>
#include <algorithm>

const int INF = 1e9;

int main() {
    int V = 4;
    std::vector<std::vector<int>> dist = {
        {0, 3, INF, 7},
        {8, 0, 2, INF},
        {5, INF, 0, 1},
        {2, INF, INF, 0}
    };

    for (int k = 0; k < V; k++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (dist[i][k] != INF && dist[k][j] != INF)
                    dist[i][j] = std::min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    std::cout << "All-Pairs Shortest Paths Matrix:\n";
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (dist[i][j] == INF) std::cout << "INF ";
            else std::cout << dist[i][j] << " ";
        }
        std::cout << "\n";
    }
    return 0;
}
