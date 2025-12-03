#include <stdio.h>

#define N 3

void transpose(int M[N][N], int T[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            T[j][i] = M[i][j];
        }
    }
}

int diagonal_sum(int M[N][N]) {
    int sum = 0;
    for (int i = 0; i < N; i++) {
        sum += M[i][i];
    }
    return sum;
}

int main(void) {
    int M[N][N] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int T[N][N];

    transpose(M, T);
    printf("Original Matrix Trace (Diagonal Sum): %d\n", diagonal_sum(M));
    printf("Transposed Matrix:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) printf("%3d ", T[i][j]);
        printf("\n");
    }
    return 0;
}
