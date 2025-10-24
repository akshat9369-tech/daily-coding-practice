#include <stdio.h>

int max_of_three_nested(int a, int b, int c) {
    if (a >= b) {
        if (a >= c) return a;
        else return c;
    } else {
        if (b >= c) return b;
        else return c;
    }
}

int max_of_three_ternary(int a, int b, int c) {
    return (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);
}

int main(void) {
    int x = 45, y = 78, z = 32;
    printf("Numbers: %d, %d, %d\n", x, y, z);
    printf("Max (nested) : %d\n", max_of_three_nested(x, y, z));
    printf("Max (ternary): %d\n", max_of_three_ternary(x, y, z));
    return 0;
}
