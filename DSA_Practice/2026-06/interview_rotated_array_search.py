"""Search in Rotated Sorted Array I and II."""

def search_rotated_unique(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid

        # Left half sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2]
    print("Target 0 index:", search_rotated_unique(arr, 0))
    print("Target 3 index:", search_rotated_unique(arr, 3))
