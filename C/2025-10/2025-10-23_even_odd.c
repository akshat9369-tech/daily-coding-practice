#include <stdio.h>

int is_even_modulo(int n) {
    return (n % 2 == 0);
}

int is_even_bitwise(int n) {
    return ((n & 1) == 0);
}

int main(void) {
    int test_values[] = {0, 1, 4, 17, 28, -5, -8};
    int count = sizeof(test_values) / sizeof(test_values[0]);

    for (int i = 0; i < count; i++) {
        int val = test_values[i];
        printf("Number %3d: modulo -> %s | bitwise -> %s\n",
               val,
               is_even_modulo(val) ? "EVEN" : "ODD ",
               is_even_bitwise(val) ? "EVEN" : "ODD ");
    }
    return 0;
}
