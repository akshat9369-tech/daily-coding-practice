#include <stdio.h>

#define N 3

int is_symmetric(int M[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < i; j++) {
            if (M[i][j] != M[j][i]) return 0;
        }
    }
    return 1;
}

int is_identity(int M[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j && M[i][j] != 1) return 0;
            if (i != j && M[i][j] != 0) return 0;
        }
    }
    return 1;
}

int main(void) {
    int sym[N][N] = {{1, 2, 3}, {2, 4, 5}, {3, 5, 6}};
    int ident[N][N] = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};

    printf("sym matrix is symmetric: %s\n", is_symmetric(sym) ? "YES" : "NO");
    printf("ident matrix is identity: %s\n", is_identity(ident) ? "YES" : "NO");
    return 0;
}
