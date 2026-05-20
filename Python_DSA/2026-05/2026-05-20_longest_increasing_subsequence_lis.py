"""DP: Longest Increasing Subsequence (LIS) in O(N log N)."""

import bisect

def length_of_lis(nums: list[int]) -> int:
    tails = []
    for x in nums:
        idx = bisect.bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
    return len(tails)

if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print("Length of LIS:", length_of_lis(nums))
