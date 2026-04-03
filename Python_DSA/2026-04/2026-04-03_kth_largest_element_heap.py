"""Heap: Find Kth Largest Element in Array Using Min-Heap."""

import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    min_heap = []
    for x in nums:
        heapq.heappush(min_heap, x)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(f"{k}nd largest element:", find_kth_largest(nums, k))
