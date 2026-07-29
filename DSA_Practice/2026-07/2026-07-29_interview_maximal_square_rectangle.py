"""Maximal Square and Maximal Rectangle in Matrix."""

def maximal_square(matrix: list[list[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_side = 0

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == "1":
                dp[r + 1][c + 1] = 1 + min(dp[r][c + 1], dp[r + 1][c], dp[r][c])
                max_side = max(max_side, dp[r + 1][c + 1])

    return max_side * max_side

if __name__ == "__main__":
    grid = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print("Maximal square area:", maximal_square(grid))
