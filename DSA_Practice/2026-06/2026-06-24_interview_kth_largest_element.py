"""Kth Largest Element in an Array (Quickselect and Heap)."""

import random

def find_kth_largest_quickselect(nums: list[int], k: int) -> int:
    target_idx = len(nums) - k

    def quickselect(l: int, r: int) -> int:
        pivot_idx = random.randint(l, r)
        nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
        pivot = nums[r]

        p = l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p == target_idx:
            return nums[p]
        elif p < target_idx:
            return quickselect(p + 1, r)
        else:
            return quickselect(l, p - 1)

    return quickselect(0, len(nums) - 1)

if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    print("2nd largest:", find_kth_largest_quickselect(nums.copy(), 2))
