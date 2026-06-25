"""Top K Frequent Elements (Bucket Sort and Heap)."""

from collections import Counter

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in count.items():
        buckets[freq].append(num)

    res = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            res.append(num)
            if len(res) == k:
                return res
    return res

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    print("Top 2 frequent elements:", top_k_frequent(nums, 2))
