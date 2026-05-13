"""DP: Subset Sum Problem and Boolean Table."""

def can_partition_subset_sum(nums: list[int], target: int) -> bool:
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for t in range(target, num - 1, -1):
            if dp[t - num]:
                dp[t] = True

    return dp[target]

if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    print("Subset sum 9 possible :", can_partition_subset_sum(arr, 9))
    print("Subset sum 30 possible:", can_partition_subset_sum(arr, 30))
