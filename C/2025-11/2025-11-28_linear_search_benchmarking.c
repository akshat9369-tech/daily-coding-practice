#include <stdio.h>

int linear_search_steps(const int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) return i + 1;
    }
    return n;
}

int binary_search_steps(const int arr[], int n, int target) {
    int low = 0, high = n - 1, steps = 0;
    while (low <= high) {
        steps++;
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) return steps;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return steps;
}

int main(void) {
    int sorted_data[64];
    for (int i = 0; i < 64; i++) sorted_data[i] = (i + 1) * 2;

    int test_targets[] = {2, 64, 128, 99};
    for (int i = 0; i < 4; i++) {
        int t = test_targets[i];
        int l_steps = linear_search_steps(sorted_data, 64, t);
        int b_steps = binary_search_steps(sorted_data, 64, t);
        printf("Target %3d -> Linear Steps: %2d | Binary Steps: %2d\n", t, l_steps, b_steps);
    }
    return 0;
}
