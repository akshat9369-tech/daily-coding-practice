"""Sorting: Counting Sort for Integer Key Ranges."""

def counting_sort(nums: list[int]) -> list[int]:
    if not nums:
        return []

    min_val = min(nums)
    max_val = max(nums)
    range_span = max_val - min_val + 1

    count = [0] * range_span
    for x in nums:
        count[x - min_val] += 1

    sorted_arr = []
    for val_offset, freq in enumerate(count):
        sorted_arr.extend([val_offset + min_val] * freq)

    return sorted_arr

if __name__ == "__main__":
    nums = [4, 2, 2, 8, 3, 3, 1, -2, 0, -2]
    print("Original:", nums)
    print("Counting Sort:", counting_sort(nums))
