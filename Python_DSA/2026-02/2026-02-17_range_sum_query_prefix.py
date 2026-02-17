"""Prefix Sum: Range Sum Query (1D Immutable)."""

class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i, val in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + val

    def sum_range(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]

if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    print("Sum range [0, 2]:", obj.sum_range(0, 2))
    print("Sum range [2, 5]:", obj.sum_range(2, 5))
    print("Sum range [0, 5]:", obj.sum_range(0, 5))
