"""Dutch National Flag: Sort Colors (0s, 1s, 2s) in One Pass."""

def sort_colors(nums: list[int]) -> list[int]:
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

if __name__ == "__main__":
    colors = [2, 0, 2, 1, 1, 0, 1, 2, 0]
    print("Original colors:", colors)
    sort_colors(colors)
    print("Sorted colors  :", colors)
