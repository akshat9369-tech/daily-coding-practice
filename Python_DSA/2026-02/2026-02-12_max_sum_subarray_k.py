"""Sliding Window: Maximum Sum Subarray of Fixed Size K."""

def max_sub_array_of_size_k(k: int, nums: list[int]) -> int:
    if len(nums) < k or k <= 0:
        return 0

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    print(f"Max sum of subarray of size {k}:", max_sub_array_of_size_k(k, arr))
