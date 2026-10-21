"""Array Rotation In-Place by K Elements."""

def rotate_array(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    if n == 0:
        return nums
    k = k % n

    def reverse(start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return nums

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("Original:", arr)
    rotate_array(arr, 3)
    print("Rotated by 3:", arr)
