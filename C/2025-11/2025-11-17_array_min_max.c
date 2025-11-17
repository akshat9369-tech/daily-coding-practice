#include <stdio.h>

void find_min_max(const int arr[], int size, int *min_val, int *max_val) {
    if (size <= 0) return;
    *min_val = arr[0];
    *max_val = arr[0];

    for (int i = 1; i < size; i++) {
        if (arr[i] < *min_val) *min_val = arr[i];
        if (arr[i] > *max_val) *max_val = arr[i];
    }
}

int main(void) {
    int data[] = {45, 12, 89, 3, 67, 99, -5, 23, 76};
    int n = sizeof(data) / sizeof(data[0]);

    int min_val, max_val;
    find_min_max(data, n, &min_val, &max_val);

    printf("Array: ");
    for (int i = 0; i < n; i++) printf("%d ", data[i]);
    printf("\nMin: %d | Max: %d\n", min_val, max_val);
    return 0;
}
