#include <iostream>
#include <vector>

int matrix_chain_multiplication(const std::vector<int>& p) {
    int n = p.size() - 1;
    std::vector<std::vector<int>> m(n, std::vector<int>(n, 0));

    for (int L = 2; L <= n; L++) {
        for (int i = 0; i < n - L + 1; i++) {
            int j = i + L - 1;
            m[i][j] = 1e9;
            for (int k = i; k < j; k++) {
                int q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1];
                if (q < m[i][j]) m[i][j] = q;
            }
        }
    }
    return m[0][n - 1];
}

int main() {
    std::vector<int> arr = {1, 2, 3, 4};
    std::cout << "Min multiplications for MCM: " << matrix_chain_multiplication(arr) << std::endl;
    return 0;
}
