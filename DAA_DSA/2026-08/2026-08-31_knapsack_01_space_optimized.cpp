#include <iostream>
#include <vector>
#include <algorithm>

int knapsack_optimized(int W, const std::vector<int>& weights, const std::vector<int>& values) {
    std::vector<int> dp(W + 1, 0);
    for (size_t i = 0; i < weights.size(); i++) {
        for (int w = W; w >= weights[i]; w--) {
            dp[w] = std::max(dp[w], dp[w - weights[i]] + values[i]);
        }
    }
    return dp[W];
}

int main() {
    std::vector<int> weights = {10, 20, 30};
    std::vector<int> values = {60, 100, 120};
    int W = 50;
    std::cout << "Max 0/1 Knapsack Value: " << knapsack_optimized(W, weights, values) << std::endl;
    return 0;
}
