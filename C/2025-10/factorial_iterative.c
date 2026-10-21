#include <stdio.h>

unsigned long long factorial_iterative(int n) {
    if (n < 0) return 0;
    unsigned long long fact = 1;
    for (int i = 2; i <= n; i++) {
        fact *= (unsigned long long)i;
    }
    return fact;
}

int main(void) {
    printf("Factorial Calculation (Iterative):\n");
    for (int n = 0; n <= 15; n++) {
        printf("%2d! = %llu\n", n, factorial_iterative(n));
    }
    return 0;
}
