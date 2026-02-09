"""Two Pointers: Container With Most Water."""

def max_area(heights: list[int]) -> int:
    left = 0
    right = len(heights) - 1
    max_water = 0

    while left < right:
        width = right - left
        h = min(heights[left], heights[right])
        max_water = max(max_water, width * h)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_water

if __name__ == "__main__":
    elevations = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("Max water capacity:", max_area(elevations))
