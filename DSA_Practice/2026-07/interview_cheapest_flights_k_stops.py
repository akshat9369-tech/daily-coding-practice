"""Cheapest Flights Within K Stops (Bellman-Ford / BFS)."""

def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    prices = [float("inf")] * n
    prices[src] = 0

    for _ in range(k + 1):
        temp = prices.copy()
        for u, v, w in flights:
            if prices[u] == float("inf"):
                continue
            if prices[u] + w < temp[v]:
                temp[v] = prices[u] + w
        prices = temp

    return -1 if prices[dst] == float("inf") else prices[dst]

if __name__ == "__main__":
    routes = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    print("Cheapest price within 1 stop:", find_cheapest_price(4, routes, 0, 3, 1))
