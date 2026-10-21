#include <iostream>
#include <vector>

int find_celebrity(int n, const std::vector<std::vector<int>>& M) {
    int candidate = 0;
    for (int i = 1; i < n; i++) {
        if (M[candidate][i] == 1) candidate = i;
    }

    for (int i = 0; i < n; i++) {
        if (i != candidate) {
            if (M[candidate][i] == 1 || M[i][candidate] == 0) return -1;
        }
    }
    return candidate;
}

int main() {
    std::vector<std::vector<int>> M = {
        {0, 1, 0},
        {0, 0, 0},
        {0, 1, 0}
    };
    std::cout << "Celebrity index: " << find_celebrity(3, M) << std::endl;
    return 0;
}
