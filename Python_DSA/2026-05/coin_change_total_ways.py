"""DP: Coin Change II (Total Number of Ways)."""

def change(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1

    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]

    return dp[amount]

if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 5
    print(f"Total combinations to make {amount}:", change(amount, coins))
