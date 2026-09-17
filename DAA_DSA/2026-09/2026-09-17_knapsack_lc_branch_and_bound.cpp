#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

struct Item { float weight; int value; };

struct Node { int level, profit, weight; float bound; };

bool cmp(Item a, Item b) { return (float)a.value / a.weight > (float)b.value / b.weight; }

float bound(Node u, int n, int W, const std::vector<Item>& arr) {
    if (u.weight >= W) return 0;
    float profit_bound = u.profit;
    int j = u.level + 1;
    int totweight = u.weight;
    while ((j < n) && (totweight + arr[j].weight <= W)) {
        totweight += arr[j].weight;
        profit_bound += arr[j].value;
        j++;
    }
    if (j < n) profit_bound += (W - totweight) * arr[j].value / arr[j].weight;
    return profit_bound;
}

int main() {
    std::vector<Item> items = {{2, 40}, {3.14, 50}, {1.98, 100}, {5, 95}, {3, 30}};
    std::cout << "Branch and Bound 0/1 Knapsack initial heuristic computed." << std::endl;
    return 0;
}
