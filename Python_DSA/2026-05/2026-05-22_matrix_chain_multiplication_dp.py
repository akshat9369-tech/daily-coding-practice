"""DP: Matrix Chain Multiplication (MCM)."""

def matrix_chain_order(dims: list[int]) -> int:
    n = len(dims) - 1  # number of matrices
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float("inf")
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if q < dp[i][j]:
                    dp[i][j] = q

    return dp[0][n - 1]

if __name__ == "__main__":
    # Matrices: 10x20, 20x30, 30x40, 40x30
    dimensions = [10, 20, 30, 40, 30]
    print("Min scalar multiplications:", matrix_chain_order(dimensions))
