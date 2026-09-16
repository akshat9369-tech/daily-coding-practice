#include <iostream>
#include <vector>
#include <queue>
#include <cmath>

struct PuzzleState {
    std::vector<std::vector<int>> board;
    int cost, depth;
};

int manhattan_distance(const std::vector<std::vector<int>>& board) {
    int dist = 0;
    for (int r = 0; r < 3; r++) {
        for (int c = 0; c < 3; c++) {
            int val = board[r][c];
            if (val != 0) {
                int target_r = (val - 1) / 3;
                int target_c = (val - 1) % 3;
                dist += std::abs(r - target_r) + std::abs(c - target_c);
            }
        }
    }
    return dist;
}

int main() {
    std::vector<std::vector<int>> start = {
        {1, 2, 3},
        {5, 6, 0},
        {7, 8, 4}
    };
    std::cout << "Initial Manhattan heuristic: " << manhattan_distance(start) << std::endl;
    return 0;
}
