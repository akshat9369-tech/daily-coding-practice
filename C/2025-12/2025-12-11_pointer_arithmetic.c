#include <stdio.h>

int main(void) {
    int numbers[] = {10, 20, 30, 40, 50};
    int count = sizeof(numbers) / sizeof(numbers[0]);
    int *ptr = numbers;

    printf("Array traversal using pointer arithmetic:\n");
    for (int i = 0; i < count; i++) {
        printf("Index %d | Address: %p | Value: %d\n", i, (void*)(ptr + i), *(ptr + i));
    }

    int *end_ptr = &numbers[count - 1];
    printf("Pointer distance (end - start): %td elements\n", end_ptr - ptr);
    return 0;
}
