#include <iostream>
#include <vector>
#include <algorithm>

double find_median_sorted_arrays(const std::vector<int>& A, const std::vector<int>& B) {
    if (A.size() > B.size()) return find_median_sorted_arrays(B, A);
    int m = A.size(), n = B.size();
    int low = 0, high = m;

    while (low <= high) {
        int partitionA = (low + high) / 2;
        int partitionB = (m + n + 1) / 2 - partitionA;

        int maxLeftA = (partitionA == 0) ? -1e9 : A[partitionA - 1];
        int minRightA = (partitionA == m) ? 1e9 : A[partitionA];

        int maxLeftB = (partitionB == 0) ? -1e9 : B[partitionB - 1];
        int minRightB = (partitionB == n) ? 1e9 : B[partitionB];

        if (maxLeftA <= minRightB && maxLeftB <= minRightA) {
            if ((m + n) % 2 == 0)
                return (std::max(maxLeftA, maxLeftB) + std::min(minRightA, minRightB)) / 2.0;
            else
                return std::max(maxLeftA, maxLeftB);
        } else if (maxLeftA > minRightB) {
            high = partitionA - 1;
        } else {
            low = partitionA + 1;
        }
    }
    return 0.0;
}

int main() {
    std::vector<int> A = {1, 3}, B = {2};
    std::cout << "Median of [1, 3] and [2]: " << find_median_sorted_arrays(A, B) << std::endl;
    return 0;
}
