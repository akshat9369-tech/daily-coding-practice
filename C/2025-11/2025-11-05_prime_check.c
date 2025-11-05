#include <stdio.h>
#include <stdbool.h>

bool is_prime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;

    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

void print_prime_factors(int n) {
    printf("Prime factors of %d: ", n);
    while (n % 2 == 0) {
        printf("2 ");
        n /= 2;
    }
    for (int i = 3; i * i <= n; i += 2) {
        while (n % i == 0) {
            printf("%d ", i);
            n /= i;
        }
    }
    if (n > 2) {
        printf("%d", n);
    }
    printf("\n");
}

int main(void) {
    int test_vals[] = {2, 17, 29, 49, 84, 100, 101};
    int count = sizeof(test_vals) / sizeof(test_vals[0]);

    for (int i = 0; i < count; i++) {
        int v = test_vals[i];
        printf("%3d: %s | ", v, is_prime(v) ? "PRIME    " : "COMPOSITE");
        print_prime_factors(v);
    }
    return 0;
}
