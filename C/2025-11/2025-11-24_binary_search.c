#include <stdio.h>

int binary_search_iterative(const int arr[], int size, int target) {
    int low = 0, high = size - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

int binary_search_recursive(const int arr[], int low, int high, int target) {
    if (low > high) return -1;
    int mid = low + (high - low) / 2;
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) return binary_search_recursive(arr, mid + 1, high, target);
    else return binary_search_recursive(arr, low, mid - 1, target);
}

int main(void) {
    int sorted[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int n = sizeof(sorted) / sizeof(sorted[0]);

    int targets[] = {23, 2, 91, 50};
    for (int i = 0; i < 4; i++) {
        int t = targets[i];
        int idx_iter = binary_search_iterative(sorted, n, t);
        int idx_rec = binary_search_recursive(sorted, 0, n - 1, t);
        printf("Target %2d | Iterative Index: %2d | Recursive Index: %2d\n",
               t, idx_iter, idx_rec);
    }
    return 0;
}
