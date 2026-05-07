"""Backtracking: Sudoku Solver Algorithm."""

def solve_sudoku(board: list[list[str]]) -> bool:
    def is_valid(r: int, c: int, ch: str) -> bool:
        for i in range(9):
            if board[r][i] == ch or board[i][c] == ch:
                return False
            box_r, box_c = 3 * (r // 3) + i // 3, 3 * (c // 3) + i % 3
            if board[box_r][box_c] == ch:
                return False
        return True

    def solve() -> bool:
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for d in "123456789":
                        if is_valid(r, c, d):
                            board[r][c] = d
                            if solve():
                                return True
                            board[r][c] = "."
                    return False
        return True

    return solve()

if __name__ == "__main__":
    puzzle = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    if solve_sudoku(puzzle):
        print("Solved Sudoku:")
        for row in puzzle:
            print(" ", " ".join(row))
