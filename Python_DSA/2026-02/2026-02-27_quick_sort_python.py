"""Sorting: Quick Sort with Lomuto and Hoare Partitions."""

def quick_sort(nums: list[int]) -> list[int]:
    arr = nums.copy()

    def _quick_sort(low: int, high: int):
        if low < high:
            pi = partition(low, high)
            _quick_sort(low, pi - 1)
            _quick_sort(pi + 1, high)

    def partition(low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    _quick_sort(0, len(arr) - 1)
    return arr

if __name__ == "__main__":
    sample = [10, 7, 8, 9, 1, 5]
    print("Original:", sample)
    print("QuickSort:", quick_sort(sample))
