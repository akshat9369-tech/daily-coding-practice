#include <stdio.h>

void print_table(int num, int limit) {
    printf("Multiplication Table for %d (up to %d):\n", num, limit);
    for (int i = 1; i <= limit; i++) {
        printf("%2d x %2d = %4d\n", num, i, num * i);
    }
}

int main(void) {
    print_table(7, 10);
    printf("\n");
    print_table(13, 5);
    return 0;
}
