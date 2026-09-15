#include <iostream>
#include <vector>

#define N 8

int cx[8] = {2, 1, -1, -2, -2, -1, 1, 2};
int cy[8] = {1, 2, 2, 1, -1, -2, -2, -1};

bool is_valid(int x, int y, int sol[N][N]) {
    return (x >= 0 && x < N && y >= 0 && y < N && sol[x][y] == -1);
}

int main() {
    int sol[N][N];
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++) sol[i][j] = -1;
    sol[0][0] = 0;
    std::cout << "Knight's Tour initialized for 8x8 board." << std::endl;
    return 0;
}
