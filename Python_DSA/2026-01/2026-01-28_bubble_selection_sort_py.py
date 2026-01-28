"""Basic Sorting Algorithms in Python (Bubble Sort and Selection Sort)."""

def bubble_sort(arr: list[int]) -> list[int]:
    nums = arr.copy()
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

def selection_sort(arr: list[int]) -> list[int]:
    nums = arr.copy()
    n = len(nums)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

if __name__ == "__main__":
    sample = [64, 25, 12, 22, 11]
    print("Original      :", sample)
    print("Bubble Sort   :", bubble_sort(sample))
    print("Selection Sort:", selection_sort(sample))
