#include <stdio.h>

long long reverse_integer(long long num, int *digit_count) {
    long long rev = 0;
    int count = 0;
    long long temp = (num < 0) ? -num : num;

    if (temp == 0) {
        *digit_count = 1;
        return 0;
    }

    while (temp > 0) {
        rev = rev * 10 + (temp % 10);
        temp /= 10;
        count++;
    }

    *digit_count = count;
    return (num < 0) ? -rev : rev;
}

int main(void) {
    long long values[] = {12345, -9876, 1000, 7, 0};
    for (int i = 0; i < 5; i++) {
        int digits = 0;
        long long rev = reverse_integer(values[i], &digits);
        printf("Input: %8lld | Digits: %2d | Reversed: %8lld\n", values[i], digits, rev);
    }
    return 0;
}
