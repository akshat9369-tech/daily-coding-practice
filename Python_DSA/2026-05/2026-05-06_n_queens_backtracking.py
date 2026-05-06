"""Backtracking: N-Queens Problem (Complete Solution)."""

def solve_n_queens(n: int) -> list[list[str]]:
    col_set = set()
    pos_diag = set()  # (r + c)
    neg_diag = set()  # (r - c)

    res = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r: int):
        if r == n:
            res.append(["".join(row) for row in board])
            return

        for c in range(n):
            if c in col_set or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            col_set.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col_set.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    return res

if __name__ == "__main__":
    solutions = solve_n_queens(4)
    print(f"Found {len(solutions)} solutions for 4-Queens.")
    for sol in solutions:
        for row in sol:
            print(" ", row)
        print()
