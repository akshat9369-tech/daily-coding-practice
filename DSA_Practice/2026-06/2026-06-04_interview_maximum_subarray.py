"""Maximum Subarray (Kadane and Divide and Conquer)."""

def max_subarray_kadane(nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = nums[0]
    for x in nums[1:]:
        curr_sum = max(x, curr_sum + x)
        max_sum = max(max_sum, curr_sum)
    return max_sum

def max_subarray_divide_conquer(nums: list[int]) -> int:
    def helper(low: int, high: int) -> int:
        if low == high:
            return nums[low]
        mid = (low + high) // 2
        left_max = helper(low, mid)
        right_max = helper(mid + 1, high)

        # Cross sum
        left_sum, curr = float("-inf"), 0
        for i in range(mid, low - 1, -1):
            curr += nums[i]
            left_sum = max(left_sum, curr)

        right_sum, curr = float("-inf"), 0
        for i in range(mid + 1, high + 1):
            curr += nums[i]
            right_sum = max(right_sum, curr)

        return max(left_max, right_max, left_sum + right_sum)

    return helper(0, len(nums) - 1)

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Kadane Max Sum       :", max_subarray_kadane(arr))
    print("Divide & Conquer Sum :", max_subarray_divide_conquer(arr))
