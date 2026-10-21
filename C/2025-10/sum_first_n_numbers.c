#include <stdio.h>

long long sum_while_loop(int n) {
    long long total = 0;
    int curr = 1;
    while (curr <= n) {
        total += curr;
        curr++;
    }
    return total;
}

long long sum_formula(int n) {
    return (long long)n * (n + 1) / 2;
}

int main(void) {
    int targets[] = {10, 50, 100, 1000};
    for (int i = 0; i < 4; i++) {
        int n = targets[i];
        long long res_loop = sum_while_loop(n);
        long long res_form = sum_formula(n);
        printf("N = %4d | While Loop: %8lld | Formula: %8lld (Match: %s)\n",
               n, res_loop, res_form, (res_loop == res_form) ? "YES" : "NO");
    }
    return 0;
}
