#include <iostream>
#include <vector>
#include <queue>
#include <cmath>

struct Node {
    int x, y, g_cost, h_cost;
    bool operator>(const Node& other) const {
        return (g_cost + h_cost) > (other.g_cost + other.h_cost);
    }
};

int heuristic(int x1, int y1, int x2, int y2) {
    return std::abs(x1 - x2) + std::abs(y1 - y2);
}

int main() {
    std::cout << "A* Heuristic Search initialized for 2D Grid navigation." << std::endl;
    std::cout << "Heuristic distance from (0, 0) to (5, 5): " << heuristic(0, 0, 5, 5) << std::endl;
    return 0;
}
