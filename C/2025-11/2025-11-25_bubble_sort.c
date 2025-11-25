#include <stdio.h>
#include <stdbool.h>

void bubble_sort(int arr[], int size, int *passes, int *swaps) {
    *passes = 0;
    *swaps = 0;
    for (int i = 0; i < size - 1; i++) {
        bool swapped = false;
        (*passes)++;
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
                (*swaps)++;
            }
        }
        if (!swapped) break;
    }
}

int main(void) {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);

    int passes = 0, swaps = 0;
    bubble_sort(arr, n, &passes, &swaps);

    printf("Sorted array: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\nPasses: %d | Total Swaps: %d\n", passes, swaps);
    return 0;
}
