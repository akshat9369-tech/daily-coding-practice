#include <stdio.h>

#define ROWS 3
#define COLS 3

void matrix_add(int A[ROWS][COLS], int B[ROWS][COLS], int C[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }
}

void print_matrix(int M[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            printf("%4d ", M[i][j]);
        }
        printf("\n");
    }
}

int main(void) {
    int A[ROWS][COLS] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int B[ROWS][COLS] = {{9, 8, 7}, {6, 5, 4}, {3, 2, 1}};
    int C[ROWS][COLS];

    matrix_add(A, B, C);
    printf("Matrix Sum A + B:\n");
    print_matrix(C);
    return 0;
}
