#include <iostream>
#include <vector>
#include <algorithm>

int length_of_lis(const std::vector<int>& nums) {
    std::vector<int> tails;
    for (int x : nums) {
        auto it = std::lower_bound(tails.begin(), tails.end(), x);
        if (it == tails.end()) tails.push_back(x);
        else *it = x;
    }
    return tails.size();
}

int main() {
    std::vector<int> arr = {10, 9, 2, 5, 3, 7, 101, 18};
    std::cout << "LIS Length O(N log N): " << length_of_lis(arr) << std::endl;
    return 0;
}
