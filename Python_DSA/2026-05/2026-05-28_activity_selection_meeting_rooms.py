"""Greedy: Activity Selection and Meeting Rooms."""

def max_activities(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # Sort by finish time
    intervals.sort(key=lambda x: x[1])
    selected = []
    last_end = float("-inf")

    for start, end in intervals:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected

def min_meeting_rooms(intervals: list[list[int]]) -> int:
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])

    rooms, max_rooms = 0, 0
    s_ptr, e_ptr = 0, 0

    while s_ptr < len(intervals):
        if starts[s_ptr] < ends[e_ptr]:
            rooms += 1
            s_ptr += 1
        else:
            rooms -= 1
            e_ptr += 1
        max_rooms = max(max_rooms, rooms)

    return max_rooms

if __name__ == "__main__":
    acts = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    chosen = max_activities(acts)
    print(f"Max activities selected ({len(chosen)}): {chosen}")

    meetings = [[0, 30], [5, 10], [15, 20]]
    print("Min conference rooms required:", min_meeting_rooms(meetings))
