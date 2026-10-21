"""Sliding Window: Minimum Size Subarray Sum."""

def min_sub_array_len(target: int, nums: list[int]) -> int:
    left = 0
    curr_sum = 0
    min_len = float("inf")

    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return min_len if min_len != float("inf") else 0

if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    print("Min subarray length for sum >= 7:", min_sub_array_len(target, nums))
