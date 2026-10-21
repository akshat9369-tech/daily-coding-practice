"""DP: 0/1 Knapsack Problem (Memoization and Tabulation)."""

def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        w, v = weights[i], values[i]
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)

    return dp[capacity]

if __name__ == "__main__":
    w = [1, 3, 4, 5]
    v = [1, 4, 5, 7]
    cap = 7
    print(f"Max value in knapsack capacity {cap}:", knapsack_01(w, v, cap))
