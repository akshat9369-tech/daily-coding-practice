#include <stdio.h>

void swap_by_ref(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void) {
    int x = 100, y = 500;
    printf("Before swap: x = %d, y = %d\n", x, y);
    swap_by_ref(&x, &y);
    printf("After swap : x = %d, y = %d\n", x, y);
    return 0;
}
