#include <iostream>

int total_solutions = 0;

void solve(int row, int cols, int d1, int d2, int n) {
    if (row == n) { total_solutions++; return; }
    int available = ((1 << n) - 1) & ~(cols | d1 | d2);
    while (available) {
        int pick = available & -available;
        available -= pick;
        solve(row + 1, cols | pick, (d1 | pick) << 1, (d2 | pick) >> 1, n);
    }
}

int main() {
    int n = 8;
    solve(0, 0, 0, 0, n);
    std::cout << "Total " << n << "-Queens solutions (bitmask): " << total_solutions << std::endl;
    return 0;
}
