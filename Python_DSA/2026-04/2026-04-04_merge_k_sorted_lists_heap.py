"""Heap: Merge K Sorted Lists Using Priority Queue."""

import heapq

def merge_k_sorted_arrays(arrays: list[list[int]]) -> list[int]:
    min_heap = []
    result = []

    for arr_idx, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], arr_idx, 0))

    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, arr_idx, elem_idx + 1))

    return result

if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print("Merged K Lists:", merge_k_sorted_arrays(lists))
