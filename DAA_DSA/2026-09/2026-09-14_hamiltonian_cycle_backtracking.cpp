#include <iostream>
#include <vector>

bool is_safe(int v, const std::vector<std::vector<int>>& graph, const std::vector<int>& path, int pos) {
    if (graph[path[pos - 1]][v] == 0) return false;
    for (int i = 0; i < pos; i++) if (path[i] == v) return false;
    return true;
}

bool ham_cycle_util(const std::vector<std::vector<int>>& graph, std::vector<int>& path, int pos) {
    if (pos == (int)graph.size()) return (graph[path[pos - 1]][path[0]] == 1);
    for (size_t v = 1; v < graph.size(); v++) {
        if (is_safe(v, graph, path, pos)) {
            path[pos] = v;
            if (ham_cycle_util(graph, path, pos + 1)) return true;
            path[pos] = -1;
        }
    }
    return false;
}

int main() {
    std::vector<std::vector<int>> g = {
        {0, 1, 0, 1, 0},
        {1, 0, 1, 1, 1},
        {0, 1, 0, 0, 1},
        {1, 1, 0, 0, 1},
        {0, 1, 1, 1, 0}
    };
    std::vector<int> path(5, -1);
    path[0] = 0;
    std::cout << "Hamiltonian Cycle exists: " << (ham_cycle_util(g, path, 1) ? "YES" : "NO") << std::endl;
    return 0;
}
