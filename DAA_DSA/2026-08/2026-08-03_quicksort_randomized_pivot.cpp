#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

int partition(std::vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i + 1], arr[high]);
    return i + 1;
}

int randomized_partition(std::vector<int>& arr, int low, int high) {
    int random_idx = low + rand() % (high - low + 1);
    std::swap(arr[random_idx], arr[high]);
    return partition(arr, low, high);
}

void randomized_quicksort(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = randomized_partition(arr, low, high);
        randomized_quicksort(arr, low, pi - 1);
        randomized_quicksort(arr, pi + 1, high);
    }
}

int main() {
    srand(42);
    std::vector<int> data = {10, 7, 8, 9, 1, 5};
    randomized_quicksort(data, 0, data.size() - 1);
    std::cout << "Randomized QuickSort result: ";
    for (int x : data) std::cout << x << " ";
    std::cout << std::endl;
    return 0;
}
