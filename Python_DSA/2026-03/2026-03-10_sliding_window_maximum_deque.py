"""Deque: Sliding Window Maximum using Monotonic Deque."""

from collections import deque

def max_sliding_window(nums: list[int], k: int) -> list[int]:
    d = deque()
    res = []

    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n:
            d.pop()
        d.append(i)

        if d[0] <= i - k:
            d.popleft()

        if i >= k - 1:
            res.append(nums[d[0]])

    return res

if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print("Sliding max (k=3):", max_sliding_window(nums, k))
