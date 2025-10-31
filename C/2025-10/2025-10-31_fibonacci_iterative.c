#include <stdio.h>

void print_fibonacci(int n) {
    if (n <= 0) return;
    long long first = 0, second = 1;

    printf("Fibonacci (%d terms): ", n);
    for (int i = 1; i <= n; i++) {
        printf("%lld%s", first, (i == n) ? "\n" : ", ");
        long long next = first + second;
        first = second;
        second = next;
    }
}

int main(void) {
    print_fibonacci(10);
    print_fibonacci(15);
    return 0;
}
