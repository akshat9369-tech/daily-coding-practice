#include <stdio.h>

int is_palindrome_number(long long n) {
    if (n < 0) return 0;
    long long original = n;
    long long reversed = 0;

    while (n > 0) {
        reversed = reversed * 10 + (n % 10);
        n /= 10;
    }

    return (original == reversed);
}

int main(void) {
    long long tests[] = {121, 12321, 1001, 12345, 0, -121};
    int count = sizeof(tests) / sizeof(tests[0]);

    for (int i = 0; i < count; i++) {
        printf("%8lld -> %s\n", tests[i],
               is_palindrome_number(tests[i]) ? "PALINDROME" : "NOT A PALINDROME");
    }
    return 0;
}
