#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int initial_size = 4;
    int *arr = (int *)calloc(initial_size, sizeof(int));
    if (!arr) return 1;

    printf("Initial calloc-zeroed: ");
    for (int i = 0; i < initial_size; i++) printf("%d ", arr[i]);
    printf("\n");

    for (int i = 0; i < initial_size; i++) arr[i] = (i + 1) * 5;

    int new_size = 8;
    int *temp = (int *)realloc(arr, new_size * sizeof(int));
    if (!temp) {
        free(arr);
        return 1;
    }
    arr = temp;

    for (int i = initial_size; i < new_size; i++) {
        arr[i] = (i + 1) * 5;
    }

    printf("Resized with realloc: ");
    for (int i = 0; i < new_size; i++) printf("%d ", arr[i]);
    printf("\n");

    free(arr);
    return 0;
}
