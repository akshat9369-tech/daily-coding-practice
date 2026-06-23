"""Search a 2D Matrix I and II."""

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = matrix[mid // cols][mid % cols]
        if mid_val == target:
            return True
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

if __name__ == "__main__":
    m = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    print("Target 3 in matrix:", search_matrix(m, 3))
    print("Target 13 in matrix:", search_matrix(m, 13))
