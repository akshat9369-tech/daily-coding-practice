"""Prefix Sum: Find Pivot / Equilibrium Index of Array."""

def pivot_index(nums: list[int]) -> int:
    total_sum = sum(nums)
    left_sum = 0

    for i, val in enumerate(nums):
        if left_sum == (total_sum - left_sum - val):
            return i
        left_sum += val

    return -1

if __name__ == "__main__":
    sample = [1, 7, 3, 6, 5, 6]
    print("Pivot index:", pivot_index(sample))
