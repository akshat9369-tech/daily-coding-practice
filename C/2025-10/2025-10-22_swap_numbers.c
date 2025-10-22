#include <stdio.h>

void swap_with_temp(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}

void swap_with_xor(int *x, int *y) {
    if (x != y) {
        *x ^= *y;
        *y ^= *x;
        *x ^= *y;
    }
}

int main(void) {
    int a = 15, b = 40;
    printf("Original: a = %d, b = %d\n", a, b);

    swap_with_temp(&a, &b);
    printf("After temp swap: a = %d, b = %d\n", a, b);

    swap_with_xor(&a, &b);
    printf("After XOR swap : a = %d, b = %d\n", a, b);

    return 0;
}
