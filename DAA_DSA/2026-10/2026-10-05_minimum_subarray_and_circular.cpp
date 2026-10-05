#include <iostream>
#include <vector>
#include <algorithm>

int min_subarray_sum(const std::vector<int>& nums) {
    int min_so_far = nums[0], curr_min = nums[0];
    for (size_t i = 1; i < nums.size(); i++) {
        curr_min = std::min(nums[i], curr_min + nums[i]);
        min_so_far = std::min(min_so_far, curr_min);
    }
    return min_so_far;
}

int main() {
    std::vector<int> arr = {3, -4, 2, -3, -1, 7, -5};
    std::cout << "Minimum Subarray Sum: " << min_subarray_sum(arr) << std::endl;
    return 0;
}
