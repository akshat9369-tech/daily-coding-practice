"""DP: Partition Equal Subset Sum."""

def can_partition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2

    dp = {0}
    for n in nums:
        next_dp = set(dp)
        for t in dp:
            if t + n == target:
                return True
            if t + n < target:
                next_dp.add(t + n)
        dp = next_dp

    return target in dp

if __name__ == "__main__":
    nums1 = [1, 5, 11, 5]
    print("Can partition [1, 5, 11, 5]:", can_partition(nums1))
    nums2 = [1, 2, 3, 5]
    print("Can partition [1, 2, 3, 5] :", can_partition(nums2))
