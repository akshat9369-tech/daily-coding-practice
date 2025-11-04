#include <stdio.h>

long long power_int(int base, int exp) {
    long long res = 1;
    for (int i = 0; i < exp; i++) {
        res *= base;
    }
    return res;
}

int is_armstrong(int n) {
    if (n < 0) return 0;
    int temp = n;
    int num_digits = 0;

    while (temp > 0) {
        num_digits++;
        temp /= 10;
    }

    temp = n;
    long long sum = 0;
    while (temp > 0) {
        int digit = temp % 10;
        sum += power_int(digit, num_digits);
        temp /= 10;
    }

    return (sum == (long long)n);
}

int main(void) {
    printf("Armstrong Numbers between 1 and 1000:\n");
    for (int i = 1; i <= 1000; i++) {
        if (is_armstrong(i)) {
            printf("%d ", i);
        }
    }
    printf("\n");
    return 0;
}
