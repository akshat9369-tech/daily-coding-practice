#include <stdio.h>

double compute(double a, double b, char op, int *error) {
    *error = 0;
    switch (op) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/':
            if (b == 0.0) {
                *error = 1;
                return 0.0;
            }
            return a / b;
        default:
            *error = 2;
            return 0.0;
    }
}

int main(void) {
    double x = 12.5, y = 2.5;
    char ops[] = {'+', '-', '*', '/', '%'};

    for (int i = 0; i < 5; i++) {
        int err = 0;
        double res = compute(x, y, ops[i], &err);
        if (err == 0) {
            printf("%.2f %c %.2f = %.2f\n", x, ops[i], y, res);
        } else if (err == 1) {
            printf("Error: Division by zero\n");
        } else {
            printf("Error: Unsupported operator '%c'\n", ops[i]);
        }
    }
    return 0;
}
