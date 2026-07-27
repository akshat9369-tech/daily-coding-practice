"""Partition Equal Subset Sum and Target Sum DP."""

def find_target_sum_ways(nums: list[int], target: int) -> int:
    dp = {0: 1}
    for n in nums:
        next_dp = {}
        for current_sum, count in dp.items():
            next_dp[current_sum + n] = next_dp.get(current_sum + n, 0) + count
            next_dp[current_sum - n] = next_dp.get(current_sum - n, 0) + count
        dp = next_dp
    return dp.get(target, 0)

if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1]
    target = 3
    print(f"Target sum {target} total ways:", find_target_sum_ways(nums, target))
