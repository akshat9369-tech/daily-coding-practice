"""Binary Search and Bisect Module in Python."""

import bisect

def binary_search_manual(arr: list[int], target: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    sorted_nums = [3, 8, 14, 22, 35, 49, 61, 78, 92]
    targets = [22, 50, 92, 1]

    for t in targets:
        idx = binary_search_manual(sorted_nums, t)
        ins_idx = bisect.bisect_left(sorted_nums, t)
        print(f"Target {t:2d} | Found Index: {idx:2d} | Bisect Insert Index: {ins_idx}")
