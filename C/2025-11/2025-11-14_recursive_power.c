#include <stdio.h>

double power_recursive(double base, int exp) {
    if (exp == 0) return 1.0;
    if (exp < 0) return 1.0 / power_recursive(base, -exp);

    double half = power_recursive(base, exp / 2);
    if (exp % 2 == 0) {
        return half * half;
    } else {
        return half * half * base;
    }
}

int main(void) {
    printf("2.0 ^ 10 = %.0f\n", power_recursive(2.0, 10));
    printf("3.0 ^ 5  = %.0f\n", power_recursive(3.0, 5));
    printf("2.0 ^ -3 = %.4f\n", power_recursive(2.0, -3));
    printf("5.0 ^ 0  = %.0f\n", power_recursive(5.0, 0));
    return 0;
}
