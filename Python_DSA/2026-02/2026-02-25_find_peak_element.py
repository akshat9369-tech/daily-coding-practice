"""Binary Search: Find Peak Element in Array."""

def find_peak_element(nums: list[int]) -> int:
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return low

if __name__ == "__main__":
    arr = [1, 2, 1, 3, 5, 6, 4]
    peak_idx = find_peak_element(arr)
    print(f"Peak element found at index {peak_idx} (value: {arr[peak_idx]})")
