"""Move Zeroes to End While Maintaining Relative Order."""

def move_zeroes(nums: list[int]) -> list[int]:
    write_idx = 0
    for read_idx in range(len(nums)):
        if nums[read_idx] != 0:
            nums[write_idx], nums[read_idx] = nums[read_idx], nums[write_idx]
            write_idx += 1
    return nums

if __name__ == "__main__":
    sample = [0, 1, 0, 3, 12, 0, 9]
    print("Before:", sample)
    move_zeroes(sample)
    print("After :", sample)
