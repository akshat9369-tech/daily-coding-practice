#include <stdio.h>

int recursive_sum_digits(int n) {
    if (n < 0) n = -n;
    if (n == 0) return 0;
    return (n % 10) + recursive_sum_digits(n / 10);
}

int recursive_count_digits(int n) {
    if (n < 0) n = -n;
    if (n < 10) return 1;
    return 1 + recursive_count_digits(n / 10);
}

int main(void) {
    int numbers[] = {12345, 9999, 407, 7, 100000};
    for (int i = 0; i < 5; i++) {
        int n = numbers[i];
        printf("Number %6d | Sum of Digits: %2d | Count of Digits: %2d\n",
               n, recursive_sum_digits(n), recursive_count_digits(n));
    }
    return 0;
}
