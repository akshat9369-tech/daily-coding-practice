"""Find Minimum in Rotated Sorted Array."""

def find_min(nums: list[int]) -> int:
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return nums[low]

if __name__ == "__main__":
    for sample in [[3, 4, 5, 1, 2], [4, 5, 6, 7, 0, 1, 2], [11, 13, 15, 17]]:
        print(f"Array {sample} -> Min: {find_min(sample)}")
