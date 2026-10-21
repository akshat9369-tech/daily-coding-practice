"""Two Pointers: Two Sum on Sorted Array."""

def two_sum_sorted(numbers: list[int], target: int) -> tuple[int, int] | None:
    left = 0
    right = len(numbers) - 1

    while left < right:
        curr = numbers[left] + numbers[right]
        if curr == target:
            return left, right
        elif curr < target:
            left += 1
        else:
            right -= 1
    return None

if __name__ == "__main__":
    nums = [2, 7, 11, 15, 20]
    target = 18
    res = two_sum_sorted(nums, target)
    print(f"Target {target} found at indices:", res)
