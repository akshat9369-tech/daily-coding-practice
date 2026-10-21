#include <stdio.h>

int main(void) {
    int a = 25, b = 7;

    printf("a = %d, b = %d\n", a, b);
    printf("Addition       (a + b) = %d\n", a + b);
    printf("Subtraction    (a - b) = %d\n", a - b);
    printf("Multiplication (a * b) = %d\n", a * b);
    printf("Division       (a / b) = %d\n", a / b);
    printf("Remainder      (a %% b) = %d\n", a % b);

    double float_div = (double)a / b;
    printf("Floating Div   (a / b) = %.4f\n", float_div);

    return 0;
}
