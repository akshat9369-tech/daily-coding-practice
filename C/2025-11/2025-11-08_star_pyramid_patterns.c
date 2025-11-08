#include <stdio.h>

void half_pyramid(int rows) {
    printf("Half Pyramid (%d rows):\n", rows);
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= i; j++) {
            printf("* ");
        }
        printf("\n");
    }
}

void full_pyramid(int rows) {
    printf("Full Pyramid (%d rows):\n", rows);
    for (int i = 1; i <= rows; i++) {
        for (int space = 1; space <= rows - i; space++) {
            printf(" ");
        }
        for (int star = 1; star <= 2 * i - 1; star++) {
            printf("*");
        }
        printf("\n");
    }
}

int main(void) {
    half_pyramid(5);
    printf("\n");
    full_pyramid(5);
    return 0;
}
