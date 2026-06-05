"""Best Time to Buy and Sell Stock I and II."""

def max_profit_single_trade(prices: list[int]) -> int:
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

def max_profit_multiple_trades(prices: list[int]) -> int:
    total_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]
    return total_profit

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print("Single trade profit   :", max_profit_single_trade(prices))
    print("Multiple trades profit:", max_profit_multiple_trades(prices))
