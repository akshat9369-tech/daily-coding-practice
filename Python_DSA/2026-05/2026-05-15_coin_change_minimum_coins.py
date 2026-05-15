"""DP: Coin Change I (Minimum Coins Needed)."""

def coin_change(coins: list[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[amount] if dp[amount] != float("inf") else -1

if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(f"Min coins for amount {amount}:", coin_change(coins, amount))
