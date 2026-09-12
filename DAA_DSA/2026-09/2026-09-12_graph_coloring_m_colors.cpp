#include <iostream>
#include <vector>

bool is_safe(int v, const std::vector<std::vector<int>>& graph, const std::vector<int>& color, int c) {
    for (size_t i = 0; i < graph.size(); i++)
        if (graph[v][i] && c == color[i]) return false;
    return true;
}

bool graph_coloring_util(const std::vector<std::vector<int>>& graph, int m, std::vector<int>& color, int v) {
    if (v == (int)graph.size()) return true;
    for (int c = 1; c <= m; c++) {
        if (is_safe(v, graph, color, c)) {
            color[v] = c;
            if (graph_coloring_util(graph, m, color, v + 1)) return true;
            color[v] = 0;
        }
    }
    return false;
}

int main() {
    std::vector<std::vector<int>> g = {
        {0, 1, 1, 1},
        {1, 0, 1, 0},
        {1, 1, 0, 1},
        {1, 0, 1, 0}
    };
    int m = 3;
    std::vector<int> color(4, 0);
    bool res = graph_coloring_util(g, m, color, 0);
    std::cout << "Graph is " << m << "-colorable: " << (res ? "YES" : "NO") << std::endl;
    return 0;
}
