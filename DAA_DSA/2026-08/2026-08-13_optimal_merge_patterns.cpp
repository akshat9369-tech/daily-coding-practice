#include <iostream>
#include <vector>
#include <queue>

int optimal_merge_cost(const std::vector<int>& files) {
    std::priority_queue<int, std::vector<int>, std::greater<int>> pq(files.begin(), files.end());
    int total_cost = 0;

    while (pq.size() > 1) {
        int first = pq.top(); pq.pop();
        int second = pq.top(); pq.pop();
        int merged = first + second;
        total_cost += merged;
        pq.push(merged);
    }
    return total_cost;
}

int main() {
    std::vector<int> files = {2, 3, 4, 5, 6, 7};
    std::cout << "Optimal merge cost: " << optimal_merge_cost(files) << std::endl;
    return 0;
}
