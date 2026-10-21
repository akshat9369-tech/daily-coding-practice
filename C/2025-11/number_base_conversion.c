#include <stdio.h>

void decimal_to_binary(int n) {
    if (n == 0) {
        printf("0\n");
        return;
    }
    int bits[32];
    int idx = 0;
    while (n > 0) {
        bits[idx++] = n % 2;
        n /= 2;
    }
    for (int i = idx - 1; i >= 0; i--) {
        printf("%d", bits[i]);
    }
    printf("\n");
}

int binary_to_decimal(const char *bin) {
    int dec = 0;
    for (int i = 0; bin[i] != '\0'; i++) {
        dec = (dec << 1) + (bin[i] - '0');
    }
    return dec;
}

int main(void) {
    int dec_vals[] = {5, 12, 29, 64, 255};
    for (int i = 0; i < 5; i++) {
        printf("Decimal %3d to Binary: ", dec_vals[i]);
        decimal_to_binary(dec_vals[i]);
    }

    const char *bin_samples[] = {"101", "1100", "11101", "1000000", "11111111"};
    for (int i = 0; i < 5; i++) {
        printf("Binary %8s to Decimal: %d\n", bin_samples[i], binary_to_decimal(bin_samples[i]));
    }
    return 0;
}
