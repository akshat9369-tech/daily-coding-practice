#include <stdio.h>

int linear_search(const int arr[], int size, int target, int *comparisons) {
    *comparisons = 0;
    for (int i = 0; i < size; i++) {
        (*comparisons)++;
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

int count_frequency(const int arr[], int size, int target) {
    int freq = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) freq++;
    }
    return freq;
}

int main(void) {
    int data[] = {14, 25, 7, 42, 19, 7, 88, 7, 33};
    int n = sizeof(data) / sizeof(data[0]);

    int comps = 0;
    int idx = linear_search(data, n, 42, &comps);
    printf("Target 42 found at index: %d (comparisons: %d)\n", idx, comps);

    int target = 7;
    printf("Target %d frequency: %d times\n", target, count_frequency(data, n, target));
    return 0;
}
