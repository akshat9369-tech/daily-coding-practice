#include <stdio.h>

int remove_duplicates(int arr[], int size) {
    if (size <= 1) return size;
    int write_idx = 1;

    for (int read_idx = 1; read_idx < size; read_idx++) {
        if (arr[read_idx] != arr[write_idx - 1]) {
            arr[write_idx++] = arr[read_idx];
        }
    }
    return write_idx;
}

int main(void) {
    int sorted_arr[] = {1, 1, 2, 2, 3, 4, 4, 4, 5, 6, 6};
    int n = sizeof(sorted_arr) / sizeof(sorted_arr[0]);

    printf("Original: ");
    for (int i = 0; i < n; i++) printf("%d ", sorted_arr[i]);
    printf("\n");

    int unique_count = remove_duplicates(sorted_arr, n);

    printf("After removing duplicates (%d elements): ", unique_count);
    for (int i = 0; i < unique_count; i++) printf("%d ", sorted_arr[i]);
    printf("\n");
    return 0;
}
