"""Longest Increasing Subsequence with Patience Sorting."""

import bisect

def length_of_lis(nums: list[int]) -> int:
    piles = []
    for x in nums:
        idx = bisect.bisect_left(piles, x)
        if idx == len(piles):
            piles.append(x)
        else:
            piles[idx] = x
    return len(piles)

if __name__ == "__main__":
    sequence = [10, 9, 2, 5, 3, 7, 101, 18]
    print("LIS length via patience sorting:", length_of_lis(sequence))
