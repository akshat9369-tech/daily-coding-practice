"""Largest Rectangle in Histogram (Monotonic Stack)."""

def largest_rectangle_area(heights: list[int]) -> int:
    stack = []  # (index, height)
    max_area = 0

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))

    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))

    return max_area

if __name__ == "__main__":
    hist = [2, 1, 5, 6, 2, 3]
    print("Largest Rectangle Area:", largest_rectangle_area(hist))
