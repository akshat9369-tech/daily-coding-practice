#include <iostream>
#include <vector>

bool subset_sum(const std::vector<int>& arr, int sum) {
    std::vector<bool> dp(sum + 1, false);
    dp[0] = true;

    for (int num : arr) {
        for (int j = sum; j >= num; j--) {
            if (dp[j - num]) dp[j] = true;
        }
    }
    return dp[sum];
}

int main() {
    std::vector<int> arr = {3, 34, 4, 12, 5, 2};
    int target = 9;
    std::cout << "Subset with sum " << target << " exists: " << (subset_sum(arr, target) ? "YES" : "NO") << std::endl;
    return 0;
}
