"""DP: Rod Cutting Problem (Unbounded Knapsack)."""

def rod_cutting(price: list[int], n: int) -> int:
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        max_val = 0
        for j in range(1, i + 1):
            max_val = max(max_val, price[j - 1] + dp[i - j])
        dp[i] = max_val

    return dp[n]

if __name__ == "__main__":
    # Prices for length 1, 2, 3, ..., 8
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    n = 8
    print(f"Max profit for rod length {n}:", rod_cutting(prices, n))
