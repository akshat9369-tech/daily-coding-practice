#include <stdio.h>

void floyds_triangle(int rows) {
    printf("Floyd's Triangle (%d rows):\n", rows);
    int num = 1;
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%3d ", num++);
        }
        printf("\n");
    }
}

void number_diamond(int n) {
    printf("Number Diamond (size %d):\n", n);
    for (int i = 1; i <= n; i++) {
        for (int sp = 1; sp <= n - i; sp++) printf(" ");
        for (int j = 1; j <= i; j++) printf("%d", j);
        for (int j = i - 1; j >= 1; j--) printf("%d", j);
        printf("\n");
    }
    for (int i = n - 1; i >= 1; i--) {
        for (int sp = 1; sp <= n - i; sp++) printf(" ");
        for (int j = 1; j <= i; j++) printf("%d", j);
        for (int j = i - 1; j >= 1; j--) printf("%d", j);
        printf("\n");
    }
}

int main(void) {
    floyds_triangle(5);
    printf("\n");
    number_diamond(4);
    return 0;
}
