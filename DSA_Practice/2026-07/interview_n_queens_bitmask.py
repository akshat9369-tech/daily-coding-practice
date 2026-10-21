"""N-Queens II (Bitmask Fast Solver)."""

def total_n_queens(n: int) -> int:
    count = 0
    all_rows = (1 << n) - 1

    def solve(cols: int, diag1: int, diag2: int):
        nonlocal count
        if cols == all_rows:
            count += 1
            return

        available = all_rows & ~(cols | diag1 | diag2)
        while available:
            pick = available & -available  # extract lowest set bit
            available -= pick
            solve(cols | pick, (diag1 | pick) << 1, (diag2 | pick) >> 1)

    solve(0, 0, 0)
    return count

if __name__ == "__main__":
    for size in range(4, 9):
        print(f"Total valid {size}-Queens solutions: {total_n_queens(size)}")
