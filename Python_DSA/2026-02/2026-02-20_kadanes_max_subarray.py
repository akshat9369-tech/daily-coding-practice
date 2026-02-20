"""Kadane's Algorithm: Maximum Subarray Sum."""

def max_sub_array(nums: list[int]) -> tuple[int, list[int]]:
    max_so_far = nums[0]
    curr_max = nums[0]
    start = end = s = 0

    for i in range(1, len(nums)):
        if nums[i] > curr_max + nums[i]:
            curr_max = nums[i]
            s = i
        else:
            curr_max += nums[i]

        if curr_max > max_so_far:
            max_so_far = curr_max
            start = s
            end = i

    return max_so_far, nums[start:end + 1]

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, subarray = max_sub_array(arr)
    print(f"Max Subarray Sum: {max_sum} | Subarray: {subarray}")
