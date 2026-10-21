#include <iostream>
#include <vector>
#include <algorithm>

int cut_rod(const std::vector<int>& price, int n) {
    std::vector<int> val(n + 1, 0);
    for (int i = 1; i <= n; i++) {
        int max_val = -1;
        for (int j = 0; j < i; j++)
            max_val = std::max(max_val, price[j] + val[i - j - 1]);
        val[i] = max_val;
    }
    return val[n];
}

int main() {
    std::vector<int> price = {1, 5, 8, 9, 10, 17, 17, 20};
    int size = price.size();
    std::cout << "Max obtainable value: " << cut_rod(price, size) << std::endl;
    return 0;
}
