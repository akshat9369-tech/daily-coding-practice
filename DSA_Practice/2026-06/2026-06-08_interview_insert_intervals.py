"""Insert Interval and Non-Overlapping Intervals."""

def insert_interval(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    result = []
    i = 0
    n = len(intervals)

    # Left non-overlapping intervals
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # Overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)

    # Right non-overlapping intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    removals = 0
    prev_end = float("-inf")

    for start, end in intervals:
        if start >= prev_end:
            prev_end = end
        else:
            removals += 1

    return removals

if __name__ == "__main__":
    current = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    new_one = [4, 8]
    print("Inserted Interval:", insert_interval(current, new_one))

    conflicts = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print("Min removals to eliminate overlaps:", erase_overlap_intervals(conflicts))
