#include <stdio.h>

int insert_at_index(int arr[], int *size, int capacity, int index, int value) {
    if (*size >= capacity || index < 0 || index > *size) return 0;
    for (int i = *size; i > index; i--) {
        arr[i] = arr[i - 1];
    }
    arr[index] = value;
    (*size)++;
    return 1;
}

int delete_at_index(int arr[], int *size, int index) {
    if (index < 0 || index >= *size) return 0;
    for (int i = index; i < *size - 1; i++) {
        arr[i] = arr[i + 1];
    }
    (*size)--;
    return 1;
}

void display(const int arr[], int size) {
    for (int i = 0; i < size; i++) printf("%d ", arr[i]);
    printf("(size: %d)\n", size);
}

int main(void) {
    int buffer[10] = {10, 20, 30, 40, 50};
    int size = 5;

    printf("Initial: "); display(buffer, size);
    insert_at_index(buffer, &size, 10, 2, 99);
    printf("Insert 99 at index 2: "); display(buffer, size);
    delete_at_index(buffer, &size, 0);
    printf("Delete at index 0: "); display(buffer, size);

    return 0;
}
