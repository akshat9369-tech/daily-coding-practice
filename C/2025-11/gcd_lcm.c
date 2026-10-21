#include <stdio.h>

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long rem = a % b;
        a = b;
        b = rem;
    }
    return (a < 0) ? -a : a;
}

long long lcm(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd(a, b)) * b;
}

int main(void) {
    long long pairs[][2] = {{12, 18}, {35, 49}, {100, 25}, {17, 19}};
    for (int i = 0; i < 4; i++) {
        long long a = pairs[i][0];
        long long b = pairs[i][1];
        printf("a = %3lld, b = %3lld -> GCD: %3lld | LCM: %5lld\n",
               a, b, gcd(a, b), lcm(a, b));
    }
    return 0;
}
