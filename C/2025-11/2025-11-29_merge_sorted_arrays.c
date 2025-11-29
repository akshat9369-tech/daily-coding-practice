#include <stdio.h>

void merge_sorted(const int a[], int n, const int b[], int m, int out[]) {
    int i = 0, j = 0, k = 0;
    while (i < n && j < m) {
        if (a[i] <= b[j]) {
            out[k++] = a[i++];
        } else {
            out[k++] = b[j++];
        }
    }
    while (i < n) out[k++] = a[i++];
    while (j < m) out[k++] = b[j++];
}

int main(void) {
    int a[] = {1, 3, 5, 7, 9};
    int b[] = {2, 4, 6, 8, 10, 12};
    int merged[11];

    merge_sorted(a, 5, b, 6, merged);

    printf("Merged sorted array: ");
    for (int i = 0; i < 11; i++) printf("%d ", merged[i]);
    printf("\n");
    return 0;
}
