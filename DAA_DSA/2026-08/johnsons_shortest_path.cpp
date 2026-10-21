#include <iostream>
#include <vector>

int main() {
    std::cout << "Johnson's Algorithm reweights edges using Bellman-Ford potential h(u) = delta(s, u)" << std::endl;
    std::cout << "Guarantees all edge weights w'(u, v) = w(u, v) + h(u) - h(v) >= 0." << std::endl;
    std::cout << "Enables running Dijkstra from all vertices in O(V^2 log V + VE)." << std::endl;
    return 0;
}
