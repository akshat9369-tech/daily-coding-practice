"""Kadane's Variation: Maximum Circular Subarray Sum."""

def max_subarray_sum_circular(nums: list[int]) -> int:
    total_sum = 0
    curr_max = 0
    max_sum = nums[0]
    curr_min = 0
    min_sum = nums[0]

    for x in nums:
        curr_max = max(x, curr_max + x)
        max_sum = max(max_sum, curr_max)

        curr_min = min(x, curr_min + x)
        min_sum = min(min_sum, curr_min)

        total_sum += x

    # If all numbers are negative
    if max_sum < 0:
        return max_sum

    return max(max_sum, total_sum - min_sum)

if __name__ == "__main__":
    arr = [5, -3, 5]
    print("Max circular subarray sum:", max_subarray_sum_circular(arr))
