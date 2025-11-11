#include <stdio.h>

long long combination(int n, int r) {
    if (r < 0 || r > n) return 0;
    if (r == 0 || r == n) return 1;
    if (r > n - r) r = n - r;

    long long res = 1;
    for (int i = 1; i <= r; i++) {
        res = res * (n - i + 1) / i;
    }
    return res;
}

void print_pascals_triangle(int rows) {
    for (int i = 0; i < rows; i++) {
        for (int sp = 0; sp < rows - i - 1; sp++) {
            printf("  ");
        }
        for (int j = 0; j <= i; j++) {
            printf("%4lld", combination(i, j));
        }
        printf("\n");
    }
}

int main(void) {
    printf("Pascal's Triangle (7 rows):\n");
    print_pascals_triangle(7);
    return 0;
}
