#include <iostream>
#include <vector>
#include <algorithm>

int min_coins(const std::vector<int>& coins, int amount) {
    std::vector<int> dp(amount + 1, 1e9);
    dp[0] = 0;
    for (int a = 1; a <= amount; a++) {
        for (int c : coins) {
            if (a >= c) dp[a] = std::min(dp[a], 1 + dp[a - c]);
        }
    }
    return dp[amount] >= 1e9 ? -1 : dp[amount];
}

long long total_ways(const std::vector<int>& coins, int amount) {
    std::vector<long long> dp(amount + 1, 0);
    dp[0] = 1;
    for (int c : coins) {
        for (int a = c; a <= amount; a++) {
            dp[a] += dp[a - c];
        }
    }
    return dp[amount];
}

int main() {
    std::vector<int> coins = {1, 2, 5};
    int amount = 5;
    std::cout << "Min coins for " << amount << ": " << min_coins(coins, amount) << std::endl;
    std::cout << "Total combinations for " << amount << ": " << total_ways(coins, amount) << std::endl;
    return 0;
}
