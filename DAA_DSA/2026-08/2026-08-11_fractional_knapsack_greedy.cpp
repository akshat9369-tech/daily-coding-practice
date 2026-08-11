#include <iostream>
#include <vector>
#include <algorithm>

struct Item { int value, weight; };

bool cmp(Item a, Item b) {
    double r1 = (double)a.value / a.weight;
    double r2 = (double)b.value / b.weight;
    return r1 > r2;
}

double fractional_knapsack(int W, std::vector<Item>& items) {
    std::sort(items.begin(), items.end(), cmp);
    double total_val = 0.0;

    for (const auto& item : items) {
        if (W >= item.weight) {
            W -= item.weight;
            total_val += item.value;
        } else {
            total_val += item.value * ((double)W / item.weight);
            break;
        }
    }
    return total_val;
}

int main() {
    std::vector<Item> items = {{60, 10}, {100, 20}, {120, 30}};
    std::cout << "Max value in knapsack (W=50): " << fractional_knapsack(50, items) << std::endl;
    return 0;
}
