#include <iostream>
#include <vector>

int optimal_bst(const std::vector<int>& keys, const std::vector<int>& freq, int n) {
    std::vector<std::vector<int>> cost(n, std::vector<int>(n, 0));

    for (int i = 0; i < n; i++) cost[i][i] = freq[i];

    for (int L = 2; L <= n; L++) {
        for (int i = 0; i <= n - L; i++) {
            int j = i + L - 1;
            cost[i][j] = 1e9;
            int fsum = 0;
            for (int k = i; k <= j; k++) fsum += freq[k];

            for (int r = i; r <= j; r++) {
                int c = ((r > i) ? cost[i][r - 1] : 0) +
                        ((r < j) ? cost[r + 1][j] : 0) + fsum;
                if (c < cost[i][j]) cost[i][j] = c;
            }
        }
    }
    return cost[0][n - 1];
}

int main() {
    std::vector<int> keys = {10, 12, 20};
    std::vector<int> freq = {34, 50, 8};
    std::cout << "Cost of Optimal BST: " << optimal_bst(keys, freq, keys.size()) << std::endl;
    return 0;
}
