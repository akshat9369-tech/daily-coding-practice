"""Greedy: Jump Game I and II (Reachability and Min Jumps)."""

def can_jump(nums: list[int]) -> bool:
    goal = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0

def jump_min_steps(nums: list[int]) -> int:
    jumps = 0
    curr_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == curr_end:
            jumps += 1
            curr_end = farthest

    return jumps

if __name__ == "__main__":
    nums1 = [2, 3, 1, 1, 4]
    print("Can jump nums1:", can_jump(nums1))
    print("Min jumps nums1:", jump_min_steps(nums1))

    nums2 = [3, 2, 1, 0, 4]
    print("Can jump nums2:", can_jump(nums2))
