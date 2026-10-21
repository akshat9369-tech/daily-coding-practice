#include <iostream>
#include <vector>
#include <algorithm>

const int INF = 1e9;

int tsp(int mask, int pos, int n, const std::vector<std::vector<int>>& dist, std::vector<std::vector<int>>& memo) {
    if (mask == (1 << n) - 1) return dist[pos][0];
    if (memo[mask][pos] != -1) return memo[mask][pos];

    int ans = INF;
    for (int next = 0; next < n; next++) {
        if ((mask & (1 << next)) == 0) {
            int new_cost = dist[pos][next] + tsp(mask | (1 << next), next, n, dist, memo);
            ans = std::min(ans, new_cost);
        }
    }
    return memo[mask][pos] = ans;
}

int main() {
    int n = 4;
    std::vector<std::vector<int>> dist = {
        {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0}
    };
    std::vector<std::vector<int>> memo(1 << n, std::vector<int>(n, -1));
    std::cout << "Min TSP Tour Cost: " << tsp(1, 0, n, dist, memo) << std::endl;
    return 0;
}
