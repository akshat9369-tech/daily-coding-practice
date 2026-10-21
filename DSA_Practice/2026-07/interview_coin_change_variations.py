"""Coin Change Variations (Finite vs Infinite Supply)."""

def coin_change_finite(coins: list[int], quantities: list[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for c, qty in zip(coins, quantities):
        for a in range(amount, -1, -1):
            if dp[a] != float("inf"):
                for k in range(1, qty + 1):
                    if a + k * c <= amount:
                        dp[a + k * c] = min(dp[a + k * c], dp[a] + k)

    return dp[amount] if dp[amount] != float("inf") else -1

if __name__ == "__main__":
    coins = [1, 2, 5]
    counts = [2, 2, 1]
    target = 9
    print(f"Min coins with limited supply for {target}:", coin_change_finite(coins, counts, target))
