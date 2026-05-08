"""Backtracking: Word Search on 2D Grid."""

def exist(board: list[list[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, i: int) -> bool:
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
            return False

        temp = board[r][c]
        board[r][c] = "#"  # visited marker

        found = (dfs(r + 1, c, i + 1) or
                 dfs(r - 1, c, i + 1) or
                 dfs(r, c + 1, i + 1) or
                 dfs(r, c - 1, i + 1))

        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

if __name__ == "__main__":
    grid = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    print("ABCCED in grid:", exist(grid, "ABCCED"))
    print("SEE in grid   :", exist(grid, "SEE"))
    print("ABCB in grid  :", exist(grid, "ABCB"))
