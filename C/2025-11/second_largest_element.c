#include <stdio.h>
#include <limits.h>

int find_second_largest(const int arr[], int size) {
    if (size < 2) return INT_MIN;
    int first = INT_MIN;
    int second = INT_MIN;

    for (int i = 0; i < size; i++) {
        if (arr[i] > first) {
            second = first;
            first = arr[i];
        } else if (arr[i] > second && arr[i] != first) {
            second = arr[i];
        }
    }
    return second;
}

int main(void) {
    int arr1[] = {12, 35, 1, 10, 34, 1};
    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    printf("Second largest in arr1: %d\n", find_second_largest(arr1, n1));

    int arr2[] = {10, 10, 10};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);
    int res2 = find_second_largest(arr2, n2);
    if (res2 == INT_MIN) {
        printf("Second largest in arr2: None exists\n");
    }
    return 0;
}
