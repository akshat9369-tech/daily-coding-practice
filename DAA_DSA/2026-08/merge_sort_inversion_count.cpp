#include <iostream>
#include <vector>

long long merge_and_count(std::vector<int>& arr, int left, int mid, int right) {
    std::vector<int> left_sub(arr.begin() + left, arr.begin() + mid + 1);
    std::vector<int> right_sub(arr.begin() + mid + 1, arr.begin() + right + 1);

    int i = 0, j = 0, k = left;
    long long inv_count = 0;

    while (i < (int)left_sub.size() && j < (int)right_sub.size()) {
        if (left_sub[i] <= right_sub[j]) {
            arr[k++] = left_sub[i++];
        } else {
            arr[k++] = right_sub[j++];
            inv_count += (left_sub.size() - i);
        }
    }
    while (i < (int)left_sub.size()) arr[k++] = left_sub[i++];
    while (j < (int)right_sub.size()) arr[k++] = right_sub[j++];

    return inv_count;
}

long long count_inversions(std::vector<int>& arr, int left, int right) {
    long long inv_count = 0;
    if (left < right) {
        int mid = left + (right - left) / 2;
        inv_count += count_inversions(arr, left, mid);
        inv_count += count_inversions(arr, mid + 1, right);
        inv_count += merge_and_count(arr, left, mid, right);
    }
    return inv_count;
}

int main() {
    std::vector<int> arr = {8, 4, 2, 1};
    long long inv = count_inversions(arr, 0, arr.size() - 1);
    std::cout << "Inversion count for [8, 4, 2, 1]: " << inv << std::endl;
    return 0;
}
