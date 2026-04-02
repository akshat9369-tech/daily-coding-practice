"""Heap: Heap Sort Algorithm Implementation."""

def heap_sort(arr: list[int]) -> list[int]:
    nums = arr.copy()
    n = len(nums)

    def heapify(size: int, i: int):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < size and nums[left] > nums[largest]:
            largest = left
        if right < size and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(size, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(i, 0)

    return nums

if __name__ == "__main__":
    data = [12, 11, 13, 5, 6, 7]
    print("Original :", data)
    print("Heap Sort:", heap_sort(data))
