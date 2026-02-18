"""Prefix Sum: Subarray Sum Equals K (Hash Map + Prefix Sum)."""

def subarray_sum(nums: list[int], k: int) -> int:
    prefix_counts = {0: 1}
    curr_sum = 0
    total_subarrays = 0

    for num in nums:
        curr_sum += num
        diff = curr_sum - k
        if diff in prefix_counts:
            total_subarrays += prefix_counts[diff]
        prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1

    return total_subarrays

if __name__ == "__main__":
    arr = [1, 2, 3, -2, 1, 1, 1, 2]
    k = 3
    print(f"Total subarrays with sum {k}:", subarray_sum(arr, k))
